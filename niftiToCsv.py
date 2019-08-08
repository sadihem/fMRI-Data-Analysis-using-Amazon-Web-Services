#!/usr/bin/python

# Requires installation of NiBabel, Numpy
#   sudo pip install nibabel
#   sudo pip install numpy
#   
# USAGE: ./csv frmiData condition

import logging
import sys
import nibabel as nib
import numpy as np

USAGE = './csv.py niftiFile condition'

logging.basicConfig( level=logging.INFO )
logger = logging.getLogger( __name__ )


if __name__ == "__main__":

  if len( sys.argv ) != 3 :
    logger.error( USAGE )
    sys.exit(0)

  niftiName = sys.argv[1]
  condition = sys.argv[2]

  img = nib.load( niftiName )
  img_data = img.get_data()

  # http://docs.scipy.org/doc/numpy/reference/arrays.nditer.html#tracking-an-index-or-multi-index
  it = np.nditer(img_data, flags=['multi_index'])
  while not it.finished:
    lastIndex = len(it.multi_index) - 1
    timeStep = it.multi_index[ lastIndex ]
    indices = ', '.join( str(x) for x in it.multi_index[0:lastIndex] )

    # indices = ', '.join( str(x) for x in it.multi_index )
    intensity = str( it[0] )

    print '{0}, {1}, {2}, {3}'.format(condition, timeStep, indices, intensity)
    it.iternext()


  
