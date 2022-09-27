import os
import sys
import glob
from shutil import move

path = sys.argv[1]  # path to input data e.g. nia_13_aligner/example_data 
result_path = path + '_results'

for tgd in glob.glob(result_path + '/*.TextGrid'):
    wav = tgd.rsplit('.',1)[0] + '.wav'
    tgd_basename = tgd.rsplit('/',1)[-1]
    wav_basename = wav.rsplit('/',1)[-1]
    wav_from_path = glob.glob(path + '/*/{}'.format(wav_basename))[0]
    spkr_folder = wav_from_path.split('/')[-2]
    result_spkr_path = os.path.join(result_path, 'wav_align_complete', spkr_folder)
    if not os.path.exists(result_spkr_path):
        os.makedirs(result_spkr_path, exist_ok=True)
    move(wav, result_spkr_path + '/' + wav_basename)
    move(tgd, result_spkr_path + '/' + tgd_basename)


remained_wav_list = glob.glob(result_path + '/*.wav')
if len(remained_wav_list) != 0:
    os.mkdir(result_path + '/wav_align_failed')
for i in range(len(remained_wav_list)):
    move(remained_wav_list[i], result_path + '/wav_align_failed/{}'.format(remained_wav_list[i].rsplit('/',1)[-1]))
