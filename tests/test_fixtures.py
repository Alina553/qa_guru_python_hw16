"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
from selene import browser, be
import pytest

@pytest.fixture(scope="function", autouse=True)
def browser_set_up():
    browser.config.base_url = 'https://github.com/'

    yield

    browser.quit()

@pytest.fixture()
def desktop_version():
    browser.config.window_width = 1920
    browser.config.window_height = 1080

@pytest.fixture()
def mobil_version():
    browser.config.window_width = 390
    browser.config.window_height = 844


def test_github_desktop(desktop_version):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-body').should(be.visible)



def test_github_mobile(mobil_version):
    browser.open('/')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-in').click()
    browser.element('.auth-form-body').should(be.visible)
