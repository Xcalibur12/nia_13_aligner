import sys
import os
import glob
import shutil

txt_path = sys.argv[1]
src_path = txt_path.rsplit('_', 1)[0]

for f in os.listdir(txt_path):
    fname = f.rsplit('.', 1)[0]
    spkr = fname.split('-')[0]
    wav = glob.glob(src_path + '/{}*/Audio/{}.wav'.format(spkr, fname))[0]
    shutil.copyfile(wav, txt_path + '/{}.wav'.format(fname))
