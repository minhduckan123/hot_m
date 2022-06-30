import string
import random
from queue import Queue
from selenium.webdriver.common.keys import Keys
import threading
import csv
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


jobs = Queue()
chars_fixed = string.ascii_letters
consonants = "bcdfghjklmnpqrstvwxyz"
vowels = "aeiou"


def runtest(t,p):
      user = "".join(random.choice(chars_fixed).lower() for x in range(random.randint(8,10))) + str(random.randint(999,9999))
      passwd = "".join(random.choice(chars_fixed).lower() for x in range(random.randint(8,10))) + str(random.randint(999,9999))
      first_n = f"{random.choice(consonants)}{random.choice(consonants)}{random.choice(vowels)}{random.choice(consonants)}"
      last_n = f"{random.choice(consonants)}{random.choice(consonants)}{random.choice(vowels)}{random.choice(consonants)}"
      chrome_options = webdriver.ChromeOptions()
      chrome_options.add_argument("--mute-audio")
      chrome_options.add_argument("--disable-notifications")
      # chrome_options.add_argument('--headless') 
      chrome_options.add_argument('--log-level=3')
      driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
      driver.maximize_window()
      # if p<2:
      #        driver.set_window_rect(p*700,0,700,500)
      # elif p<4:
      #        driver.set_window_rect((p-2)*700,500,700,500)
      # elif p<6:
      #        driver.set_window_rect((p-2)*700,500,700,500)
      sleep(5)
      driver.get("https://signup.live.com/signup?wa=wsignin1.0&rpsnv=13&ct=1656614129&rver=7.0.6737.0&wp=MBI_SSL&wreply=https%3a%2f%2foutlook.live.com%2fowa%2f%3fnlp%3d1%26RpsCsrfState%3d9da10706-f644-734c-b65a-e2d0cf94272c&id=292841&aadredir=1&CBCXT=out&lw=1&fl=dob%2cflname%2cwld&cobrandid=90015&contextid=C6C939CC110337AB&bk=1656614129&uiflavor=web&lic=1&mkt=EN-US&lc=1033&uaid=1417b52b9f1e46f4b5a55305f1f4eb4e")
      sleep(3)
      user_hotmail = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="MemberName"]')))
      user_hotmail.send_keys(user, Keys.RETURN)
      sleep(3)
      pass_hotmail = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="PasswordInput"]')))
      pass_hotmail.send_keys(passwd, Keys.RETURN)
      sleep(3)
      first_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="FirstName"]')))
      first_name.send_keys(first_n)
      last_name = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="LastName"]')))
      last_name.send_keys(last_n, Keys.RETURN)
      sleep(3)
      month = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,f'//*[@id="BirthMonth"]/option[@value="{random.randint(3,12)}"]')))
      month.click()
      day = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,f'//*[@id="BirthDay"]/option[@value="{random.randint(1,25)}"]')))
      day.click()
      year = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="BirthYear"]')))
      year.send_keys(random.randint(1950,2004), Keys.RETURN)
      sleep(3)
      input("STOP, ku!!")


      # username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="dkusername"]')))
      # username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="dkusername"]')))
      # username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="dkusername"]')))
      # username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="dkusername"]')))
      # username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="dkusername"]')))
      # username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="dkusername"]')))
      # username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="dkusername"]')))
      # username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="dkusername"]')))
      # username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="dkusername"]')))
      # username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="dkusername"]')))
      # username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="dkusername"]')))
      # username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="dkusername"]')))
      # username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="dkusername"]')))
      # username = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="dkusername"]')))
        
if __name__ == "__main__":
      def do_stuff(q,p):
            while not q.empty():
                  value = q.get()
                  runtest(value,p)
                  q.task_done()
      for i in range(1):
            jobs.put(i)
      for i in range(4):
            worker = threading.Thread(target=do_stuff, args=(jobs,i,))
            worker.start()
      print("waiting for queue to complete", jobs.qsize(), "tasks")
      jobs.join()
      print("All done, ku!")