import sys
import codecs

h2j_file = sys.argv[1] #'./aihub13_{}_hangeul2jamo.txt'.format(transcript_type) # read
j2p_file = sys.argv[2] #'./aihub13_{}_jamo2phone.txt'.format(transcript_type) # read
h2p_file = sys.argv[3] #'./aihub13_{}_hangeul2phone.txt'.format(transcript_type) # write

def make_jamo2hangeul_dict(h2j_file):
    j2h_dict = {}
    for line in codecs.open(h2j_file, 'r', encoding='utf-8').readlines():
        line = line.strip()
        #hangeul, jamo = line.split('\t')[0], line.split('\t')[1]
        hangeul, jamo = line.split()[0], ' '.join(line.split()[1:])
        j2h_dict[jamo] = hangeul
    return j2h_dict

def make_hangeul2phone(j2p_file, j2h_dict):
    w = codecs.open(h2p_file, 'w', encoding='utf-8')
    for line in codecs.open(j2p_file, 'r', encoding='utf-8').readlines():
        line = line.strip()
        jamo, phone = line.split('\t')[0], line.split('\t')[1]
        hangeul = j2h_dict[jamo]
        new_line = "{}\t{}\n".format(hangeul, phone)
        w.write(new_line)
    w.close()

def main():
    j2h_dict = make_jamo2hangeul_dict(h2j_file)
    make_hangeul2phone(j2p_file, j2h_dict)

if __name__ == '__main__':
    main()
