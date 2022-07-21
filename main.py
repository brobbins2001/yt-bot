import threading

from selenium import webdriver
from selenium.webdriver.common.by import By
from threading import Thread,Event
import random
import time
from proxy import is_bad_proxy
YOUTUBE_LINK = input("Enter link:\n")
BATCH_SIZE = int(input("Batch Size?\n"))

def do_bot_view(proxy):
    PROXY = f"<{proxy}>"
    webdriver.DesiredCapabilities.CHROME['proxy'] = {
        "httpProxy": PROXY,
        "ftpProxy": PROXY,
        "sslProxy": PROXY,
        "proxyType": "MANUAL",

    }
    rnd_time = random.randint(1, 6)
    driver = webdriver.Chrome()

    driver.get("https://www.google.com")
    driver.implicitly_wait(rnd_time)
    driver.get(YOUTUBE_LINK)

    length_ele = driver.find_element(By.XPATH, '//*[@id="movie_player"]/div[27]/div[2]/div[1]/div[1]/span[2]/span[3]')
    play_button = driver.find_element(By.XPATH, '//*[@id="movie_player"]/div[4]/button')
    auto_play_button = driver.find_element(By.XPATH, '//*[@id="movie_player"]/div[27]/div[2]/div[2]/button[1]/div/div')
    settings_button = driver.find_element(By.XPATH, '//*[@id="movie_player"]/div[27]/div[2]/div[2]/button[4]')
    quality_button = driver.find_element(By.XPATH, '//*[@id="ytp-id-17"]/div/div/div[3]')

    str_length = length_ele.get_attribute('innerHTML')
    minutes = str_length[:str_length.find(':')]
    seconds = str_length[str_length.find(':') + 1:]

    vid_time = int(minutes) * 60 + int(seconds)
    random_after_vid = random.randint(4, 20)
    total_wait = vid_time + random_after_vid

    play_button.click()
    auto_play_button.click()
    print(minutes, seconds, vid_time, total_wait)
    time.sleep(total_wait)
    driver.get("https://www.google.com")
    driver.close()

with open("http_proxies.txt", "r") as f:
    lines = f.readlines()


while len(lines) > BATCH_SIZE:
    current_list_of_proxies = lines[:BATCH_SIZE]
    count = 0
    for current_proxy in current_list_of_proxies:
        print(current_proxy)
        #if is_bad_proxy(current_proxy):
            #break
        this_thread = threading.Thread(target=do_bot_view, args=(current_proxy,))
        this_thread.start()
        if count == BATCH_SIZE-1:
            this_thread.join()
        count+=1
    lines = lines[BATCH_SIZE:]