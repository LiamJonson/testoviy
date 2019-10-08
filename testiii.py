import pytest
from selenium import webdriver
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('link',['https://stepik.org/lesson/236895/step/1',
        'https://stepik.org/lesson/236896/step/1','https://stepik.org/lesson/236897/step/1','https://stepik.org/lesson/236898/step/1','https://stepik.org/lesson/236899/step/1',
         'https://stepik.org/lesson/236903/step/1','https://stepik.org/lesson/236904/step/1','https://stepik.org/lesson/236905/step/1'])
def test_guest(browser, link):
    browser.get(link)
    time.sleep(3)
    browser.find_element_by_tag_name('textarea').send_keys(str(math.log(int(time.time()))))
    browser.find_element_by_tag_name("button").click()
    time.sleep(3)
    assert 'Correct!' == browser.find_element_by_class_name('smart-hints__hint').text





