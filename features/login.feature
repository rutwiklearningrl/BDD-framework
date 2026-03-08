Feature: login functionality

  Background:
    Given user should be on login page

    @sanity @smoke @xyz1
Scenario: valid_login_TC01
When user enters the valid credentials and click on login button
Then user should be navigated to home page
And user can see the logout link

  @sanity @smoke @xyz2
Scenario: Invalid_login_TC02
When user enters the invalid credentials and click on login button
Then user should be navigated to login page
And user can see the error message

  @abc @sanity @smoke
Scenario Outline: Invalid_login_with_multiple_dataset
When user enters the invalid credentials as "<userid>" and password as "<password>" click on login button
Then user should be navigated to login page
And user can see the error message
  Examples:
    |userid  | password|
    |ad1     |pwd1     |
    |ad2     |pwd2     |
    |ad3     |pwd3     |

