from selenium import webdriver
import time
import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def browser():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    # ustawiana automatycznie przez bibliotekę webdriver-manager
    browser = webdriver.Chrome()

    # Otwarcie strony
    browser.get('https://rp.x-coding.pl/pl/')
    browser.delete_cookie('uc_rodo_id')
    cookie = {'name': 'uc_rodo_id',
              'value': 'ex_kc2bm8fo_ffg7b6sa',
              'domain': '.rp.x-coding.pl'}
    browser.add_cookie(cookie)
    browser.refresh()

    # Zwróć przeglądarkę z setupu do testów
    yield browser

    # Zamknięcie przeglądarki
    browser.quit()

def test_home_page_link_to_login(browser):
     # Inicjalizacja menu logowania
    search_menu = browser.find_element_by_class_name('dotted-menu')
    search_menu.click()
    time.sleep(3)

    # Inicjalizacja Zaloguj/Zarejestruj się
    link_list = browser.find_elements_by_css_selector('.user-menu .category-element__title')
    link_list[2].click()

    wait = WebDriverWait(browser, 10)
    login_screen = (By.CLASS_NAME, 'login')
    wait.until(expected_conditions.visibility_of_element_located(login_screen))