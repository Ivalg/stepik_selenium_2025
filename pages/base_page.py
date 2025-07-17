import math
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


class BasePage:
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)

    def open(self):
        return self.driver.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

    def solve_quiz_and_get_code(self):
        try:  # Ожидаем появление первого алерта (с задачей)
            alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            x = alert.text.split(' ')[2]
            answer = str(math.log(abs((12 * math.sin(float(x))))))
            alert.send_keys(answer)
            alert.accept()

            try:  # Ожидаем второй алерт (с подтверждением)
                alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
                alert_text = alert.text
                print(f'Your code: {alert_text}')
                alert.accept()
                return alert_text  # Возвращаем код подтверждения
            except NoAlertPresentException:
                print('No confirmation alert presented')
                return None

        except NoAlertPresentException:
            print('No initial alert presented')
            return None
        except Exception as e:
            print(f'Error solving quiz: {str(e)}')
            return None
