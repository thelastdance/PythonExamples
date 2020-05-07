from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('/home/kutayacar/Desktop/chromedriver_linux64/chromedriver')

driver.get("http://www.python.org") #open the page

elem = driver.find_element_by_name("q")# inspect

elem.clear() # delete entry

elem.send_keys("pycon") # write into entry

elem.send_keys(Keys.RETURN ) #click enter

driver.quit() #close the browser
