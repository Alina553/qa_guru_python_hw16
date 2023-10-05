"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest
from selene import browser, be

@pytest.fixture()
def browser_setup():
    browser.config.base_url = 'https://github.com/'

#     browser.config.window_width = request.param[0]
#     browser.config.window_height = request.param[1]
@pytest.fixture(params=['desktop', 'mobile'])
def browser_window_size(request):
    if request.param == 'desktop':
        browser.config.window_width = 1920
        browser.config.window_height = 1080
    if request.param == 'mobile':
        browser.config.window_width = 390
        browser.config.window_height = 844



def test_github_desktop(browser_setup, browser_window_size):
    if browser.config.window_width <= 390:
        pytest.skip(reason='This test valid for desktop only')

    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-body').should(be.visible)


def test_github_mobile(browser_setup, browser_window_size):
    if browser.config.window_width > 390:
        pytest.skip(reason='This test valid for mobile only')

    browser.open('/')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-body').should(be.visible)
