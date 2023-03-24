# Created by vsupe at 3/10/2023
Feature: Amazon search tests


  Scenario Outline: User can search for a product on amazon
    Given Open amazon page
    When Input text <search_word>
    When Click on search button
    Then Verify that text <search_result> is shown
    Examples:
    | search_word | search_result |
    | coffee      | "coffee"      |
    | table       | "table"       |
    | mug         | "mug"         |


  Scenario: User can search for dress on amazon
    Given Open amazon page
    When Input text dress
    When Click on search button
    Then Verify that text "dress" is shown


  Scenario: User can add a product to the cart
    Given Open amazon page
    When Input text Tritan Farm to Table Pitcher
    And Click on search button
    And Click on the first product
    And Click on Add to cart button
    And Open cart page
    Then Verify cart has 1 item(s)


  Scenario: User can select and search in a department
    Given Open amazon page
    When Select department by alias audible
    And Input text Faust
    And Click on search button
    Then Verify audible department is selected


  #HW8
  Scenario: User can select and search in a department
    Given Open amazon page
    When Select department by alias appliances
    And Input text toaster
    And Click on search button
    Then Verify appliances department is selected



