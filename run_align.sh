#!/usr/bin/env bash

stage=0

# Input directory should contain speaker-wise folders, each of which contains one or more wav-txt pairs
# (check 'samples' folder as an example)

if [ $# -lt 1 ]; then
    cat >&2 <<EOF

Incorrect inputs

Usage: $0 <data-dir>
 e.g.: $0 samples

EOF
    exit 1;
fi

BASE_PATH=nia_13_aligner # Change to your environment
SRC_DATA_PATH=$BASE_PATH/$1 # Change to your environment # nia_all
#SAVE_DATA_PATH="$SRC_DATA_PATH"_processed # Do not change
SAVE_DATA_PATH=$SRC_DATA_PATH # Do not change
TOOL_PATH=$BASE_PATH/data_prep_tools # Do not change

rm -rf $TOOL_PATH/align_output $TOOL_PATH/converted $TOOL_PATH/final $1_results

if [ ! -d $SAVE_DATA_PATH ]; then
  echo "Make $SAVE_DATA_PATH"
  echo " "
  mkdir $SAVE_DATA_PATH
fi

nj=$(nproc) # default uses the maximum number of processors / change if you want to decrease the number
corpus_directory=$SAVE_DATA_PATH
#dictionary_path=$TOOL_PATH/hangeul2phone_canonical_lg.txt
dictionary_path=$TOOL_PATH/nia_13_read_word2phone.txt
acoustic_model_path=$BASE_PATH/Documents/MFA/pretrained_models/acoustic/korean.zip  # Change {YOUR DIRECTORY} to your directory
output_directory=$TOOL_PATH/align_output
# MFA align on the data using hangeul2phone.txt
if [ $stage -le 0 ]; then
echo "STEP 7: MFA Align"
if [ -d $output_directory ]; then
echo "Refreshing $output_directory ..."
rm -rf $TOOL_PATH/align_output
fi
if [ ! -d $output_directory ]; then
echo "Using $nj processors"
mfa align --clean -j $nj $corpus_directory $dictionary_path $acoustic_model_path $output_directory
fi
echo "==> DONE"
echo " "
fi

# Convert phone2jamo
if [ $stage -le 1 ]; then
echo "STEP 8: Apply phone2jamo to aligned TextGrids"
if [ ! -d $TOOL_PATH/converted ]; then
mkdir  $TOOL_PATH/converted
fi
python3 $TOOL_PATH/phone2jamo_converter.py $output_directory $TOOL_PATH/phone2jamo_dict.txt "canonical" || exit 1
echo "==> DONE"
echo " "
fi

# Change TextGrid format
if [ $stage -le 2 ]; then
echo "STEP 9: Add additional tiers to finalize the TextGrid format"
if [ ! -d $TOOL_PATH/final ]; then
mkdir  $TOOL_PATH/final
fi
praat $TOOL_PATH/finalize.praat || exit 1
echo "==> DONE"
echo " "
fi

RESULT_PATH="$SRC_DATA_PATH"_results
if [ ! -d $RESULT_PATH ]; then
mkdir $RESULT_PATH
fi

# Copy the output TextGrids to the data dir
if [ $stage -le 3 ]; then
echo "STEP 10: Copy TextGrids to $RESULT_PATH"
cp $TOOL_PATH/final/*.TextGrid $RESULT_PATH
cp $SRC_DATA_PATH/*/*.wav $RESULT_PATH
rm -rf $RESULT_PATH/*.canonical.TextGrid
echo "==> DONE"
echo " "
fi

echo "PROCESS COMPLETE"
exit 0
