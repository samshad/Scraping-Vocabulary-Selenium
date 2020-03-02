from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
import pandas as pd


webdriver_path = 'chromedriver_win32/chromedriver.exe'
chrome_options = Options()
chrome_options.add_argument("-incognito")
browser = webdriver.Chrome(webdriver_path, options=chrome_options)

url = 'https://www.vocabulary.com/lists/337395'
browser.get(url)

word_section = browser.find_elements_by_css_selector('.explore')[0]
entries = word_section.find_elements_by_css_selector('.entry')

arr = []

for entry in entries:
    word_btn = entry.find_element_by_css_selector('.dynamictext')
    word = word_btn.text.strip()
    meaning = entry.find_element_by_css_selector('.definition').text.strip()

    url = word_btn.get_attribute('href')
    browser.execute_script("window.open('');")
    browser.switch_to.window(browser.window_handles[1])

    browser.get(url)
    short_definition = ''
    long_definition = ''

    try:
        def_block = browser.find_element_by_css_selector('.blurb')
        short_definition = def_block.find_element_by_css_selector('.short').text.strip()
        long_definition = def_block.find_element_by_css_selector('.long').text.strip()
    except:
        pass

    browser.close()
    browser.switch_to.window(browser.window_handles[0])
    print([word, meaning, short_definition, long_definition, url])
    arr.append([word, meaning, short_definition, long_definition, url])

browser.quit()
df = pd.DataFrame(arr, columns=['word', 'meaning', 'short definition', 'long definition', 'url'])
df.to_csv('wordlist-2.csv', index=False)
