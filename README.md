# NIA 13번 과제 강제정렬 툴킷 사용 매뉴얼

## 0. 사전 작업

* 본 모델은 Linux 환경에서 제작되었으며, Linux 환경에서 사용할 것을 권장함.

* mfa align을 위한 conda 환경 설치\
설치 관련 링크: [Montreal Forced Aligner](https://montreal-forced-aligner.readthedocs.io/en/latest/getting_started.html) \
conda aligner 환경 만든 후 `conda activate aligner`로 환경 접속

* Linux 환경의 praat 설치\
`sudo apt-get install praat`\
관련 링크: https://www.fon.hum.uva.nl/praat/download_linux.html

## 1. 입력 데이터 구조

``` bash
input_data
├── spkr_01
│   ├── spkr_01_utt_01.txt
│   ├── spkr_01_utt_01.wav
│   ├── spkr_01_utt_02.txt
│   └── spkr_01_utt_02.wav
├── spkr_02
│   ├── spkr_02_utt_01.txt
│   └── spkr_02_utt_01.wav
└── spkr_03
    ├── spkr_03_utt_01.txt
    └── spkr_03_utt_01.wav
```

* 강제정렬 할 모든 데이터가 들어있는 단일 폴더(input_data) 아래에 화자별 폴더와 그 아래에 wav-txt의 데이터쌍이 있어야 함.\
화자가 1명이더라도 화자 폴더를 만들고, 그 안에 wav-txt 데이터 쌍을 두어야 함.

* 음성 파일은 wav 파일, 모노 채널, 16-bit precision, sampling rate 16000Hz로 변환하여 사용하는 것을 권장.\
변환 툴킷 중 `sox` 사용하면 편리하게 변환할 수 있음.\
e.g. `sox input.mp3 -c 1 -b 16 -r 16000 output.wav`

## 2. nia_13_aligner 사용법
1. `git clone https://github.com/Xcalibur12/nia_13_aligner.git`
2. 준비해둔 input_data 폴더를 nia_13_aligner로 이동/복사\
e.g. `cp -r input_data nia_13_aligner/`
3. `cd nia_13_aligner`
4. `bash run_align.sh [INPUT_DATA_FOLDER]`\
e.g. `bash run_align.sh example_data`

## 3. 강제정렬 결과 확인
* `nia_13_aligner/[INPUT_DATA_FOLDER]_results`라는 폴더 생성
* results 폴더는 강제정렬에 성공한 wav_align_complete 폴더와 강제정렬을 하지 못한 wav_align_failed 폴더로 구성
* wav_align_complete 폴더는 다시 [INPUT_DATA_FOLDER]와 동일한 화자별 폴더로 구성되어 있으며, 그 안은 wav-TextGrid 데이터쌍으로 되어 있음
* 모든 데이터가 강제정렬에 성공하였을 때는 별도의 wav_align_failed 폴더는 만들어지지 않음

## 4. SPN 관련
* 강제정렬 결과 중 SPN이 포함되어 있다면 입력한 전사 파일이 NIA 13번 과제 대본에 나온 대로 작성되어 있지 않음을 의미
* 문장을 다시 확인하여 대본에 맞게 수정 필요
