import time
import datetime
import logging
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Client:
    def __init__(self, remedy_url, driver_path):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)

        self.link = remedy_url
        self.driver = driver_path

    def WorkOrder(self, **kwargs):
        """
        Create a WorkOrder in Remedy.

        This requires your remedy homepage to be set to the
        Work Order Console.

        kwargs = {
            'customers': '',
            'queue_name': '',
            'summary': '',
            'notes': '['', '']',
            'service': '',
            'work_details': '',
            'operational_tier_1': '',
            'operational_tier_2': '',
            'operational_tier_3': '',

        }
        """

        self.customer = kwargs['customer']
        self.queue_name = kwargs['queue_name']
        self.work_order_number = ''
        self.summary = kwargs['summary']
        self.notes = kwargs['notes']
        self.service = kwargs['service']
        self.work_details = kwargs['work_details']
        self.operational_tier_1 = kwargs['operational_tier_1']
        self.operational_tier_2 = kwargs['operational_tier_2']
        self.operational_tier_3 = kwargs['operational_tier_3']

        try:
            startTime = datetime.datetime.now()
            browser = webdriver.Chrome(self.driver)
            browser.get(self.link)
            time.sleep(2)

            # Check for Work Order Console
            if browser.find_element_by_xpath('//*[@id="WIN_0_304248710"]/fieldset/div/dl/dd[3]/span[2]/a').text == 'Work Order Console':
                new_work_order = browser.find_element_by_class_name(
                    'arfid301868900')
                new_work_order.click()
                time.sleep(3)
                customer = browser.find_element_by_id(
                    'arid_WIN_2_303530000')
                customer.click()
                customer.clear()
                customer.click()
                customer.send_keys(self.customer)
                time.sleep(2)
                customer.send_keys(Keys.DOWN)
                customer.send_keys(Keys.ENTER)

                try:
                    time.sleep(1)
                    alert_close = browser.find_element_by_xpath(
                        "//div[@id='popup_2']//button")
                    alert_close.click()
                except:
                    logging.INFO('No Popup found')

                if self.notes != None:
                    notes = browser.find_element_by_id(
                        'arid_WIN_2_1000000151')
                    notes.send_keys(self.notes)

                summary = browser.find_element_by_id(
                    'arid_WIN_2_1000000000')
                summary.send_keys(self.summary)

                service = browser.find_element_by_id(
                    'arid_WIN_2_200000020')
                service.click()
                service.send_keys(self.service)
                time.sleep(3)
                service.send_keys(Keys.DOWN)
                service.send_keys(Keys.ENTER)

                reported_source = browser.find_element_by_id(
                    'arid_WIN_2_1000000215')
                reported_source.click()
                reported_source.send_keys(Keys.DOWN)
                reported_source.send_keys(Keys.ENTER)
                time.sleep(1)
                support_group = browser.find_element_by_id(
                    'arid_WIN_2_1000003229')
                support_group.click()
                support_group.send_keys(self.queue_name)
                time.sleep(1)
                support_group.send_keys(Keys.DOWN)
                support_group.send_keys(Keys.ENTER)

                reported_source = browser.find_element_by_id(
                    'arid_WIN_2_1000000164')
                reported_source.click()
                reported_source.send_keys(Keys.DOWN)
                reported_source.send_keys(Keys.DOWN)
                reported_source.send_keys(Keys.DOWN)
                reported_source.send_keys(Keys.ENTER)

                if self.work_details != None:
                    work_details = browser.find_element_by_id(
                        'arid_WIN_2_304247080')
                    work_details.clear()
                    work_details_list = []
                    if type(self.work_details) == str:
                        work_details_list.append(self.work_details)
                    if self.work_details == list:
                        work_details_list = self.work_details
                    for item in work_details_list:
                        work_details.send_keys(self.work_details)
                        add_button = browser.find_element_by_id(
                            'WIN_2_304250790')
                        add_button.click()
                        time.sleep(2)

                browser.find_element_by_xpath(
                    "//a[text()='Categorization']").click()

                operational_tier_1 = browser.find_element_by_id(
                    'arid_WIN_2_1000000063')
                operational_tier_1.click()
                operational_tier_1.send_keys(self.operational_tier_1)
                time.sleep(1)
                operational_tier_1.send_keys(Keys.DOWN)
                operational_tier_1.send_keys(Keys.ENTER)

                operational_tier_2 = browser.find_element_by_id(
                    'arid_WIN_2_1000000064')
                operational_tier_2.click()
                operational_tier_2.send_keys(self.operational_tier_2)
                time.sleep(1)
                operational_tier_2.send_keys(Keys.DOWN)
                operational_tier_2.send_keys(Keys.ENTER)

                operational_tier_3 = browser.find_element_by_id(
                    'arid_WIN_2_1000000065')
                operational_tier_3.click()
                operational_tier_3.send_keys(self.operational_tier_3)
                time.sleep(1)
                operational_tier_3.send_keys(Keys.DOWN)
                operational_tier_3.send_keys(Keys.ENTER)

                incident_value = browser.find_element_by_xpath(
                    "//div[@id='WIN_0_304248710']//dd[@arid='304247442']")
                wo_text = incident_value.text.split(" ")
                # incident_text[0] is the INC number
                self.work_order_number = wo_text[0]

                save = browser.find_element_by_id('WIN_2_300000300')
                save.click()

                try:
                    time.sleep(1)
                    alert_close = browser.find_element_by_xpath(
                        "//div[@id='popup_2']//button")
                    alert_close.click()
                except:
                    pass

                try:
                    time.sleep(7)
                    alert_close = browser.find_element_by_xpath(
                        "//div[@id='popup_2']//button")
                    alert_close.click()
                except:
                    logging.INFO('No Popup found')

                time.sleep(5)
            else:
                logging.INFO(
                    'Please set Remedy homepage to Work Order Console.')
        except Exception as e:
            print('ERROR... \n{}'.format(e))

        finally:
            logout = browser.find_element_by_id('WIN_0_300000044')
            logout.click()
            time.sleep(2)
            browser.get('https://google.com')
            time.sleep(5)
            browser.quit()

        return self.work_order_number
