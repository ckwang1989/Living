import os

def get_price_vol_daily(csv_p):
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
				Dates.append(Date)
				Open_last, High_last, Low_last, Close_last, Volume_last = Open, High, Low, Close, Volume
	return Closes, Opens, Lowes, Highes, Volumes, Dates