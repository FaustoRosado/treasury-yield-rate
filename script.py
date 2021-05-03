#!/env/bin/python3

import datetime as dt

from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import requests


url = 'https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yield'

def scrape_data(url):
    print("scraping")
    
    yield_curve = pd.read_html(url) 
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
    data = scrape_data(url)

    plt.style.use('ggplot')
    plt.figure(figsize=(12, 10))
    # plt.plot(yield_curve_10_2['date'], yield_curve_10_2['10 yr'], yield_curve_10_2['2 yr'])
    plt.plot(data['date'], data['10 yr'], "-b", label="10 year")
    plt.plot(data['date'], data['2 yr'], "-r", label="2 year")

    plt.title('10 year & 2 year Treasury Rates for April 2021')
    plt.xlabel('Date')
    plt.xticks(rotation=45, fontsize='medium')
    plt.ylabel('Interest Rate')
    plt.legend()
    # plt.show()
    # plt.plot(data)
    plt.savefig(f'charts/{filename}.png')
    print("completed")

    plt.style.use('ggplot')
    plt.figure(figsize=(12, 10))
    plt.plot(data['date'], data['10yr - 2yr'], 'g--', label='10-2 Yr Spread')
    plt.title('10-2 Treasury Yield Spread for April 2021')
    plt.xlabel('Date')
    plt.xticks(rotation=45, fontsize='medium')
    plt.ylabel('10-2 Spread')
    plt.legend()
    

    plt.savefig(f'charts/{filename}.png')
    print("completed")


def main():
    data = scrape_data(url)
    dt_now = dt.datetime.now()
    dt_fmt = dt_now.strftime("%m-%d-%y-%H%M%S")
    make_chart(np.arange(10), f'10_2-yield-curve-{dt_fmt}')

if __name__ == '__main__':
    main()
