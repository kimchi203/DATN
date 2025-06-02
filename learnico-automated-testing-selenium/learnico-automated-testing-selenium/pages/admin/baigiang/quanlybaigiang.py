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
from testcase.testcase_quanlybaigiang import *
# For video recording
recording = True
driver = None
# video_path = os.path.join(os.getcwd(), "TestReport", "Video", "quanlybaigiang", "record_lesson_management.avi")
#
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


def Quanlybaigiang(driver, Ttenbaigiang,Stenbb,Sloaibaigiang, Ttenbgbb,dmbg,lbg,tmotaqlbg, gio, phut, giay, Ttenbgbbvd, dmbgvd, lbgvd, Ttenbgbbaudio, dmbgaudio, lbgaudio, Ttenbgtrung, stenbgbbaudio, stenbgbbvd,stenbgbb, sdmbgbb, slbgbb,stenbaigiang, sdmbg, Slbg, smotaqlbg,sgio, sphut, sgiay, video_path):
    name_module = "baigiang"
    # time.sleep(3)
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Bài giảng')])[1]"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Quản lý bài giảng')])[1]"))).click()
    time.sleep(1)
    #Thêm bài giảng khi nhập trùng tên bài giảng và danh mục bài giảng đã tồn tại
    # QLBG_T_5(driver, Ttenbgtrung)
    # element = WebDriverWait(driver, 5).until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, "//li[contains(text(),'Bài giảng đã tồn tại.')]"))
    # )
    # if element.is_displayed():
    #     print("Pass: Thêm bài giảng khi nhập trùng tên bài giảng và danh mục bài giảng đã tồn tại")
    #     save_test_result("Them_bai_giang_khi_nhap_trung_ten_danh_muc_da_ton_tai", "pass", video_path)
    #
    # else:
    #     print("Fail: Thêm bài giảng khi nhập trùng tên bài giảng và danh mục bài giảng đã tồn tại")
    #     screenshot = take_screenshot(driver, "QLBG_T_5.png", name_module)
    #     save_test_result("Them_bai_giang_khi_nhap_trung_ten_danh_muc_da_ton_tai", "fail", video_path, screenshot)
    #
    # #Thêm bài giảng khi không nhập trường bắt buộc
    # QLBG_T_6(driver)
    # element = WebDriverWait(driver, 5).until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, "//li[contains(text(),'Tên bài giảng không được để trống!')]"))
    # )
    # if element.is_displayed():
    #     print("Pass: Thêm bài giảng khi không nhập trường bắt buộc")
    #     save_test_result("Them_bai_giang_khi_khong_nhap_truong_bat_buoc", "pass", video_path)
    #
    # else:
    #     print("Fail: Thêm bài giảng khi không nhập trường bắt buộc")
    #     screenshot = take_screenshot(driver, "QLBG_T_6.png", name_module)
    #     save_test_result("Them_bai_giang_khi_khong_nhap_truong_bat_buoc", "fail", video_path, screenshot)
    #
    # WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Xác nhận')]"))).click()
    # #Thêm bài giảng với file ảnh > 25MB
    # QLBG_T_8(driver)
    # element = WebDriverWait(driver, 5).until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, "//h2[contains(text(),'Lưu ý')]"))
    # )
    # if element.is_displayed():
    #     print("Pass: Thêm bài giảng với file ảnh > 25MB")
    #     save_test_result("Them_bai_giang_voi_file_>25MB", "pass", video_path)
    #
    # else:
    #     print("Fail: Thêm bài giảng với file ảnh > 25MB")
    #     screenshot = take_screenshot(driver, "QLBG_T_8.png", name_module)
    #     save_test_result("Them_bai_giang_voi_file_>25MB", "fail", video_path, screenshot)
    #
    # driver.find_element(By.XPATH, "//button[contains(text(),'OK')]").click()
    # WebDriverWait(driver, 5).until( EC.presence_of_element_located((By.XPATH, "(//div[@class='modal-footer']//button)[1]"))
    # ).click()
    #
    # #Kiểm tra click vào nút Hủy của popup thêm mới bài giảng
    # WebDriverWait(driver, 5).until(EC.presence_of_element_located(
    #     (By.XPATH, "(//button[@id='saveData']/..//button)[1]"))
    # ).click()
    # element = WebDriverWait(driver, 5).until(
    #     EC.presence_of_element_located(
    #         (By.XPATH, "//h1[contains(text(),'Quản lý bài giảng')]"))
    # )
    # if element.is_displayed():
    #     print("Pass: Kiểm tra click vào nút Hủy của popup thêm mới bài giảng")
    #     save_test_result("Kiem_tra_click_vao_nut_huy_của_popup_them_moi_bai_giang", "pass", video_path)
    #
    # else:
    #     print("Fail: Kiểm tra click vào nút Hủy của popup thêm mới bài giảng")
    #     screenshot = take_screenshot(driver, "QLBG_T_7.png", name_module)
    #     save_test_result("Kiem_tra_click_vao_nut_huy_của_popup_them_moi_bai_giang", "fail", video_path, screenshot)
    #
    #
    #
    # #Thêm mới bài giảng khi chọn loại bài giảng là audio
    # QLBG_T_4(driver, Ttenbgbbaudio, dmbgaudio, lbgaudio, gio, phut, giay, tmotaqlbg)
    # WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//input[@id='table_search_all']"))).send_keys(Ttenbgbbaudio)
    # driver.find_element(By.XPATH, "//input[@id='table_search_all']").send_keys(Keys.ENTER)
    # k = driver.find_elements(By.XPATH, '//table[@id="tableData"]//tbody//tr')
    # j = len(k)
    # if (j > 0):
    #     time.sleep(2)
    #     v_test = driver.find_element(By.XPATH, "((//table[@id='tableData']//tbody//tr//td)[3]//span)[1]").text
    #     if v_test == Ttenbgbbaudio:
    #         print("Pass: Thêm mới bài giảng khi chọn loại bài giảng là audio")
    #         save_test_result("Them_moi_bai_giang_khi_chon_loai_bai_giang_la_audio", "pass", video_path)
    #
    #         #Sửa bài giảng khi chọn loại bài giảng là audio
    #         QLBG_S_5(driver, stenbgbbaudio, dmbgaudio, lbgaudio, gio, phut, giay, tmotaqlbg)
    #         WebDriverWait(driver, 10).until(
    #             EC.element_to_be_clickable((By.XPATH, "//input[@id='table_search_all']"))).clear()
    #         WebDriverWait(driver, 10).until(
    #             EC.element_to_be_clickable((By.XPATH, "//input[@id='table_search_all']"))).send_keys(stenbgbbaudio)
    #         driver.find_element(By.XPATH, "//input[@id='table_search_all']").send_keys(Keys.ENTER)
    #         time.sleep(1)
    #         k = driver.find_elements(By.XPATH, '//table[@id="tableData"]//tbody//tr')
    #         j = len(k)
    #         if (j > 0):
    #             v2_test = driver.find_element(By.XPATH, "((//table[@id='tableData']//tbody//tr//td)[3]//span)[1]").text
    #             if v2_test == stenbgbbaudio:
    #                 print("Pass: Sửa bài giảng khi chọn loại bài giảng là audio")
    #                 save_test_result("Sua_bai_giang_khi_chon_loai_bai_giang_la_audio", "pass", video_path)
    #                 time.sleep(1)
    #
    #                 QLBG_X_1(driver)
    #                 print("Pass xóa")
    #             else:
    #                 screenshot = take_screenshot(driver, "QLBG_S_5.png", name_module)
    #                 print("Failse: Sửa bài giảng khi chọn loại bài giảng là audio")
    #                 save_test_result("Sua_bai_giang_khi_chon_loai_bai_giang_la_audio", "fail", video_path,
    #                                  screenshot)
    #     else:
    #         screenshot = take_screenshot(driver, "QLBG_T_4.png", name_module)
    #         print("Failse: Thêm mới bài giảng khi chọn loại bài giảng là audio")
    #         save_test_result("Them_moi_bai_giang_khi_chon_loai_bai_giang_la_audio", "fail", video_path, screenshot)
    #
    # #Thêm mới bài giảng khi chọn loại bài giảng là video
    # time.sleep(1)
    # QLBG_T_3(driver, Ttenbgbbvd, dmbgvd, lbgvd)
    # WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//input[@id='table_search_all']"))).clear()
    # WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//input[@id='table_search_all']"))).send_keys(Ttenbgbbvd)
    # driver.find_element(By.XPATH, "//input[@id='table_search_all']").send_keys(Keys.ENTER)
    # k = driver.find_elements(By.XPATH, '//table[@id="tableData"]//tbody//tr')
    # j = len(k)
    # if (j > 0):
    #     time.sleep(2)
    #     v_test = driver.find_element(By.XPATH, "((//table[@id='tableData']//tbody//tr//td)[3]//span)[1]").text
    #     if v_test == Ttenbgbbvd:
    #         print("Pass: Thêm mới bài giảng khi chọn loại bài giảng là video")
    #         save_test_result("Them_moi_bai_giang_khi_chon_loai_bai_giang_la_video", "pass", video_path)
    #
    #         # sửa bài giảng khi chọn loại bài giảng là video
    #         QLBG_S_4(driver, stenbgbbvd, dmbgvd, lbgvd)
    #         WebDriverWait(driver, 10).until(
    #             EC.element_to_be_clickable((By.XPATH, "//input[@id='table_search_all']"))).clear()
    #         WebDriverWait(driver, 10).until(
    #             EC.element_to_be_clickable((By.XPATH, "//input[@id='table_search_all']"))).send_keys(stenbgbbvd)
    #         driver.find_element(By.XPATH, "//input[@id='table_search_all']").send_keys(Keys.ENTER)
    #         time.sleep(1)
    #         k = driver.find_elements(By.XPATH, '//table[@id="tableData"]//tbody//tr')
    #         j = len(k)
    #         if (j > 0):
    #             v2_test = driver.find_element(By.XPATH, "((//table[@id='tableData']//tbody//tr//td)[3]//span)[1]").text
    #             if v2_test == stenbgbbvd:
    #                 print("Pass: sửa bài giảng khi chọn loại bài giảng là video")
    #                 save_test_result("Sua_bai_giang_khi_chon_loai_bai_giang_la_video", "pass", video_path)
    #                 time.sleep(1)
    #                 QLBG_X_1(driver)
    #                 print ("pass xóa")
    #             else:
    #                 screenshot = take_screenshot(driver, "QLBG_S_4.png", name_module)
    #                 print("Failse: sửa bài giảng khi chọn loại bài giảng là video")
    #                 save_test_result("Sua_bai_giang_khi_chon_loai_bai_giang_la_video", "fail", video_path,
    #                                  screenshot)
    #
    #     else:
    #         screenshot = take_screenshot(driver, "QLBG_T_3.png", name_module)
    #         print("Failse: Thêm mới bài giảng khi chọn loại bài giảng là video")
    #         save_test_result("Them_moi_bai_giang_khi_chon_loai_bai_giang_la_video", "fail", video_path, screenshot)
    #
    # #Thêm mới bài giảng bắt buộc
    # QLBG_T_2(driver, Ttenbgbb, dmbg,lbg)
    # WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//input[@id='table_search_all']"))).clear()
    # WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "//input[@id='table_search_all']"))).send_keys(Ttenbgbb)
    # driver.find_element(By.XPATH, "//input[@id='table_search_all']").send_keys(Keys.ENTER)
    # k = driver.find_elements(By.XPATH, '//table[@id="tableData"]//tbody//tr')
    # j = len(k)
    # if (j > 0):
    #     time.sleep(2)
    #     v_test = driver.find_element(By.XPATH, "((//table[@id='tableData']//tbody//tr//td)[3]//span)[1]").text
    #     if v_test == Ttenbgbb:
    #         print("Pass: Thêm mới bài giảng trường bắt buộc")
    #         save_test_result("Them_moi_bai_giang_truong_bat_buoc", "pass", video_path)
    #
    #         #Sửa bài giảng khi nhập trùng tên bài giảng và danh mục bài giảng đã tồn tại
    #         QLBG_S_6(driver, Ttenbgtrung)
    #         element = WebDriverWait(driver, 5).until(
    #         EC.presence_of_element_located(
    #                 (By.XPATH, "//li[contains(text(),'Bài giảng đã tồn tại.')]"))
    #         )
    #         if element.is_displayed():
    #             print("Pass: Sửa bài giảng khi nhập trùng tên bài giảng và danh mục bài giảng đã tồn tại")
    #             save_test_result("Sua_bai_giang_khi_nhap_trung_ten_danh_muc_da_ton_tai", "pass", video_path)
    #
    #         else:
    #             print("Fail: Sửa bài giảng khi nhập trùng tên bài giảng và danh mục bài giảng đã tồn tại")
    #             screenshot = take_screenshot(driver, "QLBG_S_6.png", name_module)
    #             save_test_result("Sua_bai_giang_khi_nhap_trung_ten_danh_muc_da_ton_tai", "fail", video_path, screenshot)
    #
    #         #Sửa bài giảng khi không nhập trường bắt buộc
    #         QLBG_S_7(driver)
    #         element = WebDriverWait(driver, 5).until(
    #         EC.presence_of_element_located(
    #                 (By.XPATH, "//li[contains(text(),'Tên bài giảng không được để trống!')]"))
    #         )
    #         if element.is_displayed():
    #             print("Pass: Sửa bài giảng khi không nhập trường bắt buộc")
    #             save_test_result("Sua_bai_giang_khi_khong_nhap_truong_bat_buoc", "pass", video_path)
    #
    #         else:
    #             print("Fail: Sửa bài giảng khi không nhập trường bắt buộc")
    #             screenshot = take_screenshot(driver, "QLBG_S_7.png", name_module)
    #             save_test_result("Sua_bai_giang_khi_khong_nhap_truong_bat_buoc", "fail", video_path, screenshot)
    #         WebDriverWait(driver, 10).until(
    #             EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Xác nhận')]"))).click()
    #
    #         #Sửa bài giảng với file ảnh > 25MB
    #         QLBG_S_9(driver)
    #         element = WebDriverWait(driver, 5).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, "//h2[contains(text(),'Lưu ý')]"))
    #         )
    #         if element.is_displayed():
    #             print("Pass: Sửa bài giảng với file ảnh > 25MB")
    #             save_test_result("Sua_bai_giang_voi_file_>25MB", "pass", video_path)
    #
    #         else:
    #             print("Fail: Sửa bài giảng với file ảnh > 25MB")
    #             screenshot = take_screenshot(driver, "QLBG_S_9.png", name_module)
    #             save_test_result("Sua_bai_giang_voi_file_>25MB", "fail", video_path, screenshot)
    #
    #         driver.find_element(By.XPATH, "//button[contains(text(),'OK')]").click()
    #         WebDriverWait(driver, 5).until( EC.presence_of_element_located((By.XPATH, "(//div[@class='modal-footer']//button)[1]"))
    #         ).click()
    #         #Kiểm tra click vào nút Hủy của popup thêm mới bài giảng
    #         WebDriverWait(driver, 5).until(EC.presence_of_element_located(
    #             (By.XPATH, "(//button[@id='saveData']/..//button)[1]"))
    #         ).click()
    #         element = WebDriverWait(driver, 5).until(
    #             EC.presence_of_element_located(
    #                 (By.XPATH, "//h1[contains(text(),'Quản lý bài giảng')]"))
    #         )
    #         if element.is_displayed():
    #             print("Pass: Kiểm tra click vào nút Hủy của popup sửa bài giảng")
    #             save_test_result("Kiem_tra_click_vao_nut_huy_của_popup_sua_bai_giang", "pass", video_path)
    #
    #         else:
    #             print("Fail: Kiểm tra click vào nút Hủy của popup sửa bài giảng")
    #             screenshot = take_screenshot(driver, "QLBG_S_8.png", name_module)
    #             save_test_result("Kiem_tra_click_vao_nut_huy_của_popup_sua_bai_giang", "fail", video_path, screenshot)
    #         # Sửa bài giảng bắt buộc
    #         QLBG_S_3(driver, stenbgbb, sdmbgbb, slbgbb)
    #         WebDriverWait(driver, 10).until(
    #             EC.element_to_be_clickable((By.XPATH, "//input[@id='table_search_all']"))).clear()
    #         WebDriverWait(driver, 10).until(
    #             EC.element_to_be_clickable((By.XPATH, "//input[@id='table_search_all']"))).send_keys(stenbgbb)
    #         driver.find_element(By.XPATH, "//input[@id='table_search_all']").send_keys(Keys.ENTER)
    #         k = driver.find_elements(By.XPATH, '//table[@id="tableData"]//tbody//tr')
    #         j = len(k)
    #         if (j > 0):
    #             time.sleep(2)
    #             v_test = driver.find_element(By.XPATH, "((//table[@id='tableData']//tbody//tr//td)[3]//span)[1]").text
    #             if v_test == stenbgbb:
    #                 print("Pass: Sửa bài giảng bắt buộc")
    #                 save_test_result("sua_bai_giang_truong_bat_buoc", "pass", video_path)
    #
    #                 QLBG_X_1(driver)
    #                 time.sleep(2)
    #                 print("pass xóa")
    #
    #             else:
    #                 screenshot = take_screenshot(driver, "QLBG_S_3.png", name_module)
    #                 print("Failse: Sửa bài giảng bắt buộc")
    #                 save_test_result("Sua_bai_giang_truong_bat_buoc", "fail", video_path, screenshot)
    #
    #     else:
    #         screenshot = take_screenshot(driver, "QLBG_T_2.png", name_module)
    #         print("Failse: Thêm mới bài giảng trường bắt buộc")
    #         save_test_result("Them_moi_bai_giang_truong_bat_buoc", "fail", video_path, screenshot)

    #Thêm mới bài giảng tất cả các trường
    time.sleep(1)
    QLBG_T_1(driver, Ttenbaigiang,Stenbb,Sloaibaigiang, tmotaqlbg, gio, phut, giay)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='table_search_all']"))).clear()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='table_search_all']"))).send_keys(Ttenbaigiang)
    driver.find_element(By.XPATH, "//input[@id='table_search_all']").send_keys(Keys.ENTER)
    k = driver.find_elements(By.XPATH, '//table[@id="tableData"]//tbody//tr')
    j = len(k)
    if (j > 0):
        time.sleep(2)
        v_test = driver.find_element(By.XPATH, "((//table[@id='tableData']//tbody//tr//td)[3]//span)[1]").text
        if v_test == Ttenbaigiang:
            print("Pass: Thêm thành công")
            save_test_result("Thêm bài giảng", "pass", video_path)


            # Kiểm tra cập nhật bài giảng hiển thị đúng dữ liệu
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='btnAdd']"))).click()
            time.sleep(1)
            ten = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='lectureTitle']"))).get_attribute(
                "value")
            lbg = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Danh mục bài giảng')]//../span"))).get_attribute(
                "value")
            dmbg = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//label[contains(text(),'Loại bài giảng')]/../span"))).get_attribute(
                "value")
            mota = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//textarea[@id='lectureDescription']"))).get_attribute(
                "value")

            h = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//input[@id='lectureHourAllow']"))).get_attribute(
                "value")
            p = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//input[@id='lectureMinuteAllow']"))).get_attribute(
                "value")
            s = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//input[@id='lectureSecondAllow']"))).get_attribute(
                "value")
            if ten == Ttenbaigiang and lbg ==Sloaibaigiang and dmbg == Stenbb and mota == tmotaqlbg and h == gio and p == phut and s == giay:
                print("Pass: Kiểm tra cập nhật bài giảng hiển thị đúng dữ liệu")
                save_test_result("Kiem_tra_cap_nhat_bai_giang_hien_thi_dung_du_lieu", "pass", video_path)
            else:
                screenshot = take_screenshot(driver, "QLBG_S_1.png", name_module)
                print("Fail: Xem lại chức năng Kiểm tra cập nhật bài giảng hiển thị đúng dữ liệu")
                save_test_result("Kiem_tra_cap_nhat_bai_giang_hien_thi_dung_du_lieu", "fail", video_path, screenshot)

            #Sửa bài giảng tất cả các trường
            QLBG_S_2(driver, stenbaigiang, sdmbg, Slbg, smotaqlbg,sgio, sphut, sgiay)
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='table_search_all']"))).clear()
            WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='table_search_all']"))).send_keys(stenbaigiang)
            driver.find_element(By.XPATH, "//input[@id='table_search_all']").send_keys(Keys.ENTER)
            k = driver.find_elements(By.XPATH, '//table[@id="tableData"]//tbody//tr')
            j = len(k)

            if (j > 0):
                time.sleep(2)
                v_test_sua = driver.find_element(By.XPATH, "((//table[@id='tableData']//tbody//tr//td)[3]//span)[1]").text
                print(v_test_sua)
                if v_test_sua == stenbaigiang:
                    print("Pass: sửa thành công")
                    save_test_result("Sửa bài giảng", "pass", video_path)
                    #Xóa
                    QLBG_X_1(driver)
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//input[@id='table_search_all']"))).clear()
                    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='table_search_all']"))).send_keys(stenbaigiang)
                    driver.find_element(By.XPATH, "//input[@id='table_search_all']").send_keys(Keys.ENTER)

                    rows = driver.find_elements(By.XPATH, '//table[@id="tableData"]//tbody//tr')
                    found = False  # Ban đầu giả định chưa tìm thấy bài giảng cần kiểm tra

                    j = len(rows)
                    if (j >= 1):
                        time.sleep(3)
                        v_a = driver.find_element(By.XPATH, "//table/tbody//tr[1]").text
                        if v_a != "Không tìm thấy kết quả":
                            i = 1
                            while i <= j:
                                time.sleep(3)
                                print("//table/tbody//tr[" + str(i) + "]//td[3]")
                                ten_bg = driver.find_element(By.XPATH, "//table/tbody//tr[" + str(
                                    i) + "]//td[3]").text  # Lấy tên bài giảng ở cột 3
                                if ten_bg == stenbaigiang:
                                    found = True
                                    break
                                i = i + 1
                        elif v_a == "Không tìm thấy kết quả":
                            found = False

                    if found:
                        screenshot = take_screenshot(driver, "delete_quanlybaigiang.png", name_module)
                        print("Fail: Bài giảng vẫn còn - chức năng xóa cần xem lại")
                        save_test_result("Xóa bài giảng", "fail", video_path, screenshot)
                    else:
                        print("Pass: Xóa thành công")
                        save_test_result("Xóa bài giảng", "pass", video_path)

                else:
                    screenshot = take_screenshot(driver, "edit_quanlybaigiang.png", name_module)
                    print("Failse: Xem lại chức năng sửa")
                    save_test_result("Sửa bài giảng", "fail", video_path, screenshot)
        else:
            screenshot =take_screenshot(driver, "QLBG_T_1.png", name_module)
            print("Failse: Xem lại chức năng thêm")
            save_test_result("Thêm bài giảng", "fail", video_path, screenshot)
    return
if __name__ == '__main__':
    # v_b = os.path.join("TestReport", "Video", "quanlybaigiang", "record.avi")
    # filename = os.path.join(os.getcwd(), v_b)
    # print(filename)
    Ttenbaigiang = data["quanlybaigiang"]["add"]["tenbg"]
    Stenbb = data["quanlybaigiang"]["addbb"]["dmbg"]
    Sloaibaigiang = data["quanlybaigiang"]["addbb"]["lbg"]
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

    #Bắt đầu quay video
    recording = True
    video_thread = threading.Thread(target=record_screen)
    video_thread.start()

    try:
        driver = Login()
        Quanlybaigiang(driver, Ttenbaigiang,Stenbb,Sloaibaigiang, Ttenbgbb,dmbg,lbg,tmotaqlbg, gio, phut, giay, Ttenbgbbvd, dmbgvd, lbgvd, Ttenbgbbaudio, dmbgaudio, lbgaudio,Ttenbgtrung, stenbgbbaudio,stenbgbbvd,stenbgbb, sdmbgbb, slbgbb,stenbaigiang, sdmbg, Slbg, smotaqlbg,sgio, sphut, sgiay,video_path) #video_path
    finally:
        driver.quit()
        recording = False
        video_thread.join()
        print("[✔] Đã quay video và chụp ảnh hoàn tất.")
        print("\n[KẾT QUẢ KIỂM THỬ]:")
        for i, result in enumerate(test_results, start=1):
            print(
                f"Testcase {i}: {result['testcase']}, {result['status']}, {result['video']}, Screenshot: {result['screenshot']}")
