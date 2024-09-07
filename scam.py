from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException, TimeoutException
import time

# Setup the driver (this example uses Chrome)
driver = webdriver.Chrome()  # specify the path if not in PATH
driver.get("https://appinventivb.com/")
time.sleep(6)  # Initial wait for the site to load

try:
    # Input Username using placeholder text
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Type Username']"))
    )
    username_input.send_keys("#####")

    # Input Password using placeholder text
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Type Password']"))
    )
    password_input.send_keys("#####")

    # Click the Login Button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="login-page"]/form/div[2]/button'))
    )
    login_button.click()
    time.sleep(5)  # Wait for post-login processes to complete

    # Main action loop
    while True:
        try:
            start_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="footer"]/div/div[2]'))
            )
            start_button.click()
        except TimeoutException:
            print("Start button is not clickable or not found.")
            break  # Exit the loop if the start button is not clickable or not found

        time.sleep(2)
        start_miss = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[4]'))
        )
        start_miss.click()

        time.sleep(7)
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div/div[2]/div/div[7]/div[2]/div[2]/div[4]'))
        )
        submit_button.click()
        time.sleep(4)

        input_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/div[2]/div/div[8]/div/div/div/div[1]/label'))
        )
        input_element.click()

except NoSuchElementException:
    print("Some elements were not found on the page. Check the IDs and the page structure.")
finally:
    # Clean up
    driver.quit()

print("Automation completed.")
