#! /usr/bin/env python3

"A script to perform the linear regression and create the plot."

import sys
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

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
    plt.plot(x,slope *x +intercept, color = 'C' +str(color_index),label = category)
    color_index += 1
plt.xlabel(x_col)
plt.ylabel(y_col)
plt.legend()
plt.savefig("XXXXX-Petal vs sepal length.png")

quit()



#alternative ways 

x1 = Iris_virginica.petal_length_cm
y1 = Iris_virginica.sepal_length_cm
regression = stats.linregress(x1, y1)
slope = regression.slope
intercept = regression.intercept
plt.scatter(x1, y1, label = 'Iris_virginica')
plt.plot(x1, slope * x1 + intercept, color = "orange", label = 'Iris_virginica line')

x2 = Iris_setosa.petal_length_cm
y2 = Iris_setosa.sepal_length_cm
regression = stats.linregress(x2, y2)
slope = regression.slope
intercept = regression.intercept
plt.scatter(x2, y2, label = 'Iris_setosa')
plt.plot(x2, slope * x2 + intercept, color = "red", label = 'Iris_setosa line')

x3 = Iris_versicolor.petal_length_cm
y3 = Iris_versicolor.sepal_length_cm
regression = stats.linregress(x3, y3)
slope = regression.slope
intercept = regression.intercept
plt.scatter(x3, y3, label = 'Iris_versicolor')
plt.plot(x3, slope * x3 + intercept, color = "blue", label = 'Iris_versicolor line')

plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.legend()
plt.savefig("AA-Iris_virginica petal vs sepal length.png")
quit()

#Three plots in one figures

dataframe = pd.read_csv(sys.argv[1], error_bad_lines=False)
Iris_virginica = dataframe[dataframe.species == "Iris_virginica"]
Iris_setosa = dataframe[dataframe.species == "Iris_setosa"]
Iris_versicolor = dataframe[dataframe.species == "Iris_versicolor"]
#print(Iris_versicolor)
#fig =plt.figure()
plt.figure()

x1 = Iris_virginica.petal_length_cm
y1 = Iris_virginica.sepal_length_cm
regression = stats.linregress(x1, y1)
slope = regression.slope
intercept = regression.intercept
plt.subplot(3,1,1)
plt.scatter(x1, y1, label = 'Data')
plt.plot(x1, slope * x1 + intercept, color = "orange", label = 'Fitted line')
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.legend()
#plt.savefig("Iris_virginica petal vs sepal length.png")
#quit()


x2 = Iris_setosa.petal_length_cm
y2 = Iris_setosa.sepal_length_cm
regression = stats.linregress(x2, y2)
slope = regression.slope
intercept = regression.intercept
plt.subplot(3,1,2)
plt.scatter(x2, y2, label = 'Data')
plt.plot(x2, slope * x2 + intercept, color = "orange", label = 'Fitted line')
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.legend()
#plt.savefig("Iris_setosa petal vs sepal length.png")
#quit()


x3 = Iris_versicolor.petal_length_cm
y3 = Iris_versicolor.sepal_length_cm
regression = stats.linregress(x3, y3)
slope = regression.slope
intercept = regression.intercept
plt.subplot(3,1,3)
plt.scatter(x3, y3, label = 'Data')
plt.plot(x3, slope * x3 + intercept, color = "orange", label = 'Fitted line')
plt.xlabel("Petal length (cm)")
plt.ylabel("Sepal length (cm)")
plt.legend()
#plt.savefig("Iris versicolor petal vs sepal length.png")
#fig.savefig("test2.png")
plt.savefig("Petal vs Sepal length.png")
#quit()

#print(__name__)
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print ('You failed to provide proper input ')
    sys.exit(1)  # abort because of error

