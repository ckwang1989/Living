# plot
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

def get_price_vol_daily(csv_p):
	''' load price & volume from csv file
		input :
			csv_p: the path of csv

		output:
			Closes, Opens, Lowes, Highes, Volumes, Dates: type is list(1d)
	'''
	Dates, Opens, Closes, Lowes, Highes, Volumes = [], [], [], [], [], []
	Open_last, High_last, Low_last, Close_last, Volume_last = 0, 0, 0, 0, 0
	with open(csv_p, 'r') as f_r:
		for idx, line in enumerate(f_r.readlines()):
			if idx:
				line = line.split(',')
				Date, Open, High, Low, Close, Adj_Close, Volume = line[0], line[1], line[2], line[3], line[4], line[5], (line[6].strip('\n'))
				if Open == 'null' or High == 'null' or Low == 'null' or Close == 'null' or Volume == 'null':
					Open, High, Low, Close, Volume = Open_last, High_last, Low_last, Close_last, Volume_last
				Closes.append(float(Close))
				Opens.append(float(Open))
				Lowes.append(float(Low))
				Highes.append(float(High))
				Volumes.append(int(Volume))
				#if '-01-02' in Date:
				Dates.append(Date[2:])
				#else:
				#	Dates.append('')
				Open_last, High_last, Low_last, Close_last, Volume_last = Open, High, Low, Close, Volume
	return Closes, Opens, Lowes, Highes, Volumes, Dates

def plot(x, y, start_date, x_axis_interval=200):
	# https://blog.csdn.net/funnyPython/article/details/83925573?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task

	''' plot a 2d(x,y) curve
		input :
			x: the date, from earliest date in hostorical data, shape is (num of date, )
			y: the price, shape is (num of date, num of price curve)
			start_date: the earliest date

		output:
			2d curve
	'''
	# the param of plot
	mpl.rcParams['lines.linewidth'] = 1
	mpl.rcParams['figure.figsize'] = (15, 15)
	plt.gcf().set_size_inches(15, 15)

	ax=plt.gca()
	a = list(range(len(x)))
	plt.xticks(a, x, rotation=90, fontsize=10)
	for label in ax.get_xticklabels():
		label.set_visible(False)
	for label in ax.get_xticklabels()[::x_axis_interval]:
		label.set_visible(True)

	plt.plot(x, y)
	plt.show()
