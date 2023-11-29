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
      | Jane       | Sam       | ABC Inc.       | jane.sam@example.com     |
      | Omar       | Hosny     | Meero Inc.     | meero.inc@gmail.com     |
      | Willy      | Mike      | Pearson Inc.   | @example.com     |

  Scenario Outline: Missing Input with Different Scenarios
    Given I navigate to the PHPTravelsDemo request form
    When I fill in the form with "<first_name>", "<last_name>", "<business_name>", "<email>", but leave "<missing_field>" empty
    And I provide the correct result for num1+num2
    And I submit the form
    Then I should see an error message indicating missing information

    Examples:
      | missing_field | first_name | last_name | business_name | email                    |
      | first_name    | John       | Doe       | ABC Inc.       | john.doe@example.com     |
      | last_name     | Jane       | Sam       | ABC Inc.       | jane.sam@example.com     |
      | business_name | Omar       | Hosny     | Meero Inc.     | meero.inc@gmail.com     |
      | email         | Willy      | Mike      | Pearson Inc.   | @example.com     |


  Scenario Outline: Incorrect Result for num1+num2 with Different Data
    Given I navigate to the PHPTravelsDemo request form
    When I fill in the form with "<first_name>", "<last_name>", "<business_name>", "<email>"
    AND I provide an incorrect result for num1+num2
    And I submit the form
    Then I should see an error message indicating an incorrect result for num1+num2

    Examples:
      | first_name | last_name | business_name | email                    |
      | John       | Doe       | ABC Inc.       | john.doe@example.com     |
      | Jane       | Sam       | ABC Inc.       | jane.sam@example.com     |
      | Omar       | Hosny     | Meero Inc.     | meero.inc@gmail.com     |
      | Willy      | Mike      | Pearson Inc.   | @example.com     |

  Scenario Outline: Successful Login with registered email and password
    Given I navigate to the login page
    When I enter valid login "<email>", "<password>" credentials
    And I click the login button
    Then I should be redirected to the dashboard

    Examples:
    | email | password |
    | tseeker803@yahoo.com | test123 |

  Scenario Outline: Unsuccessful Login with unregistered email and password
    Given I navigate to the login page
    When I enter valid login "<email>", "<password>" credentials
    And I click the login button
    Then I should be redirected to the dashboard

    Examples:
    | email | password |
    | tseeker803123@yahoo.com | test1234 |