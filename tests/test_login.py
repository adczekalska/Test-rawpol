import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.get('https://rp.x-coding.pl/pl/user')
    browser.delete_cookie('uc_rodo_id')
    cookie = {'name': 'uc_rodo_id',
              'value': 'ex_kc2bm8fo_ffg7b6sa',
              'domain': '.rp.x-coding.pl'}
    browser.add_cookie(cookie)
    browser.refresh()

    wait = WebDriverWait(browser, 10)
    login_button = (By.CLASS_NAME, 'rw-form__button')
    wait.until(expected_conditions.element_to_be_clickable(login_button))

    yield browser
    browser.quit()

def test_login(browser):
    # Inicjalizacja elementu z loginem i wpisanie loginu
    login_input = browser.find_element_by_id('login')
    login_input.send_keys('xcoding')

    # Inicjalizacja elementu z hasłem i wpisanie hasła
    password_input = browser.find_element_by_id('password')
    password_input.send_keys('tester')

    # Kliknięcie button Zaloguj
    login_button = browser.find_element_by_class_name('rw-form__button')
    login_button.click()
    time.sleep(15)

    wait = WebDriverWait(browser, 30)
    cart = (By.CLASS_NAME, 'icon-rp-koszyk')
    wait.until(expected_conditions.visibility_of_element_located(cart))