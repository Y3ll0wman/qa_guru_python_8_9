import allure
from selene import browser, be, by, have
from allure_commons.types import Severity



def test_issue_name_selene():
    browser.open('/')
    browser.element('.search-input').should(be.visible).click()
    browser.element('#query-builder-test').should(be.visible).type('eroshenkoam/allure-example').press_enter()
    browser.element(by.link_text('eroshenkoam/allure-example')).should(be.visible).click()
    browser.element('#issues-tab').should(be.visible).click()
    browser.element(by.link_text('Issue_created_to_test_allure_reports')).should(be.visible).click()
    browser.element('.gh-header-title').should(have.text('Issue_created_to_test_allure_reports'))


def test_issue_name_allure_dynamic_steps():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.NORMAL)
    allure.dynamic.label('owner', 'Y3ll0wman')
    allure.dynamic.feature('Задачи в репозитории')
    allure.dynamic.story('Название задачи отображается не зарегистрированному пользователю')
    allure.dynamic.link('https://github.com/', name='Testing')

    with allure.step("Открыть github.com"):
        browser.open('/')
    with allure.step("Нажать на поисковую строку"):
        browser.element('.search-input').should(be.visible).click()
    with allure.step("Ввести 'eroshenkoam/allure-example' и нажать Enter"):
        browser.element('#query-builder-test').should(be.visible).type('eroshenkoam/allure-example').press_enter()
    with allure.step("Нажать на ссылку содержащую текст 'eroshenkoam/allure-example'"):
        browser.element(by.link_text('eroshenkoam/allure-example')).should(be.visible).click()
    with allure.step("Кликнуть на Issues-tab"):
        browser.element('#issues-tab').should(be.visible).click()
    with allure.step("Нажать на ссылку содержащую текст 'Issue_created_to_test_allure_reports'"):
        browser.element(by.link_text('Issue_created_to_test_allure_reports')).should(be.visible).click()
    with allure.step("Проверить, что заголовок содержит текст 'Issue_created_to_test_allure_reports'"):
        browser.element('.gh-header-title').should(have.text('Issue_created_to_test_allure_reports'))


@allure.tag('web')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'Y3ll0wman')
@allure.feature('Задачи в репозитории')
@allure.story('Название задачи отображается не зарегистрированному пользователю')
@allure.link('https://github.com/', name='Testing')
def test_issue_name_allure_decorator_steps():
    open_github()
    click_on_the_search_input()
    type_search_request()
    click_on_the_title_in_search_results()
    click_on_issues_tab()
    click_on_the_title_issue()
    check_title_text()


@allure.step("Открыть github.com")
def open_github():
    browser.open('/')


@allure.step("Нажать на поисковую строку")
def click_on_the_search_input():
    browser.element('.search-input').should(be.visible).click()


@allure.step("Ввести 'eroshenkoam/allure-example' и нажать Enter")
def type_search_request():
    browser.element('#query-builder-test').should(be.visible).type('eroshenkoam/allure-example').press_enter()


@allure.step("Нажать на ссылку содержащую текст 'eroshenkoam/allure-example'")
def click_on_the_title_in_search_results():
    browser.element(by.link_text('eroshenkoam/allure-example')).should(be.visible).click()


@allure.step("Кликнуть на Issues-tab")
def click_on_issues_tab():
    browser.element('#issues-tab').should(be.visible).click()


@allure.step("Нажать на ссылку содержащую текст 'Issue_created_to_test_allure_reports'")
def click_on_the_title_issue():
    browser.element(by.link_text('Issue_created_to_test_allure_reports')).should(be.visible).click()


@allure.step("Проверить, что заголовок содержит текст 'Issue_created_to_test_allure_reports'")
def check_title_text():
    browser.element('.gh-header-title').should(have.text('Issue_created_to_test_allure_reports'))
