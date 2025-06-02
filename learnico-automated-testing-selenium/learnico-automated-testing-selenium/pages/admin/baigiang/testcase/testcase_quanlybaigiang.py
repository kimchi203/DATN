import time
import threading
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import cv2
import os
import numpy as np
import pyautogui
import pygetwindow as gw
from PIL import Image

def QLBG_T_1(driver, Ttenbaigiang,Stenbb,Sloaibaigiang, tmotaqlbg, gio, phut, giay):
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btnAdd']"))).click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='lectureTitle']").send_keys(Ttenbaigiang)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Danh mục bài giảng')]//../span"))).click()
    driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys(Stenbb)
    driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys(Keys.ENTER)
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Loại bài giảng')]/../span"))).click()
    driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys(Sloaibaigiang)
    driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys(Keys.ENTER)
    driver.find_element(By.XPATH, "//input[@id='lectureHourAllow']").send_keys(gio)
    driver.find_element(By.XPATH, "//input[@id='lectureMinuteAllow']").send_keys(phut)
    driver.find_element(By.XPATH, "//input[@id='lectureSecondAllow']").send_keys(giay)
    driver.find_element(By.XPATH, "//input[@id='lecturePreview']").click()
    driver.find_element(By.XPATH, "//input[@id='lectureIsPayment']").click()
    price = "300000"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='lecturePrice']"))).clear()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='lecturePrice']"))).send_keys(price)
    time.sleep(1)
    driver.find_element(By.XPATH, "//label[contains(text(),'Ảnh minh họa')]/..//span").click()
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btnUploadFiles']"))).click()
    time.sleep(1)
    folder = r"D:\DATN\Anh"
    filename = "Toan.jpg"
    full_path = os.path.join(folder, filename)
    pyautogui.write(full_path)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)
    driver.find_element(By.XPATH, "(//div[@id = 'file-explorer-content']/div/div/div)[2]").click()
    driver.find_element(By.XPATH, "//button[@id='btnChooseImage']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//textarea[@id='lectureDescription']").send_keys(tmotaqlbg)
    driver.find_element(By.XPATH, "//button[@id='saveData']").click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Lưu')]"))).click()


def QLBG_T_2(driver, Ttenbgbb,dmbg,lbg):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btnAdd']"))).click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='lectureTitle']").send_keys(Ttenbgbb)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Danh mục bài giảng')]//../span"))).click()
    driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys(dmbg)
    driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys(Keys.ENTER)
    time.sleep(1)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Loại bài giảng')]/../span"))).click()
    driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys(lbg)
    driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys(Keys.ENTER)
    driver.find_element(By.XPATH, "//button[@id='saveData']").click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Lưu')]"))).click()
def QLBG_T_3(driver, Ttenbgbbvd,dmbgvd,lbgvd):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btnAdd']"))).click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='lectureTitle']").send_keys(Ttenbgbbvd)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Danh mục bài giảng')]//../span"))).click()
    driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys(dmbgvd)
    driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys(Keys.ENTER)
    time.sleep(1)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Loại bài giảng')]/../span"))).click()
    driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys(lbgvd)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Video bài giảng')]"))).click()
    driver.find_element(By.XPATH, "//button[@id='btnAddFile']").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Video bài giảng')]/..//span"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btnUploadFiles']"))).click()
    time.sleep(1)
    folder = r"D:\DATN\Anh"
    filename = "Matran.mp4"
    full_path = os.path.join(folder, filename)
    pyautogui.write(full_path)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)
    driver.find_element(By.XPATH, "(//div[@id = 'file-explorer-content']/div/div/div)[2]").click()
    driver.find_element(By.XPATH, "//button[@id='btnChooseImage']").click()
    driver.find_element(By.XPATH, "//button[@id='saveDataFile']").click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Lưu')])[1]"))).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Lưu')]"))).click()

def QLBG_T_4(driver,Ttenbgbbaudio,dmbgaudio,lbgaudio, gio, phut, giay,tmotaqlbg):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btnAdd']"))).click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='lectureTitle']").send_keys(Ttenbgbbaudio)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Danh mục bài giảng')]//../span"))).click()
    driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys(dmbgaudio)
    driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys(Keys.ENTER)
    time.sleep(1)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Loại bài giảng')]/../span"))).click()
    driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys(lbgaudio)
    driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys(Keys.ENTER)
    driver.find_element(By.XPATH, "//input[@id='lectureHourAllow']").send_keys(gio)
    driver.find_element(By.XPATH, "//input[@id='lectureMinuteAllow']").send_keys(phut)
    driver.find_element(By.XPATH, "//input[@id='lectureSecondAllow']").send_keys(giay)
    driver.find_element(By.XPATH, "//input[@id='lecturePreview']").click()
    driver.find_element(By.XPATH, "//input[@id='lectureIsPayment']").click()
    price = "300000"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='lecturePrice']"))).clear()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@id='lecturePrice']"))).send_keys(price)
    time.sleep(1)
    driver.find_element(By.XPATH, "//label[contains(text(),'Ảnh minh họa')]/..//span").click()
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btnUploadFiles']"))).click()
    time.sleep(1)
    folder = r"D:\DATN\Anh"
    filename = "Toan.jpg"
    full_path = os.path.join(folder, filename)
    pyautogui.write(full_path)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)
    driver.find_element(By.XPATH, "(//div[@id = 'file-explorer-content']/div/div/div)[2]").click()
    driver.find_element(By.XPATH, "//button[@id='btnChooseImage']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//label[contains(text(),'Tệp bài giảng')]/..//span").click()
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btnUploadFiles']"))).click()
    time.sleep(1)
    folder = r"D:\DATN\Anh"
    filename = "Omemthatlau.mp3"
    full_path = os.path.join(folder, filename)
    pyautogui.write(full_path)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)
    driver.find_element(By.XPATH, "(//div[@id = 'file-explorer-content']/div/div/div)[2]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[@id='btnChooseImage']").click()
    driver.find_element(By.XPATH, "//textarea[@id='lectureDescription']").send_keys(tmotaqlbg)
    driver.find_element(By.XPATH, "//button[@id='saveData']").click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Lưu')]"))).click()

def QLBG_T_5(driver,Ttenbgtrung):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btnAdd']"))).click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='lectureTitle']").send_keys(Ttenbgtrung)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Lưu')])[1]"))).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Lưu')]"))).click()

def QLBG_T_6(driver):
    driver.find_element(By.XPATH, "//input[@id='lectureTitle']").clear()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Lưu')])[1]"))).click()

def QLBG_T_8(driver):
    driver.find_element(By.XPATH, "//label[contains(text(),'Ảnh minh họa')]/..//span").click()
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btnUploadFiles']"))).click()
    time.sleep(1)
    folder = r"D:\DATN\Anh"
    filename = "kimchi.jpg"
    full_path = os.path.join(folder, filename)
    pyautogui.write(full_path)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)

def QLBG_S_3(driver, stenbgbb,sdmbgbb,slbgbb):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "((//table[@id='tableData']//tbody//tr//td)[8]//button[2])[1]"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='lectureTitle']"))).clear()
    driver.find_element(By.XPATH, "//input[@id='lectureTitle']").send_keys(stenbgbb)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Danh mục bài giảng')]//../span"))).click()
    driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys(sdmbgbb)
    driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys(Keys.ENTER)
    time.sleep(1)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Loại bài giảng')]/../span"))).click()
    driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys(slbgbb)
    driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys(Keys.ENTER)
    driver.find_element(By.XPATH, "//button[@id='saveData']").click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Lưu')]"))).click()
def QLBG_S_4(driver, stenbgbbvd,dmbgvd,lbgvd):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "((//table[@id='tableData']//tbody//tr//td)[8]//button[2])[1]"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='lectureTitle']"))).clear()
    driver.find_element(By.XPATH, "//input[@id='lectureTitle']").send_keys(stenbgbbvd)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Danh mục bài giảng')]//../span"))).click()
    driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys(dmbgvd)
    driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys(Keys.ENTER)
    time.sleep(1)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Loại bài giảng')]/../span"))).click()
    driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys(lbgvd)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Video bài giảng')]"))).click()
    driver.find_element(By.XPATH, "//button[@id='btnAddFile']").click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//label[contains(text(),'Chất lượng')]/..//span)[1]"))).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@class = 'select2-search__field']"))).send_keys("480p")
    driver.find_element(By.XPATH, "//input[@class = 'select2-search__field']").send_keys(Keys.ENTER)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Video bài giảng')]/..//span"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btnUploadFiles']"))).click()
    time.sleep(1)
    folder = r"D:\DATN\Anh"
    filename = "cryforme.mp4"
    full_path = os.path.join(folder, filename)
    pyautogui.write(full_path)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)
    driver.find_element(By.XPATH, "(//div[@id = 'file-explorer-content']/div/div/div)[2]").click()
    driver.find_element(By.XPATH, "//button[@id='btnChooseImage']").click()
    driver.find_element(By.XPATH, "//button[@id='saveDataFile']").click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Lưu')])[1]"))).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Lưu')]"))).click()

def QLBG_S_5(driver,stenbgbbaudio,dmbgaudio,lbgaudio, gio, phut, giay,tmotaqlbg):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "((//table[@id='tableData']//tbody//tr//td)[8]//button[2])[1]"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='lectureTitle']"))).clear()
    driver.find_element(By.XPATH, "//input[@id='lectureTitle']").send_keys(stenbgbbaudio)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Danh mục bài giảng')]//../span"))).click()
    driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys(dmbgaudio)
    driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys(Keys.ENTER)
    time.sleep(1)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Loại bài giảng')]/../span"))).click()
    driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys(lbgaudio)
    driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys(Keys.ENTER)
    driver.find_element(By.XPATH, "//input[@id='lectureHourAllow']").send_keys(gio)
    driver.find_element(By.XPATH, "//input[@id='lectureMinuteAllow']").send_keys(phut)
    driver.find_element(By.XPATH, "//input[@id='lectureSecondAllow']").send_keys(giay)
    driver.find_element(By.XPATH, "//input[@id='lecturePreview']").click()
    driver.find_element(By.XPATH, "//input[@id='lectureIsPayment']").click()
    driver.find_element(By.XPATH, "//label[contains(text(),'Ảnh minh họa')]/..//span").click()
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btnUploadFiles']"))).click()
    time.sleep(1)
    folder = r"D:\DATN\Anh"
    filename = "Tieng anh.jpg"
    full_path = os.path.join(folder, filename)
    pyautogui.write(full_path)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)
    driver.find_element(By.XPATH, "(//div[@id = 'file-explorer-content']/div/div/div)[2]").click()
    driver.find_element(By.XPATH, "//button[@id='btnChooseImage']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//label[contains(text(),'Tệp bài giảng')]/..//span").click()
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btnUploadFiles']"))).click()
    time.sleep(1)
    folder = r"D:\DATN\Anh"
    filename = "Kysivaanhsang.mp3"
    full_path = os.path.join(folder, filename)
    pyautogui.write(full_path)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)
    driver.find_element(By.XPATH, "(//div[@id = 'file-explorer-content']/div/div/div)[2]").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[@id='btnChooseImage']").click()
    driver.find_element(By.XPATH, "//textarea[@id='lectureDescription']").clear()
    driver.find_element(By.XPATH, "//textarea[@id='lectureDescription']").send_keys(tmotaqlbg)
    driver.find_element(By.XPATH, "//button[@id='saveData']").click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Lưu')]"))).click()

def QLBG_S_2(driver, stenbaigiang,sdmbg, Slbg, smotaqlbg, sgio, sphut, sgiay):
    time.sleep(2)
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "((//table[@id='tableData']//tbody//tr//td)[8]//button[2])[1]"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='lectureTitle']"))).clear()
    driver.find_element(By.XPATH, "//input[@id='lectureTitle']").send_keys(stenbaigiang)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Danh mục bài giảng')]//../span"))).click()
    driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys(sdmbg)
    driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys(Keys.ENTER)
    time.sleep(1)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Loại bài giảng')]/../span"))).click()
    driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys(Slbg)
    driver.find_element(By.XPATH, "//input[@class='select2-search__field']").send_keys(Keys.ENTER)
    driver.find_element(By.XPATH, "//input[@id='lectureHourAllow']").send_keys(sgio)
    driver.find_element(By.XPATH, "//input[@id='lectureMinuteAllow']").send_keys(sphut)
    driver.find_element(By.XPATH, "//input[@id='lectureSecondAllow']").send_keys(sgiay)
    driver.find_element(By.XPATH, "//input[@id='lecturePreview']").click()
    driver.find_element(By.XPATH, "//input[@id='lectureIsPayment']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//label[contains(text(),'Ảnh minh họa')]/..//span").click()
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btnUploadFiles']"))).click()
    time.sleep(2)
    folder = r"D:\DATN\Anh"
    filename = "Tieng anh.jpg"
    full_path = os.path.join(folder, filename)
    pyautogui.write(full_path)
    time.sleep(2)
    pyautogui.press('enter')
    time.sleep(2)
    driver.find_element(By.XPATH, "(//div[@id = 'file-explorer-content']/div/div/div)[2]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//button[@id='btnChooseImage']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//textarea[@id='lectureDescription']").clear()
    driver.find_element(By.XPATH, "//textarea[@id='lectureDescription']").send_keys(smotaqlbg)
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[@id='saveData']").click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Lưu')]"))).click()

def QLBG_S_6(driver,Ttenbgtrung):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "((//table[@id='tableData']//tbody//tr//td)[8]//button[2])[1]"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='lectureTitle']"))).clear()
    driver.find_element(By.XPATH, "//input[@id='lectureTitle']").send_keys(Ttenbgtrung)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Lưu')])[1]"))).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Lưu')]"))).click()

def QLBG_S_7(driver):
    driver.find_element(By.XPATH, "//input[@id='lectureTitle']").clear()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Lưu')])[1]"))).click()

def QLBG_S_9(driver):
    driver.find_element(By.XPATH, "//label[contains(text(),'Ảnh minh họa')]/..//span").click()
    time.sleep(1)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btnUploadFiles']"))).click()
    time.sleep(1)
    folder = r"D:\DATN\Anh"
    filename = "kimchi.jpg"
    full_path = os.path.join(folder, filename)
    pyautogui.write(full_path)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(2)

def QLBG_X_1(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='btn btn-icon btn-admin-delete'])[1]"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Xóa')]"))).click()
def QLBG_X_2(driver):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//button[@class='btn btn-icon btn-admin-delete'])[1]"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Hủy')]"))).click()
