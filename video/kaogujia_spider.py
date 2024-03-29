import time

import cookie_util
from selenium import webdriver
from selenium.webdriver.common.by import By


# 浏览器初始化
def browser_initial(url):
    browser = webdriver.Chrome()
    browser.get(url)
    return browser


if __name__ == '__main__':
    kao_gu_jia_url = 'https://www.kaogujia.com/homeOverview'
    driver = browser_initial(kao_gu_jia_url)
    cookie_util.load_cookies(driver)
    # 登录之后，重新访问主页
    driver.get(kao_gu_jia_url)

    # 选商品
    commodity_li = driver.find_element("xpath", "/html/body/div/div[4]/div[2]/ul/li[2]")
    commodity_li.click()

    # 输入框
    search_input = driver.find_element("xpath", "/html/body/div/div[4]/div[2]/div/div/div[1]/input")
    search_input.send_keys("狗粮")  # 重新这是搜索关键字

    # 打印渲染后的页面
    html_element = driver.find_element(By.XPATH, '/html')
    print(html_element.get_attribute('outerHTML'))

    time.sleep(1000000)





