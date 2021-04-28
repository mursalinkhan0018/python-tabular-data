#! /usr/bin/env python3

"A script to perform the linear regression and create the plot."
import sys
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy

def main(dataframe):
	dataframe = pd.read_csv(sys.argv[1], error_bad_lines=False)
	groups ="species"
	x_col="petal_length_cm"
	y_col="sepal_length_cm"
	if groups:
		grouped_dataframes = dataframe.groupby(groups)
	else:
		grouped_dataframes = ('all', dataframe),

	color_index = 1
	for category, df in grouped_dataframes:
		x = df[x_col]
		y = df[y_col]
		regression = stats.linregress(x, y)
		slope = regression.slope
		intercept = regression.intercept
		plt.scatter(x, y, label = category, color = 'C' + str(color_index))
		plt.plot(x,slope * x +intercept, color = 'C' +str(color_index),label = category)
		color_index += 1
		plt.xlabel(x_col)
		plt.ylabel(y_col)
		plt.legend()
		plt.savefig("qqq-Petal vs sepal length.png")

if __name__ == '__main__':
	main(sys.argv[1])