EM=""
PASSWORD=""
# from bs4 import BeautifulSoup
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3912867225&geoId=102713980&keywords=web%20development%20intern&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true")




try:
    skip=driver.find_element(By.XPATH,'/html/body/div[5]/div/div/section/button/icon/svg')
    skip.click()
except Exception as e:
    pass
#
# #to let the page load fully usse time.sleep(2) so that automation does not get affected
time.sleep(2)
login=driver.find_element(By.XPATH,"/html/body/div[2]/a[1]")
login.click()

time.sleep(2)

em=driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div[1]/form/div[1]/input')
em.send_keys(EM)

ps=driver.find_element(By.XPATH, '/html/body/div/main/div[2]/div[1]/form/div[2]/input')
ps.send_keys(PASSWORD)

# /html/body/div[1]/main/div[2]/div[1]/form/div[3]/button
lg=driver.find_element(By.XPATH, '/html/body/div[1]/main/div[2]/div[1]/form/div[3]/button')
lg.click()
time.sleep(2)

apply=driver.find_element(By.XPATH,'/html/body/div[5]/div[3]/div[4]/div/div/main/div/div[2]/div[2]/div/div[2]/div/div[1]/div/div[1]/div/div[1]/div/div[6]/div/div/div/button/span')
apply.click()

submit=driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button/span')
submit.click()

next=driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div/div[2]/form/footer/div[2]/button[2]')
next.click()



