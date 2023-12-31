from selenium.webdriver.common.by import By
from random import randint


class FormPageLocators:
    FIRST_NAME = (By.ID, "firstName")
    LAST_NAME = (By.ID, "lastName")
    EMAIL = (By.ID, "userEmail")
    GENDER = (By.XPATH, f"//label[@for = 'gender-radio-{randint(1, 3)}']")
    MOBILE = (By.ID, "userNumber")
    SUBJECT = (By.ID, "subjectsInput")
    HOBBIES = (By.XPATH, f"//label[@for = 'hobbies-checkbox-{randint(1, 3)}']")
    FILE_INPUT = (By.ID, "uploadPicture")
    CURRENT_ADDRESS = (By.ID, "currentAddress")
    STATE = (By.ID, "react-select-3-input")
    CITY = (By.ID, "react-select-4-input")
    SUBMIT = (By.ID, "submit")
    RESULT_TABLE = (By.XPATH, "//div[@class= 'table-responsive']//td[2]")

