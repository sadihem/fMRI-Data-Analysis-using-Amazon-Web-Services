#!/usr/bin/python

import logging
import sys
import csv

USAGE = './condition.py demographicFile subcodeQuery'

logging.basicConfig( level=logging.INFO )
logger = logging.getLogger( __name__ )


def conditionToInt(condition):
  condition = str(condition)
  if condition == "SCZ" or condition == "SCZ-SIB":
    return 1
  return 0



if __name__ == "__main__":

  if len( sys.argv ) != 3 :
    logger.error( USAGE )
    sys.exit(0)

  demographicFileName = sys.argv[1]
  subcodeQuery = sys.argv[2]

  with open( demographicFileName, "r" ) as demographicFileObject:
    demographicFileReader = csv.DictReader( demographicFileObject, delimiter='\t' )
    
    for row in demographicFileReader:
      if subcodeQuery == row[ 'subcode' ]:
        print '{0}'.format( conditionToInt( row[ 'condit' ] ) )
        # print '{0}, {1}'.format( conditionToInt( row[ 'condit' ] ), row[ 'condit' ] )
        sys.exit(0)

  print 'error: {0} was not found'.format( subcodeQuery )
  sys.exit(0)
  