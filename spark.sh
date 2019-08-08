#!/bin/bash

SPARK_DIR=spark
SPARK_AWS=$SPARK_DIR/ec2/spark-ec2

CLUSTER=fmri
KEY_PAIR=data
IDENTITY_FILE=confidential/$KEY_PAIR.pem
INSTANCE=m3.xlarge
REGION=us-west-2
ZONE=us-west-2a
NUM_SLAVES=4

source confidential/config.sh

USAGE="./spark <action>\n\n<action> can be: launch, destroy, login, stop, start, get-master, reboot-slaves"

if [[ $# -ne 1 ]]; then
  echo -e "$USAGE"
  exit
fi

./$SPARK_AWS \
  --key-pair=$KEY_PAIR \
  --identity-file=$IDENTITY_FILE \
  --region=$REGION \
  --zone=$ZONE \
  --instance-type=$INSTANCE \
  --slaves=$NUM_SLAVES \
  $1 $CLUSTER
