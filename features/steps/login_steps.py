from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

from utils.excel_reader import ExcelReader


@given(u'user should be on login page')
def step_impl(context):
    print("Niramala")
    context.test_data=ExcelReader.get_test_data(
        "Data/Testdata.xlsx","Sheet1")
    print(context.test_data)
    context.driver = webdriver.Chrome()
    context.driver.get("http://localhost:100")

@when(u'user enters the valid credentials and click on login button')
def step_impl(context):
    context.driver.find_element(By.NAME, "user_name").send_keys(context.test_data[0]["userid"])
    context.driver.find_element(By.NAME, "user_password").send_keys(context.test_data[0]["password"])
    context.driver.find_element(By.NAME,"Login").click()

@when('user enters the invalid credentials and click on login button')
def step_impl(context):
    context.driver.find_element(By.NAME, "user_name").send_keys(context.test_data[1]["userid"])
    context.driver.find_element(By.NAME, "user_password").send_keys(context.test_data[1]["password"])
    context.driver.find_element(By.NAME,"Login").click()

@then(u'user should be navigated to home page')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Home").is_displayed()

@then('user should be navigated to login page')
def step_impl(context):
    context.driver.find_element(By.NAME, "user_name").is_displayed()

@then(u'user can see the logout link')
def step_impl(context):
    context.driver.find_element(By.LINK_TEXT, "Logout").is_displayed()
    context.driver.find_element(By.LINK_TEXT, "Logout").click()

@then('user can see the error message')
def step_impl(context):
    context.driver.find_element(By.XPATH,"//td[contains(text(),'You must specify a valid username and password.')]").is_displayed()

@when('user enters the invalid credentials as "{userid}" and password as "{password}" click on login button')
def step_impl(context,userid,password):
    context.driver.find_element(By.NAME, "user_name").clear()
    context.driver.find_element(By.NAME, "user_name").send_keys(userid)
    context.driver.find_element(By.NAME, "user_password").clear()
    context.driver.find_element(By.NAME, "user_password").send_keys(password)
    context.driver.find_element(By.NAME, "Login").click()



