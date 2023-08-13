# Omniverse

3 python files were uploaded:

# LaserPointerXT #
will show the 8 points of the 3d cube enclosing the objects (but projected as 2d XY pixels on the image)

# bboxDrawCSV  #
load from the CSV using the images paths and bboxes, the output will be all the images with their corresponding bbox drawn on them.

# combine_csv_column #
usages--> combine_csv_columns('A.csv', 'B.csv', 'c.csv')
it suumes the first column of A.csv need to be added as the last column in B.csv, and finaly is saved as C.csv.

it is also assumed that A and Bhave the same number of rows for the corresponding ID number (1 = LP, 0 = vehicle)

