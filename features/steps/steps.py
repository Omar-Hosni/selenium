from selenium import webdriver
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time
from capmonster_python import RecaptchaV2Task

API_KEY = "e2b2224dca7c549d21eeb3cf8c431197"
capmonster = RecaptchaV2Task(API_KEY)


'''
Demo Request
'''
@given(u'I navigate to the PHPTravelsDemo request form')
def launchBrowser(context):
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(options=options)

@when(u'I fill in the form with "{first_name}", "{last_name}", "{business_name}", "{email}"')
def fillForm(context, first_name, last_name, business_name, email):
    context.driver.get('https://phptravels.com/demo/')

    context.driver.find_element(By.NAME,'first_name').send_keys(first_name)
    context.driver.find_element(By.NAME,'last_name').send_keys(last_name)
    context.driver.find_element(By.NAME,'business_name').send_keys(business_name)
    context.driver.find_element(By.NAME,'email').send_keys(email)

@when(u'I fill in the form with "{first_name}", "{last_name}", "{business_name}", "{email}", but leave "{missing_field}" empty')
def partialFillForm(context, missing_field, first_name, last_name, business_name, email):
    context.driver.get('https://phptravels.com/demo/')

    if missing_field == 'first_name':
        first_name=""
    if missing_field == 'last_name':
        last_name=""
    if missing_field == 'business_name':
        business_name=""
    if missing_field == 'email':
        email=""
    
    
    context.driver.find_element(By.NAME,'first_name').send_keys(first_name)
    context.driver.find_element(By.NAME,'last_name').send_keys(last_name)
    context.driver.find_element(By.NAME,'business_name').send_keys(business_name)
    context.driver.find_element(By.NAME,'email').send_keys(email)


@when(u'I provide the correct result for num1+num2')
def inputResultSum(context):
    num1 = context.driver.find_element(By.ID,'numb1').text
    print(num1)

    num2 = context.driver.find_element(By.ID,'numb2').text
    print(num2)

    res = int(num1) + int(num2)
    context.driver.find_element(By.ID,'number').send_keys(f'{res}')

@when(u'I provide an incorrect result for num1+num2')
def inputResultSumWrong(context):
    num1 = context.driver.find_element(By.ID,'numb1').text
    print(num1)

    num2 = context.driver.find_element(By.ID,'numb2').text
    print(num2)

    res = int(num1) + int(num2)
    context.driver.find_element(By.ID,'number').send_keys(f'{res+1}')


@when(u'I submit the form')
def submit(context):
    context.driver.find_element(By.ID, 'demo').click()
    time.sleep(2)

@then('I should see a success message')
def printSuccess(context):
    context.driver.find_element(By.ID, 'colored') 
    context.driver.close()

@then(u'I should see an error message indicating missing information')
def printMissingInput(context):
    try:
        # Switch to the alert
        alert = Alert(context.driver)

        # Get the text from the prompt
        prompt_text = alert.text
        print(f"Prompt Text: {prompt_text}")

        # Accept the prompt (click OK)
        alert.accept()
    except UnexpectedAlertPresentException:
        print("Unexpected alert present. Handling it.")
        alert = context.driver.switch_to.alert
        alert.accept()

@then(u'I should see an error message indicating an incorrect result for num1+num2')
def errorMessageResultSum(context):
    try:
        # Switch to the alert
        alert = Alert(context.driver)

        # Get the text from the prompt
        prompt_text = alert.text
        print(f"Prompt Text: {prompt_text}")

        # Accept the prompt (click OK)
        alert.accept()
    except UnexpectedAlertPresentException:
        print("Unexpected alert present. Handling it.")
        alert = context.driver.switch_to.alert
        alert.accept()



'''
Sign up
'''
@given(u'I navigate to registration page')
def launchRegistration(context):
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(options=options)

@when('I fill the registration form')
def fillRegistrationForm(context):
    context.driver.get('https://phptravels.org/register.php')

    context.driver.find_element(By.ID, 'inputFirstName').send_keys('omar')
    context.driver.find_element(By.ID, 'inputLastName').send_keys('hosny')
    context.driver.find_element(By.ID, 'inputEmail').send_keys('omar@gmail.com')
    context.driver.find_element(By.ID, 'inputAddress1').send_keys('Bethlen utca, 45, 2, 7')
    context.driver.find_element(By.ID, 'inputCity').send_keys('Debrecen')
    context.driver.find_element(By.ID, 'inputPostcode').send_keys('4026')
    
    context.driver.find_element(By.ID, 'inputNewPassword1').send_keys('test123')
    context.driver.find_element(By.ID, 'inputNewPassword2').send_keys('test123')
    time.sleep(15)

@when(u'I click on captcha')
def registrationCaptcha(context):
    '''
    website = "https://phptravels.org/register.php"
    captcha_class ="rc-anchor-container"
    captcha_key="6LdJtY8UAAAAADTgIWYnG_VKkfNqqB-w8CdQFL7Y"

    task_id = capmonster .create_task(website, captcha_key)
    result = capmonster.join_task_result(task_id).get("gRecaptchaResponse")
    context.driver.execute_script("document.getElementsByClassName(`g-recaptcha-response`)[0].innerHTML = " f"'{result}';")
    context.driver.find_element(By.ID, "recaptcha-demo-submit").click()
    '''

    time.sleep(2)

@when(u'I submit the registration form')
def submitRegistration(context):
    context.driver.find_element(By.XPATH,'/html/body/section/div/div[1]/div[2]/div/form/p/input').click()

@then(u'I should get error message')
def getErrorRegistration(context):
    text = context.driver.find_element(By.CLASS_NAME,'alert alert-danger').text
    print(text)

'''
LOGIN
'''
@given(u'I navigate to the login page')
def launchLogin(context):
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(options=options)


@when(u'I enter valid login "{email}", "{password}" credentials')
def loginForm(context, email, password):
    context.driver.get('https://phptravels.org/login')

    context.driver.find_element(By.ID,'inputEmail').send_keys(email)
    context.driver.find_element(By.ID,'inputPassword').send_keys(password)

    captcha_element = context.driver.find_element(By.ID, 'recaptcha-anchor')
    captcha_element.click()
    time.sleep(2)

@when(u'I click the login button')
def loginBtn(context):
    context.driver.find_element(By.ID,'login').click()

@then(u'I should be redirected to the dashboard')
def checkNavigation(context):
    dashboard_link = 'https://phptravels.org/clientarea.php'
    current_url = context.driver.current_url

    if dashboard_link in current_url:
        print(f"The dashboard link '{dashboard_link}' is currently open.")
    else:
        print(f"The dashboard link is not currently open. Current URL: {current_url}")


'''
@given(u'launch chrome browser')
def launchBrowser(context):
    options = webdriver.ChromeOptions()
    context.driver = webdriver.Chrome(options=options)

    
@when(u'open orange hrm homepage')
def getPage(context):
    context.driver.get('https://phptravels.com/demo/')

@then(u'verify that the logo present on the page')
def verifyLogo(context):
    #status =context.driver.find_element_by_xpath("//div[@id=divLogo']//img").is_displayed()
    image_alt_text = 'phptravels'
    xpath_expression = f"//img[@alt='{image_alt_text}']"
    context.driver.find_elements(By.XPATH, xpath_expression)

@then(u'navigate to trial')
def closeBrowser(context):
    context.driver.get('https://www.orangehrm.com/en/30-day-free-trial')
    time.sleep(2)

@when(u'navigate to the 30-day free trial page')
def navigate_to_free_trial(context):
    context.driver.get('https://www.orangehrm.com/en/30-day-free-trial')

@when(u'enter valid credentials')
def enter_valid_credentials(context):
    free_trial_section = WebDriverWait(context.driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, 'free-trial-section'))
    )
    
    username_input = free_trial_section.find_element(By.ID, 'Form_submitForm_subdomain')[0]
    fullname_input = free_trial_section.find_element(By.ID, 'Form_getForm_Name')[0]
    email_input = free_trial_section.find_element(By.ID, 'Form_getForm_Email')[0]
    phonenumber_input = free_trial_section.find_element(By.ID, 'Form_getForm_Contact')[0]
    password_input = free_trial_section.find_element(By.ID, 'Form_submitForm_password')[0]

    username_input.send_keys('jncholas')
    fullname_input.send_keys('John Nicholas')
    email_input.send_keys('test@gmail.com')
    phonenumber_input.send_keys('123123122')
    password_input.send_keys('valid_password')


@when(u'click on captcha button')
def click_captcha_button(context):
    captcha_checkbox = context.driver.find_elements(By.CLASS_NAME, 'rc-anchor-center-item.rc-anchor-checkbox-label')
    context.driver.execute_script("arguments[0].click();", captcha_checkbox)

@when(u'click on the trial button')
def click_trial_button(context):
    trial_button = context.driver.find_elements(By.NAME, 'yt0')
    trial_button.click()

@then(u'verify that the subscription is successful')
def verify_successful_subscription(context):
    success_message = context.driver.find_elements(By.CLASS_NAME, 'success-message').text
    assert 'Subscription successful' in success_message


@then(u'close the browser')
def closeBrowser(context):
    context.driver.quit()
'''