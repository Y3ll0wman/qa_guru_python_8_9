import allure
from selene import browser, be, by, have


def test_issue_name_selene():
    browser.open('https://github.com/')
    browser.element('.search-input').should(be.visible).click()
    browser.element('#query-builder-test').should(be.visible).type('eroshenkoam/allure-example').press_enter()
    browser.element(by.link_text('eroshenkoam/allure-example')).should(be.visible).click()
    browser.element('#issues-tab').should(be.visible).click()
    browser.element(by.link_text('Issue_created_to_test_allure_reports')).should(be.visible).click()
    browser.element('.gh-header-title').should(have.text('Issue_created_to_test_allure_reports'))
    print()
