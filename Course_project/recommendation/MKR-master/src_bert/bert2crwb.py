import numpy as np

kg_bert = np.load('../data/douban/20wbert/kg_bert.npy', allow_pickle=True)
bert_len = len(kg_bert)
word2idx = {}
uid2bert = {}
idx2bert = {}

idx = 0
num = 0

for line in open('../data/douban/kg.txt', encoding='utf-8'):
    if num >= bert_len:
        break
    array = line.strip().split('\t')
    if array[2] not in word2idx.keys():
        word2idx[array[2]] = idx
        idx2bert[idx] = kg_bert[num][2]
        idx += 1
    if array[0] not in uid2bert.keys():
        uid2bert[array[0]] = kg_bert[num][2]
    num += 1

np.save('../data/douban/wor2idx.npy', word2idx)
np.save('../data/douban/uid2bert.npy', uid2bert)
np.save('../data/douban/idx2bert.npy', idx2bert)



