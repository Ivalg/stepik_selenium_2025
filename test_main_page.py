from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"


def go_to_login_page(driver):
    login_link = driver.find_element(By.CSS_SELECTOR, "#login_link")
    login_link.click()


def test_guest_can_go_to_login_page(driver):
    driver.get(link)
    go_to_login_page(driver)

# def test_guest_can_go_to_login_page(driver):
#     link = "http://selenium1py.pythonanywhere.com/"
#     driver.get(link)
#     login_link = driver.find_element(By.CSS_SELECTOR, "#login_link")
#     login_link.click()
