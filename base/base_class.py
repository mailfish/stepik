import datetime

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import ScreenshotException

class Base:
    def __init__(self,driver):
        self.driver: WebDriver = driver

    # Getter
    def element_find(self,locator):
        # try:
           return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, locator)))
        # except Exception:
        #     print(Exception)

    # Action
    def element_click(self, element):
            self.element_find(element).click()

    def element_is_displayed(self, element):
        return self.element_find(element).is_displayed()

    def element_text(self, element):
        return self.element_find(element).text

    def element_send_keys(self, element, text):
        return self.element_find(element).send_keys(text)

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    # Метод для перехода к элементу
    def move_to_element(self,locator): # Поиск элемента на страницы для навигации на него
        actions = ActionChains(self.driver)  #
        actions.move_to_element(self.element_find(locator)).perform()  # наведение на требуемые объект страницы, по локатору

    # """Method assert word"""
    @staticmethod
    def assert_word(word, result):
        try:
            value_word = word.text
            assert value_word == result
            print(f"Текст word {value_word} совпадает c result {result}")
        except:
            print(f"Ошибка cравнения текста для {word}")

    # """Method assert URL"""

    def assert_url(self, result):
        try:
            get_url = self.driver.current_url
            assert get_url == result
            print(f"\n{result} - good value URL")
        except:
            print(f"Ошибка сравнения URL для {result}")

    # """Method Screenshot"""

    def get_screenshot(self, page_name):
        """Создание скриншота"""
        try:
            now_date = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
            name_screenshot = page_name + "_screenshot " + now_date + ".png"
            self.driver.save_screenshot(f"../screen/{name_screenshot}")
            print(f"Сделан скриншот страницы {page_name}")
        except:
            print(f"Ошибка создания скриншота {page_name}")
