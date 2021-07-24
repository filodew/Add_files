import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from tkinter import *

creds = 'tempfile.temp'  # This just sets the variable creds to 'tempfile.temp'


def Add_uhfile():

    global c_name
    global c_pass



    # path to chrome webdriver and destination web address in maximum browser window
    driver = webdriver.Chrome(executable_path=r'C:\uhfa\driver\chromedriver.exe')
    driver.get('https://vhq-test.vfims.com')
    driver.maximize_window()

    # Log in
    email_company = driver.find_element_by_xpath("//input[@id='txtCompanyName']")

    with open(creds) as f:
        data = f.readlines()  # This takes the entire document we put the info into and puts it into the data variable
        c_name = data[0].rstrip()  # Data[0], 0 is the first line, 1 is the second and so on.
        c_pass = data[1].rstrip()  # Using .rstrip() will remove the \n (new line) word from before when we input it

    # input login information (in this case it is email address)
    email_company.send_keys(c_name)
    driver.find_element_by_xpath("//button[@id='Btnsubmit']").click() # click the submit button

    time.sleep(2) # additional time for load the webpage or objects on the webpage

    logpass = driver.find_element_by_xpath("//input[@id='txtpassword']") # find the place to enter the password
    logpass.send_keys(c_pass) #entering the password
    driver.find_element_by_xpath("//button[@id='Btnsubmit']").click() # click the submit button

    time.sleep(10)

    # VHQ menu operation
    driver.find_element_by_xpath("//*[@id='content']/a/span").click() # click the content
    driver.find_element_by_xpath("//*[@id='manageContents']/a/span").click() # click the manage content

    time.sleep(2)

    driver.find_element_by_xpath("//a[@id='contentLibrarysublink']").click() # click the library

    time.sleep(3)

    things = os.listdir("/uhfa/things/") # Files list from directory

    # for loop - adding files to the vhq library
    for thing in things:
        arg = os.path.splitext(thing)
        print(arg)
        if len(arg) != 2:
            continue

        if not((arg[1] == ".jpg") or (arg[1] == ".eet")):
            continue

        driver.find_element_by_xpath("//button[@title='Upload File']").click() # click the Upload file button

        time.sleep(3)

        # file upload support
        upload_input = driver.find_element_by_id("fileinput")

        print(thing)

        # change the current working directory
        os.chdir("/uhfa/things/")

        path = os.path.abspath(thing)
        #path = os.path.abspath("fd2.tar.000.jpg")
        file = open("dodane.txt", "a")
        file_name = os.path.basename(os.path.abspath(thing))
        #print(file_name)
        part_file_name = str(file_name)
        file.write(part_file_name + (" . "))
        upload_input.send_keys(path)

        contentname = driver.find_element_by_id("fileContentName")
        # file = open("dodane.txt")
        # last_line = file.read()
        contentname.send_keys("v240m_79_" + part_file_name)

        cententversion = driver.find_element_by_id("fileVersionAdd")
        # zamienić poniższe na zmienną przed logowaniem - nie zapomnij!!!
        cententversion.send_keys("2.5.0.0.79") # change the content version before start

        # click button "Next" (Upload file)
        driver.find_element_by_id("btnNextContent").click()

        # Models - checkboxes
        driver.find_element_by_id("chkModel-90").click()  # v240m 2G
        driver.find_element_by_id("chkModel-87").click()  # v240m 3G
        driver.find_element_by_id("chkModel-76").click()  # v240m 3G Plus
        driver.find_element_by_id("chkModel-99").click()  # v240m 3G Plus camera
        driver.find_element_by_id("chkModel-107").click()  # v240m 3GWB
        driver.find_element_by_id("chkModel-123").click()  # v240m B-FF
        driver.find_element_by_id("chkModel-89").click()  # v240m 3GBWC
        driver.find_element_by_id("chkModel-122").click()  # v240m BT/WIFI

        # click button "Next" (Upload file)
        driver.find_element_by_id("btnNextContent").click()

        time.sleep(2)

        # selectiong items from the drop-down menu
        driver.find_element_by_xpath("//*[@id='selectTargetUser_chosen']/a").click()
        driver.find_element_by_xpath("//*[@id='selectTargetUser_chosen']/div/ul/li[2]").click()

        time.sleep(1)

        driver.find_element_by_xpath("//*[@id='selectDeviceFileLocation_chosen']/a/div/b").click()
        driver.find_element_by_xpath("//*[@id='selectDeviceFileLocation_chosen']/div/div/input").send_keys('u')

        driver.find_element_by_xpath("//*[@id='selectDeviceFileLocation_chosen']/div/ul/li").click()

        driver.find_element_by_xpath("//*[@id='selectFileNameOnDevice_chosen']/a").click()

        driver.find_element_by_xpath("//*[@id='selectFileNameOnDevice_chosen']/div/div/input").send_keys(part_file_name,
                                                                                                         Keys.DOWN,
                                                                                                         Keys.ENTER)
        # Click cancel button - protection against adding unnecessary file until program is fully ready.
        #driver.find_element_by_xpath("//*[@id='btnCancelContent']").click()
        driver.find_element_by_xpath("//*[@id='btnUploadContent']").click()
        time.sleep(4)
        driver.find_element_by_xpath("//*[@id='infoBtnOk']").click()


        # click Upload File button
        # driver.find_element_by_xpath("//*[@id='btnUploadContent']").click()

        #driver.quit() # zamyka wszystkie otwarte przez selenium
        # driver.close() - tylko to okno na którym byliśmy skupieni


    Done()

def Done():
    global rootB

    rootB = Tk()  # This now makes a new window.
    rootB.geometry("400x200")
    rootB.title('Done')  # This makes the window title 'Done'

    myLabel21 = Label(rootB, text="Well Done!")
    myLabel21.pack()

    rootB.mainloop()
