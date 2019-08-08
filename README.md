#fMRI

- Apache Spark
  - https://spark.apache.org/docs/latest/

- NiBabel
  - NIfTI1
    - http://nipy.sourceforge.net/nibabel/

- fMRI Visualization
  - http://www.brainvoyager.com/index.html

- Create an AWS Account
- Get AWS Access Key ID and AWS Secret Access Key
  - Add both to confidential/config.sh
- Get SSH RSA Key-Pair
  - Add to confidential/
  - Add to spark.sh
- ./spark.sh login
- mkdir -p data
- aws s3 sync s3://utk-eecs-fmri/fmri/ data


