import threading

from selenium import webdriver
from selenium.webdriver.common.by import By

def is_bad_proxy(pip):
    try:
        PROXY = f"<{pip}>"
        webdriver.DesiredCapabilities.CHROME['proxy'] = {
            "httpProxy": PROXY,
            "ftpProxy": PROXY,
            "sslProxy": PROXY,
            "proxyType": "MANUAL",

        }
        driver = webdriver.Chrome()
        driver.get("https://www.google.com")
        driver.get("https://www.youtube.com")
        driver.quit()
        return True
    except:
        return False
    return False
