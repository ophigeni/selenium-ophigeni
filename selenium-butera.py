import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import threading


def watch_link(url):
    options = Options()
    options.use_chromium = True
    options.add_argument("-inprivate"),
    options.add_argument("--disable-gpu"),
    options.add_argument("--headless"),
    options.add_argument("--no-sandbox"),
    options.add_argument("--incognito"),
    options.add_argument("--disable-dev-shm-usage")

    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options) # Modify the path here...

    print("Watching:"+"https://www.youtube.com/watch?v="+url)
    driver.get("https://youtube.com/watch?v="+url)


    time.sleep(3)
    try:
        
        driver.find_element_by_xpath('//*[@id="shorts-inner-container"]').click()
    except Exception as e:
        ActionChains(driver).send_keys("k").perform()
    time.sleep(10)




link_to_watch = ["OESq2h5kSWg"]


time_to_watch = 1
threads = []
i = 1
for link in link_to_watch:
    for ttw in range(time_to_watch):
        threads.append(threading.Thread(target=watch_link, args=(link, ) ,name=str(i)))
        i+=1

for thread in threads:
  thread.start()

for thread in threads:
  thread.join()

print("done")
