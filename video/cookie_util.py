from selenium import webdriver
import time
import json


def get_cookies(url):
    driver = webdriver.Chrome()
    driver.get(url)
    # 网页打开后20秒内，手动登录账户
    time.sleep(30)
    # 将cookie写入文件，保存为json格式
    with open('cookies.txt', 'w') as f:
        f.write(json.dumps(driver.get_cookies()))
    driver.close()


def load_cookies(driver):
    driver.delete_all_cookies()
    with open('cookies.txt', 'r') as f:
        cookie_list = json.load(f)
        for cookie in cookie_list:
            driver.add_cookie(cookie)


if __name__ == '__main__':
    get_cookies('https://www.kaogujia.com/homeOverview')
