#!/usr/bin/python

# ./spark-submit spark.py fmriData.csv

import sys
import os

from pyspark import SparkContext
from pyspark.mllib.classification import LogisticRegressionWithSGD
from pyspark.mllib.regression import LabeledPoint
from numpy import array

if __name__ == "__main__":

  csvName = sys.argv[1]
  path = os.path.realpath( csvName )

  context = SparkContext( 'local', 'fmri analysis' )
  context.addFile( path )

  
