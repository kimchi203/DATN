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
import json
from testcase.testcase_danhmucbaigiang import *
from selenium.common.exceptions import TimeoutException

# Biến toàn cục
recording = True
driver = None
# video_path = os.path.join(os.getcwd(), "TestReport", "Video", "danhmucbaigiang", "record.avi")

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


def Danhmucbaigiang(driver, tentrung, Tten,Tcapcha, Tmota,Stendmbg, Smotadmbg, Ttenbb,Stenbb,video_path): #video_path, Tten, Tmota, Stendmbg, Smotadmbg,
    # name_module="danhmucbaigiang"
    time.sleep(5)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Bài giảng')])[1]"))).click()
    time.sleep(2)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//span[contains(text(),'Danh mục bài giảng')])[1]"))).click()

    #Thêm mới danh mục bài giảng trùng tên
    # DMBG_T_3(driver, tentrung)
    # element = WebDriverWait(driver, 5).until(
    #         EC.presence_of_element_located((By.XPATH, "//li[contains(text(),'Tên danh mục bài giảng đã tồn tại.')]"))
    # )
    # if element.is_displayed():
    #     print("Pass: Thêm mới danh mục bài giảng đã tồn tại tên")
    #     save_test_result("them_moi_danh_muc_bai_giang_da_ton_tai_ten", "pass", video_path)
    #
    # else:
    #     print("Fail: Xem lại chức năng Thêm mới danh mục bài giảng đã tồn tại tên")
    #     screenshot = take_screenshot(driver, "DMBG_T_3.png", name_module)
    #     save_test_result("them_moi_danh_muc_bai_giang_da_ton_tai_ten", "fail", video_path, screenshot)
    # driver.find_element(By.XPATH,"//button[contains(text(),'OK')]").click()
    #
    # #Thêm danh mục bài giảng khi không nhập trường bắt buộc
    # DMBG_T_4(driver)
    # element = WebDriverWait(driver, 5).until(
    #     EC.presence_of_element_located((By.XPATH, "//li[contains(text(),'Tên không được để trống')]"))
    # )
    # if element.is_displayed():
    #     print("Pass: Thêm mới danh mục bài giảng khi không nhập trường bắt buộc")
    #     save_test_result("them_moi_danh_muc_bai_giang_khi_khong_nhap_truong_bat_buoc", "pass", video_path)
    #
    # else:
    #     print("Fail: Xem lại chức năng Thêm mới danh mục bài giảng khi không nhập trường bắt buộc")
    #     screenshot = take_screenshot(driver, "DMBG_T_4.png", name_module)
    #     save_test_result("them_moi_danh_muc_bai_giang_hi_khong_nhap_truong_bat_buoc", "fail", video_path, screenshot)
    # driver.find_element(By.XPATH, "//button[contains(text(),'OK')]").click()
    #
    # #Kiểm tra click vào nút Hủy của popup thêm mới danh mục bài giảng
    # DMBG_T_5(driver)
    # element = WebDriverWait(driver, 5).until(
    #     EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Danh mục bài giảng')]"))
    # )
    # if element.is_displayed():
    #     print("Pass: Kiểm tra click vào nút Đóng của popup thêm mới danh mục bài giảng")
    #     save_test_result("Dong_popup_them_moi_danh_muc_bai_giang", "pass", video_path)
    #
    # else:
    #     print("Fail: Xem lại chưc năng khi click vào nút Đóng của popup thêm mới danh mục bài giảng")
    #     screenshot = take_screenshot(driver, "DMBG_T_5.png", name_module)
    #     save_test_result("Dong_popup_them_moi_danh_muc_bai_giang", "fail", video_path, screenshot)
    #
    # DMBG_T_1 (driver,Tten,Tcapcha, Tmota )
    # WebDriverWait(driver, 5).until(
    #     EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Vật lý')]/../..//i"))
    # ).click()
    # v_test = driver.find_element(By.XPATH, "//span[contains(text(),'Vật lý')]/../..//li").text
    # time.sleep(1)
    # if v_test == Tten:
    #     print("Pass: Thêm thành công")
    #     save_test_result("Them_thanh_cong_danh_muc_bai_giang", "pass", video_path)
    #
    #     #Kiểm tra cập nhật danh mục bài giảng đã tồn tại tên
    #     DMBG_S_3(driver, tentrung)
    #     element = WebDriverWait(driver, 5).until(
    #         EC.presence_of_element_located((By.XPATH, "//div[contains(text(),'Cập nhật danh mục bài giảng không thành công!')]"))
    #     )
    #     if element.is_displayed():
    #         print("Pass: Cập nhật danh mục bài giảng đã tồn tại tên")
    #         save_test_result("Cap_nhat_danh_muc_bai_giang_da_ton_tai_ten", "pass", video_path)
    #
    #     else:
    #         print("Fail: Xem lại chức năng cập nhật danh mục bài giảng đã tồn tại tên")
    #         screenshot = take_screenshot(driver, "DMBG_S_3.png", name_module)
    #         save_test_result("Cap_nhat_danh_muc_bai_giang_da_ton_tai_ten", "fail", video_path, screenshot)
    #
    #     # Kiểm tra Cập nhật danh mục bài giảng khi không nhập trường bắt buộc
    #     DMBG_S_4(driver)
    #     element = WebDriverWait(driver, 5).until(
    #         EC.presence_of_element_located((By.XPATH, "//li[contains(text(),'Tên không được để trống')]"))
    #     )
    #     if element.is_displayed():
    #         print("Pass: Cập nhật danh mục bài giảng khi không nhập trường bắt buộc")
    #         save_test_result("Cap_nhat_danh_muc_bai_giang_khi_khong_nhap_truong_bat_buoc", "pass", video_path)
    #
    #
    #     else:
    #         print("Fail: Xem lại chức năng Cập nhật danh mục bài giảng khi không nhập trường bắt buộc")
    #         screenshot = take_screenshot(driver, "DMBG_S_4.png", name_module)
    #         save_test_result("Cap_nhat_danh_muc_bai_giang_hi_khong_nhap_truong_bat_buoc", "fail", video_path,
    #                          screenshot)
    #     driver.find_element(By.XPATH, "//button[contains(text(),'OK')]").click()
    #
    #     # Kiểm tra Cập nhật danh mục bài giảng khi không nhập trường bắt buộc
    #     DMBG_s_5(driver)
    #     element = WebDriverWait(driver, 5).until(
    #         EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Danh mục bài giảng')]"))
    #     )
    #     if element.is_displayed():
    #         print("Pass: Kiểm tra click vào nút Đóng của popup cập nhật danh mục bài giảng")
    #         save_test_result("Dong_popup_cap_nhat_danh_muc_bai_giang", "pass", video_path)
    #
    #     else:
    #         print("Fail: Xem lại chưc năng khi click vào nút Đóng của popup câp nhật danh mục bài giảng")
    #         screenshot = take_screenshot(driver, "DMBG_S_5.png", name_module)
    #         save_test_result("Dong_popup_cap_nhat_danh_muc_bai_giang", "fail", video_path, screenshot)
    #
    #     #Kiểm tra sửa thành công
    #     DMBG_S_1(driver, Stendmbg, Smotadmbg)
    #     WebDriverWait(driver, 5).until(
    #         EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Vật lý')]/../..//i"))
    #     ).click()
    #     s_test = driver.find_element(By.XPATH, "//span[contains(text(),'Vật lý')]/../..//li").text
    #     time.sleep(1)
    #     if s_test == Stendmbg:
    #         print("Pass: Cập nhật danh mục bài giảng khi nhập tất cả các trường")
    #         save_test_result("Cap_nhat_danh_muc_bai_giang_khi_sua_tat_ca_truong", "pass", video_path)
    #
    #         DMBG_X_1(driver)
    #         try:
    #             WebDriverWait(driver, 5).until(
    #                 EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'Vật lý')]/../..//i"))
    #             ).click()
    #             x1_test = driver.find_element(By.XPATH, "//span[contains(text(),'Vật lý')]/../..//li").text
    #             time.sleep(1)
    #             if x1_test.is_displayed():
    #                 if x1_test== Stendmbg:
    #                     print("Failse: Xem lại chức năng xóa danh mục bài giảng cấp con")
    #                     screenshot = take_screenshot(driver, "DMBG_X_1.png", name_module)
    #                     save_test_result("xoa_danh_muc_bai_giang_cap_con_thanh_cong", "fail", video_path, screenshot)
    #                 else:
    #                     print("Pass: xóa danh mục bài giảng cấp con thành công")
    #                     save_test_result("xoa_danh_muc_bai_giang_cap_con_thanh_cong", "pass", video_path)
    #             else:
    #                 print("Pass: xóa danh mục bài giảng cấp con thành công")
    #                 save_test_result("xoa_danh_muc_bai_giang_cap_con_thanh_cong", "pass", video_path)
    #         except TimeoutException:
    #             print("Pass: xóa danh mục bài giảng cấp con thành công")
    #             save_test_result("xoa_danh_muc_bai_giang_cap_con_thanh_cong", "pass", video_path)
    #
    #     else:
    #         print("Failse: Xem lại Kiểm tra cập nhật danh mục bài giảng khi nhập tất cả các trường")
    #         screenshot = take_screenshot(driver, "DMBG_S_1.png", name_module)
    #         save_test_result("Cap_nhat_danh_muc_bai_giang_khi_sua_tat_ca_truong", "fail", video_path, screenshot)
    #
    # else:
    #     print("Failse: Xem lại chức năng thêm")
    #     screenshot = take_screenshot(driver, "DMBG_T_1.png", name_module)
    #     save_test_result("Them_thanh_cong_danh_muc_bai_giang", "fail", video_path, screenshot)
    #

    # Thêm dmbg bắt buộc
    DMBG_T_2(driver, Ttenbb)
    # Verify addition
    k = driver.find_elements(By.XPATH, '//ul[@id="tree"]//li//span[@class="branchName"]')
    j = len(k)
    v_kq = 0
    if j > 0:
        tbb_test = driver.find_element(By.XPATH, "(//ul[@id='tree']//li//span[@class='branchName'])[1]").text
        time.sleep(1)
        if tbb_test == Ttenbb:
            print("Pass: Thêm danh mục bài giảng vào trường bắt buộc thành công")
            save_test_result("Them_danh_muc_bai_giang_vao_truong_bat_buoc", "pass", video_path)
            # Chỉ cập nhật trường bắt buộc
            DMBG_S_2(driver, Stenbb)
            k = driver.find_elements(By.XPATH, '//ul[@id="tree"]//li//span[@class="branchName"]')
            j = len(k)
            if j > 0:
                sbb_test = driver.find_element(By.XPATH, "(//ul[@id='tree']//li//span[@class='branchName'])[1]").text
                time.sleep(1)
                if sbb_test == Stenbb:
                    print("Pass: Cập nhật danh mục bài giảng khi chỉ nhập trường bắt buộc thành công")
                    save_test_result("Cap_nhat_danh_muc_bai_giang_voi_truong_bat_buoc", "pass", video_path)

                    #Kiểm tra nút Hủy
                    DMBG_X_3(driver)
                    element = WebDriverWait(driver, 5).until(
                        EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Danh mục bài giảng')]"))
                    )
                    if element.is_displayed():
                        print("Pass: Kiểm tra click vào nút Hủy của popup xóa danh mục")
                        save_test_result("Huy_popup_xoa_danh_muc_bai_giang", "pass", video_path)

                    else:
                        print("Fail: Xem lại chưc năng khi click vào nút Hủy của popup xóa danh mục")
                        screenshot = take_screenshot(driver, "DMBG_X_3.png", name_module)
                        save_test_result("Huy_popup_xoa_danh_muc_bai_giang", "fail", video_path, screenshot)

                    # Xóa cấp cha
                    # DMBG_X_2(driver)
                    # time.sleep(3)
                    # k = driver.find_elements(By.XPATH, '//ul[@id="tree"]//li//span[@class="branchName"]')
                    # j = len(k)
                    # if j > 0:
                    #     xcc_test = driver.find_element(By.XPATH, "(//ul[@id='tree']//li//span[@class='branchName'])[1]").text
                    #     time.sleep(1)
                    #     print(v_test)
                    #     if xcc_test != Stenbb:
                    #         print("Pass: xóa danh mục bài giảng cấp cha thành công")
                    #         save_test_result("Xoa_danh_muc_bai_giang_cap_cha", "pass", video_path)
                    #     else:
                    #         screenshot=take_screenshot(driver, "DMBG_X_2.png",name_module)
                    #         print("Failse: Xem lại chức năng xóa danh mục bài giảng cấp cha")
                    #         save_test_result("Xoa_danh_muc_bai_giang_cap_cha", "fail", video_path, screenshot)
                else:
                    screenshot=take_screenshot(driver, "DMBG_S_2.png",name_module)
                    print("Failse: Xem lại chức năng Cập nhật danh mục bài giảng khi chỉ nhập trường bắt buộc")
                    save_test_result("Cap_nhat_danh_muc_bai_giang_voi_truong_bat_buoc", "fail", video_path, screenshot)
        else:
            screenshot=take_screenshot(driver, "DMBG_T_2.png",name_module)
            print("Failse: Xem lại chức năng Thêm danh mục bài giảng vào trường bắt buộc thành công")
            save_test_result("Them_danh_muc_bai_giang_vao_truong_bat_buoc", "fail", video_path, screenshot)
            v_kq = 2
    return test_results



if __name__ == '__main__':
    Tten = data["danhmucbaigiang"]["themfull"]["ten"]
    Tcapcha = data["danhmucbaigiang"]["themfull"]["capcha"]
    Tmota = data["danhmucbaigiang"]["themfull"]["mota"]
    Stendmbg = data["danhmucbaigiang"]["suafull"]["ten"]
    Smotadmbg = data["danhmucbaigiang"]["suafull"]["mota"]
    tentrung = data["danhmucbaigiang"]["fail"]["ten"]
    Ttenbb = data["danhmucbaigiang"]["thembatbuoc"]["ten"]
    Stenbb = data["danhmucbaigiang"]["suabatbuoc"]["ten"]

    # Bắt đầu quay video
    recording = True
    video_thread = threading.Thread(target=record_screen)
    video_thread.start()

    try:
        driver = Login()
        Danhmucbaigiang(driver, tentrung, Tten,Tcapcha, Tmota, Stendmbg, Smotadmbg,Ttenbb,Stenbb,video_path)#video_path Tten, Tmota, Stendmbg, Smotadmbg
    finally:
        driver.quit()
        recording = False
        video_thread.join()
        print("[✔] Đã quay video và chụp ảnh hoàn tất.")
        print("\n[KẾT QUẢ KIỂM THỬ]:")
        for i, result in enumerate(test_results, start=1):
            print(
                f"Testcase {i}: {result['testcase']}, {result['status']}, {result['video']}, Screenshot: {result['screenshot']}")
