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
from danhmucbaigiang import *
from loaibaigiang import *
from quanlybaigiang import *
from dangnhap import *
from image_report_test import *
from testcase.testcase_danhmucbaigiang import *
from testcase.testcase_quanlybaigiang import *
from testcase.testcase_loaibaigiang import *
from testcase.testcase_dangnhap import *

import json
recording = True
video_path = os.path.join(os.getcwd(), "TestReport", "Video", "baigiang", "record_lesson.avi")

def record_screen():
    global recording  # Biến điều khiển vòng lặp ghi hình

    screen_size = pyautogui.size()  # Lấy kích thước màn hình
    fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Định dạng video
    out = cv2.VideoWriter(video_path, fourcc, 10.0, screen_size)  # Tạo đối tượng ghi video

    while recording:
        img = pyautogui.screenshot()  # Chụp màn hình
        frame = np.array(img)  # Chuyển ảnh sang mảng
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Chuyển màu sang BGR
        out.write(frame)  # Ghi khung hình

    out.release()  # Kết thúc ghi video

def baigiang(driver, tentrung, Tten,Tcapcha, Tmota,Stendmbg, Smotadmbg, Ttenbb,Stenbb, Ttenlbgtrung, Ttenlbgbb, Stenlbgbb, Tloaibaigiang, Tmotalbg, Sloaibaigiang, Smotalbg, Ttenbaigiang, tmotaqlbg, f_username, p_password, p_username, f_password,c_username, c_password, Ttenbgbb,dmbg,lbg, gio, phut, giay, Ttenbgbbvd, dmbgvd, lbgvd, Ttenbgbbaudio, dmbgaudio, lbgaudio, Ttenbgtrung, stenbgbbaudio, stenbgbbvd,stenbgbb, sdmbgbb, slbgbb,stenbaigiang, sdmbg, Slbg, smotaqlbg,sgio, sphut, sgiay,video_path):
    name_module = "baigiang"
    DangNhap(driver, f_username, p_password, p_username, f_password, c_username, c_password, video_path, name_module)
    time.sleep(1)
    Danhmucbaigiang(driver, tentrung, Tten,Tcapcha, Tmota,Stendmbg, Smotadmbg, Ttenbb,Stenbb, video_path)
    time.sleep(3)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Loại bài giảng')])[1]"))).click()
    Loaibaigiang(driver, Ttenlbgtrung, Ttenlbgbb, Stenlbgbb, Tloaibaigiang, Tmotalbg, Sloaibaigiang, Smotalbg, video_path)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Bài giảng')])[1]"))).click()
    time.sleep(1)
    Quanlybaigiang(driver, Ttenbaigiang,Stenbb,Sloaibaigiang, Ttenbgbb,dmbg,lbg,tmotaqlbg, gio, phut, giay, Ttenbgbbvd, dmbgvd, lbgvd, Ttenbgbbaudio, dmbgaudio, lbgaudio, Ttenbgtrung, stenbgbbaudio, stenbgbbvd,stenbgbb, sdmbgbb, slbgbb,stenbaigiang, sdmbg, Slbg, smotaqlbg,sgio, sphut, sgiay,video_path) #video_path

    # Vào danh mục bài giảng
    time.sleep(1)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Danh mục bài giảng')])[1]"))).click()
    # Xóa danh mục
    time.sleep(2)
    DMBG_X_2(driver)
    time.sleep(3)
    k = driver.find_elements(By.XPATH, '//ul[@id="tree"]//li//span[@class="branchName"]')
    j = len(k)
    if j > 0:
        xcc_test = driver.find_element(By.XPATH, "(//ul[@id='tree']//li//span[@class='branchName'])[1]").text
        time.sleep(1)
        if xcc_test != Stenbb:
            print("Pass: xóa danh mục bài giảng cấp cha thành công")
            save_test_result("Xoa_danh_muc_bai_giang_cap_cha", "pass", video_path)
        else:
            screenshot = take_screenshot(driver, "DMBG_X_2.png", name_module)
            print("Failse: Xem lại chức năng xóa danh mục bài giảng cấp cha")
            save_test_result("Xoa_danh_muc_bai_giang_cap_cha", "fail", video_path, screenshot)
    #Vào loại bài giảng
    time.sleep(2)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Loại bài giảng')])[1]"))).click()
    #Tìm kiếm
    time.sleep(1)
    search_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "table_search_all")))
    search_box.clear()
    search_box.send_keys(Sloaibaigiang)
    search_box.send_keys(Keys.ENTER)
    #Xóa loại bài giảng
    LBG_X_1(driver)
    search_box.clear()
    search_box.send_keys(Sloaibaigiang)
    search_box.send_keys(Keys.ENTER)

    rows = driver.find_elements(By.XPATH, '//table[@id="tableData"]//tbody//tr//td')
    if len(rows) > 1:
        screenshot = take_screenshot(driver, "LBG_X_1.png", name_module)
        print("Fail: Xem lại chức năng xóa")
        save_test_result("Xóa loại bài giảng", "fail", video_path, screenshot)
    else:
        print("Pass: Xóa thành công")
        save_test_result("Xóa loại bài giảng", "pass", video_path)
    time.sleep(1)

if __name__ == '__main__':
    thoi_gian_hien_tai = datetime.now()
    # Đăng nhập
    f_username = data["login"]["fail"]["username"]
    f_password = data["login"]["fail"]["password"]
    p_username = data["login"]["pass"]["username"]
    p_password = data["login"]["pass"]["password"]
    c_username = data["login"]["chuakichhoat"]["username"]
    c_password = data["login"]["chuakichhoat"]["password"]

    #Danh mục bài giảng
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



    # Bắt đầu quay video
    recording = True
    #video_thread = threading.Thread(target=record_screen, args=(video_path,))
    video_thread = threading.Thread(target=record_screen,)
    video_thread.start()

    try:
        driver = open()
        baigiang(driver, tentrung, Tten,Tcapcha, Tmota,Stendmbg, Smotadmbg, Ttenbb,Stenbb, Ttenlbgtrung, Ttenlbgbb, Stenlbgbb, Tloaibaigiang, Tmotalbg, Sloaibaigiang, Smotalbg, Ttenbaigiang, tmotaqlbg, f_username, p_password, p_username, f_password,c_username, c_password, Ttenbgbb,dmbg,lbg, gio, phut, giay, Ttenbgbbvd, dmbgvd, lbgvd, Ttenbgbbaudio, dmbgaudio, lbgaudio, Ttenbgtrung, stenbgbbaudio, stenbgbbvd,stenbgbb, sdmbgbb, slbgbb,stenbaigiang, sdmbg, Slbg, smotaqlbg,sgio, sphut, sgiay,video_path)
    finally:
        driver.quit()
        recording = False
        video_thread.join()
        print("[✔] Đã quay video và chụp ảnh hoàn tất.")
        print("\n[KẾT QUẢ KIỂM THỬ]:")
        for i, result in enumerate(test_results, start=1):
            print(
                f"Testcase {i}: {result['testcase']}, {result['status']}, {result['video']}, Screenshot: {result['screenshot']}")
        ketthuc = datetime.now()
        formatted_time_2 = ketthuc.strftime('%d-%m-%Y %H:%M:%S')
        # Tính toán sự chênh lệch thời gian
        chenh_lech_thoi_gian = ketthuc - thoi_gian_hien_tai
        tongsotestcase, thanh_cong, that_bai, loi = information_testsuite(test_results)
        repot_html(tong_sotestcase=tongsotestcase, thanh_cong=thanh_cong, that_bai=that_bai, loi=loi,
                   testsuite=test_results, thoi_gian_hien_tai=thoi_gian_hien_tai, ketthuc=ketthuc,
                   chenh_lech_thoi_gian=chenh_lech_thoi_gian, browser_version='test')