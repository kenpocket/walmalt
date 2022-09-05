from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class fingVerifChrome():
    prefs = {
        'profile.default_content_settings': {
            'profile.default_content_setting_values': {
                'images': 2,
                'javascript': 2
            }}}

    def __init__(self):
        self.options = Options()
        self.options.add_experimental_option("prefs", self.prefs)
        self.options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.options.add_argument("service_args = ['–ignore - ssl - errors = true', '–ssl - protocol = TLSv1']")
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('disable-infobars')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument("--disable-blink-features=AutomationControlled")
        # self.options.add_argument('--headless')
        self.options.add_argument("start-maximized")
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        self.options.add_argument("--disable-blink-features=AutomationControlled")

    def modifyEnviroment(self, proxyIP=None):
        if proxyIP:
            self.options.add_argument(f'--proxy-server={proxyIP}')
        browser = webdriver.Chrome(options=self.options)
        browser.set_page_load_timeout(60)
        browser.set_script_timeout(45)
        if browser.execute_script("return navigator.webdriver"):
            browser.execute_cdp_cmd(
                "Page.addScriptToEvaluateOnNewDocument",
                {"source": """
                               Object.defineProperty(window, 'navigator', {
                                   value: new Proxy(navigator, {
                                   has: (target, key) => (key === 'webdriver' ? false : key in target),
                                   get: (target, key) =>
                                       key === 'webdriver'
                                       ? undefined
                                       : typeof target[key] === 'function'
                                       ? target[key].bind(target)
                                       : target[key]
                                   })
                               });
                            """
                 },
            )
        original_user_agent_string = browser.execute_script("return navigator.userAgent")
        browser.execute_cdp_cmd("Network.setUserAgentOverride",
                                {"userAgent": original_user_agent_string.replace("Headless", ""), }, )
        emulate_touch = False
        if emulate_touch:
            browser.execute_cdp_cmd(
                "Page.addScriptToEvaluateOnNewDocument",
                {
                    "source": """
                        Object.defineProperty(navigator, 'webdriver', {get: () => 1})
                       """
                },
            )
        browser.set_window_size(1080, 800)
        return browser
