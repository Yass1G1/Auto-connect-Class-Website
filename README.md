# Auto-connect-Class-Website

A script (in python with Selenium Library) that let you choose between 2 "classes" and then sign you in to the website of my teacher

## How to use it :
1. Understand the code
2. Modify it as you want
3. Enjoy your beer

## More seriously : 
1. [Download Webdriver of your desired browser](https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/)
2. Change the ``` driver ``` variable to locate the drivers that you downloaded (to allow the script to launch your browser)
3. Change the ``` driver.get(<https://link-to-your.website/>) ``` parentheses to add your own website (link to the sign in page)
4. Change this ``` 19. driver.find_element_by_xpath("//input[@id='<USER_FORM_TAG>']").send_keys("<USERNAME>") ``` 
5. And this ``` 21. driver.find_element_by_xpath("//input[@id='<PASS_FORM_TAG>']").send_keys("<USERNAME>") ```

(Sorry for bad explanations, this my very own script that I didn't made it to be changed but it can easily be modified ^^)

**Enjoy ! 🌈**

