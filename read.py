#!/usr/bin/python

# Requires installation of NiBabel, Matplotlib, Numpy
#   sudo pip install nibabel
#   sudo pip install matplotlib
#   sudo pip install numpy
#   
# USAGE: ./read frmiData

import sys
import nibabel as nib
import matplotlib.pyplot as plt

def show_slices(slices):
  """ Function to display row of image slices """
  print 'show_slices(slices)'
  fig, axes = plt.subplots(1, len(slices))
  for i, slice in enumerate(slices):
    axes[i].imshow(slice.T, cmap="gray", origin="lower")


if __name__ == "__main__":

  niftiName = sys.argv[1]

  img = nib.load( niftiName )
  img_data = img.get_data()

  slice_0 = img_data[26, :, :, 0] # yz plane at x = 26 and t = 0
  slice_1 = img_data[:, 30, :, 0] # xz plane at y = 30 and t = 0
  slice_2 = img_data[:, :, 16, 0] # xy plane at z = 16 and t = 0

  # Same slice at diffent time steps
  # slice_0 = img_data[40, :, :, 0]
  # slice_1 = img_data[40, :, :, 1]
  # slice_2 = img_data[40, :, :, 136]

  # Intesity at a certain point at a certain time
  # print 'img_data[26, 30, 16, 0]: ' + str( img_data[26, 30, 16, 0] )

  show_slices( [ slice_0, slice_1, slice_2 ] )
  plt.suptitle( "Slices for fMRI image" )
  plt.show()


  
