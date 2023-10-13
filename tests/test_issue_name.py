import allure
from allure_commons.types import Severity
from selene import browser, be, by, have


def test_issue_name_selene():
    browser.open('https://github.com/')
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
        browser.open('https://github.com/')
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

