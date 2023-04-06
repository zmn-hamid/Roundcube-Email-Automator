import os
import time
import logging
import traceback

import pyautogui

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

import config as CONFIG

from get_data import Data


logging.basicConfig(format='%(asctime)s [%(levelname)s] %(message)s',
                    level=logging.INFO)


class WaitUntil:
    '''
        ## Get element when it appeared/disappeared in the page
        - waits until the element exists/not exists, then returns
        - if the limit is reached, it will return `False`
    '''

    def __init__(self, driver: WebDriver) -> None:
        self.dr = driver

    def exists(self, find_by, query, sleeptime: int = 1, limit_exists: int = 3):
        if sleeptime > limit_exists:
            return False
        if element := self.dr.find_element(find_by, query):
            return element
        logging.info('waiting for upload: %ss' % sleeptime)
        time.sleep(sleeptime)
        WaitUntil.exists(find_by, query, sleeptime + 1, limit_exists)

    def not_exists(self, find_by, query, sleeptime: int = 1, limit_not_exists: int = 60):
        if sleeptime > limit_not_exists:
            return False
        if len(self.dr.find_elements(find_by, query)) == 0:
            return True
        logging.info('waiting for upload: %ss' % sleeptime)
        time.sleep(sleeptime)
        WaitUntil.not_exists(find_by, query, sleeptime + 1, limit_not_exists)


def main(driver: WebDriver):
    # login
    driver.get(CONFIG.LOGIN_URL)
    if username := wait_until.exists(By.ID, 'rcmloginuser'):
        username.send_keys(CONFIG.USERNAME)
    if password := wait_until.exists(By.ID, 'rcmloginpwd'):
        password.send_keys(CONFIG.PASSWORD)
    if submit_login := wait_until.exists(By.ID, 'rcmloginsubmit'):
        submit_login.click()
    time.sleep(1)

    # iterate in users
    data = Data()
    for user in data.get_users():
        logging.info('')
        logging.info('==============================')
        logging.info('')
        logging.info('sending to %s (%s)' % (user['name'], user['email']))
        try:
            # go to compose
            if wait_until.exists(By.XPATH, '//*[@id="messagelist-header"]/span'):
                driver.get(CONFIG.COMPOSE_URL)

            # enter data
            pyautogui.write(user['email'])  # receivers
            pyautogui.press(['tab', 'tab', 'tab'])
            pyautogui.write(data.get_email_subject())  # email subject
            pyautogui.press(['tab'])
            pyautogui.write(data.get_email_body() % user['name'])  # email body
            time.sleep(1)

            # attachments
            if attachments := data.get_attachments():
                for attachment in attachments:
                    driver.find_element(
                        By.XPATH, '//*[@id="compose-attachments"]/div/button').click()
                    time.sleep(2)
                    pyautogui.write('"%s"' % attachment)
                    pyautogui.press('enter')
                    wait_until.not_exists(
                        By.XPATH, '//li[@class="uploading"]', 1)
            time.sleep(1)

            # send
            driver.find_element(By.XPATH, '//button[@value="Send"]').click()
            logging.info('done.')
            time.sleep(3)
        except:
            traceback.print_exc()
            logging.info('failed')


if __name__ == '__main__':
    # init
    options = Options()
    options.add_argument('--log-level=3')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    wait_until = WaitUntil(driver=driver)

    main(driver=driver)

    if input('close the driver and exit? [y/n]: ').lower() == 'y':
        driver.close()
        os._exit(0)
