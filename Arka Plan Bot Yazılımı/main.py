# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 00:10:36 2022

@author: hasan
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.opera.options import Options#Chrome için opera yerien Chrome.options yazarız.
import time
from pyautogui import *



options = Options()
options.headless = True

driver = webdriver.Opera(options=options)
driver.get("https://www.instagram.com")