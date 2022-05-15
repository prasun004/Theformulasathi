import os
from selenium.webdriver import Firefox 
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


PATH = os.path.join(os.getcwd(), 'driver', 'geckodriver')
URLS = [ 
    'https://www.cuemath.com/algebra/algebraic-formulas/',
    "https://www.cuemath.com/geometry-formulas/"
]

def open_in_youtube(formula):

    service = Service(executable_path=PATH)
    browser = Firefox(service=service)
    browser.get("https://www.youtube.com/results?search_query=" + formula)

    sleep(2)

    elem = browser.find_element(By.XPATH, '//*[@id="video-title"]')
    elem.click()

    sleep(3)




formulas = {}

service = Service(executable_path=PATH)
browser = Firefox(service=service)

print("Fetching Formulas ......")

browser.get(URLS[0])

elements = browser.find_elements(By.XPATH, '/html/body/div[3]/div/main/div/div/div[1]/div[1]/div[2]/div/div[2]/div/div/div[1]/ul[3]/*')

file = open('formulas.txt', 'w')

for element in elements:

    file.write(element.text + '\n')


browser.get(URLS[1])

sleep(3)

elements = browser.find_elements(By.TAG_NAME, 'li')

for i in range(16):
    element = elements[i]

    txt = element.text.replace('\n', "")

    file.write(txt + '\n')

    
file.close()
browser.quit()

del file 

file = open('formulas.txt')

for line in file.readlines():

    elem = line.strip('\n').split('=')
    
    if len(elem) == 3:

        formulas[elem[0]] = elem[2]

    else:

        formulas[elem[0]] = elem[1]

file.close()

del file

print("Hello, I am Prasun Formula Bot, i will tell you formulas")

while True:

    user_inp = input("Ask me anything >> ").replace(' ', '').lower()

    if user_inp == 'all':

        print(formulas)
        continue

    for key, value in formulas.items():

        if user_inp in key.replace(' ', '') or key.replace(' ', '') in user_inp:

            print(value)

            ch = input('Do you want to watch it in youtube (y/n) : ').lower()

            if ch == 'y':

                open_in_youtube(user_inp)
            break

        elif user_inp in value.replace(' ',  '') or value.replace(' ', '') in user_inp:

            print(key)

            ch = input('Do you want to watch it in youtube (y/n) : ').lower()

            if ch == 'y':

                open_in_youtube(user_inp)
            break

    else:

        print('Could not get formula !')
