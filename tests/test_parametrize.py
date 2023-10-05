"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser, be


@pytest.fixture()
def browser_setup(request):
    browser.config.base_url = 'https://github.com/'
    if request.param == 'desktop':
        browser.config.window_width = 1920
        browser.config.window_height = 1080
    elif request.param == 'mobile':
        browser.config.window_width = 390
        browser.config.window_height = 844
    else:
        raise 'Invalid browsers parameters'

    yield

    browser.quit()

@pytest.mark.parametrize('browser_setup', ['desktop'], indirect=True)
def test_github_desktop(browser_setup):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-body').should(be.visible)

@pytest.mark.parametrize('browser_setup', ['mobile'], indirect=True)
def test_github_mobile(browser_setup):
    browser.open('/')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-body').should(be.visible)
