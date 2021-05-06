

## YOUR CODE HERE


#!/usr/bin/env python

"""

ABOUT:
    script to create a correlation matrix from world happiness data

DATA:
    data produced by: http://unsdsn.org/about-us/vision-and-organization
    data compilied from: https://worldhappiness.report


DIRECTORIES
    You can modify the DATA_DIR and IMAGE_DIR directly or create a directory called 'data'
    and another called 'images'.  Ensure the csv file is in the data dir

"""

import os
import re
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


## plot style, fonts and colors
sns.set(style="ticks", color_codes=True)

DATA_DIR = os.path.join("..","data") 
IMAGE_DIR = os.path.join("..","images")

def run_data_ingestion():
    """
    ready the data for EDA
    """

    print("... data ingestion")
    
    ## load the data and print the shape
    df = pd.read_csv(os.path.join(DATA_DIR,"world-happiness.csv"),index_col=0)

    ## clean up the column names
    df.columns = [re.sub("\s+","_",col) for col in df.columns.tolist()]

    ## drop the rows that have NaNs
    df.dropna(inplace=True)

    ## sort the data for more intuitive visualization
    df.sort_values(['Year', "Happiness_Score"], ascending=[True, False], inplace=True)

    return(df)


def create_plot(df):
    """
    plotting a diagonal correlation matrix

    inspired by: https://seaborn.pydata.org/examples/many_pairwise_correlations.html
    """

    print("... creating plot")

    # Compute the correlation matrix
    corr = df.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(11, 9))

    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(230, 20, as_cmap=True)

    # Draw the heatmap with the mask and correct aspect ratio
    sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0, 
                square=True, linewidths=.5, cbar_kws={"shrink": .5})
    
    image_path = os.path.join(IMAGE_DIR,"happiness-correlation.png")
    plt.savefig(image_path,bbox_inches='tight',pad_inches = 0,dpi=200)
    print("{} created.".format(image_path))
    
if __name__ == "__main__":

   df = run_data_ingestion()
   create_plot(df)