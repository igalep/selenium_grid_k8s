import pytest
from selenium.webdriver.common.by import By
import random

URL='https://www.saucedemo.com/'


@pytest.mark.parametrize(
    'wd_driver, username, password',
    [
        ('chrome', 'standard_user', 'secret_sauce'),
        ('chrome', 'problem_user', 'secret_sauce'),
        ('firefox', 'visual_user', 'secret_sauce'),
    ], indirect=['wd_driver'])
def test_swag_store(wd_driver, username, password):
    driver = wd_driver

    driver.get(URL)

    user_name_elem = driver.find_element(By.CSS_SELECTOR, '#user-name')
    user_name_elem.send_keys(username)
    password_elem = driver.find_element(By.CSS_SELECTOR, '#password')
    password_elem.send_keys(password)

    login_button_elem = driver.find_element(By.ID, 'login-button')
    login_button_elem.click()

    items_list = driver.find_elements(By.CSS_SELECTOR, '.inventory_item')
    list_size = len(items_list)

    dice = random.randint(1, list_size)
    for i in range(dice):
        item_elem = items_list[i]
        item_elem.find_element(By.CSS_SELECTOR, 'button[data-test^="add-to-cart"]').click()

    shopping_cart_badge = int(driver.find_element(By.CSS_SELECTOR, '.shopping_cart_badge').text)


    assert dice == shopping_cart_badge , f'for browser {driver.name}, the number of added items is different from the cart_badge'



