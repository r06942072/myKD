#from openpyxl import Workbook, load_workbook
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import Select


if __name__ == '__main__':
    # read from excel
    print("Start read from input.xlsx")
    df_in = pd.read_excel("input.xlsx")
    df_in_first_col = df_in.iloc[:,0] #first column
    stocks = df_in_first_col.tolist()
    print(stocks)

    # capture data from web
    print("Start selenium")
    browser = webdriver.Chrome()

    # write reporrt to excel
    print("Write to xlsx")

    print("Finish script")
