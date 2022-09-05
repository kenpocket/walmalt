from playwright.sync_api import Playwright, sync_playwright, expect
import re
from urllib.parse import quote
import json


def run(playwright: Playwright, keywords: str) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://play.google.com/store/apps/
    page.goto("https://play.google.com/store/apps/")

    # Click [aria-label="搜索"]
    # page.locator("[aria-label=\"搜索\"]").click()
    page.locator("[aria-label=\"Search\"]").click()

    # Fill [placeholder="搜索应用和游戏"]
    # page.locator("[placeholder=\"搜索应用和游戏\"]").fill("Remind: School Communication")
    page.locator("[placeholder=\"Search for apps & games\"]").fill(keywords)

    # Press Enter
    page.locator("[placeholder=\"Search for apps & games\"]").press("Enter")
    page.wait_for_url("https://play.google.com/store/search?q={}&c=apps".format(quote(keywords)))
    if page.locator('''//a[@class="Qfxief"]''').count() != 1:
        wait_url = 'https://play.google.com/store/apps/details?id=' + \
                   page.locator('''//a[@class="Si6A0c Gy4nib"]''').first.get_attribute('href').split('?id=')[-1]
    else:
        wait_url = 'https://play.google.com/store/apps/details?id=' + \
                   page.locator('''//a[@class="Qfxief"]''').get_attribute('href').split('?id=')[-1]
        # Click .Qfxief
    # print(wait_url)
    page.goto(wait_url)
    try:
        page.wait_for_url(wait_url)
    except:
        return

    # Click [aria-label="查看“关于此应用”的更多相关信息"]
    # page.locator("[aria-label=\"查看“关于此应用”的更多相关信息\"]").click()
    page.locator("[aria-label=\"See more information on About this app\"]").click()
    # page.wait_for_url("https://play.google.com/store/apps/details?id=com.remind101")
    try:
        abouts = page.locator('''//div/html-blob''').nth(0).inner_text()
    except:
        abouts = 'null'
    # Close page
    try:
        stars = page.locator('''//div[@itemprop="starRating"]/div[@aria-label]''').nth(0).inner_text()
        star = re.findall(r'\d+\.\d+', stars)[0]
    except:
        star = 'null'
    logo = page.locator('''//div/c-wiz/div/img''').nth(0).get_attribute('src')
    print('<-***')
    print(logo)
    print(star)
    print(abouts)
    print('***->')
    page.close()

    # ---------------------
    context.close()
    browser.close()


file = open('result.json', 'r', encoding='utf-8')
data = file.readlines()
with sync_playwright() as playwright:

    for d in data:
        d = json.loads(d.strip())
        print(d[name])
        run(playwright, keywords=d['name'])
