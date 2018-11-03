import matplotlib.pyplot as plt

# x-coordinates of left side of bars
left = [1, 2, 3, 4, 5]

#heights of bar
height = [10, 24, 36, 40, 5]

#labels for bars
tick_label = ['one', 'two', 'three', 'four', 'five']

# ploting a bar chart
plt.bar(left,height, tick_label=tick_label,width=0.8, color=['red', 'green'])

#naming the x-axis
plt.xlabel('x-axis')
#naming the y-axis
plt.ylabel('y-axis')
#plot title
plt.title('my bar chart!')

#functions to show the plot 
plt.show()

