import getData
import pandas as pd
import os
import sys


if not os.path.isdir("data"):
    os.mkdir("data")
    getData.getData()
    sys.exit("Data has been downloaded and is the downloads dir. Import the csv files into the associated 'data' dir")

if not os.path.isfile("2020-citibikedata.csv"):
    getData.cleanData()

if os.path.isfile("2020-citibikedata.csv"):
    getData.formatData()