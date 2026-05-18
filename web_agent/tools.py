###工具函数
###Agent的“手”
###老版、requests + BeautifulSoup，无法处理现代网页的JavaScript渲染，获取的内容有限。
# import requests
# from bs4 import BeautifulSoup

# def get_webpage_content(url):

#     response = requests.get(url)

#     soup = BeautifulSoup(response.text, "html.parser")

#     text = soup.get_text()

#     return text[:5000]

###新版、真正浏览器渲染
"""
    更新了什么？？
    现在不是requests在访问网页，而是真正浏览器在打开网页。
    browser = p.chromium.launch(headless=True) 这一行代码启动了一个无头浏览器实例。
    page.goto(url) 这一行代码让浏览器打开指定的URL。
    page.goto(url) 浏览器打开网页后，页面上的JavaScript会被执行，动态内容会被加载，这样我们就能获取到完整的网页内容了。
    page.content() 这一行代码获取了当前页面的HTML内容，这时候的HTML已经包含了JavaScript渲染后的内容了。
    最后我们返回了前5000个字符，避免内容过长导致处理困难
"""
from playwright.sync_api import sync_playwright

def get_webpage_content(url):

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=True)

        page = browser.new_page()

        page.goto(url)

        page.wait_for_timeout(5000)

        text = page.content()

        browser.close()

        return text[:5000]