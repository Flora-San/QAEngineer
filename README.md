
### SauceDemo Web Automation Using Python, Selenium & Pytest
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
### Exercise Automate a test case for a website using Selenium WebDriver 
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
