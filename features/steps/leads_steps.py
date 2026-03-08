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
