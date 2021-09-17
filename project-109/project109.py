import random
import csv
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("StudentsPerformance.csv"); 
file_data= df['math score'].tolist()

mean = statistics.mean(file_data)
mode = statistics.mode(file_data)
median = statistics.median(file_data)

deviation = statistics.stdev(file_data)

stdev_start1,stdev_end1 = mean-deviation,mean+deviation
stdev_start2,stdev_end2 = mean-(2*deviation),mean+(2*deviation)
stdev_start3,stdev_end3 = mean-(3*deviation),mean+(3*deviation)

fig = ff.create_distplot([file_data],["Result"],show_hist=False)

fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN")) 
fig.add_trace(go.Scatter(x=[stdev_start1, stdev_start1], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION start 1")) 
fig.add_trace(go.Scatter(x=[stdev_end1, stdev_end1], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1")) 
fig.add_trace(go.Scatter(x=[stdev_start2, stdev_start2], y=[0, 0.17], mode="lines", name="STANDARD start 2")) 
fig.add_trace(go.Scatter(x=[stdev_end2, stdev_end2], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))

fig.show()

stdev1_list = [result for result in file_data if result > stdev_start1 and result < stdev_end1]
stdev2_list = [result for result in file_data if result > stdev_start2 and result < stdev_end2]
stdev3_list = [result for result in file_data if result > stdev_start3 and result < stdev_end3]

print("{}% of data lies within 1st standard deviation".format(len(stdev1_list)*100/len(file_data)))
print("{}% of data lies within 2nd standard deviation".format(len(stdev2_list)*100/len(file_data)))
print("{}% of data lies within 3rd standard deviation".format(len(stdev3_list)*100/len(file_data)))