from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Login(usernam, password):
    # Tạo một Options object
    chrome_options = Options()
    # Thêm đường dẫn của ChromeDriver vào Options
    chrome_options.add_argument("--webdriver.chrome.driver=exec_path")

    # Khởi tạo trình điều khiển (driver) với Options
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("http://www.learnico.id.vn/sign-in")
    driver.maximize_window()
    # time.sleep(5)

    driver.find_element(By.XPATH, "//input[@id='username']").send_keys(usernam)
    driver.find_element(By.XPATH, "//input[@id='password']").send_keys(password)
    driver.find_element(By.XPATH, "//button[@id='btnLogin']").click()
    # time.sleep(3)
    try:
        # Chờ xem có nút OK không (có thể là thông báo đăng nhập thành công hoặc thất bại)
        ok_button = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'OK')]"))
        )
        ok_button.click()

        time.sleep(1)  # Chờ một chút để chuyển trang nếu cần

        # Kiểm tra xem đã chuyển sang Dashboard chưa (ví dụ kiểm tra URL hoặc một phần tử đặc trưng)
        if "dashboard" in driver.current_url.lower():
            print("✅ Đăng nhập thành công! Đã vào dashboard.")
            return True
        else:
            print("❌ Đăng nhập thất bại. Vẫn ở trang login.")
            return False

    except TimeoutException:
        print("❌ Không xuất hiện nút OK sau khi đăng nhập. Có thể hệ thống bị lỗi.")
        return False
    finally:
        driver.find_element(By.XPATH, "//input[@id='username']").clear()
        driver.find_element(By.XPATH, "//input[@id='password']").clear()


#case1
def test_login_cases():
    test_cases = [
        {"username": "admin", "password": "sai_pass", "expect_success": False},
        {"username": "sai_user", "password": "admin123", "expect_success": False},
        {"username": "", "password": "admin123", "expect_success": False},
        {"username": "admin", "password": "", "expect_success": False},
        {"username": "", "password": "", "expect_success": False},
        {"username": "admin", "password": "123456", "expect_success": True},
    ]

    for i, case in enumerate(test_cases, start=1):
        print(f"\n===> Running Test Case {i}: {case}")
        result = Login(case["username"], case["password"])
        if result == case["expect_success"]:
            print("✅ Passed")
        else:
            print("❌ Failed")








