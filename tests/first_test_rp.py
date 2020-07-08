from selenium import webdriver
import time


def test_my_first_chrome_selenium_test():
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

    # Inicjalizacja menu logowania
    search_menu = driver.find_element_by_class_name('dotted-menu')
    search_menu.click()
    time.sleep(3)

    # Inicjalizacja Zaloguj/Zarejestruj się
    search_login = driver.find_element_by_class_name('category-element__title')
    search_login.click()
    time.sleep(3)

    # Inicjalizacja elementu z loginem i wpisanie loginu
    #search_login_input = browser.find_element_by_id('login')
    #search_login_input.send_keys('xcoding')

    # Inicjalizacja elementu z hasłem i wpisanie hasła
    #search_password_input = browser.find_element_by_id('password')
    #search_password_input.send_keys('tester')

    # Kliknięcie button Zaloguj
    #search_button = browser.find_element_by_class_name('rw-form__button')
    #search_button.click()
    #time.sleep(5)

    # Zamknięcie przeglądarki
    driver.quit()
