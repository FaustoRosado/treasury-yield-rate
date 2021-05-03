#!/env/bin/python3

import datetime as dt

from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt
import numpy as np
import requests

url = 'https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yield'

def scrape_data(url):
    print("scraping")
    
    yield_curve = pd.read_html(url, parse_dates = True) 
    yield_curve = yield_curve[1].dropna(how = 'any')

    yield_curve_10_2 = yield_curve.iloc[:,[0,6,10]]
    yield_curve_10_2.columns = ['date', '2 yr', '10 yr']

    yield_curve.iloc[:,[6,10]] = yield_curve_10_2[['2 yr', '10 yr']].astype(float)

    yield_curve_10_2['10yr - 2yr'] = yield_curve_10_2['10 yr'] - yield_curve_10_2['2 yr']

    return yield_curve_10_2
    #req = requests.get("https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yield")
    #soup = bs(req.text)

def make_chart(data, filename):
    print("generating matplotlib chart")
    plt.plot(data)
    plt.savefig(f'charts/{filename}.png')
    print("completed")

def main():
    scrape_data()
    dt_now = dt.datetime.now()
    dt_fmt = dt_now.strftime("%m-%d-%y-%H%M%S")
    make_chart(np.arange(10), f'test-{dt_fmt}')

if __name__ == '__main__':
    main()
