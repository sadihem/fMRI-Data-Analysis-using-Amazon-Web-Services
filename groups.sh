#!/bin/bash

source config.sh

for dataGroup in $GROUPS_DIR/*; do
  $DATA_DIR/group.sh $dataGroup
done