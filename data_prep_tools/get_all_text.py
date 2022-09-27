import sys
import os
import codecs

SAVE_DATA_PATH = sys.argv[1]
TOOL_PATH_FILE = sys.argv[2] # TOOL_PATH + filename (canonical or actual)

w = codecs.open(TOOL_PATH_FILE, 'w', encoding='utf-8')

for f in sorted(os.listdir(SAVE_DATA_PATH)):
    if f.endswith('.txt'):
        utt = codecs.open(SAVE_DATA_PATH + '/' + f, 'r', encoding='utf-8').read()
        w.write('{}\n'.format(utt))

w.close()
