import sys
import json
import codecs
import glob

DATA_PATH = sys.argv[1]
FILES = DATA_PATH + "/*/STT/*-R[WS]*.json"
SAVE_PATH = sys.argv[2]

def get_script_utterance(json_file):
    file_basename = json_file.split('/')[-1].rsplit('.',1)[0]
    w = codecs.open(SAVE_PATH + '/' + file_basename + '_16k.txt', 'w', encoding='utf-8')
    st_python = json.load(open(json_file))
    script_utt = st_python['QuestionInfo']['description']
    w.write(script_utt)
    w.close()

def main():
    for f in glob.glob(FILES):
        get_script_utterance(f)

if __name__ == '__main__':
    main()
