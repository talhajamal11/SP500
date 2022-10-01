# using Yahoo Finance API
import requests
import matplotlib as mpl
import numpy as np
import json
from yahoo_fin import stock_info as SI
import datetime

amazon_weekly = SI.get_data("amzn", start_date="01/01/2010",
                            end_date="09/16/2022", index_as_date=True, interval="1d")

print(amazon_weekly)
