import numpy as np

kg_bert = np.load('../data/douban/2wbert/kg_bert.npy', allow_pickle=True)
bert_len = len(kg_bert)

num = 0
e2e = {}
writer = open('../data/douban/kg.txt', 'w', encoding='utf-8')
for line in open('../data/douban/kg.txt', encoding='utf-8'):
    if num >= bert_len:
        break
    array = line.strip().split('\t')
    e2e[array[0]] = array[2]
    writer.write(line)
    num += 1
writer.close()

user_cnt = 0

item_set = set(e2e.keys())
user_pos_ratings = dict()
user_neg_ratings = dict()
for line in open('../data/douban/douban_ratings.txt', encoding='utf-8').readlines()[1:]:
    array = line.strip().split('\t')

    uid = array[1]
    if uid not in e2e.keys():  # the item is not in the final item set
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

print('converting rating file ...')
writer = open('../data/douban/douban_ratings.txt', 'w', encoding='utf-8')
user_cnt = 0
user_index_old2new = dict()
for user_index_old, pos_item_set in user_pos_ratings.items():
    if user_index_old not in user_index_old2new:
        user_index_old2new[user_index_old] = user_cnt
        user_cnt += 1
    user_index = user_index_old2new[user_index_old]

    for item in pos_item_set:
        writer.write('{}\t{}\t{}\n'.format(user_index, item, 1))
    unwatched_set = item_set - pos_item_set
    if user_index_old in user_neg_ratings:
        unwatched_set -= user_neg_ratings[user_index_old]
    for item in np.random.choice(list(unwatched_set), size=len(pos_item_set), replace=False):
        writer.write('{}\t{}\t{}\n'.format(user_index, item, 0))
writer.close()