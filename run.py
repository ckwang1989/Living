import os
import pandas as pd
import numpy as np

from utils.io import get_price_vol_daily, plot



def main():
	p = '/Users/Wiz/Downloads/AMD.csv'
	Closes, Opens, Lowes, Highes, Volumes, Dates = get_price_vol_daily(p)
	plot(np.asarray(Dates), np.asarray([Highes, Lowes]).T, Dates)

if __name__ == '__main__':
	main()
