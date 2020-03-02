from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
from time import sleep


webdriver_path = 'chromedriver_win32/chromedriver.exe'
chrome_options = Options()
chrome_options.add_argument("-incognito")
browser = webdriver.Chrome(webdriver_path, options=chrome_options)

url = ''
browser.get(url)
a = 0
arr = []
st = set()

while a < 52:
    try:
        word = browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[1]/a[1]/div/h1').text.strip()
        print(word)
        browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[1]/a[1]/div').click()
        definitions = browser.find_elements_by_css_selector('p')
        defs = ''
        for _ in definitions:
            defs += _.text.strip() + '\n'
        if 'Magoosh' not in word:
            st.add((word, defs.strip()))
        sleep(2)
        browser.find_element_by_xpath('/html/body/div/div/div/div[2]/div/div[2]/a[1]').click()
        sleep(2)
    except:
        pass

    a += 1

for i in st:
    arr.append([i[0], i[1]])
print(len(arr))

df = pd.DataFrame(arr, columns=['word', 'definition'])
df.to_csv('gre1.csv', index=False)
