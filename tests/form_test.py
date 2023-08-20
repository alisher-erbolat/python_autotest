from pages.form_page import FormPage


class TestFormPage:

    def test_form1(self, driver):
        form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
        form_page.open()
        first_data = "Alisher Duzmagambetov alisher@gmail.com"
        form_page.fill_form_and_submit(first_data)
        result = form_page.get_result()
        result_text = result[0] + " " + result[1]
        assert first_data == result_text

    # def test_form2(self, driver):
    #     form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
    #     form_page.open()
    #     first_data = "Johnny Depp johnny@gmail.com"
    #     form_page.fill_form_and_submit(first_data)
    #     result = form_page.get_result()
    #     result_text = result[0] + " " + result[1]
    #     assert first_data == result_text
    #
    # def test_form3(self, driver):
    #     form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
    #     form_page.open()
    #     first_data = "Leonardo DiCaprio leonardo@gmail.com"
    #     form_page.fill_form_and_submit(first_data)
    #     result = form_page.get_result()
    #     result_text = result[0] + " " + result[1]
    #     assert first_data == result_text
