from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import cv2
import os
import numpy as np
import pyautogui
import json
import random
import time
from datetime import datetime

import requests
import shutil
import psutil

from requests.auth import HTTPBasicAuth

api_key='ac8a2c5e5338621c742b7818ce9404e3'
client_id = 'adfa722df32f2f9'
username_stream='automobileGeo@yopmail.com'
password_stream='Geo1762024'

driver = None
test_results = []

recording = True


def Login():
    # Tạo một Options object
    global driver
    chrome_options = Options()
    # Thêm đường dẫn của ChromeDriver vào Options
    chrome_options.add_argument("--webdriver.chrome.driver=exec_path")

    # Khởi tạo trình điều khiển (driver) với Options
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("http://www.learnico.id.vn/sign-in")
    driver.maximize_window()
    # time.sleep(5)

    # loggin
    driver.find_element(By.XPATH, "//input[@id='username']").send_keys("admin")
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys("123456")
    driver.find_element(By.XPATH, "//button[@id='btnLogin']").click()
    time.sleep(5)

    return driver


# def record_screen(name_module):
#
#     v_b = os.path.join("TestReport", "Video",name_module, "record.avi")
#     filename = os.path.join(os.getcwd(), v_b)
#     global recording  # Biến điều khiển vòng lặp ghi hình
#
#     # Tạo thư mục nếu chưa có
#     dir_path = os.path.dirname(filename)
#     if not os.path.exists(dir_path):
#         os.makedirs(dir_path)
#
#     screen_size = pyautogui.size()  # Lấy kích thước màn hình
#     fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Định dạng video
#     out = cv2.VideoWriter(filename, fourcc, 10.0, screen_size)  # Tạo đối tượng ghi video
#
#     while recording:
#         img = pyautogui.screenshot()  # Chụp màn hình
#         frame = np.array(img)  # Chuyển ảnh sang mảng
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Chuyển màu sang BGR
#         out.write(frame)  # Ghi khung hình
#
#     out.release()  # Kết thúc ghi video

def take_screenshot(driver, filename,name_module):
    v_b = os.path.join("TestReport", "Anh", name_module)
    folder_path = os.path.join(os.getcwd(), v_b)
    screenshot_path = os.path.join(folder_path, filename)
    driver.save_screenshot(screenshot_path)
    print(f"[✔] Screenshot saved: {screenshot_path}")
    return screenshot_path

def save_test_result(name_testcase, status, video, screenshot=None):
    test_results.append({
        "testcase": name_testcase,
        "status": status,
        "video": video,
        "screenshot": screenshot
    })

def information_testsuite(test_results):
    tongsotestcase=len(test_results)
    thanh_cong,that_bai,loi=[0,0,0]
    for a in test_results:
        status=a['status']
        if status=='pass':
            thanh_cong=thanh_cong+1
        elif status=='fail':
            that_bai=that_bai+1
        elif status == 'err':
            loi=loi+1
    return tongsotestcase, thanh_cong, that_bai, loi
def upload_image_to_imgbb(api_key, image_path, expiration=None):
    url = "https://api.imgbb.com/1/upload"
    with open(image_path, "rb") as file:
        image_data = file.read()
    payload = {
            "key": api_key,
            "image": image_data
    }
    if expiration:
        payload["expiration"] = expiration

        # Using files for multipart/form-data
    files = {
            'image': (image_path, image_data)
    }
    response = requests.post(url, data=payload, files=files)
    if response.status_code == 200:
        result = response.json()
        image_url = result['data']['url']
        return image_url
    else:
        print(f"Failed to upload image. Status code: {response.status_code}")
        try:
            print(response.json())
        except ValueError:
            print(response.text)
        return None
# def upload_image_to_imgur(image_path, client_id):
#     url = "https://api.imgur.com/3/image"
#     headers = {'Authorization': f'Client-ID {client_id}'}
#
#     with open(image_path, 'rb') as file:
#         files = {'image': file}
#         response = requests.post(url, headers=headers, files=files)
#
#     if response.status_code == 200:
#         return response.json()['data']['link']
#     else:
#         print(f"Failed to upload image. Status code: {response.status_code}")
#         print(response.text)
#         return None
def upload_video(username, password, video_path):
    url = 'https://api.streamable.com/upload'
    with open(video_path, 'rb') as f:
        response = requests.post(url, files={'file': f}, auth=HTTPBasicAuth(username, password))
        if response.status_code == 200:
            result = response.json()
            return f"https://streamable.com/{result['shortcode']}", result['shortcode']
        else:
            print(f"Upload failed: {response.status_code}")
            print(response.text)
            return None, None



# def record_screen(video_path):
#     global recording  # Biến điều khiển vòng lặp ghi hình
#
#     screen_size = pyautogui.size()  # Lấy kích thước màn hình
#     fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Định dạng video
#     out = cv2.VideoWriter(video_path, fourcc, 10.0, screen_size)  # Tạo đối tượng ghi video
#
#     while recording:
#         img = pyautogui.screenshot()  # Chụp màn hình
#         frame = np.array(img)  # Chuyển ảnh sang mảng
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Chuyển màu sang BGR
#         out.write(frame)  # Ghi khung hình
#
#     out.release()  # Kết thúc ghi video
with open('test_data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

if __name__ == '__main__':
    name_module="danhmucbaigiang"
    v_b = os.path.join("TestReport", "Video", name_module, "record_" + name_module + ".avi")
    filename = os.path.join(os.getcwd(), v_b)
    print(filename)