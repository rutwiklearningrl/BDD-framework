Feature: Leads functionality

  Background:
    Given user should be on login page
    When user enters the valid credentials and click on login button

@lead
Scenario: Create_lead_with_mandatory_fields_TC04
  When user click on new lead link
  And user fill the mandatory fields and click on save button
  Then lead should be created successfully
