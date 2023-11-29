Feature: PHPTravelsDemo Request Form

  Scenario: Successful Submission
    Given I navigate to the PHPTravelsDemo request form
    When I fill in the form with correct information
    And I provide the correct result for num1+num2
    And I submit the form
    Then I should see a success message

  Scenario: Missing Input
    Given I navigate to the PHPTravelsDemo request form
    When I leave one or more required fields empty
    And I provide the correct result for num1+num2
    And I submit the form
    Then I should see an error message indicating missing information

  Scenario: Incorrect Result for num1+num2
    Given I navigate to the PHPTravelsDemo request form
    When I fill in the form with correct information
    And I provide an incorrect result for num1+num2
    And I submit the form
    Then I should see an error message indicating an incorrect result for num1+num2
