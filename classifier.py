#this script calculates the probability that a collection of fMRI 4D data point belong to a SZ patient:       normal==0  SZ==1
#all data shoud be seperated by spaces not comma's

from pyspark.mllib.classification import LogisticRegressionWithSGD
from pyspark.mllib.regression import LabeledPoint
from numpy import array
import numpy as np
import logging
import sys
import os
import time
from pyspark import SparkContext, SparkConf


# Load and parse the data 
def parsePoint(line):
  values = [float(x) for x in line.split(', ')]
  return LabeledPoint(values[0], values[1:])


USAGE = './condition.py trainFile testFile'

logging.basicConfig( level=logging.INFO )
logger = logging.getLogger( __name__ )

if __name__ == "__main__":

  if len( sys.argv ) != 3 :
    logger.error( USAGE )
    sys.exit(0)

  trainFile = sys.argv[1]
  testFile = sys.argv[2]

  sc = SparkContext("local", "SVM: Schizophrenia")

  trainData = sc.textFile( trainFile )
  # sc.parallelize( trainData )
  train = trainData.map( parsePoint )
  train.persist()

  testData = sc.textFile( testFile )
  # sc.parallelize( testData )
  test = testData.map( parsePoint )
  test.persist()

  model = LogisticRegressionWithSGD.train(train)
  labelsAndPreds = test.map(lambda p: (p.label, model.predict(p.features)))
  # accuracy = labelsAndPreds.filter(lambda (v, p): True if p == 1.0 else False ).count() / float(test.count())
  error = labelsAndPreds.filter(lambda (v, p): int(v) != int(p) ).count() / float(test.count())

  with open("error.txt", "w") as f:
    f.write( "Accuracy: {0}\n".format( 1 - error ) )
    f.write( "Error: {0}\n".format( error ) )

  labelsAndPreds.saveAsTextFile( str(time.time()) + ".txt" )

