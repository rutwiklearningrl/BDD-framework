import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@when(u'user click on new lead link')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT,"New Lead").click()

@when(u'user fill the mandatory fields and click on save button')
def step_impl(context):
    context.driver.find_element(By.NAME, "lastname").send_keys(context.test_data[2]["lastname"])
    context.driver.find_element(By.NAME, "company").send_keys(context.test_data[2]["company"])
    context.driver.find_element(By.NAME, "button").click()

@then(u'lead should be created successfully')
def step_impl(context):
    lname=context.driver.find_element(By.XPATH, "//td[text()='Last Name:']/following::td[1]").text
    print(lname)
    comp= context.driver.find_element(By.XPATH, "//td[text()='Company:']/following::td[1]").text
    print(comp)

@when('user click on Leads button and search the existing data using search fields')
def step_impl(context):
    time.sleep(1)
    context.driver.find_element(By.LINK_TEXT,"Leads").click()
    time.sleep(1)
    context.driver.find_elements(By.XPATH, "//input[@name='lastname']")[1].send_keys(context.test_data[2]["lastname"])
    context.driver.find_elements(By.XPATH,"//input[@name='company']")[1].send_keys(context.test_data[2]["company"])
    context.driver.find_element(By.XPATH,"//td[@align='center']/following:: input[@value='Search'][2]").click()
    time.sleep(1)

@when ('user edit the data and save the details')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//tr[@class='oddListRow'][1]/following::*[contains(text(),' Nirmala')][1]").click()
    time.sleep(1)
    context.driver.find_element(By.XPATH,"//input[@value='Edit']").click()
    time.sleep(1)
    context.driver.find_element(By.XPATH, "//input[@name='lastname']").clear()
    context.driver.find_element(By.XPATH,"//input[@name='lastname']").send_keys(context.test_data[3]["lastname"])
    context.driver.find_element(By.XPATH,"//input[@name='company']").clear()
    context.driver.find_element(By.XPATH,"//input[@name='company']").send_keys(context.test_data[3]["company"])
    time.sleep(1)
    context.driver.find_element(By.XPATH,"//input[@name='button']").click()

@then ('lead data should be updated after saving the changes')
def step_impl(context):
    lname1=context.driver.find_element(By.XPATH,"//td[text()='Last Name:']/following::td[1]").text
    print(lname1)
    comp1=context.driver.find_element(By.XPATH,"//td[text()='Company:']/following::td[1]").text
    print(comp1)



