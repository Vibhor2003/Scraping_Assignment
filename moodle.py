from selenium import webdriver
from selenium.webdriver.common.keys import Keys

val1 = input("Username : ")
val2 = input("Password : ")

driver = webdriver.Firefox(executable_path=".\geckodriver.exe")
driver.get("https://moodle.iitd.ac.in/login/index.php")

para = driver.find_element_by_id("login").text
res = para.split()
if (para.find('enter')==-1):
    if (para.find('+')!=-1):
        captcha = int(res[8])+int(res[10])
    else:
        captcha = int(res[8])-int(res[10]) 
else:
    if (para.find('first')!=-1):
        captcha = int(res[10])
    else:
        captcha = int(res[12])

s1 = driver.find_element_by_id("username")
s1.send_keys(val1)

s2 = driver.find_element_by_id("password")
s2.send_keys(val2)

s3 = driver.find_element_by_id("valuepkg3")
s3.clear()
s3.send_keys(captcha)

search = driver.find_element_by_id("loginbtn")
search.send_keys(Keys.RETURN)
