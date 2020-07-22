import pytest
from selenium import webdriver
import time

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

def test_searching_in_rawpol(browser):

    # Znalezienie paska wyszukiwania i szukanie
    search_bar = browser.find_element_by_id('main-searchbox')
    search_bar.send_keys('rękawiczki')

    # Znalezienie guzika wyszukiwania (lupki)
    search_button = browser.find_element_by_class_name('icon-rp.icon-rp-lupa_ffffff')

    # Szukanie
    search_button.click()
    time.sleep(5)

    #wait = WebDriverWait(browser, 30)
    #search_result = (By.CSS_SELECTOR, '.list-tile__title.nowrap')
    #wait.until(expected_conditions.visibility_of_element_located(search_result))

    # Sprawdzenie że jeden z wyników ma tytuł 'RNIT-REVEX'
    list_of_title_elements = browser.find_elements_by_css_selector('.list-tile__title.nowrap')
    list_of_titles = []
    for element in list_of_title_elements:
      list_of_titles.append(element.text)
    assert "RNIT-REVEX" in list_of_titles