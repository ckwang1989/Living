import os
import pandas as pd

from utils.io import get_price_vol_daily

def main():
	p = '/Users/Wiz/Downloads/AMD.csv'
	Closes, Opens, Lowes, Highes, Volumes, Dates = get_price_vol_daily(p)



if __name__ == '__main__':
	main()
