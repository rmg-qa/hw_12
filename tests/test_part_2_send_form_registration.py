import allure
from selene import browser
from pages.page_registration_form import RegistrationFormMethods, SimpleRegistration
from data.user import user_student


@allure.title("Successful fill form registration")
def test_send_form_registration(setup_browser):
    user = user_student
    with allure.step('Открываем страницу формы'):
        open_page_registrations = RegistrationFormMethods()
        simple_registrations = SimpleRegistration()
        open_page_registrations.open_page(setup_browser)
        browser.driver.execute_script("$('#fixedban').remove()")
        browser.driver.execute_script("$('footer').remove()")
    with allure.step('Процесс регистрации нового пользователя'):
        simple_registrations.simple_registration(setup_browser, user)
    with allure.step('Проверка, что регистрация прошла успешно'):
        simple_registrations.assert_simple_registration(setup_browser)
