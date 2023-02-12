from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import os
import wget
import random


class Download_IG():
    def __init__(self,acc,pwd,save,category):
        self.account = acc
        self.password = pwd
        self.save_dir = save
        self.cate = category
        
    def waits_web_login(self, ID, key):
        global driver
        element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((ID, str(key))))
        return element

    def web_driver(self):
        # acounts = ["chien_pingru",'chikichikichiachia','c8763_chien']
        # acount = random.choice(acounts)
        options = webdriver.EdgeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        global driver
        driver = webdriver.Edge(options=options)
        driver.set_window_size(500,800)
        driver.get("https://www.instagram.com/")
        username = self.waits_web_login(str(By.NAME),"username")
        password = self.waits_web_login(str(By.NAME),"password")
        login = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button')
        username.clear()
        password.clear()
        username.send_keys(self.account)
        password.send_keys(self.password)
        time.sleep(1)
        login.click()
        self.waits_web_login(By.XPATH,"//button[text()='稍後再說']").click()
        self.waits_web_login(By.XPATH,"//button[text()='稍後再說']").click()
        # folderpath = r'C:\Users\Admin\Desktop\python\Independent_project\IG_imgs'
        folderpath = self.save_dir
        # keywords = ["#比基尼",'#泳裝','#比基尼泳裝']
        keywords_dic = {'cat':["#貓",'#貓咪','#貓奴','cat'],'dog':["#狗",'#狗狗','#狗奴','#dog'],
                        'bird':["#鳥",'#小鳥','#寵物鳥','bird'],'horse':["#馬",'#小馬','#horse', '#pony']}
        keywords = keywords_dic.get(self.cate)
        try:
            k = folderpath.split('/')[-1]
            if k != self.cate:
                path = os.path.join(folderpath,self.cate)
                os.mkdir(path)
            else:
                path = folderpath
        except:
            pass

        for keyword in keywords:
            self.waits_web_login(By.CLASS_NAME, "_aaw8").click()
            search = self.waits_web_login(By.CLASS_NAME, "_aauy")
            search.send_keys(keyword)
            time.sleep(3)
            ActionChains(driver).send_keys(Keys.ENTER).perform()
            ActionChains(driver).send_keys(Keys.ENTER).perform()
            time.sleep(5)
            
            for i in range(5):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                soup = BeautifulSoup(driver.page_source, 'html.parser')
                img_line = soup.find_all('div','_aagv')
                for imgs in img_line:
                    for img in imgs.select('img'):
                        # print(img.get('src'))
                        url = img.get('src')
                        img_name = os.path.basename(url).split('?')[0].split('.')[0]+'.jpg'
                        save_img = os.path.join(path,img_name)
                        if not os.path.exists(save_img):
                            wget.download(url,save_img)
                            # count+=1
                time.sleep(5)
            driver.back()
    def run(self):
        self.web_driver()