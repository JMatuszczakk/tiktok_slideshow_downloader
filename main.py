from playwright.sync_api import sync_playwright
from urllib.request import urlretrieve
import time
import os
import random
import sys
url = input("Wpisz url slajdszoła:")

playwright = sync_playwright().start()
browser = playwright.chromium.launch(headless=True)
page = browser.new_page()
page.goto("https://ttsave.app/en/slide")

page.wait_for_load_state("networkidle")

page.locator('body > div.fc-consent-root > div.fc-dialog-container > div.fc-dialog.fc-choice-dialog > div.fc-footer-buttons-container > div.fc-footer-buttons > button.fc-button.fc-cta-consent.fc-primary-button > p').click()
page.locator('#input-query').fill(url)
page.locator("#btn-download").click()

#get the url of button
# url1 = page.locator("#button-download-ready > a:nth-child(2)").get_attribute("href")
# print(url1)
# url2 = page.locator("#button-download-ready > a:nth-child(4)").get_attribute("href")
# print(url2)

time.sleep(3)
# ile_zdjec = int(input("Enter the number of images:"))
urls = []
for i in range(2, 20, 2):
    try: 
        if "SLIDE" in page.locator(f"#button-download-ready > a:nth-child({i})").text_content():
            url = page.locator(f"#button-download-ready > a:nth-child({i})").get_attribute("href")
            if url not in urls:
                urls.append(url)
        else:
            break
    except:
        break
browser.close()
playwright.stop()
print("Znaleziono "+str(len(urls))+" zdjęć")
print("Pobieranie zdjęć...")
#download every url using urllib
#if using mac print mac
random_int = random.randint(0, 1000)

if sys.platform == 'darwin':
    print("KORZYSTASZ Z MACA")
    os.mkdir(str(random_int))
    for i in range(len(urls)):
        urlretrieve(urls[i], f"{random_int}/{i}.jpg")
else:
    base_filepath = os.getcwd()
    print("KORZYSTASZ Z TEGO GORSZEGO SYSTEMU")
    print("KORZYSTASZ Z TEGO GORSZEGO SYSTEMU")
    print("KORZYSTASZ Z TEGO GORSZEGO SYSTEMU")
    os.mkdir(f"{base_filepath}\\{random_int}")
    for i in range(len(urls)):
        urlretrieve(urls[i], f"{base_filepath}\\{random_int}\\{i}.jpg")
print("Pobieranie zakończone")
print("Zdjęcia znajdziesz w folderze "+str(random_int))
print("Pozdrawiam serdecznie")