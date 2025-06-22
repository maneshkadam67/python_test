import tempfile
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager


def test_search_valid_product():
    options = webdriver.ChromeOptions()


    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')

    # temp_profile = tempfile.mkdtemp()
    # options.add_argument(f'--user-data-dir={temp_profile}')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


    # driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo")
    time.sleep(2)
    driver.find_element(By.NAME,"search").send_keys("HP")
    print("entered hp")
    time.sleep(2)
    driver.find_element(By.XPATH,"//*[@id=\"search\"]/span/button").click()
    print("clicked search")
    time.sleep(4)
    print("Run successfully in docker ...................this")
    driver.quit()



