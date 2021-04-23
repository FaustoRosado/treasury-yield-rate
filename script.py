#!/env/bin/python3

import datetime as dt

from bs4 import BeautifulSoup as bs
import matplotlib.pyplot as plt
import numpy as np
import requests

def scrape_data():
    print("scraping")
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
