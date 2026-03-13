Feature: Leads functionality

  Background:
    Given user should be on login page
    When user enters the valid credentials and click on login button

@lead
Scenario: Create_lead_with_mandatory_fields_TC04
  When user click on new lead link
  And user fill the mandatory fields and click on save button
  Then lead should be created successfully

  @lead1
Scenario: Edit_existing_lead_TC05
  When user click on Leads button and search the existing data using search fields
  And user edit the data and save the details
  Then lead data should be updated after saving the changes