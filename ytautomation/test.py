from selenium import webdriver
from time import sleep
import tkinter

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:/Users/SN Raju/AppData/Local/Google/Chrome/User Data')
# options.add_argument('--profile-directory="Default"')

def upload(title,descp):
    driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
    driver.get("http://studio.youtube.com")
    sleep(3)
    upload = driver.find_element_by_xpath('//*[@id="upload-button"]/div').click()
    sleep(2)
    video = driver.find_element_by_xpath('//*[@id="select-files-button"]/div').click()
    sleep(10)
    driver.find_element_by_id('textbox').clear()
    ttle = driver.find_element_by_xpath('//*[@id="textbox"]').send_keys(title)
    description = driver.find_element_by_xpath('/html/body/ytcp-uploads-dialog/paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-details/div/ytcp-uploads-basics/ytcp-mention-textbox[2]/ytcp-form-input-container/div[1]/div[2]/ytcp-mention-input/div').send_keys(descp)
    link = driver.find_element_by_xpath('//*[@id="details"]/ytcp-video-info/div/div[2]/div[2]/ytcp-icon-button/iron-icon').click()
    r = tkinter.Tk()
    text = r.clipboard_get()
    r.withdraw()
    r.update()
    r.destroy()
    print("\n\nShareable Link: ", text)
    next = driver.find_element_by_xpath('//*[@id="next-button"]/div').click()
    option1 = driver.find_element_by_xpath('/html/body/ytcp-uploads-dialog/paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-details/div/ytcp-uploads-basics/ytcp-form-audience/ytcp-audience-picker/div[3]/paper-radio-group/paper-radio-button[2]/div[1]/div[1]').click()
    sleep(2)
    next2 = driver.find_element_by_xpath('//*[@id="next-button"]/div').click()
    next3 = driver.find_element_by_xpath('//*[@id="next-button"]/div').click()
    sleep(2)
    option2 = driver.find_element_by_xpath('//*[@id="privacy-radios"]/paper-radio-button[3]').click()
    save = driver.find_element_by_xpath('//*[@id="done-button"]/div').click()	
    sleep(5)
    close = driver.find_element_by_xpath('//*[@id="close-button"]/div').click()
   
def main():
    print("--------------Youtube Upload Automation---------------\n")
    title = input("Enter the title to Video: ")
    descp = input("Enter Description to Video: ")
    upload(title,descp)


main()

