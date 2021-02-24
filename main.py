from selenium import webdriver
import re

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://github.com")
driver.maximize_window()
driver.implicitly_wait(10)
driver.set_page_load_timeout(30)
driver.set_script_timeout(30)

""" SCENARIO 1
- Verify that by clicking on "Sign in" button user is redirected to login page
"""
driver.find_element_by_xpath("//a[@href = '/login']").click()
actual_title = driver.title
print(f"actual title is - {actual_title}")
expected_title = "Sign in to GitHub · GitHub"
assert expected_title == actual_title

""" SCENARIO 2
- Verify that username and password fields are mandatory in login page
"""
driver.find_element_by_id('password').send_keys("password")
driver.find_element_by_name('commit').click()
actual_errMsg = driver.find_element_by_xpath("//div[@class='container-lg px-2']").text
print(f"actual error message is - {actual_errMsg}")
expected_errMsg = "Incorrect username or password."
assert expected_errMsg == actual_errMsg

""" SCENARIO 3
- Verify that inserting m.ie into email field in reset_password page displays message "Can't find
that email, sorry."
"""
driver.find_element_by_link_text("Forgot password?").click()
driver.find_element_by_id('email_field').send_keys("m.ie")
driver.find_element_by_name('commit').click()
actual_errMsg = driver.find_element_by_xpath("//div[@class='container-lg px-2']").text
print(f"actual error message is - {actual_errMsg}")
expected_errMsg = "That address is not a"
if re.search(expected_errMsg, actual_errMsg):
    print("YES,string '{0}' is present in string '{1}' ".format(expected_errMsg, actual_errMsg))
else:
    print("NO,string '{0}' is not present in string {1} ".format(expected_errMsg, actual_errMsg))

""" SCENARIO 4
Verify that inserting empty value into email field in reset_password page displays message
"Can't find that email, sorry."
"""
driver.find_element_by_name('commit').click()
actual_errMsg = driver.find_element_by_xpath("//div[@class='container-lg px-2']").text
print(f"actual error message is - {actual_errMsg}")
expected_errMsg = "That address is not a"
if re.search(expected_errMsg, actual_errMsg):
    print("YES,string '{0}' is present in string '{1}' ".format(expected_errMsg, actual_errMsg))
else:
    print("NO,string '{0}' is not present in string {1} ".format(expected_errMsg, actual_errMsg))

""" SCENARIO 5
- Verify that clicking on "Sign up" button will redirect user into "join github" page
"""
driver.get("https://github.com")
driver.find_element_by_link_text("Sign up").click()
actual_title = driver.title
print(f"actual title is - {actual_title}")
expected_title = "Join GitHub · GitHub"
assert expected_title == actual_title

""" SCENARIO 6
- Verify that "join github" page contains text "Create your personal account"
"""
actual_text = driver.find_element_by_xpath("//h1[contains(text(),'Create your account')]").text
expected_text = "Create your account"
assert expected_text == actual_text
