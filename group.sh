#!/bin/bash

source config.sh

USAGE="./data.sh dataGroup"

if [[ $# -ne 1 ]]; then
  echo "$USAGE"
  exit
fi

DATA_GROUP=$1
# echo "$DATA_GROUP"

mkdir -p $OUT_DIR
mkdir -p $BOLD_DIR

for subjectDir in $DATA_GROUP/*; do
  subject="$(basename $subjectDir)"

  boldData=$subjectDir/$SUBJECT_DATA/$TASK/$BOLD_FILE

  condition=$($SRC_DIR/condition.py $META_DIR/$META_FILE $subject)
  outFile="$OUT_DIR/$subject$OUT_FILE_EXT"
  $(cp $boldData $BOLD_DIR/$subject.$BOLD_FILE_EXT)

  echo "$boldData -> $outFile"

  $($SRC_DIR/niftiToCsv.py $boldData $condition > $outFile)
done
