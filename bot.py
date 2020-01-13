from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep



class InstaBot:


    def __init__(self, username , pw):
        self.driver = webdriver.Chrome("D:\\instabot\\chromedriver\\chromedriver.exe")
        self.username = username
        self.pw = pw
        
        self.driver.get("https://www.instagram.com/")
        sleep(2)
        driver = self.driver
        
        login_button = driver.find_element_by_xpath("//a[@href='/accounts/login/?source=auth_switcher']")
        login_button.click()
        sleep(2)
        username = driver.find_element_by_xpath("//input[@name ='username']")
        username.clear()
        username.send_keys(self.username)
        pw = driver.find_element_by_xpath("//input[@name='password']")
        pw.clear()
        pw.send_keys(self.pw)
        sign_in = driver.find_element_by_xpath("//button[@type='submit']")
        sign_in.click()
        sleep(2)
    

    def get_unfollowers(self):
       Not_now =  self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")
       Not_now.click()
       self.driver.find_element_by_xpath("//a[@href='/{}/']".format(self.username)).click()
       sleep(4)
       self.driver.find_element_by_xpath("//a[contains(@href,'/following')]").click()
       following = self.get_names()
       self.driver.find_element_by_xpath("//a[contains(@href,'/followers')]").click()
       followers = self.get_names()
       not_following_back = [user for user in following if user not in followers]
       print(not_following_back)



    def get_names(self):  
       driver = self.driver 
       fBody  = driver.find_element_by_xpath("//div[@class='isgrP']")
       scroll = 0
       while scroll < 20: # scroll 5 times
         driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
         sleep(1)
         scroll += 1

       fList  = driver.find_elements_by_xpath("//div[@class='isgrP']//li")
       print("fList len is {}".format(len(fList)))

       print("ended")

       last_ht,ht = 0,1
       while last_ht != ht:
           last_ht = ht
           sleep(1)
           ht = self.driver.execute_script("""arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;""",fBody)
           links = fBody.find_elements_by_tag_name('a')
           names = [name.text for name in links if name.text != '']
        # close button
           self.driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/div[2]/button")\
            .click()
           return names
        
    
        




InstaBot('username','pw').get_unfollowers()    
