
### Demo Sauce Web Automation Using Python, Selenium & Pytest
For this  solution approach I'm using **Python, Selenium & Pytest** 
check in your local if you already have these configurations, otherwise you can install
with the following configurations, the described below is for linux.

**Check Python**
first check if you already have Python installed in your system
```
# Check the Python 3 version
$ python3 --version
```
otherwise you can install Python with the following command line:

```
$ sudo apt-get update
$ sudo apt-get install python3.8 python3-pip
```

**Install Selenium**
with the following command line :
```
pip install selenium
```
Install Chromedriver to handle the window browser, for this test we use Chrome Browser.
check which version works in your system [ChromeDriver](https://chromedriver.chromium.org/getting-started)

**Install pytest**

pytest
```
pip install pytest
```
you can run testcases from terminal using pytest
```
pytest test_checkout.py
```
----
### Exercise Test Plan for Automated Tests Cases
**Test Case:** Login and buy a product E2E on [SauceDemo](https://www.saucedemo.com/)

**Test Steps:**
1. Launch the web browser.

2. Navigate to the website: [SauceDemo](https://www.saucedemo.com/).

3. Enter a valid username and password.

4. Click the "Login" button.

5. Verify that the user is redirected to the inventory page.

6. Verify that you can select a product.

7. Verify you can check the product in the cart page.

8. Buy the selected product and checkout.

9. Fill the fields with data to complete the checkout.

10. Assert the quantity and price of the product selected.

11. Log out from the website.

-----
**Test Plan for [SauceDemo](https://www.saucedemo.com/)**

**1. Test Objectives:**

The main objectives of testing the website [SauceDemo](https://www.saucedemo.com/) are to ensure that it functions correctly, provides a smooth user experience, and maintains security and data integrity. Specific objectives include:

- Verify that users can successfully log in and navigate the site.
- Ensure that product listings are displayed accurately and can be added to the cart.
- Confirm that the checkout and payment processes function correctly.
- Test the site's compatibility across different browsers and devices.
- Validate the security of user data, including authentication mechanisms.
- Check for responsiveness and overall performance.

**2. Test Environment:**

**2.1. Hardware:**
- Various devices (PC, Mac, mobile phones, tablets)
- Different operating systems (Windows, macOS, Android, iOS)

**2.2. Software:**
- Web browsers (Google Chrome, Mozilla Firefox, Safari, Microsoft Edge)
- Selenium WebDriver for test automation
- Programming language (e.g., Python)
- Test management and reporting tools (e.g., pytest, Allure)
- VPN and proxy tools for security testing (if required)

**2.3. Test Data:**
- Valid and invalid usernames and passwords for login testing
- Product information for inventory and shopping cart testing

**3. Test Scenarios:**

**3.1. User Authentication:**
- Verify that a valid user can log in successfully.
- Check that an invalid user cannot log in.
- Test the "Forgot Password" functionality.

**3.2. Product Listing and Cart:**
- Ensure that products are displayed accurately.
- Confirm that users can add and remove items from the shopping cart.
- Check for proper calculation of item totals and taxes.
- Test the shopping cart's checkout process.

**3.3. Checkout and Payment:**
- Validate the checkout process, including shipping and payment options.
- Verify that orders are successfully placed.
- Test the cancellation of orders and order history.
- Ensure that the checkout process is secure and sensitive data is protected.

**3.4. Compatibility:**
- Test the website on various browsers (Chrome, Firefox, Safari, Edge).
- Ensure responsiveness on different devices (PC, Mac, mobile, tablet).
- Confirm compatibility with different screen resolutions.

**3.5. Security Testing:**
- Test for vulnerabilities such as SQL injection, XSS, CSRF, and authentication flaws.
- Verify that user data is encrypted and stored securely.
- Perform session management and user access control testing.

**3.6. Performance and Load Testing:**
- Test the website's performance under normal and peak load conditions.
- Check for slow-loading pages, errors, or timeouts.
- Measure response times and server resource utilization.

**4. Test Cases:**

Detailed test cases will be developed for each of the above test scenarios. These test cases will include step-by-step instructions, expected results, and acceptance criteria.

**5. Test Data:**

- User account data (valid and invalid usernames and passwords).
- Sample product data for inventory and shopping cart testing.
- Test payment information for checkout and payment testing.

**6. Test Schedule:**

The testing schedule will be determined based on project timelines and priorities. It will include the test execution, bug reporting, and retesting phases.

**7. Defect Management:**

A defect management process will be established to report, track, prioritize, and resolve any issues encountered during testing. This will include bug tracking tools and a clear workflow for the development and testing teams.

**8. Test Reporting:**

Test results will be documented using test management and reporting tools. Reports will include information about the test objectives, test cases executed, pass/fail status, and any issues identified during testing.

**9. Risks and Mitigation:**

Identify potential risks and develop mitigation strategies to ensure that testing proceeds smoothly and achieves the test objectives.

**10. Exit Criteria:**

The test plan will be considered complete when all the test cases and scenarios have been executed, defects have been addressed, and the test objectives have been met.

**11. Sign-off:**

The test plan will be reviewed and approved by relevant stakeholders before testing begins.

This test plan provides a comprehensive approach to testing [SauceDemo](https://www.saucedemo.com/)  and ensures that the website meets its objectives in terms of functionality, performance, security, and compatibility.


----

### API Bonus
For this  CRUD (Create, Read, Update, Delete) API test actions for the [Reqres.in](https://reqres.in/) API using **Python and pytest.**
In CRUD, we will focus on testing the "/users" endpoint, which is a common endpoint for user-related operations.
Also, ensure that you have the **requests** library installed by running

```
pip install requests 
```

if you haven't already.

you can run testcases from terminal using pytest
```
pytest crud.py
```
