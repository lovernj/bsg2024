from selenium import webdriver
from selenium.webdriver.common.by import By
def setup(login:tuple[str,str],headless:bool=False) -> webdriver.Firefox:
    """Create a BSG session. 
       Parameters:
           login: Tuple of username and password strings
           headless: If True, then setup the webdriver in headless mode.
       Returns:
           webdriver.Firefox
    """
    options = webdriver.FirefoxOptions()
    if headless:
        options.add_argument("--headless")
    driver = webdriver.Firefox(service=webdriver.FirefoxService(executable_path="C:\Program Files\geckodriver\geckodriver.exe"),options=options)
    driver.get("https://www.bsg-online.com/")
    assert "Business Strategy Game" in driver.title
    # Login to BSG
    driver.find_element(By.ID, "acct_name").send_keys(login[0])
    driver.find_element(By.ID, "passwdInput").send_keys(login[1])
    driver.find_element(By.ID, "loginbutton").click()
    # Get to the Decisions page
    driver.get("https://www.bsg-online.com/users/program/v3")
    return driver
