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
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from chung import *
from image_report_test import *
from testcase.testcase_dangnhap import *
import json
recording = True
driver = None

# video_path = os.path.join(os.getcwd(), "TestReport", "Video", "dangnhap", "login_record.avi")
# def record_screen():
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

def open ():
    global driver
    chrome_options = Options()
    # Thêm đường dẫn của ChromeDriver vào Options
    chrome_options.add_argument("--webdriver.chrome.driver=exec_path")

    # Khởi tạo trình điều khiển (driver) với Options
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("http://www.learnico.id.vn/sign-in")
    driver.maximize_window()
    time.sleep(2)
    return  driver
def DangNhap(driver, f_username, p_password, p_username, f_password,c_username, c_password, video_path, name_module):
    #Test case Đăng nhập sai tên tài khoản
    # name_module = "dangnhap"
    DN_2(driver,f_username, p_password)
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Đăng nhập thất bại')]"))
    )
    # Kiểm tra nếu phần tử có tồn tại => Pass
    if element.is_displayed():
        print("Pass: Đăng nhập sai tên tài khoản")
        save_test_result("Dang_nhap_sai_ten_tai_khoan", "pass", video_path)

    else:
        print("Fail: Xem lại chức năng đăng nhập khi nhập sai tên tài khoản")
        screenshot = take_screenshot(driver, "DN_2.png", name_module)
        save_test_result("Dang_nhap_sai_ten_tai_khoan", "fail", video_path, screenshot)

    # Test case Đăng nhập sai mật khẩu
    DN_3(driver, p_username, f_password)
    element = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Đăng nhập thất bại')]"))
    )
    if element.is_displayed():
        print("Pass: Đăng nhập sai mật khẩu")
        save_test_result("Dang_nhap_sai_mat_khau", "pass", video_path)

    else:
        print("Fail: Xem lại chức năng đăng nhập khi nhập sai mật khẩu")
        screenshot = take_screenshot(driver, "DN_3.png", name_module)
        save_test_result("Dang_nhap_sai_mat_khau", "fail", video_path, screenshot)

    # Test case Đăng nhập để trống tên tài khoản
    DN_4(driver, p_password)
    k = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//li[contains(text(),'Tài khoản không được bỏ trống!')]"))
    )
    if k.is_displayed():
        print("Pass: Đăng nhập để trống tên tài khoản")
        save_test_result("Dang_nhap_de_trong_ten_tai_khoan", "pass", video_path)

    else:
        print("Fail: Xem lại chức năng đăng nhập khi để trống tên tài khoản")
        screenshot = take_screenshot(driver, "DN_4.png", name_module)
        save_test_result("Dang_nhap_de_trong_ten_tai_khoan", "fail", video_path, screenshot)

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'OK')]"))
    ).click()

    # Test case Đăng nhập để trống mật khẩu
    DN_5(driver, p_username)
    i = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//li[contains(text(),'Mật khẩu không được bỏ trống!')]"))
    )
    if i.is_displayed():
        print("Pass: Đăng nhập để trống mật khẩu")
        save_test_result("Dang_nhap_de_trong_mat_khau", "pass", video_path)

    else:
        print("Fail: Xem lại chức năng đăng nhập khi để trống mật khẩu")
        screenshot = take_screenshot(driver, "DN_5.png", name_module)
        save_test_result("Dang_nhap_de_trong_mat_khau", "fail", video_path, screenshot)

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'OK')]"))
    ).click()

    # Test case Đăng nhập với tài khoản chưa được kích hoạt
    DN_6(driver, c_username, c_password)
    d = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Đăng nhập thất bại')]"))
    ).text

    v = "Tài khoản chưa được kích hoạt. Vui lòng kiểm tra email để kích hoạt tài khoản"
    if v == d:
        print("Pass: Đăng nhập với tài khoản chưa được kích hoạt")
        save_test_result("Dang_nhap_voi_tai_khoan_chua_duoc_kich_hoat", "pass", video_path)

    else:
        print("Fail: Xem lại chức năng đăng nhập khi tài khoản chưa được kích hoạt")
        screenshot = take_screenshot(driver, "DN_6.png", name_module)
        save_test_result("Dang_nhap_voi_tai_khoan_chua_duoc_kich_hoat", "fail", video_path, screenshot)

    # Test case Đăng nhập thành công
    DN_1(driver,p_username, p_password)
    b = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Thống kê')]"))
    )
    if b.is_displayed():
        print("Pass: Đăng nhập thành công")
        #Mảng chứa tên test case, trạng thái, link video
        save_test_result("Dang_nhap_thanh_cong", "pass", video_path)

    else:
        print("Fail: Xem lại chức năng đăng nhập")
        #Chụp ảnh khi lỗi
        screenshot = take_screenshot(driver, "DN_1.png", name_module)
        # Mảng chứa tên test case, trạng thái, link video, ảnh fail
        save_test_result("Dang_nhap_thanh_cong", "fail", video_path, screenshot)
    return test_results

if __name__ == '__main__':

    f_username = data["login"]["fail"]["username"]
    f_password = data["login"]["fail"]["password"]
    p_username = data["login"]["pass"]["username"]
    p_password = data["login"]["pass"]["password"]
    c_username = data["login"]["chuakichhoat"]["username"]
    c_password = data["login"]["chuakichhoat"]["password"]

    recording = True
    video_thread = threading.Thread(target=record_screen)
    video_thread.start()

    try:
        driver = open()
        DangNhap(driver, f_username, p_password, p_username, f_password, c_username, c_password)
    finally:
        driver.quit()
        recording = False
        video_thread.join()
        print("[✔] Đã quay video và chụp ảnh hoàn tất.")
        print("\n[KẾT QUẢ KIỂM THỬ]:")
        for i, result in enumerate(test_results, start=1):
            print(
                f"Testcase {i}: {result['testcase']}, {result['status']}, {result['video']}, Screenshot: {result['screenshot']}")


