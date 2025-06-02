import time
import threading
import cv2
import os
import numpy as np
import pyautogui
import pygetwindow as gw
from PIL import Image
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from chung import *
from baigiang import *
from danhmucbaigiang import *
from loaibaigiang import *
from quanlybaigiang import *
from image_report_test import *
from dangnhap import *
from testcase.testcase_danhmucbaigiang import *
from testcase.testcase_quanlybaigiang import *
from testcase.testcase_loaibaigiang import *
from testcase.testcase_dangnhap import *
import json

# Thông tin tài khoản LambdaTest
# username = "kimchi15062k3"
# access_key = "lTxZKAOGoj58KKPt34KfD5oeqK4Yd5hT8jJqW5b1DVSy4eeLqT"

username = "kimchi062k3"
access_key = "LT_eT0c6Bpxib4SD7LCO18rhAVYykuw5lVvNlWPP7WoT4jABHr"
# Danh sách cấu hình trình duyệt cần kiểm thử
browsers = [
    {"browser": "Chrome", "version": "latest", "os": "Windows 10"},
    {"browser": "Edge", "version": "latest", "os": "Linux"},
    {"browser": "Firefox", "version": "latest", "os": "macOS Monterey"}
]

# Hàm lấy options theo browser name
def get_options(browser_name, capabilities):
    if browser_name == "Chrome":
        options = ChromeOptions()
    elif browser_name == "Edge":
        options = EdgeOptions()
    elif browser_name == "Firefox":
        options = FirefoxOptions()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    for key, value in capabilities.items():
        options.set_capability(key, value)
    return options


# Hàm chạy test
def run_test(capabilities):
    capabilities.update({
        "build": "CrossBrowser Testing - Learnico",
        "name": f"{capabilities['browser']} - {capabilities['os']}",
        "platform": capabilities["os"],
        "selenium_version": "4.0.0",
    })

    # URL LambdaTest Grid
    url = f"https://{username}:{access_key}@hub.lambdatest.com/wd/hub"
    options = get_options(capabilities["browser"], capabilities)

    driver = webdriver.Remote(command_executor=url, options=options)

    try:
        driver.get("http://www.learnico.id.vn/sign-in")
        time.sleep(2)
        baigiang(driver, tentrung, Tten,Tcapcha, Tmota,Stendmbg, Smotadmbg, Ttenbb,Stenbb, Ttenlbgtrung, Ttenlbgbb, Stenlbgbb, Tloaibaigiang, Tmotalbg, Sloaibaigiang, Smotalbg, Ttenbaigiang, tmotaqlbg, f_username, p_password, p_username, f_password,c_username, c_password, Ttenbgbb,dmbg,lbg, gio, phut, giay, Ttenbgbbvd, dmbgvd, lbgvd, Ttenbgbbaudio, dmbgaudio, lbgaudio, Ttenbgtrung, stenbgbbaudio, stenbgbbvd,stenbgbb, sdmbgbb, slbgbb,stenbaigiang, sdmbg, Slbg, smotaqlbg,sgio, sphut, sgiay,video_path)
        print(f"PASS: {capabilities['browser']} on {capabilities['os']}")
        driver.execute_script("lambda-status=passed")
    except Exception as e:
        print(f"FAIL: {capabilities['browser']} on {capabilities['os']} -- {e}")
        driver.execute_script("lambda-status=failed")
    finally:
        driver.quit()


# Lặp qua từng trình duyệt
for caps in browsers:
    # Đăng nhập
    # Đăng nhập
    f_username = data["login"]["fail"]["username"]
    f_password = data["login"]["fail"]["password"]
    p_username = data["login"]["pass"]["username"]
    p_password = data["login"]["pass"]["password"]
    c_username = data["login"]["chuakichhoat"]["username"]
    c_password = data["login"]["chuakichhoat"]["password"]

    # Danh mục bài giảng
    Tten = data["danhmucbaigiang"]["themfull"]["ten"]
    Tcapcha = data["danhmucbaigiang"]["themfull"]["capcha"]
    Tmota = data["danhmucbaigiang"]["themfull"]["mota"]
    Stendmbg = data["danhmucbaigiang"]["suafull"]["ten"]
    Smotadmbg = data["danhmucbaigiang"]["suafull"]["mota"]
    tentrung = data["danhmucbaigiang"]["fail"]["ten"]
    Ttenbb = data["danhmucbaigiang"]["thembatbuoc"]["ten"]
    Stenbb = data["danhmucbaigiang"]["suabatbuoc"]["ten"]

    # Loại bài giảng
    Ttenlbgtrung = data["loaibaigiang"]["fail"]["ten"]
    Ttenlbgbb = data["loaibaigiang"]["addbb"]["ten"]
    Stenlbgbb = data["loaibaigiang"]["editbb"]["ten"]
    Tloaibaigiang = data["loaibaigiang"]["add"]["ten"]
    Tmotalbg = data["loaibaigiang"]["add"]["mota"]
    Sloaibaigiang = data["loaibaigiang"]["edit"]["ten"]
    Smotalbg = data["loaibaigiang"]["edit"]["mota"]
    # Quản lý bài giảng
    Ttenbaigiang = data["quanlybaigiang"]["add"]["tenbg"]
    gio = data["quanlybaigiang"]["add"]["gio"]
    phut = data["quanlybaigiang"]["add"]["phut"]
    giay = data["quanlybaigiang"]["add"]["giay"]
    tmotaqlbg = data["quanlybaigiang"]["add"]["mota"]
    Ttenbgbb = data["quanlybaigiang"]["addbb"]["tenbg"]
    lbg = data["quanlybaigiang"]["addbb"]["lbg"]
    dmbg = data["quanlybaigiang"]["addbb"]["dmbg"]
    Ttenbgbbvd = data["quanlybaigiang"]["addvd"]["tenbg"]
    lbgvd = data["quanlybaigiang"]["addvd"]["lbg"]
    dmbgvd = data["quanlybaigiang"]["addvd"]["dmbg"]
    Ttenbgbbaudio = data["quanlybaigiang"]["addaudio"]["tenbg"]
    dmbgaudio = data["quanlybaigiang"]["addaudio"]["dmbg"]
    lbgaudio = data["quanlybaigiang"]["addaudio"]["lbg"]
    Ttenbgtrung = data["quanlybaigiang"]["addtrung"]["tenbg"]
    stenbgbbaudio = data["quanlybaigiang"]["editaudio"]["tenbg"]
    stenbgbbvd = data["quanlybaigiang"]["editvd"]["tenbg"]
    stenbgbb = data["quanlybaigiang"]["suabb"]["tenbg"]
    sdmbgbb = data["quanlybaigiang"]["suabb"]["dmbg"]
    slbgbb = data["quanlybaigiang"]["suabb"]["lbg"]
    stenbaigiang = data["quanlybaigiang"]["edit"]["tenbg"]
    sdmbg = data["quanlybaigiang"]["edit"]["dmbg"]
    Slbg = data["quanlybaigiang"]["edit"]["lbg"]
    smotaqlbg = data["quanlybaigiang"]["edit"]["mota"]
    sgio = data["quanlybaigiang"]["edit"]["gio"]
    sphut = data["quanlybaigiang"]["edit"]["phut"]
    sgiay = data["quanlybaigiang"]["edit"]["giay"]

    video_path = "video.mp4"  # nếu bạn cần video

    run_test(caps)



driver = webdriver.Remote(
    command_executor="https://<username>:<access_key>@hub.lambdatest.com/wd/hub",
    options=options
)






