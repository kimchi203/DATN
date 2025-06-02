import time
import threading
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def DMBG_T_2(driver, Ttenbb):
    # Thêm mới
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "(//h1[contains(text(),'Danh mục bài giảng')]/../../../..//button)[1]"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='name']"))).send_keys(Ttenbb)
    driver.find_element(By.XPATH, "//button[@id='btnUpdateItem']").click()
    driver.find_element(By.XPATH, "(//button[contains(text(),'Lưu')])[2]").click()
    time.sleep(1)

def DMBG_T_3 (driver, tentrung):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "(//h1[contains(text(),'Danh mục bài giảng')]/../../../..//button)[1]"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='name']"))).send_keys(tentrung)
    driver.find_element(By.XPATH, "//button[@id='btnUpdateItem']").click()
    driver.find_element(By.XPATH, "(//button[contains(text(),'Lưu')])[2]").click()
    time.sleep(1)

def DMBG_T_4 (driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='name']"))).clear()
    driver.find_element(By.XPATH, "//button[@id='btnUpdateItem']").click()
    time.sleep(1)

def DMBG_T_5 (driver):
    driver.find_element(By.XPATH, "//button[contains(text(),'Đóng')]").click()
    time.sleep(1)

def DMBG_T_1 (driver,Tten,Tcapcha, Tmota ):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.XPATH, "(//h1[contains(text(),'Danh mục bài giảng')]/../../../..//button)[1]"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='name']"))).send_keys(Tten)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//h4[contains(text(),'Thêm mới danh mục bài giảng ')]/../..//div[2]//div[2]//span)[1]"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type = 'search']"))).send_keys(Tcapcha)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@type = 'search']"))).send_keys(Keys.ENTER)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//textarea[@id='description']"))).send_keys(
        Tmota)
    driver.find_element(By.XPATH, "//button[@id='btnUpdateItem']").click()
    driver.find_element(By.XPATH, "(//button[contains(text(),'Lưu')])[2]").click()
    time.sleep(1)

def DMBG_S_1(driver, Stendmbg, Smotadmbg):
    time.sleep(1)
    driver.find_element(By.XPATH, "(//span[contains(text(),'Vật lý')]/../..//li//span)[1]").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='name']"))).clear()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='name']"))).send_keys(Stendmbg)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//textarea[@id='description']"))).clear()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//textarea[@id='description']"))).send_keys(
        Smotadmbg)
    driver.find_element(By.XPATH, "//button[@id='btnUpdateItem']").click()
    driver.find_element(By.XPATH, "(//button[contains(text(),'Lưu')])[2]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[contains(text(),'OK')]").click()

    time.sleep(1)
def  DMBG_S_2(driver, Stenbb):
    # Sửa
    driver.find_element(By.XPATH, "(//ul[@id='tree']//li//span[@class='branchName'])[1]").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='name']"))).clear()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='name']"))).send_keys(Stenbb)
    driver.find_element(By.XPATH, "//button[@id='btnUpdateItem']").click()
    driver.find_element(By.XPATH, "(//button[contains(text(),'Lưu')])[2]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[contains(text(),'OK')]").click()

    time.sleep(1)
def DMBG_S_3(driver,tentrung):
    driver.find_element(By.XPATH, "(//span[contains(text(),'Vật lý')]/../..//li//span)[1]").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='name']"))).clear()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='name']"))).send_keys(tentrung)
    driver.find_element(By.XPATH, "//button[@id='btnUpdateItem']").click()
    driver.find_element(By.XPATH, "(//button[contains(text(),'Lưu')])[2]").click()
    time.sleep(1)

def DMBG_S_4(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='name']"))).clear()
    driver.find_element(By.XPATH, "//button[@id='btnUpdateItem']").click()
    time.sleep(1)

def DMBG_s_5 (driver):
    driver.find_element(By.XPATH, "//button[contains(text(),'Đóng')]").click()
    time.sleep(1)

def DMBG_X_1(driver,):
    dm_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//span[contains(text(),'Vật lý')]/../..//li//span)[1]")))
    ActionChains(driver).move_to_element(dm_element).perform()
    time.sleep(1)
    driver.find_element(By.XPATH, "//span[contains(text(),'Vật lý')]/../..//li//button//span").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Xóa')]"))).click()
    time.sleep(1)
    #(//button[@class = 'btn btn-admin-delete']//span)[4]
def DMBG_X_2(driver):
    dm_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "(//ul[@id='tree']//li//span[@class='branchName'])[1]")))
    ActionChains(driver).move_to_element(dm_element).perform()
    time.sleep(1)
    driver.find_element(By.XPATH, "(//button[@class='btn btn-admin-delete']//span)[1]").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Xóa')]"))).click()

def DMBG_X_3(driver):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "(//ul[@id='tree']//li//span[@class='branchName'])[1]")))
    ActionChains(driver).move_to_element(element).perform()
    driver.find_element(By.XPATH, "(//button[@class='btn btn-admin-delete']//span)[1]").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Hủy')]"))).click()

