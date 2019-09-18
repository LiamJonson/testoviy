from selenium import webdriver

import unittest


def func_reg(link):
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element_by_class_name('form-control.first').send_keys("Ivan")
    browser.find_element_by_xpath(
        '//div[@class=\'first_block\']/descendant::input[@placeholder=\'Input your last name\']').send_keys("Petrov")
    browser.find_element_by_css_selector('input[placeholder=\'Input your email\']').send_keys(
        "Smolensk@mail.com")
    browser.find_element_by_css_selector("button.btn").click()
    return browser.find_element_by_tag_name("h1").text


class TestReg(unittest.TestCase):
    def test_page1(self):
        self.assertEqual(func_reg('http://suninjuly.github.io/registration1.html'),
                         'Congratulations! You have successfully registered!', 'No Reg')

    def test_page2(self):
        self.assertEqual(func_reg('http://suninjuly.github.io/registration2.html'),
                         'Congratulations! You have successfully registered!', 'No Reg')

if __name__ == "__main__":
    unittest.main()
