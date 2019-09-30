# ReedRadialTechnical
Emma Reed's Radial Technical Challenge

# Requirements
Run using python 3.6.1 but should work with all stable verisons of python3

Required Libraries
-numpy
-matplotlib
-pandas

# To Run
To run the csv generation, run radial_technical.py from the command line. This does require there to be a "Hospital General Information.csv" in the same directory. This will produce a file called "hospitals_by_county.csv"

# Extra Credit
To determine the correlation of the "Mortality national comparison" and "Readmission national comparison" to the "Hospital Overall Rating", I generated box plots showing the spread of the ratings over the comparisons. There are images showing these plots as well as the code required to generate these plots. 

NOTE: In these graphs, 1 is "Below the national average", 2 is "Same as the National Average", 3 is "Above the national average"

I found that in the case of both variables, the minited categorical nature made it challenging to determine true correlation. While the graphs prove that there is loose correlation when comparing the medians, there is also a wide enough spread that the correlation seems irrelevant in both cases.
