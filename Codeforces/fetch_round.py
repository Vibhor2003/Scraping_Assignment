from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image
import os

contest = input("Contest No. - ")
if (int(contest)>0 and int(contest)<1493):
    print("Please wait site is loading")
    c=0
    left = ""

    driver = webdriver.Firefox(executable_path="..\\geckodriver.exe")
    driver.get("https://codeforces.com/contest/"+contest)

    page1 = driver.find_elements_by_xpath("//td[@class='id dark left']")
    for td in page1:
        left = left + td.text + " "
        c=c+1

    page2 = driver.find_elements_by_xpath("//td[@class='id left']")
    for td in page2:
        left = left + td.text + " "
        c=c+1

    if (c%2==0):
        page3 = driver.find_elements_by_xpath("//td[@class='id bottom dark left']")
        for td in page3:
            left = left + td.text + " "

    else:
        page3 = driver.find_elements_by_xpath("//td[@class='id bottom left']")
        for td in page3:
            left = left + td.text + " "

    res = left.split()
    print("Directories are creating")

    parent1 = "./"
    path = os.path.join(parent1,contest)
    os.mkdir(path)

    parent2 = "./"+contest+"/"

    for x in res:
        c=1
        path = os.path.join(parent2,x)
        os.mkdir(path)
        link = driver.find_element_by_link_text(x)
        link.click()
        ss = driver.find_elements_by_xpath("//div[@class='problem-statement']")
        for div in ss:
            div.screenshot(contest+"\\"+x+"\\image.png")
        ipt = driver.find_elements_by_xpath("//div[@class='input']")
        for div in ipt:
            f = open(contest+"\\"+x+"\\"+str(c)+"input.txt" , 'w')
            f.write(div.text)
            f.close()
            newf = open(contest+"\\"+x+"\\"+str(c)+"input.txt" , 'r')
            lines = newf.readlines()
            newf.close()
            afile = open(contest+"\\"+x+"\\"+str(c)+"input.txt" , 'w')
            for line in lines:
                if (line.strip("\n") != "input")and(line.strip("\n") != "Copy"):
                    afile.write(line)
            afile.close()
            c=c+1
        c=1
        opt = driver.find_elements_by_xpath("//div[@class='output']")
        for div in opt:
            f = open(contest+"\\"+x+"\\"+str(c)+"output.txt" , 'w')
            f.write(div.text)
            f.close()
            newf = open(contest+"\\"+x+"\\"+str(c)+"output.txt" , 'r')
            lines = newf.readlines()
            newf.close()
            afile = open(contest+"\\"+x+"\\"+str(c)+"output.txt" , 'w')
            for line in lines:
                if (line.strip("\n") != "output")and(line.strip("\n") != "Copy"):
                    afile.write(line)
            afile.close()
            c=c+1
        driver.back()
    print("All directories have been created")
    driver.close()
else:
    print("Wrong Contest No.")
