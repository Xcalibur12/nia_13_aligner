import os
import sys
import shutil

path = sys.argv[1]  # '/data2/16k/16k_nia_v5/tgd_final_v3'

for f in sorted(os.listdir(path)):
    if f.endswith('.TextGrid'):
        spkr = f.split('-')[0]
        file_basename = f.rsplit('.',1)[0]
        if not os.path.exists(path + '/' + spkr):
            os.makedirs(path + '/' + spkr)
        shutil.move(path + '/' + file_basename + '.wav', path + '/' + spkr + '/')
        shutil.move(path + '/' + file_basename + '.TextGrid', path + '/' + spkr + '/')
        #shutil.move(path + '/' + file_basename + '.txt', path + '/' + spkr + '/')
