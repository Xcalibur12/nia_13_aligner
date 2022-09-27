import os
import sys
import codecs

INPUT_PATH = sys.argv[1]  #'./output/w2v2/'  # TextGrid
p2j_file = sys.argv[2] #'./phone2jamo_dict.txt'
data_type = sys.argv[3]

def make_phone2jamo_dict(p2j_file):
    p2j_dict = {}
    for line in codecs.open(p2j_file, 'r', encoding='utf-8').readlines():
        line = line.strip()
        phone, jamo = line.split()[0], line.split()[1]
        p2j_dict[phone] = jamo
    return p2j_dict

def convert_phone2jamo_textgrid(p2j_dict, INPUT_PATH):
    for spkr in os.listdir(INPUT_PATH):
        spkr_path = os.path.join(INPUT_PATH, spkr)
        for f in os.listdir(spkr_path):
            if f.endswith('.TextGrid'):
                w = codecs.open('data_prep_tools/converted/{}.{}.TextGrid'.format(f.rsplit('.',1)[0], data_type), 'w', encoding='utf-8')
                for line in codecs.open(INPUT_PATH + '/' + spkr + '/' + f, 'r', encoding='utf-8').readlines():
                    line = line.strip()
                    if '"' in line:
                        phone = line.split('"')[1]
                        if phone in p2j_dict.keys():
                            new_line = '"{}"'.format(p2j_dict[phone])
                            w.write(new_line + '\n')
                        else:
                            w.write(line + '\n')
                    else:
                        w.write(line + '\n')

def main():
    p2j_dict = make_phone2jamo_dict(p2j_file)
    convert_phone2jamo_textgrid(p2j_dict, INPUT_PATH)

if __name__ == '__main__':
    main()
