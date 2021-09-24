from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
import datetime
import array
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

# Important information

usegoogle = False

# username
username = ""
# password
password = ""


# google info
email = ""
epass = ""

# start day
month = 9
day = 20
year = 2021
# end day
endmonth = 12
endday = 31
endyear = 2021

#  teacher ids
#  peffer - 92
#  millard - 80
#  wong - 125
# cooper - 30
# shockley - 110


tueteach = 110
wedteach = 110
thurteach = 110
friteach = 110

teacharr = [tueteach, wedteach, thurteach, friteach]
print(teacharr[0])
date = str(month) + "/" + str(day) + "/" + str(year)

#
driver = webdriver.Chrome(ChromeDriverManager().install())


def login():
    driver.get("https://teachmore.org/american/students/makeStudentAppointments.php")
    sleep(2)
    driver.find_element_by_id("access_login") \
        .send_keys(username)
    driver.find_element_by_id("access_password") \
        .send_keys(password)
    driver.find_element_by_xpath('//*[@id="loginForm"]/input[3]') \
        .click()
    driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/div[1]/a/button") \
        .click()

    sleep(0.5)


def glogin():
    driver.get("https://teachmore.org/american/students/makeStudentAppointments.php")
    sleep(3)
    driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div/div[1]/a/img') \
        .click()
    driver.find_element_by_xpath('//*[@id="identifierId"]') \
        .send_keys(email)
    driver.find_element_by_xpath('//*[@id="identifierId"]') \
        .send_keys(Keys.RETURN)
    sleep(0.5)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input"))).click()
    sleep(0.5)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input"))).send_keys(epass)
    driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input') \
        .send_keys(Keys.RETURN)
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div[1]/div/div[2]/div[1]/a/button"))).send_keys(epass)
    driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/div[1]/a/button").click()
    sleep(1.5)






#
#
#
# def follow():
#     for j in range(50):
#         # for i in range(5):
#             driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[3]/div[2]/div[2]/div/div/div/div[1]/div[3]/button') \
#                 .click()
#             sleep(1.5)
#             # driver.find_element_by_class_name("_7UhW9  PIoXz        qyrsm           uL8Hv         ").click()
#             # sleep(1.5)
#         driver.refresh()
#         sleep(1)

def runn():
    today = datetime.datetime(year, month, day)
    dayy = today.weekday()
    sleep(0.7)
    driver.find_element_by_xpath(
        "//*[@id='calendar']/div[2]/div/table/tbody/tr/td/div/div/div/table/tbody/tr[5]/td[1]/div") \
        .click()

    x = driver.find_element_by_id('select1')
    # x.click()
    drop = Select(x)
    drop.select_by_index(teacharr[dayy-1])
    # sleep(0.5)
    # sleep(1)
    x = driver.find_element_by_id('eventType')
    drop = Select(x)
    drop.select_by_index(1)
    x = driver.find_element_by_id('datepicker')
    x.click()
    x.clear()
    x.send_keys(date)
    # sleep(0.5)
    # drop = Select(x)
    # drop.select_by_index(1)
    driver.find_element_by_xpath("//*[@id='createAppointmentModal']/div/div/div[3]/div/div/div[2]/button") \
        .click()


def skipvalid():
    today = datetime.datetime(year, month, day)
    print(today.weekday())
    if today.weekday() >= 5 or today.weekday() == 0 or today.weekday() == 3:
        return False
    return True


def valid():
    today = datetime.datetime(year, month, day)
    print(today.weekday())
    if today.weekday() >= 5 or today.weekday() == 0:
        return False
    return True


def incrementday():
    global year
    global month
    global day
    curday = datetime.datetime(year, month, day)
    print(curday.date())
    curday += datetime.timedelta(days=1)
    year = curday.year
    month = curday.month
    day = curday.day


if usegoogle:
    glogin()
else:
    login()
while month < 13:
    date = str(month) + "/" + str(day) + "/" + str(year)
    if valid():
        runn()
    else:
        print(date)
    if day == endday and month == endmonth and year == endyear:
        break
    incrementday()


driver.close()
