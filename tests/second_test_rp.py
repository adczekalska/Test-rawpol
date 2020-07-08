from selenium import webdriver
import time

def test_searching_in_rawpol():
    # Uruchomienie przeglądarki Chrome. Ścieżka do chromedrivera
    driver = webdriver.Chrome(executable_path=r'/Users/ada/Downloads/chromedriver')

    # Otwarcie strony RP
    driver.get('https://rp.x-coding.pl/pl/')
    driver.delete_cookie('uc_rodo_id')
    cookie = {'name': 'uc_rodo_id',
              'value': 'ex_kc2bm8fo_ffg7b6sa',
              'domain': '.rp.x-coding.pl'}
    driver.add_cookie(cookie)
    driver.refresh()
    time.sleep(2)

    # Znalezienie paska wyszukiwania i szukanie
    search_bar = driver.find_element_by_id('main-searchbox')
    search_bar.send_keys('rękawiczki')
    time.sleep(3)

    # Znalezienie guzika wyszukiwania (lupki)
    search_button = driver.find_element_by_class_name('icon-rp.icon-rp-lupa_ffffff')

    # Szukanie
    search_button.click()

    # Sprawdzenie że pierwszy wynik ma tytuł 'RNIT-REVEX'
    list_of_title_elements = driver.find_elements_by_class_name("result__title")
    list_of_titles = []
    for element in list_of_title_elements:
      list_of_titles.append(element.text)
    assert "RNIT-REVEX" in list_of_titles

    # Zamknięcie przeglądarki
    driver.quit()