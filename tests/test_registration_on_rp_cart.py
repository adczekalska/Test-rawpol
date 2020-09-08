import pytest
from selenium import webdriver
import time
import string
import random


from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def browser():
    browser = webdriver.Chrome()
    browser.get('https://rp-prod.x-coding.pl/pl/user')
    browser.delete_cookie('uc_rodo_id')
    cookie = {'name': 'uc_rodo_id',
              'value': 'ex_kc2bm8fo_ffg7b6sa',
              'domain': '.rp-prod.x-coding.pl'}
    browser.add_cookie(cookie)
    browser.refresh()

    wait = WebDriverWait(browser, 20)
    login_button = (By.CLASS_NAME, 'rw-form__button')
    wait.until(expected_conditions.element_to_be_clickable(login_button))

    yield browser
    browser.quit()

def test_should_open_registration(browser):
    registration_tab = browser.find_element_by_css_selector('a:not(.v-tabs__item--active).v-tabs__item')
    registration_tab.click()

    wait = WebDriverWait(browser, 5)
    register_button = (By.CLASS_NAME, 'v-btn__content')
    wait.until(expected_conditions.element_to_be_clickable(register_button))

    register_button = browser.find_element_by_class_name('v-btn__content')
    register_button.click()

    wait = WebDriverWait(browser, 30)
    registration_modal = (By.ID, 'registration-modal')
    wait.until(expected_conditions.element_to_be_clickable(registration_modal))

    id_input = browser.find_element_by_css_selector("[aria-label='NIP** / ID Number *']")
    id_input.send_keys('8822115443')

    login_input = browser.find_element_by_css_selector(("[aria-label='Login *']"))
    login_input.send_keys(get_random_string(12))

    password_input = browser.find_element_by_css_selector("[aria-label='Hasło *']")
    password_input.send_keys('testowanie')

    repeat_password_input = browser.find_element_by_css_selector("[aria-label='Powtórz hasło *']")
    repeat_password_input.send_keys('testowanie')

    name_input = browser.find_element_by_css_selector("[aria-label='Imię *']")
    name_input.send_keys('Ada')

    last_name_input = browser.find_element_by_css_selector("[aria-label='Nazwisko *']")
    last_name_input.send_keys('Czekalska')

    email_input = browser.find_element_by_css_selector("[aria-label='E-mail *']")
    email_input.send_keys('a.czekalska@xcitstudio.com')

    telephone_input = browser.find_element_by_css_selector("[aria-label='Telefon kontaktowy *']")
    telephone_input.send_keys('535558353')

    next_button = browser.find_element_by_css_selector('.buttons-container .rp-btn.primary')
    next_button.click()

    wait = WebDriverWait(browser, 5)
    gus_dialog = (By.CLASS_NAME, '.gus_dialog')
    wait.until(expected_conditions.invisibility_of_element(gus_dialog))

    download_button = browser.find_element_by_class_name('.button .v-btn__content')
    download_button.click()

    use_data_button = browser.find_element_by_class_name('.button .v-btn__content')
    use_data_button.click()

    next_button = browser.find_element_by_css_selector('.buttons-container .rp-btn.primary')
    next_button.click()

    wait = WebDriverWait(browser, 5)
    address = (By.CLASS_NAME, '.address-tile__content')
    wait.until(expected_conditions.invisibility_of_element(address))

    next_button = browser.find_element_by_css_selector('.buttons-container .rp-btn.primary')
    next_button.click()

def get_random_string(length):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))







