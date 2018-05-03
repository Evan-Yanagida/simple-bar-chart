import matplotlib.pyplot as plt

#See Line 39
#Calculate x_offset (in order to center text for number of steps walked each day to each bar)
def calc_x_offset(steps_walked_value):
	num_of_digits = len(str(steps_walked_value))
	x_offset = .925 - (num_of_digits - 1)*.075

	return x_offset

#INPUT DATA
days_of_the_week = [1,2,3,4,5,6,7]
steps_walked = [10, 1200, 1, 2379, 300, 2329, 6541]

#See Line 39
#Allows the labeling of number of steps (blue bold text) to work
fig, ax = plt.subplots() 

x = days_of_the_week
y = steps_walked
plt.bar(x, y)


#TEXT: Hide y-axis label and ticks
cur_axes = plt.gca()
cur_axes.axes.get_yaxis().set_visible(False)

#TEXT: Set x-axis label and ticks
labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
plt.xlabel('Day of the Week', weight="semibold", size='medium')
plt.xticks(x, labels, rotation='vertical', fontname="monospace", size='x-small')

#TEXT: Set title for the bar chart
plt.title('Sweatcoin Steps', weight="black", size="xx-large")

#TEXT: Add the values for number of steps walked, to the ends of each bar, in blue bold font
#Also centers these values to the bar adaptively regardless of variance in how many digits there are for number of steps
for i, v in enumerate(y):
    ax.text(i + calc_x_offset(steps_walked[i]), v + .25, str(steps_walked[i]), color="blue", fontweight="bold")

#SPACING: Set a bottom margin to fit x-axis' text into the figure
plt.subplots_adjust(bottom=0.25)


#Display the bar chart
plt.show()