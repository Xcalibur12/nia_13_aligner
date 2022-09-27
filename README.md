# nia_13_aligner

## 0. 사전 작업

* mfa align을 위한 conda 환경 설치\
설치 관련 링크: https://montreal-forced-aligner.readthedocs.io/en/latest/getting_started.html

* jamo 라이브러리 설치\
`pip install jamo`

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

강제정렬 할 모든 데이터가 들어있는 단일 폴더(input_data) 아래에 화자별 폴더와 그 아래에 wav-txt의 데이터쌍이 있어야 함.\
화자가 1명이더라도 화자 폴더를 만들고, 그 안에 wav-txt 데이터 쌍을 두어야 함.

## 2. nia_13_aligner 사용법
1. `git clone https://github.com/Xcalibur12/nia_13_aligner.git`
2. `cd nia_13_aligner`
3. `bash run_align.sh [INPUT_DATA_FOLDER]`\
e.g. `bash run_align.sh input_data`
