from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re 

driver = webdriver.Chrome()
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

def is_valid_phone(phone_number):
    return re.fullmatch(r"\d{10}", phone_number) is not None  

driver.find_element(By.ID, "firstName").send_keys("Tran")
driver.find_element(By.ID, "lastName").send_keys("Van A")
driver.find_element(By.ID, "userEmail").send_keys("vana@example.com")
driver.find_element(By.XPATH, "//label[text()='Female']").click()

phone_input = driver.find_element(By.ID, "userNumber")
phone_number = "0987654321"  

if is_valid_phone(phone_number):
    phone_input.send_keys(phone_number)
    print(" Số điện thoại hợp lệ, tiếp tục form.")
else:
    print(" Số điện thoại không hợp lệ! Hãy nhập số đúng 10 chữ số.")
    driver.quit()  

driver.find_element(By.ID, "dateOfBirthInput").click()
driver.find_element(By.XPATH, "//option[text()='1995']").click()
driver.find_element(By.XPATH, "//option[text()='March']").click()
driver.find_element(By.XPATH, "//div[contains(@class,'react-datepicker__day') and text()='15']").click()

subject = driver.find_element(By.ID, "subjectsInput")
subject.send_keys("English")
subject.send_keys(Keys.RETURN)

driver.find_element(By.XPATH, "//label[text()='Reading']").click()

driver.find_element(By.ID, "currentAddress").send_keys("456 Đường DEF, Quận ABC, Thành phố HN")

driver.find_element(By.ID, "react-select-3-input").send_keys("Uttar Pradesh")
driver.find_element(By.ID, "react-select-3-input").send_keys(Keys.RETURN)
driver.find_element(By.ID, "react-select-4-input").send_keys("Agra")
driver.find_element(By.ID, "react-select-4-input").send_keys(Keys.RETURN)

driver.find_element(By.ID, "submit").click()

modal = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "modal-content")))
assert "Thanks for submitting the form" in modal.text
print("Form đã được submit thành công!")

time.sleep(3)
driver.quit()
