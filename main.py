from playwright.sync_api import sync_playwright

s = sync_playwright().start()
chrome = s.chromium.launch(headless=False)
context = chrome.new_context()
page = context.new_page()
page.goto('https://www.popsilla.com/fortnite')
headers = {
    'Host': 'en.softonic.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}
