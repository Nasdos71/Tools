from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Wont work if 2FA bcs i am lazier than that, get yo ass to at least enter the acc on yo ip once smh 


user_user = input("Discord Email: ")
pass_pass =  input("Discord Pass: ")


chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--headless")

dv = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(dv, 30)

try:
    dv.get("https://discord.com/login?redirect_to=%2Fchannels%2F%40me")
except Exception as e:
    print(f"cant access site: {e}")

try:
    user_f = wait.until(EC.presence_of_element_located((By.ID, 'uid_7')))
    user_f.send_keys(user_user)
except Exception as e:
    print(f"cant find user field: {e}")

try:
    pass_f = wait.until(EC.presence_of_element_located((By.NAME, 'password')))
    pass_f.send_keys(pass_pass)
except Exception as e:
    print(f"cant find password field: {e}")

try:    
    sub_but = wait.until(EC.presence_of_element_located((By.XPATH, "//*[text()='Log In']")))
    sub_but.click()
except Exception as e:
    print(f"cant press login button: {e}")

WebDriverWait(dv, 10)

try:
    all_tab = wait.until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'item_c2739c') and @role='tab' and text()='All']")))
    all_tab.click()
except Exception as e:
    print(f"cant click 'All' tab: {e}")


try:
    list_friends = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "peopleListItem_d51464")))
except Exception as e:
    print(f"Cant find list of friends: {e}")

fr_list = []


try:
    for f in list_friends:
        user_info = f.find_element(By.CLASS_NAME, 'userInfo_f3939d')
        username = user_info.find_element(By.CLASS_NAME, 'username_f3939d').text
        tag = user_info.find_element(By.CLASS_NAME, 'discriminator_f3939d').text
        status = user_info.find_element(By.CLASS_NAME, 'text_f7ebfd').text
        fr_list.append(f"Username: {username} ({status})\n\n")
except Exception as e:
    print(f"problem with filtering data: {e}")


with open("Friends.txt", "w", encoding="utf-8") as f:
    for fr in fr_list:
        f.write(fr + "\n")

time.sleep(20)
dv.quit()
