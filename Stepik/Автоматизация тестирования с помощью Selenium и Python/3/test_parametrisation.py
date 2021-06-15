import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()


link_id_list = ['895', '896', '897', '898', '899', '903', '904', '905']


@pytest.mark.parametrize('link_id', link_id_list)
def test_link(browser, link_id):
    link = f"https://stepik.org/lesson/236{link_id}/step/1"
    browser.get(link)
    # time.sleep(5)
    field = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.string-quiz__textarea.ember-text-area")))
    answer = math.log(int(time.time()))
    field.send_keys(str(answer))
    button = WebDriverWait(browser, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.submit-submission')))
    button.click()
    result = browser.find_element_by_css_selector('pre.smart-hints__hint')
    result_message = result.text
    assert result_message == 'Correct!', f'Test failed\n {link_id}\n {result_message}'
