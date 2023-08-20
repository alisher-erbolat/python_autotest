from selenium.webdriver import Keys

from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators


class FormPage(BasePage):

    def fill_form_and_submit(self, data):
        self.remove_footer()
        data = data.split(" ")
        self.element_is_visible(Locators.FIRST_NAME).send_keys(data[0])
        self.element_is_visible(Locators.LAST_NAME).send_keys(data[1])
        self.element_is_visible(Locators.EMAIL).send_keys(data[2])
        self.element_is_visible(Locators.GENDER).click()
        self.element_is_visible(Locators.MOBILE).send_keys("2546116161")
        self.element_is_visible(Locators.SUBJECT).send_keys("Maths")
        self.element_is_visible(Locators.SUBJECT).send_keys(Keys.ENTER)
        self.element_is_visible(Locators.HOBBIES).click()
        self.element_is_visible(Locators.FILE_INPUT).send_keys(r"C:\Users\alish\PycharmProjects\pythonProject4\file.txt")
        self.element_is_visible(Locators.CURRENT_ADDRESS).send_keys("Aktobe")
        self.element_is_visible(Locators.STATE).send_keys("NCR")
        self.element_is_visible(Locators.STATE).send_keys(Keys.ENTER)
        self.element_is_visible(Locators.CITY).send_keys("Delhi")
        self.element_is_visible(Locators.CITY).send_keys(Keys.ENTER)
        self.element_is_visible(Locators.SUBMIT).click()

    def get_result(self):
        result_list = self.elements_are_visible(Locators.RESULT_TABLE)
        result_text = []
        for i in result_list:
            result_text.append(i.text)
        return result_text
