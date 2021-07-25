# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, logging
import configparser

class Newconfigparser(configparser.ConfigParser):

    def __init__(self,defaults=None):

        configparser.ConfigParser.__init__(self,defaults=None)

    def optionxform(self, optionstr):

        return optionstr


class BarcoWarrantyInfoTestCase(unittest.TestCase):
    def setUp(self):
        self.config = Newconfigparser()
        self.config.read('config.ini')
        if self.config['ENVSetting']['Browser'] == "CHROME":
            self.driver = webdriver.Chrome()
        elif self.config['ENVSetting']['Browser'] == "FIREFOX":
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()
        self.driver.set_window_size(int(self.config['ENVSetting']['Browser_width']), int(self.config['ENVSetting']['Browser_height']))
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

    def test_Type_Correct_Serial_Number_to_enter_Correct_Page(self):
        driver = self.driver
        driver.get(self.config['ENVSetting']['URL'])
        driver.find_element_by_id(self.config['ElementPath']['Serial number']).click()
        driver.find_element_by_id(self.config['ElementPath']['Serial number']).clear()
        driver.find_element_by_name(self.config['ElementPath']['Serial number']).send_keys(self.config['ValueSetting']['CorrectSerialNumber'])
        driver.find_element_by_xpath(self.config['ElementPath']['Get info']).click()
        response = driver.find_elements_by_class_name(self.config['ElementPath']['Warranty results'])
        for value in response:
            response_temp =  (value.text)
        result_temp = response_temp.splitlines()
        result= dict(zip(result_temp[::2], result_temp[1::2]))
        self.assertEqual(self.config._sections['SerialNumberGetInfo'], result, "The Get Info's Infomation Not Correct")

    def test_Special_Character(self):
        driver = self.driver
        driver.get(self.config['ENVSetting']['URL'])
        driver.find_element_by_id("SerialNumber").click()
        driver.find_element_by_id("SerialNumber").clear()
        driver.find_element_by_name(self.config['ElementPath']['Serial number']).send_keys(self.config['ValueSetting']['SpecialSerialNumber'])
        driver.find_element_by_xpath(self.config['ElementPath']['Get info']).click()
        response = driver.find_elements_by_class_name(self.config['ElementPath']['Vaildation'])
        result_tmp = []
        for value in response:
            result_tmp.append(value.text)
        result = [tmp for tmp in result_tmp if tmp != '']
        self.assertEqual(self.config['ResultMessage']['SpecialCharacterResult'], result[0], "The Special Character Display Wrong Message")

    def test_Minimum_Six_Characters_Required(self):
        driver = self.driver
        driver.get(self.config['ENVSetting']['URL'])
        driver.find_element_by_id("SerialNumber").click()
        driver.find_element_by_id("SerialNumber").clear()
        driver.find_element_by_name(self.config['ElementPath']['Serial number']).send_keys(self.config['ValueSetting']['ShortThanSixSerialNumber'])
        driver.find_element_by_xpath(self.config['ElementPath']['Get info']).click()
        response = driver.find_elements_by_class_name(self.config['ElementPath']['Vaildation'])
        result_tmp = []
        for value in response:
            result_tmp.append(value.text)
        result = [tmp for tmp in result_tmp if tmp != '']
        self.assertEqual(self.config['ResultMessage']['ShortThanSixSerialNumberResult'], result[0], "The Mininum Six Character Display Wrong Message")

    def test_Type_Wrong_Will_Display_Error_Message(self):
        driver = self.driver
        driver.get(self.config['ENVSetting']['URL'])
        driver.find_element_by_id("SerialNumber").click()
        driver.find_element_by_id("SerialNumber").clear()
        driver.find_element_by_name(self.config['ElementPath']['Serial number']).send_keys(self.config['ValueSetting']['WrongSerialNumber'])
        driver.find_element_by_xpath(self.config['ElementPath']['Get info']).click()
        time.sleep(10)
        response = driver.find_element_by_xpath(self.config['ElementPath']['WrongMessage'])
        self.assertEqual(self.config['ResultMessage']['WrongSerialNumberResult'], response.text, "Type Wrong Serial Number Not Display Error Message")

    def test_Type_Any_Wrong_Serial_Number_Can_Not_Get_Correct_Info(self):
        SNList_tmp = self.config['WrongErrorSerialNumbersList']['WrongSerialNumberList']
        SNList = SNList_tmp.split(',')
        for index in range(len(SNList)):
            driver = self.driver
            driver.get(self.config['ENVSetting']['URL'])
            driver.find_element_by_id("SerialNumber").click()
            driver.find_element_by_id("SerialNumber").clear()
            driver.find_element_by_name(self.config['ElementPath']['Serial number']).send_keys(SNList[index])
            driver.find_element_by_xpath(self.config['ElementPath']['Get info']).click()
            time.sleep(10)
            response = driver.find_element_by_xpath(self.config['ElementPath']['WrongMessage'])
            self.assertEqual(self.config['ResultMessage']['WrongSerialNumberResult'], response.text, "Type Wrong Serial Number Not Display Error Message")

    def test_How_Many_Response_Times_About_Get_Info(self):
        driver = self.driver
        driver.get(self.config['ENVSetting']['URL'])
        driver.find_element_by_id(self.config['ElementPath']['Serial number']).click()
        driver.find_element_by_id(self.config['ElementPath']['Serial number']).clear()
        driver.find_element_by_name(self.config['ElementPath']['Serial number']).send_keys(self.config['ValueSetting']['CorrectSerialNumber'])
        driver.find_element_by_xpath(self.config['ElementPath']['Get info']).click()
        navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
        times = 0
        while True:
            response = driver.find_elements_by_class_name(self.config['ElementPath']['Warranty results'])
            for value in response:
                response_temp =  (value.text)
            result_temp = response_temp.splitlines()
            result= dict(zip(result_temp[::2], result_temp[1::2]))
            if self.config._sections['SerialNumberGetInfo'] == result:
                responseStart = driver.execute_script("return window.performance.timing.responseStart")
                break
            else:
                times += 1
                if times > 10:
                    break
                    assert False, "Can not Get Respone, please contact QA to Recheck Type Correct Serial Number Issue"
        response_time = responseStart - navigationStart
        print (response_time)

        driver = self.driver
        driver.get(self.config['ENVSetting']['URL'])
        driver.find_element_by_id("SerialNumber").click()
        driver.find_element_by_id("SerialNumber").clear()
        driver.find_element_by_name(self.config['ElementPath']['Serial number']).send_keys(self.config['ValueSetting']['WrongSerialNumber'])
        driver.find_element_by_xpath(self.config['ElementPath']['Get info']).click()
        navigationStart = driver.execute_script("return window.performance.timing.navigationStart")
        times = 0
        while True:
            response = driver.find_element_by_xpath(self.config['ElementPath']['WrongMessage'])
            if self.config['ResultMessage']['WrongSerialNumberResult'] == response.text:
                responseStart = driver.execute_script("return window.performance.timing.responseStart")
                break
            else:
                times += 1
                if times > 10:
                    break
                    assert False, "Can not Get Respone, please contact QA to Recheck Type Wrong Serial Number Issue"
        response_time = responseStart - navigationStart
        print (response_time)

    def test_Click_Read_Our_Warranty_Policy_Turn_to_Correct_Page_or_Not(self):
        driver = self.driver
        driver.get(self.config['ENVSetting']['URL'])
        driver.find_element_by_link_text(self.config['ElementPath']['Policy']).click()
        windows=driver.window_handles
        driver.switch_to.window(windows[-1])
        self.assertEqual(self.config['ResultMessage']['PolicyPageTitleResult'], driver.title, "Click Read Our Warranty Policy Did Not Turn to Policy Page")
if __name__ == "__main__":
    import xmlrunner
    runner = xmlrunner.XMLTestRunner(output='Barco')
    unittest.main(testRunner=runner)
    unittest.main()
