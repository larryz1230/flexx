from time import sleep
import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

# Important information
# username
username = "username"
# password
password = "password"
# start day
month = 10
day = 18
year = 2021

# end day
endmonth = 10
endday = 22
endyear = 2021

date = str(month) + "/" + str(day) + "/" + str(year)

#
driver = webdriver.Chrome(ChromeDriverManager().install())


# driver = webdriver.Chrome("C:/Users/larry/Desktop/chromedriver.exe")


def login():
    driver.get("https://teachmore.org/american/students/makeStudentAppointments.php")
    sleep(3)
    driver.find_element_by_id("access_login") \
        .send_keys(username)
    driver.find_element_by_id("access_password") \
        .send_keys(password)
    driver.find_element_by_xpath('//*[@id="loginForm"]/input[3]') \
        .click()
    sleep(3)
    driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/div[1]/a/button") \
        .click()

    sleep(2)
    runn()



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
    sleep(1)
    driver.find_element_by_xpath(
        "//*[@id='calendar']/div[2]/div/table/tbody/tr/td/div/div/div/table/tbody/tr[5]/td[1]/div") \
        .click()

    x = driver.find_element_by_id('select1')
    # x.click()
    drop = Select(x)
    drop.select_by_index(92)
    # sleep(1)
    x = driver.find_element_by_id('eventType')
    drop = Select(x)
    drop.select_by_index(1)
    x = driver.find_element_by_id('datepicker')
    x.click()
    x.clear()
    x.send_keys(date)
    # drop = Select(x)
    # drop.select_by_index(1)
    driver.find_element_by_xpath("//*[@id='createAppointmentModal']/div/div/div[3]/div/div/div[2]/button") \
        .click()


def valid():
    today = datetime.datetime(year, month, day)
    # print(today.weekday())
    if today.weekday() >= 5 or today.weekday() == 0:
        # print("FALSLSALAS")
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


glogin()
# login()
# while month < 13:
#     date = str(month) + "/" + str(day) + "/" + str(year)
#     if valid():
#         runn()
#     if day == endday and month == endmonth and year == endyear:
#         break
#     incrementday()


driver.close()
