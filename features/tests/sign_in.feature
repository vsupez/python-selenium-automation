# Created by vsupe at 2/17/2023
Feature: Logged out user sees Sign in page when clicking on Returns and orders
  # Enter feature description here

#  Scenario: User sees Sign in page
#    Given Open amazon page
#    When User click on Returns and orders
#    Then Verify that user sees Sign in page


  Scenario: Verify that Sign in popup is visible for few seconds
    Given Open amazon page
    Then Verify that Sign in popup is shown
    When Wait for 8 sec
    Then Verify Sign in popup disappears