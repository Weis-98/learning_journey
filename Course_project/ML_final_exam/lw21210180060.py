import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import torch
from torch import nn
from torch.utils.data import DataLoader
from datetime import datetime
import torch.nn.functional as F

from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# %matplotlib inline

# path = r'D:\PythonProjects\附件1\\回归预测.xls'
path = r'回归预测.xls'
train = pd.read_excel(path, sheet_name='训练集', header=None, names=[str(i) for i in range(32)])
test = pd.read_excel(path, sheet_name='测试集', header=None, names=[str(i) for i in range(32)])

train_input = pd.concat([train, pd.get_dummies(train['30'])], axis=1)
train_label = train['31']

test_input = pd.concat([test, pd.get_dummies(test['30'])], axis=1)
test_label = test['31']

del train_input['30'], train_input['31'], test_input['30'], test_input['31']

# 训练集验证集划分
train_input, valid_input, train_label, valid_label = train_test_split(train_input, train_label, test_size=0.2,
                                                                      shuffle=True, random_state=59)

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(train_input.describe())

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(train_label.describe())


def type2tensor(raw_input, raw_label):
    process_input = torch.tensor(raw_input.values).float()
    process_label = torch.tensor(raw_label.values).float().reshape(-1, 1)
    return process_input, process_label


train_input, train_label = type2tensor(train_input, train_label)
valid_input, valid_label = type2tensor(valid_input, valid_label)
test_input, test_label = type2tensor(test_input, test_label)

scaler = MinMaxScaler()
scaler.fit(train_input)

y_scaler = StandardScaler()
y_scaler.fit(train_label)


# label_x = label_x.float().reshape(-1, 1)
def scaler_data(raw_input, raw_label, scaler, y_scaler):
    input_scaler = scaler.transform(raw_input).astype('float32')
    label_scaler = y_scaler.transform(raw_label).astype('float32')

    data = []
    for i in range(len(input_scaler)):
        data.append((input_scaler[i], label_scaler[i]))

    return data


train_data = scaler_data(train_input, train_label, scaler, y_scaler)
valid_data = scaler_data(valid_input, valid_label, scaler, y_scaler)
test_data = scaler_data(test_input, test_label, scaler, y_scaler)


# dim 37
# min ave_test_loss = 0.74597 with scaler
class ResidualBlock(nn.Module):
    def __init__(self, layer, innlayer, dropout=0.1):
        super().__init__()
        self.ln1 = nn.Linear(layer, innlayer)
        self.dropout1 = nn.Dropout(dropout)

        self.ln2 = nn.Linear(innlayer, layer)

    def forward(self, x):
        residual = x
        x = self.dropout1(F.relu(self.ln1(x)))
        x = F.relu(self.ln2(x))
        return residual + x


class CNN(nn.Module):
    def __init__(self):
        super(CNN, self).__init__()

        self.blocks = nn.ModuleList()
        self.blocks.append(nn.Sequential(
            ResidualBlock(30, 32),
            nn.Linear(30, 16),
            ResidualBlock(16, 10),
        ))

        self.blocks_cat = nn.ModuleList()
        self.blocks_cat.append(nn.Sequential(
            nn.Linear(7, 16),
            nn.ReLU(),
            nn.Dropout(0.1)
        ))
        self.predict = nn.Sequential(
            nn.Linear(16, 1)
        )

    def forward(self, x):
        num_batch = x.shape[0]
        x, xc = x[:, 0:30], x[:, 30:]
        for block in self.blocks:
            x = block(x)
        for block in self.blocks_cat:
            xc = block(xc)
        x = self.predict((x + xc).view(num_batch, -1))

        return x


class Trainer:
    def __init__(self, train_set, valid_set, use_cuda=True, batch_size=5, opt='adam', best_save=True):
        self.train_loader = DataLoader(train_set, batch_size=batch_size, shuffle=True)
        self.valid_loader = DataLoader(valid_set, batch_size=batch_size, shuffle=False)

        # 设备选择
        self.device = torch.device("cuda" if use_cuda and torch.cuda.is_available() else "cpu")
        self.net = CNN().to(self.device)
        print(self.net)

        # 优化器选择
        if opt == 'sgd':
            self.opt = torch.optim.SGD(self.net.parameters(), lr=1e-5)
        elif opt == 'sgd_mom':
            self.opt = torch.optim.SGD(self.net.parameters(), lr=1e-5, momentum=0.9)
        elif opt == 'ada':
            self.opt = torch.optim.Adagrad(self.net.parameters(), lr=1e-3)
        elif opt == 'adam':
            self.opt = torch.optim.Adam(self.net.parameters(), lr=1e-3, weight_decay=0.10125)
        elif opt == 'rms':
            self.opt = torch.optim.RMSprop(self.net.parameters(), lr=1e-3, alpha=0.99)
        else:
            print('opt type %s not supported' % opt)
        self.opt_name = opt

        # 损失函数定义
        self.loss_func = nn.MSELoss()
        #         self.loss_func = nn.MSELoss()

        # other
        self.train_losses = list()
        self.valid_record = list()
        self.best_save = best_save

    def train(self, epochs=30):
        for epoch in range(1, epochs + 1):
            epoch_loss = self.train_epoch(epoch)
            self.train_losses.append(epoch_loss)
            valid_loss = self.eval(epoch)
            if self.best_save and len(self.valid_record) > 0 and valid_loss < min(self.valid_record):
                torch.save(self.net.state_dict(), 'model_best_{}'.format(self.opt_name))
            self.valid_record.append(valid_loss)

        train_loss = np.array(self.train_losses)
        np_valid_record = np.array(self.valid_record)
        np.savez('train_%s.npz' % self.opt_name,
                 train=train_loss, test=np_valid_record)

    def train_epoch(self, epoch):
        self.net.train()
        opt = self.opt
        train_loss = 0
        start_time = datetime.now()
        for i, (data, label) in enumerate(self.train_loader):
            data, label = data.to(self.device), label.to(self.device)
            opt.zero_grad()
            output = self.net(data)
            output = output.reshape(label.size())
            loss = self.loss_func(output, label)
            loss.backward()
            opt.step()
            train_loss += loss.item()

        end_time = datetime.now()
        run_time = end_time - start_time

        train_loss /= len(self.train_loader.dataset)

        if epoch % 100 == 0 and epoch != 0:
            print('\nepoch %d:' % epoch)
            print('train: average loss %.4f, using %d seconds' % (train_loss, run_time.seconds))

        return train_loss

    def eval(self, epoch):
        self.net.eval()
        valid_loss = 0

        start_time = datetime.now()
        for i, (data, label) in enumerate(self.valid_loader):
            data, label = data.to(self.device), label.to(self.device)
            output = self.net(data)
            output = output.reshape(label.size())
            valid_loss += self.loss_func(output, label).item()

        end_time = datetime.now()
        run_time = end_time - start_time

        valid_loss /= len(self.valid_loader.dataset)
        if epoch % 100 == 0 and epoch != 0:
            avg_time = run_time.microseconds // len(self.valid_loader.dataset)
            print('valid: average loss %.4f, average using %d ms' % (valid_loss, avg_time))

        return valid_loss

    def test(self, test_set, batch_size=32):
        test_loader = DataLoader(test_set, batch_size=batch_size)
        self.net.eval()

        start_time = datetime.now()

        preds = []
        label = []
        for i, (data, label_i) in enumerate(test_loader):
            data = data.to(self.device)
            output = self.net(data)
            output = output.reshape(-1, 1).detach().cpu().numpy()
            preds.append(output)
            label.append(label_i)

        preds = np.concatenate(preds, axis=0)
        label = np.concatenate(label, axis=0)

        end_time = datetime.now()
        run_time = end_time - start_time
        avg_time = run_time.microseconds // len(test_loader.dataset)

        print('average using {} ms'.format(avg_time))

        return preds, label


def setup_seed(seed):
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    np.random.seed(seed)
    # random.seed(seed)
    torch.backends.cudnn.deterministic = True
    return


setup_seed(3)
# 1:289 5:289 10:286 12:288 13:288
# lambda=0.01

# lambda=0.05 3:273 20:275
# lambda=0.1  1:273 3:270 20也不行
# lambda=0.2  5:272 9:269
# lambda=0.15
# lambda=0.125
# lambda=0.1125
# lambda=0.10125
trainer = Trainer(train_set=train_data, valid_set=valid_data, use_cuda=True, batch_size=300, opt='adam', best_save=True)

trainer.train(epochs=200)

loss_train_test = pd.DataFrame()
loss_train_test['train_loss'] = trainer.train_losses
loss_train_test['valid_loss'] = trainer.valid_record
loss_train_test['iteration'] = loss_train_test.index
loss_train_test = loss_train_test.melt(id_vars=["iteration"], var_name="type", value_name="loss")
fig = sns.lineplot(data=loss_train_test, x='iteration', y='loss', hue='type')
loss_fig = fig.get_figure()
loss_fig.savefig('loss.png')

print('min valid_record is {}'.format(min(trainer.valid_record)))

# best model load
trainer.net.load_state_dict(torch.load('model_best_{}'.format(trainer.opt_name)))

result, res_label = trainer.test(test_data, batch_size=549)
result = y_scaler.inverse_transform(result)
res_label = y_scaler.inverse_transform(res_label)
pd.DataFrame((result.round() - res_label)).describe()

fig = plt.figure()
fig1 = sns.relplot(x=[i for i in range(1, len((result - res_label)) + 1)], y=(result - res_label).T[0], kind='scatter')
fig1.set_xlabels("test No.")
fig1.set_ylabels("residual")
# fig.savefig('residual.png')

errors = (result.round() - res_label)
print('MSE', sum(errors * errors) / len(errors))

delta = errors / res_label
print('sum of delta', sum(delta * delta))

print('Mean sum of delta', sum(delta * delta)/len(errors))

res = pd.DataFrame(errors)
fig = plt.figure()
fig2 = sns.distplot(res, bins=20)
# fig2.get_figure().savefig('残差分布图与密度估计.png')
