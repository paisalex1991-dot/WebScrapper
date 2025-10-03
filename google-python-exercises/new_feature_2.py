import tkinter as tk
from tkinter import messagebox, filedialog
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import threading
import time

## text added for git testing


# Global variable for the results box
result_box = None

# Paths to your ChromeDriver and optional Chrome binary
CHROME_PATH = r"C:\01_PROGRAME\Chrome\chrome-win64\chrome-win64\chrome.exe"
CHROMEDRIVER_PATH  = r"C:\01_PROGRAME\Chrome\chromedriver-win64\chromedriver-win64\chromedriver.exe"

# Base URL
BASE_URL = "https://mcscertified.com/product-directory/"

def scrape_products_selenium():

    ### new_feature 2!!!!!!!!!!



def main():

##tbd

if __name__ == "__main__":
    main()