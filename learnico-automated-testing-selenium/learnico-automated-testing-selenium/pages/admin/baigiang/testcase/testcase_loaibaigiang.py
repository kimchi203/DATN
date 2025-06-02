import time
import threading
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

def LBG_T_1(driver, Tloaibaigiang, Tmotalbg):
    driver.find_element(By.XPATH, "(//h1[contains(text(),'Loại bài giảng')]/../../../..//button)[1]").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "name"))).send_keys(Tloaibaigiang)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "description"))).send_keys(Tmotalbg)
    driver.find_element(By.ID, "submitButton").click()
    driver.find_element(By.XPATH, "(//button[contains(text(),'Lưu')])[2]").click()

def LBG_T_2(driver, Ttenlbgbb):
    driver.find_element(By.XPATH, "(//h1[contains(text(),'Loại bài giảng')]/../../../..//button)[1]").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "name"))).send_keys(Ttenlbgbb)
    driver.find_element(By.ID, "submitButton").click()
    driver.find_element(By.XPATH, "(//button[contains(text(),'Lưu')])[2]").click()

def LBG_T_3(driver, Ttenlbgtrung):
    driver.find_element(By.XPATH, "(//h1[contains(text(),'Loại bài giảng')]/../../../..//button)[1]").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "name"))).send_keys(Ttenlbgtrung)
    driver.find_element(By.ID, "submitButton").click()
    driver.find_element(By.XPATH, "(//button[contains(text(),'Lưu')])[2]").click()

def LBG_T_4(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "name"))).clear()
    driver.find_element(By.ID, "submitButton").click()

def LBG_T_5(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Đóng')]"))).click()


def LBG_S_2(driver, Sloaibaigiang, Smotalbg):

    driver.find_element(By.CLASS_NAME, "btn-admin-edit").click()
    name_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "name")))
    name_input.clear()
    name_input.send_keys(Sloaibaigiang)

    desc_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "description")))
    desc_input.clear()
    desc_input.send_keys(Smotalbg)

    driver.find_element(By.ID, "submitButton").click()
    driver.find_element(By.XPATH, "(//button[contains(text(),'Lưu')])[2]").click()
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'OK')]"))).click()

def LBG_S_3(driver,Stenlbgbb):
    driver.find_element(By.CLASS_NAME, "btn-admin-edit").click()
    name_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "name")))
    name_input.clear()
    name_input.send_keys(Stenlbgbb)
    driver.find_element(By.ID, "submitButton").click()
    driver.find_element(By.XPATH, "(//button[contains(text(),'Lưu')])[2]").click()
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'OK')]"))).click()
def LBG_S_4(driver,Ttenlbgtrung):
    name_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "name")))
    name_input.clear()
    name_input.send_keys(Ttenlbgtrung)
    driver.find_element(By.ID, "submitButton").click()
    driver.find_element(By.XPATH, "(//button[contains(text(),'Lưu')])[2]").click()

def LBG_S_5(driver):
    name_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "name")))
    name_input.clear()
    driver.find_element(By.ID, "submitButton").click()

def LBG_S_6(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Đóng')]"))).click()

def LBG_X_1(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-admin-delete"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Xóa')]"))).click()

def LBG_X_2(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-admin-delete"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Hủy')]"))).click()