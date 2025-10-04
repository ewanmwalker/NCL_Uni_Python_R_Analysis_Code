# -*- coding: utf-8 -*-
"""
Assessment 3 - Class Test

Q4
"""
#import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('music.csv')  

##
df1 = df[df["No_Ratings"]<800]


x = (df1.max())[4]






#df_2010s = df[(df["Year"]>2009) & (df["Year"]<2021)]
#ratings_2010s = df["Average_Rating"].to_numpy()


#dfcj = df[df["Genres"]=="Cool Jazz"]

#ar = dfcj["Average_Rating"].to_numpy()
#yr = dfcj["Year"].to_numpy()

#plt.plot(yr, ar, "-o")
