import sys
import codecs
from jamo import h2j, j2hcj

input_file = sys.argv[1]
input_file_name = input_file.split('/')[-1].split('.')[0]
word_list = []
for line in codecs.open(input_file, 'r', encoding='utf-8').readlines():
    line = line.strip()
    words = line.split()
    word_list.extend(words)

word_list = list(set(word_list))

data_type = input_file.split('/')[-1].split('_')[2]

w1 = codecs.open(sys.argv[2], 'w', encoding='utf-8')
w2 = codecs.open(sys.argv[3], 'w', encoding='utf-8')

for wrd in word_list:
    jamo_str = j2hcj(h2j(wrd))
    w1.write("{} {}\n".format(wrd, jamo_str))
    w2.write("{}\n".format(jamo_str))

w1.close()
w2.close()
