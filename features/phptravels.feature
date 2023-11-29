Feature: PHPTravelsDemo Request Form

  Scenario Outline: Successful Submission with Different Data
    Given I navigate to the PHPTravelsDemo request form
    When I fill in the form with "<first_name>", "<last_name>", "<business_name>", "<email>"
    And I provide the correct result for num1+num2
    And I submit the form
    Then I should see a success message

    Examples:
      | first_name | last_name | business_name | email                    |
      | John       | Doe       | ABC Inc.       | john.doe@example.com     |

  Scenario Outline: Missing Input with Different Scenarios
    Given I navigate to the PHPTravelsDemo request form
    When I leave "first_name" empty
    And I provide the correct result for num1+num2
    And I submit the form
    Then I should see an error message indicating missing information

    Examples:
      | first_name           |
      | last_name            |
      | business_name        |
      | email                |

  Scenario Outline: Incorrect Result for num1+num2 with Different Data
    Given I navigate to the PHPTravelsDemo request form
    When I fill in the form with "<first_name>", "<last_name>", "<business_name>", "<email>"
    AND I provide an incorrect result for num1+num2
    And I submit the form
    Then I should see an error message indicating an incorrect result for num1+num2

    Examples:
      | first_name | last_name | business_name | email                    |
      | John       | Doe       | ABC Inc.       | john.doe@example.com     |
