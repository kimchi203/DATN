import time
import threading
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def DN_1(driver,p_username, p_password):
    driver.find_element(By.XPATH, "//input[@id='username']").clear()
    driver.find_element(By.XPATH, "//input[@id='password']").clear()
    driver.find_element(By.XPATH, "//input[@id='username']").send_keys(p_username)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys(p_password)
    driver.find_element(By.XPATH, "//button[@id='btnLogin']").click()
    # time.sleep(3)
    time.sleep(2)

def DN_2(driver,f_username, p_password):
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='username']").send_keys(f_username)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys(p_password)
    driver.find_element(By.XPATH, "//button[@id='btnLogin']").click()
    # time.sleep(3)
    time.sleep(2)

def DN_3(driver,p_username,f_password):
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='username']").clear()
    driver.find_element(By.XPATH, "//input[@id='password']").clear()
    driver.find_element(By.XPATH, "//input[@id='username']").send_keys(p_username)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys(f_password)
    driver.find_element(By.XPATH, "//button[@id='btnLogin']").click()
    # time.sleep(3)
    time.sleep(1)

def DN_4(driver,p_password):
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='username']").clear()
    driver.find_element(By.XPATH, "//input[@id='password']").clear()
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys(p_password)
    driver.find_element(By.XPATH, "//button[@id='btnLogin']").click()
    # time.sleep(3)
    time.sleep(2)

def DN_5(driver,p_username):
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='username']").clear()
    driver.find_element(By.XPATH, "//input[@id='password']").clear()
    driver.find_element(By.XPATH, "//input[@id='username']").send_keys(p_username)
    driver.find_element(By.XPATH, "//button[@id='btnLogin']").click()
    # time.sleep(3)
    time.sleep(1)

def DN_6(driver,c_username, c_password):
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='username']").clear()
    driver.find_element(By.XPATH, "//input[@id='password']").clear()
    driver.find_element(By.XPATH, "//input[@id='username']").send_keys(c_username)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys(c_password)
    driver.find_element(By.XPATH, "//button[@id='btnLogin']").click()
    # time.sleep(3)
    time.sleep(1)