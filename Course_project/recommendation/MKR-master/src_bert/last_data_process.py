import numpy as np

idx2bert = np.load('../data/douban/idx2bert.npy', allow_pickle=True).item()
word2idx = np.load('../data/douban/wor2idx.npy', allow_pickle=True).item()
uid2bert = np.load('../data/douban/uid2bert.npy', allow_pickle=True).item()

bertL = 4

kg_bert = np.load('../data/douban/20wbert/kg_bert.npy', allow_pickle=True)
bert_len = len(kg_bert)
kg_final = []
num = 0
relation_id2index = dict()
relation_cnt = 0
for line in open('../data/douban/kg.txt', encoding='utf-8'):
    if num >= bert_len:
        break
    array = line.strip().split('\t')
    relation = array[1]
    if relation not in relation_id2index:
        relation_id2index[relation] = relation_cnt
        relation_cnt += 1
    relation = relation_id2index[relation]
    writer = [uid2bert[array[0]][:, :bertL], relation, idx2bert[word2idx[array[2]]][:, :bertL]]
    kg_final.append(writer)
    num += 1
kg_final = np.array(kg_final)
np.save('../data/douban/kg_final.npy', kg_final)


user_cnt = 0

item_set = set(uid2bert.keys())
user_pos_ratings = dict()
user_neg_ratings = dict()
for line in open('../data/douban/douban_ratings.txt').readlines()[1:]:
    array = line.strip().split('\t')

    uid = array[1]
    if uid not in uid2bert.keys():  # the item is not in the final item set
        continue
    # movie_bert = uid2bert[uid]

    user_index_old = int(array[0])
    rating = float(array[2])
    if rating >= 4:
        if user_index_old not in user_pos_ratings:
            user_pos_ratings[user_index_old] = set()
        user_pos_ratings[user_index_old].add(uid)
    else:
        if user_index_old not in user_neg_ratings:
            user_neg_ratings[user_index_old] = set()
        user_neg_ratings[user_index_old].add(uid)

user_index_old2new = dict()
print('converting rating file ...')
writer = []
user_cnt = 0
user_index_old2new = dict()
for user_index_old, pos_item_set in user_pos_ratings.items():
    if user_index_old not in user_index_old2new:
        user_index_old2new[user_index_old] = user_cnt
        user_cnt += 1
    user_index = user_index_old2new[user_index_old]

    for item in pos_item_set:
        writer.append([user_index, uid2bert[item][:, :bertL], 1, item])
    unwatched_set = item_set - pos_item_set
    if user_index_old in user_neg_ratings:
        unwatched_set -= user_neg_ratings[user_index_old]
    for item in np.random.choice(list(unwatched_set), size=len(pos_item_set), replace=False):
        writer.append([user_index, uid2bert[item][:, :bertL], 0, item])
writer = np.array(writer)
np.save('../data/douban/ratings_final.npy', writer)