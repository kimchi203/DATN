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
from testcase.testcase_loaibaigiang import *
recording = True
driver = None
# video_path = os.path.join(os.getcwd(), "TestReport", "Video", "loaibaigiang", "record_lesson_type.avi")
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


def Loaibaigiang(driver, Ttenlbgtrung, Ttenlbgbb, Stenlbgbb, Tloaibaigiang, Tmotalbg, Sloaibaigiang, Smotalbg, video_path): #video_path
    # name_module = "loaibaigiang"
    # time.sleep(5)
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Bài giảng')])[1]"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Loại bài giảng')])[1]"))).click()
    time.sleep(1)
    # Thêm mới loại bài giảng trùng tên
    # LBG_T_3(driver, Ttenlbgtrung)
    # element = WebDriverWait(driver, 5).until(
    #     EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Loại bài giảng')]/..//li"))
    # ).text
    # v = 'Tên loại bài giảng đã tồn tại.'
    # if v == element:
    #     print("Pass: Thêm mới loại bài giảng đã tồn tại tên")
    #     save_test_result("them_moi_loai_bai_giang_da_ton_tai_ten", "pass", video_path)
    #
    # else:
    #     print("Fail: Xem lại chức năng Thêm mới loại bài giảng đã tồn tại tên")
    #     screenshot = take_screenshot(driver, "LBG_T_3.png", name_module)
    #     save_test_result("them_moi_loai_bai_giang_da_ton_tai_ten", "fail", video_path, screenshot)
    #
    # WebDriverWait(driver, 5).until(
    #     EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'OK')]"))
    # ).click()
    # #Không thêm giữ liệu vào trường bắt buộc
    # LBG_T_4(driver)
    # element = WebDriverWait(driver, 5).until(
    #     EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Loại bài giảng')]/..//li"))
    # ).text
    # v = 'Loại bài giảng không được để trống.'
    # if v == element:
    #     print("Pass: Thêm loại bài giảng khi không nhập trường bắt buộc")
    #     save_test_result("them_moi_loai_bai_giang_khi_Khong_nhap_truong_bat_buoc", "pass", video_path)
    #
    # else:
    #     print("Fail: Xem lại chức năng Thêm loại bài giảng khi không nhập trường bắt buộc")
    #     screenshot = take_screenshot(driver, "LBG_T_4.png", name_module)
    #     save_test_result("them_moi_loai_bai_giang_khi_Khong_nhap_truong_bat_buoc", "fail", video_path, screenshot)
    #
    # WebDriverWait(driver, 5).until(
    #     EC.presence_of_element_located((By.XPATH, "//button[contains(text(),'OK')]"))
    # ).click()
    # LBG_T_5(driver)
    # element = WebDriverWait(driver, 5).until(
    #     EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Loại bài giảng')]"))
    # )
    # if element.is_displayed():
    #     print("Pass: Kiểm tra click vào nút Đóng của popup thêm mới loại bài giảng")
    #     save_test_result("Kiem_tra_click_vao_nut_Dong_cua_popup_them_moi_loai_bai_giang", "pass", video_path)
    #
    # else:
    #     print("Fail: Xem lại chức năng Kiểm tra click vào nút Đóng của popup thêm mới loại bài giảng")
    #     screenshot = take_screenshot(driver, "LBG_T_5.png", name_module)
    #     save_test_result("Kiem_tra_click_vao_nut_Dong_cua_popup_them_moi_loai_bai_giang", "fail", video_path, screenshot)
    #
    # #Thêm mới chỉ nhập trường bắt buộc
    # LBG_T_2(driver, Ttenlbgbb)
    # search_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "table_search_all")))
    # search_box.clear()
    # search_box.send_keys(Ttenlbgbb)
    # time.sleep(1)
    # search_box.send_keys(Keys.ENTER)
    # time.sleep(1)
    # rows = driver.find_elements(By.XPATH, '//table[@id="tableData"]//tbody//tr//td')
    # if len(rows) > 1:
    #     print("Pass: Thêm mới loại bài giảng chỉ nhập trường bắt buộc thành công")
    #     save_test_result("them_moi_loai_bai_giang_chi_nhap_truong_bat_buoc", "pass", video_path)
    #
    #     #Kiểm tra cập nhật loại bài giảng hiển thị đúng dữ liệu
    #     driver.find_element(By.CLASS_NAME, "btn-admin-edit").click()
    #     name_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "name"))).get_attribute("value")
    #     if name_input == Ttenlbgbb:
    #         print("Pass: Kiểm tra cập nhật loại bài giảng hiển thị đúng dữ liệu")
    #         save_test_result("Kiem_tra_cap_nhat_loai_bai_giang_hien_thi", "pass", video_path)
    #     else:
    #         screenshot = take_screenshot(driver, "LBG_S_1.png", name_module)
    #         print("Fail: Xem lại chức năng Kiểm tra cập nhật loại bài giảng hiển thị đúng dữ liệu")
    #         save_test_result("Kiem_tra_cap_nhat_loai_bai_giang_hien_thi", "fail", video_path, screenshot)
    #
    #     #Sửa loại bài giảng khi nhập trùng loại bài giảng đã tồn tại
    #     LBG_S_4(driver, Ttenlbgtrung)
    #     element = WebDriverWait(driver, 5).until(
    #         EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Loại bài giảng')]/..//li"))
    #     ).text
    #     v = 'Tên loại bài giảng đã tồn tại.'
    #     if v == element:
    #         print("Pass: Sửa loại bài giảng đã tồn tại tên")
    #         save_test_result("Sua_loai_bai_giang_da_ton_tai_ten", "pass", video_path)
    #
    #     else:
    #         print("Fail: Xem lại chức năng sửa loại bài giảng đã tồn tại tên")
    #         screenshot = take_screenshot(driver, "LBG_S_4.png", name_module)
    #         save_test_result("sua_loai_bai_giang_da_ton_tai_ten", "fail", video_path, screenshot)
    #     WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'OK')]"))).click()
    #
    #     #Sửa loại bài giảng khi không nhập trường bắt buộc
    #     LBG_S_5(driver)
    #     element = WebDriverWait(driver, 5).until(
    #         EC.presence_of_element_located((By.XPATH, "//h2[contains(text(),'Loại bài giảng')]/..//li"))
    #     ).text
    #     v = 'Loại bài giảng không được để trống.'
    #     if v == element:
    #         print("Pass: Sửa loại bài giảng khi không nhập trường bắt buộc")
    #         save_test_result("sua_loai_bai_giang_khi_Khong_nhap_truong_bat_buoc", "pass", video_path)
    #
    #     else:
    #         print("Fail: Xem lại chức năng sửa loại bài giảng khi không nhập trường bắt buộc")
    #         screenshot = take_screenshot(driver, "LBG_S_5.png", name_module)
    #         save_test_result("sua_loai_bai_giang_khi_Khong_nhap_truong_bat_buoc", "fail", video_path, screenshot)
    #
    #     WebDriverWait(driver, 10).until(
    #         EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'OK')]"))).click()
    #
    #     #Kiểm tra click vào nút Đóng của popup cập nhật loại bài giảng
    #     LBG_S_6(driver)
    #     element = WebDriverWait(driver, 5).until(
    #         EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Loại bài giảng')]"))
    #     )
    #     if element.is_displayed():
    #         print("Pass: Kiểm tra click vào nút Đóng của popup sửa loại bài giảng")
    #         save_test_result("Kiem_tra_click_vao_nut_Dong_cua_popup_sua_loai_bai_giang", "pass", video_path)
    #
    #     else:
    #         print("Fail: Xem lại chức năng Kiểm tra click vào nút Đóng của popup sửa loại bài giảng")
    #         screenshot = take_screenshot(driver, "LBG_S_6.png", name_module)
    #         save_test_result("Kiem_tra_click_vao_nut_Dong_cua_popup_sua_loai_bai_giang", "fail", video_path,screenshot)
    #
    #     #Sửa loại bài giảng khi chỉ sửa trường bắt buộc
    #     LBG_S_3(driver,Stenlbgbb)
    #     search_box.clear()
    #     search_box.send_keys(Stenlbgbb)
    #     search_box.send_keys(Keys.ENTER)
    #     rows = driver.find_elements(By.XPATH, '//table[@id="tableData"]//tbody//tr//td')
    #     if len(rows) > 1:
    #         print("Pass: Sửa loại bài giảng khi chỉ sửa trường bắt buộc")
    #         save_test_result("Sua_loai_bai_giang_khi_chi_sua_truong_bat_buoc", "pass", video_path)
    #
    #         #Hủy xóa
    #         LBG_X_2(driver)
    #         element = WebDriverWait(driver, 5).until(
    #             EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Loại bài giảng')]"))
    #         )
    #         if element.is_displayed():
    #             print("Pass: Kiểm tra click vào nút Hủy của popup xóa loại bài giảng")
    #             save_test_result("Kiem_tra_click_vao_nut_Huy_cua_popup_xoa_loai_bai_giang", "pass", video_path)
    #
    #         else:
    #             print("Fail: Xem lại chức năng Kiểm tra click vào nút Huy của popup xóa loại bài giảng")
    #             screenshot = take_screenshot(driver, "LBG_X_2.png", name_module)
    #             save_test_result("Kiem_tra_click_vao_nut_Huy_cua_popup_xoa_loai_bai_giang", "fail", video_path,
    #                              screenshot)
    #
    #         #Xóa
    #         LBG_X_1(driver)
    #         # search_box.clear()
    #         # search_box.send_keys(Stenlbgbb)
    #         # search_box.send_keys(Keys.ENTER)
    #         #
    #         # rows = driver.find_elements(By.XPATH, '//table[@id="tableData"]//tbody//tr//td')
    #         # if len(rows) > 1:
    #         #     screenshot = take_screenshot(driver, "LBG_X_1.png", name_module)
    #         #     print("Fail: Xem lại chức năng xóa")
    #         #     save_test_result("Xóa loại bài giảng", "fail", video_path, screenshot)
    #         # else:
    #         #     print("Pass: Xóa thành công")
    #         #     save_test_result("Xóa loại bài giảng", "pass", video_path)
    #
    #     else:
    #         screenshot = take_screenshot(driver, "LBG_S_3.png", name_module)
    #         print("Fail: Xem lại chức năng Sửa loại bài giảng khi chỉ sửa trường bắt buộc")
    #         save_test_result("Sua_loai_bai_giang_khi_chi_sua_truong_bat_buoc", "fail", video_path, screenshot)
    #
    #
    #
    # else:
    #     screenshot = take_screenshot(driver, "LBG_T_2.png", name_module)
    #     print("Fail: Xem lại chức năng Thêm mới loại bài giảng chỉ nhập trường bắt buộc")
    #     save_test_result("them_moi_loai_bai_giang_chi_nhap_truong_bat_buoc", "fail", video_path, screenshot)

    #Thêm tất cả các trường
    LBG_T_1(driver, Tloaibaigiang, Tmotalbg)
    search_box = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "table_search_all")))
    search_box.clear()
    search_box.send_keys(Tloaibaigiang)
    search_box.send_keys(Keys.ENTER)
    rows = driver.find_elements(By.XPATH, '//table[@id="tableData"]//tbody//tr//td')
    if len(rows) > 1:
        print("Pass: Thêm mới loại bài giảng vào tất cả các trường thành công")
        save_test_result("Them_moi_loai_bai_giang_tat_ca_cac_truong", "pass", video_path)

        #Sửa tất cả các trường
        LBG_S_2(driver, Sloaibaigiang, Smotalbg)

        search_box.clear()
        search_box.send_keys(Sloaibaigiang)
        search_box.send_keys(Keys.ENTER)
        rows = driver.find_elements(By.XPATH, '//table[@id="tableData"]//tbody//tr//td')
        if len(rows) > 1:
            print("Pass: Sửa loại bài giảng tất cả các trường thành công")
            save_test_result("Sua_loai_bai_giang_tat_ca_truong_thanh_cong", "pass", video_path)
            #Xóa
            # LBG_X_1(driver)
            # search_box.clear()
            # search_box.send_keys(Sloaibaigiang)
            # search_box.send_keys(Keys.ENTER)
            #
            # rows = driver.find_elements(By.XPATH, '//table[@id="tableData"]//tbody//tr//td')
            # if len(rows) > 1:
            #     screenshot = take_screenshot(driver, "LBG_X_1.png", name_module)
            #     print("Fail: Xem lại chức năng xóa")
            #     save_test_result("Xóa loại bài giảng", "fail", video_path, screenshot)
            # else:
            #     print("Pass: Xóa thành công")
            #     save_test_result("Xóa loại bài giảng", "pass", video_path)
        else:
            screenshot = take_screenshot(driver, "LBG_S_2.png", name_module)
            print("Fail: Xem lại chức năng Sửa loại bài giảng tất cả các trường")
            save_test_result("Sua_loai_bai_giang_tat_ca_truong_thanh_cong", "fail", video_path, screenshot)
    else:
        screenshot = take_screenshot(driver, "LBG_T_1.png", name_module)
        print("Fail: Xem lại chức năng thêm mới loại bài giảng vào tất cả các trường")
        save_test_result("Them_moi_loai_bai_giang_tat_ca_cac_truong", "fail", video_path, screenshot)
    return test_results
if __name__ == '__main__':
    Ttenlbgtrung = data["loaibaigiang"]["fail"]["ten"]
    Ttenlbgbb = data["loaibaigiang"]["addbb"]["ten"]
    Stenlbgbb = data["loaibaigiang"]["editbb"]["ten"]
    Tloaibaigiang = data["loaibaigiang"]["add"]["ten"]
    Tmotalbg = data["loaibaigiang"]["add"]["mota"]
    Sloaibaigiang = data["loaibaigiang"]["edit"]["ten"]
    Smotalbg = data["loaibaigiang"]["edit"]["mota"]

    # Bắt đầu quay video
    recording = True
    video_thread = threading.Thread(target=record_screen)
    video_thread.start()

    try:
        driver = Login()
        Loaibaigiang(driver, Ttenlbgtrung, Ttenlbgbb,Stenlbgbb, Tloaibaigiang, Tmotalbg, Sloaibaigiang, Smotalbg,video_path) #video_path
    finally:
        driver.quit()
        recording = False
        video_thread.join()
        print("[✔] Đã quay video và chụp ảnh hoàn tất.")
        print("\n[KẾT QUẢ KIỂM THỬ]:")
        for i, result in enumerate(test_results, start=1):
            print(
                f"Testcase {i}: {result['testcase']}, {result['status']}, {result['video']}, Screenshot: {result['screenshot']}")
