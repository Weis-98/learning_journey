

writer = open('../../data/douban/kg_title2entity.txt', 'w', encoding='utf-8')
for line in open('../../data/douban/kg.txt', encoding='utf-8'):
    # line = line.replace(',', ' ')
    array = line.strip().split('\t')
    if array[1] == 'title':
        temp = array[2]
    else:
        # writer.write('{},{},{}\n'.format(temp, array[1], array[2]))
        writer.write('{}\t{}\t{}\n'.format(temp, array[1], array[2]))
writer.close()

