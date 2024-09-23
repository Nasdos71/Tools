from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--disable-extensions")
# chrome_options.add_argument("--headless") 


dv = webdriver.Chrome(options=chrome_options)
dv.get("https://books.toscrape.com/catalogue/category/books_1/index.html")

wait = WebDriverWait(dv, 30)
time.sleep(5)


catgs = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@Class='nav nav-list']/li")))
list = []
list = catgs[0].text.split('\n')
list.pop(0)

dirct = os.getcwd()
for tag in list:
        
    link = dv.find_element(By.LINK_TEXT, tag)
    link.click()
    # WebDriverWait(dv, 2)
    contents = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ol[@Class='row']/li")))
    books = []
    books.append(tag)

# this gets the name in website not the full name make it to get the title, am dead rn so cya later boom boom;;;
    for bok in contents:
        dict = {
            "Name" : bok.text.split('\n')[0],
            "Price" : bok.text.split('\n')[1],
            "Status" : bok.text.split('\n')[2]
        }
        books.append(dict)
    
    while True:
        try:
            dv.find_element(By.LINK_TEXT, "next").click()
        except:
            break
            
        contents = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ol[@Class='row']/li")))
        for bok in contents:
            dict = {
            "Name" : bok.text.split('\n')[0],
            "Price" : bok.text.split('\n')[1],
            "Status" : bok.text.split('\n')[2]
         }
            books.append(dict)
    
    # path = os.path.join(dirct, "/Books/" + tag +'.txt')

    with open(tag + '.txt', 'w') as f:
        f.write(" Categeory: " + books[0] + '\n\n')
        f.write("---------------------------------\n")
        books.pop(0)
        for book in books:
            f.write("Name : " + book['Name'] + '\n')
            f.write("Price : " + book['Price']+ '\n')
            f.write("Status : " + book['Status']+ '\n')
            f.write("---------------------------------\n")
            
dv.quit()