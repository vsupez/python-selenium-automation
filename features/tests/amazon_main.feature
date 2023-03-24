# Created by vsupe at 3/11/2023
Feature: Amazon main page tests
  # Enter feature description here

  Scenario: User can see hamburger menu
    Given Open amazon page
    Then Verify hamburger menu icon is present


  Scenario: User can see language options
    Given Open amazon page
    When Hover over language options
    Then Verify spanish option is present

   #HW8
  Scenario: User can see the details when hover over New Arrivals
    Given Open New Arrivals page
    When Hover over New Arrivals
    Then Verify that user sees deals