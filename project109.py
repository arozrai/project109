import random
import csv
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv")
file_data = df["reading score"].tolist()

stdev1_list = [result for result in file_data if result > stdev_start1 and result < stdev_end1]
stdev2_list = [result for result in file_data if result > stdev_start2 and result < stdev_end2]
stdev3_list = [result for result in file_data if result > stdev_start3 and result < stdev_end3]

print("{}% of data lies within 1st standard deviation".format(len(stdev1_list)*100/len(file_data)))
print("{}% of data lies within 2nd standard deviation".format(len(stdev2_list)*100/len(file_data)))
print("{}% of data lies within 3rd standard deviation".format(len(stdev3_list)*100/len(file_data)))