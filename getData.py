import os
from selenium import webdriver
import time
import pandas as pd

def getData():
    driver = webdriver.Chrome()
    for x in range(1,13):
        if x < 10:
            x = f'0{x}'
        driver.get(f"https://s3.amazonaws.com/tripdata/2020{x}-citibike-tripdata.csv.zip")
    time.sleep(60)
    driver.close()
    driver.quit()

def cleanData():
    files = os.listdir("data")
    data = dict()
    for file in files:
        df = pd.read_csv("data/" +  file, low_memory=False)
        if not len(data):
            for x in df.columns:
                data[x] = []
        df = df.sample(n=int(.1*len(df)), random_state=5)
        for x in df.columns:
            data[x] = data[x] + df[x].tolist()
    pd.DataFrame(data).to_csv('2020-citibikedata.csv', index=False)

def formatData():
    df = pd.read_csv("2020-citibikedata.csv", low_memory=False)
    df.loc[df["gender"] == 0, "gender"] = "other"
    df.loc[df["gender"] == 1, "gender"] = "male"
    df.loc[df["gender"] == 2, "gender"] = "female"
    df.to_csv("2020-citibikedata.csv", index=False)