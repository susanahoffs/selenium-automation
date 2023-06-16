from time import sleep, time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import urllib.request
import time
import csv
import random
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
 
driver_path = 'C:/Users/Admin/Desktop/Faucet-Tidefi/chromedriver.exe'
url = 'https://discord.com/channels/973057323805311026/979272741150687262' #Thay link kênh discord vào đây
options = webdriver.ChromeOptions()
service = ChromeService(executable_path=driver_path)

options.add_argument('--disable-extensions')
options.add_argument("user-data-dir=C:/Users/Admin/AppData/Local/Google/Chrome/User Data") 

file  = open('info.csv')
reader = csv.reader(file, delimiter=',')

for row in reader:
    options.add_argument('--profile-directory=%s' % (row[0])) #e.g. Profile 3
    print(row[0])
    driver = webdriver.Chrome(service=service, options=options)
    driver.get(url)

    time.sleep(5)

    element = driver.find_element(By.CLASS_NAME, "overflow-1wOqNV")
    element.click()

    msg_class = "markup-eYLPri.editor-H2NA06.slateTextArea-27tjG0.fontSize16Padding-XoMpjI"

    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, msg_class)))

    driver.find_element(By.CLASS_NAME, msg_class).send_keys(row[1]) #thay ?tdfy bằng từ khóa muốn faucet
    driver.find_element(By.CLASS_NAME, msg_class).send_keys(Keys.ENTER)
    time.sleep(4)
    driver.quit()

file.close()
