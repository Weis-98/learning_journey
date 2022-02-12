import argparse
import numpy as np

def split_method(relation, strings):
    split_task = {
        'tags': '#',
        'type': " / ",
        'directors': ' / ',
        'writers': ' / ',
        'actors': ' / '
    }
    if relation in split_task.keys():
        items = strings.strip().split(split_task[relation])
        j = 0
        for i in range(len(items)):
            if items[j] == '':
                items.pop(j)
            else:
                j += 1
    elif relation == 'reviews_count':
        items = strings.strip().split(' ')
        items = [items[1]]
    elif relation == 'rating_people':
        items = [strings[:-3]]
    else:
        items = [strings]
    return items


def csv2KG():
    file = '../data/' + DATASET + '/movie_br.txt'
    print('reading csv file: ' + file + ' ...')
    number2id = open('../data/' + DATASET + '/item_index2entity_id.txt', 'w', encoding='utf-8')
    writer = open('../data/' + DATASET + '/kg.txt', 'w', encoding='utf-8')

    keys = ["number", "id", "title", "rate", "rating_people", "directors",
            "writers", "actors", "type", "reviews_count", "tags"]
    tails = ["title", "rate", "rating_people", "directors",
            "writers", "actors", "type", "reviews_count", "tags"]
    num2keys = {}
    for i, item in enumerate(keys):
        num2keys[i] = item

    for line in open(file, encoding='utf-8').readlines():
        values = line.strip().split('\t')
        if values[0] == '"number"':
            continue
        number2id.write('%s\t%s\n' % (values[1][1:-1], values[1][1:-1]))

        for k, v in num2keys.items():
            if v in tails and values[k] and values[k] != '""' and values[k]!= '"None"':
                items = split_method(v, values[k][1:-1])
                for item in items:
                    writer.write('%s\t%s\t%s\n' % (values[1][1:-1], v, item))
    writer.close()
    number2id.close()

def csv2Rating():
    file = '../data/' + DATASET + '/user_br.txt'
    print('reading csv file: ' + file + ' ...')
    writer = open('../data/' + DATASET + '/douban_ratings.txt', 'w', encoding='utf-8')
    writer.write('"user_id";"ID";"Rating"\n')
    tag_writer = open('../data/' + DATASET + '/tags.txt', 'w', encoding='utf-8')
    tag_writer.write('"user_id";"tag";"counts"\n')
    for line in open(file, encoding='utf-8').readlines():
        values = line.strip().split('\t')
        if values[1] == 'name':
            continue
        user_id = values[0]
        user_name = values[1]

        rate = eval(values[2])
        for key, value in rate.items():
            writer.write('{}\t{}\t{}\n'.format(user_id, key, value))

        tags = eval(values[3])
        for key, value in tags.items():
            tag_writer.write('{}\t{}\t{}\n'.format(user_id, key, value))

    writer.close()
    tag_writer.close()




if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('-d', type=str, default='douban', help='which dataset to preprocess')
    args = parser.parse_args()
    DATASET = args.d

    csv2KG()
    csv2Rating()

