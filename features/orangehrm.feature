Feature: OrangeHRM 30-day Free Trial Login
  Scenario: Logo presence on OrangeHRM home page
      Given launch chrome browser
      When open orange hrm homepage
      Then verify that the logo present on the page
      And close the browser

  Scenario: User logs in with valid credentials
    Given launch chrome browser
    When navigate to the 30-day free trial page
    And enter valid credentials
    And click on captcha button
    And click on the trial button
    Then verify that the subscription is successful
    And close the browser
  
  