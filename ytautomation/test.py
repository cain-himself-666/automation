from selenium import webdriver
from time import sleep
import tkinter
import pandas as pd

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:/Users/RJ/AppData/Local/Google/Chrome/User Data')
options.add_argument('--profile-directory=Default')
options.add_argument('--disable-web-security')
driver = webdriver.Chrome(options=options, executable_path="chromedriver.exe")
driver.get("http://studio.youtube.com")

class ytauto:

    def elementLoaded(self, element):
        try:
            driver.find_element_by_xpath(element)
            print("\nFound the element   : " + element)
            return True
        except:
            print("\nFinding the element : " + element)
            sleep(2)
            return self.elementLoaded(element)

    def upload(self):
        if self.elementLoaded('//*[@id="upload-button"]/div'):
            upld = driver.find_element_by_xpath('//*[@id="upload-button"]/div').click()
            driver.find_element_by_xpath('//*[@id="content"]/input').send_keys(self.video)

        if self.elementLoaded('//*[@id="textbox"]'):
            driver.find_element_by_id('textbox').clear()
            ttle = driver.find_element_by_xpath('//*[@id="textbox"]').send_keys(self.title)
            description = driver.find_element_by_xpath('/html/body/ytcp-uploads-dialog/paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-details/div/ytcp-uploads-basics/ytcp-mention-textbox[2]/ytcp-form-input-container/div[1]/div[2]/ytcp-mention-input/div').send_keys(self.descp)
            sleep(3)
            link = driver.find_element_by_xpath('//*[@id="details"]/ytcp-video-info/div/div[2]/div[2]/ytcp-icon-button/iron-icon').click()
            driver.find_element_by_xpath('//*[@id="file-loader"]').send_keys(self.thumbnail)
            moptions = driver.find_element_by_xpath('//*[@id="details"]/div/div/ytcp-button/div').click()
            tag = driver.find_element_by_xpath('/html/body/ytcp-uploads-dialog/paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-details/div/ytcp-uploads-advanced/ytcp-form-input-container/div[1]/div[2]/ytcp-free-text-chip-bar/ytcp-chip-bar/div/input').send_keys(self.tags)
            r = tkinter.Tk()
            text = r.clipboard_get()
            r.withdraw()
            r.update()
            r.destroy()
            next = driver.find_element_by_xpath('//*[@id="next-button"]/div').click()
            option1 = driver.find_element_by_xpath('/html/body/ytcp-uploads-dialog/paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-details/div/ytcp-uploads-basics/ytcp-form-audience/ytcp-audience-picker/div[3]/paper-radio-group/paper-radio-button[2]/div[1]/div[1]').click()
            next2 = driver.find_element_by_xpath('//*[@id="next-button"]/div').click()

        if self.elementLoaded('//*[@id="next-button"]/div'):
            next3 = driver.find_element_by_xpath('//*[@id="next-button"]/div').click()

        if self.elementLoaded('/html/body/ytcp-uploads-dialog/paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[1]/paper-radio-button/div[1]/div[1]'):
            if(self.privacy == "Public"):
                option2 = driver.find_element_by_xpath('/html/body/ytcp-uploads-dialog/paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[1]/paper-radio-group/paper-radio-button[3]/div[1]/div[1]').click()
            elif(self.privacy == "Unlisted"):
                option2 = driver.find_element_by_xpath('/html/body/ytcp-uploads-dialog/paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[1]/paper-radio-group/paper-radio-button[2]/div[1]/div[1]').click()
            else:
                option2 = driver.find_element_by_xpath('/html/body/ytcp-uploads-dialog/paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[1]/paper-radio-group/paper-radio-button[1]/div[1]/div[1]').click()

            save = driver.find_element_by_xpath('//*[@id="done-button"]/div').click()

        if self.elementLoaded('//*[@id="close-button"]/div'):
            close = driver.find_element_by_xpath('//*[@id="close-button"]/div').click()
            print("\n\nShareable Link: ", text)

    def __init__(self):
        print("--------------Youtube Upload Automation---------------\n")
        df = pd.read_excel('test.xlsx')
        specific_dataset = df.loc[df['Operation'] == 'Upload']
        for i in specific_dataset.index:
            self.video = specific_dataset.Video[i]
            self.title = specific_dataset.Title[i]
            self.descp = specific_dataset.Description[i]
            self.thumbnail = specific_dataset.Thumbnail[i]
            self.tags = specific_dataset.Tags[i]
            self.privacy = specific_dataset.Privacy[i]
            self.upload()

def main():
    bot = ytauto()
    
if __name__ == '__main__':
    main()