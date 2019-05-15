from selenium import webdriver


driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.baidu.com')


input = driver.find_element_by_id('kw') #定位搜索框
sleep(2)
input.send_keys(Keys.SHIFT, 'what ') #字母会变味大写WHAT
sleep(2)
input.send_keys('is python')
sleep(2)
input.send_keys(Keys.CONTROL, 'a') #control + a 全选
sleep(2)
input.send_keys(Keys.CONTROL, 'c') #control + c 复制
sleep(2)
input.send_keys(Keys.BACKSPACE)
sleep(2)
input.send_keys(Keys.CONTROL, 'v')#control + v 粘贴
sleep(2)
input.send_keys(Keys.ENTER)
sleep(5)
driver.quit()


#----------------chromedriver install----------------#
# 1. 下载Chromedriver（mac.zip）一定要和chrome版本对应，否则无法打开
# 2. 将下载的zip解压，并将chromedriver.exe放在 usr/local/bin 路径下即可 
# 3. Chrome每次更新都可能需要换新的chromedriver
