#!/usr/bin/env python3
# MAKE SURE TO CHANGE THE PATH OF YOUR DOUJIN DOWNLOADS! (line 39)
# Please enter the following into your command line (CMD) to run this script:
# 1. pip install -r /path/to/requirements.txt
# 2. python SAVE_EVERYTHING.py
# Do note that manual login is required as you will have to complete the captcha

import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import requests
import os
from fpdf import FPDF
import shutil
from PIL import Image
import zipfile

# Initialize the WebDriver
driver = webdriver.Firefox()

def remove_special_characters(input_string):
    return re.sub(r'[^a-zA-Z0-9\s]', '', input_string)

def empty_folder(folder_path):
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)
    print('emptied folder')

def compress_to_cbz(img_paths, title):
    # Define the path to save the .cbz file
    cbz_file_path = f'V:\dojins\Favorites'
    
    try:
        # Create a zip file with .cbz extension
        with zipfile.ZipFile(cbz_file_path, 'w') as cbz:
            for img_path in img_paths:
                # Add the image to the cbz file
                img_filename = os.path.basename(img_path)  # Get the image filename
                cbz.write(img_path, img_filename)  # Add the image to the cbz archive
        
        print(f'CBZ saved to {cbz_file_path}')
    except Exception as e:
        print(f"Error creating CBZ: {e}")

def dirty_fuck(xpath):
    driver.find_element(By.XPATH, xpath).click()

    TITLE = remove_special_characters(driver.find_element(By.CSS_SELECTOR, '.title').text)
    print("here is the first manga", TITLE)
    # Create a folder 
    # Create a directory to save images
    os.makedirs('downloaded_images', exist_ok=True)

    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[1]/a/img').click()
    i = 0
    img_paths = []
    while True:
        try:
            image_element = driver.find_element(By.XPATH, '/html/body/div[2]/section[3]/a/img')
            img_url = image_element.get_attribute('src')
            # Download the image using requests
            img_data = requests.get(img_url).content
            img_path = os.path.join('downloaded_images', f'image_{i}.jpg')
            
            with open(img_path, 'wb') as handler:
                handler.write(img_data)

            rel_path = f'downloaded_images/image_{i}.jpg'
            img_paths.append(rel_path)
            driver.find_element(By.XPATH, '/html/body/div[2]/section[3]/a').click()
            i = i + 1
        except NoSuchElementException:
            print('end of hentai')
            break
    driver.back()
    driver.back()
    driver.back()
    compress_to_cbz(img_paths, TITLE)
    empty_folder('downloaded_images')

try: 
    driver.get('https://nhentai.net/login/')

    # Login
    print("Please log in manually...")
    WebDriverWait(driver, timeout=300).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/nav/div/ul[2]/li[2]'))
    )

    # Navigate to user's favorites (filthy fuck)
    driver.get('https://nhentai.net/favorites/')

    # repeat until every page has been downloaded DRY
    while True:
        print('begin!')
        try:
            j = 1
            while True:
                try:
                    dirty_fuck(f'/html/body/div[2]/div/div[{j}]/div/a')
                    # go to first manga
                    j = j + 1
                except Exception as e:
                    print('onto the next page')
                    break
            driver.find_element(By.CSS_SELECTOR, '.next').click()

        except Exception as e:
            print(f'An error occurred: {e}')
            break

finally:
    driver.quit()
#!/usr/bin/env python3
# MAKE SURE TO CHANGE THE PATH OF YOUR DOUJIN DOWNLOADS! (line 39)
# Please enter the following into your command line (CMD) to run this script:
# 1. pip install -r /path/to/requirements.txt
# 2. python SAVE_EVERYTHING.py
# Do note that manual login is required as you will have to complete the captcha

import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import requests
import os
from fpdf import FPDF
import shutil
from PIL import Image
import zipfile

# Initialize the WebDriver
driver = webdriver.Firefox()

def remove_special_characters(input_string):
    return re.sub(r'[^a-zA-Z0-9\s]', '', input_string)

def empty_folder(folder_path):
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            os.remove(item_path)
        elif os.path.isdir(item_path):
            shutil.rmtree(item_path)
    print('emptied folder')

def compress_to_cbz(img_paths, title):
    # Define the path to save the .cbz file
    cbz_file_path = f'V:\dojins\Favorites'
    
    try:
        # Create a zip file with .cbz extension
        with zipfile.ZipFile(cbz_file_path, 'w') as cbz:
            for img_path in img_paths:
                # Add the image to the cbz file
                img_filename = os.path.basename(img_path)  # Get the image filename
                cbz.write(img_path, img_filename)  # Add the image to the cbz archive
        
        print(f'CBZ saved to {cbz_file_path}')
    except Exception as e:
        print(f"Error creating CBZ: {e}")

def dirty_fuck(xpath):
    driver.find_element(By.XPATH, xpath).click()

    TITLE = remove_special_characters(driver.find_element(By.CSS_SELECTOR, '.title').text)
    print("here is the first manga", TITLE)
    # Create a folder 
    # Create a directory to save images
    os.makedirs('downloaded_images', exist_ok=True)

    driver.find_element(By.XPATH, '/html/body/div[2]/div[1]/div[1]/a/img').click()
    i = 0
    img_paths = []
    while True:
        try:
            image_element = driver.find_element(By.XPATH, '/html/body/div[2]/section[3]/a/img')
            img_url = image_element.get_attribute('src')
            # Download the image using requests
            img_data = requests.get(img_url).content
            img_path = os.path.join('downloaded_images', f'image_{i}.jpg')
            
            with open(img_path, 'wb') as handler:
                handler.write(img_data)

            rel_path = f'downloaded_images/image_{i}.jpg'
            img_paths.append(rel_path)
            driver.find_element(By.XPATH, '/html/body/div[2]/section[3]/a').click()
            i = i + 1
        except NoSuchElementException:
            print('end of hentai')
            break
    driver.back()
    driver.back()
    driver.back()
    compress_to_cbz(img_paths, TITLE)
    empty_folder('downloaded_images')

try: 
    driver.get('https://nhentai.net/login/')

    # Login
    print("Please log in manually...")
    WebDriverWait(driver, timeout=300).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/nav/div/ul[2]/li[2]'))
    )

    # Navigate to user's favorites (filthy fuck)
    driver.get('https://nhentai.net/favorites/')

    # repeat until every page has been downloaded DRY
    while True:
        print('begin!')
        try:
            j = 1
            while True:
                try:
                    dirty_fuck(f'/html/body/div[2]/div/div[{j}]/div/a')
                    # go to first manga
                    j = j + 1
                except Exception as e:
                    print('onto the next page')
                    break
            driver.find_element(By.CSS_SELECTOR, '.next').click()

        except Exception as e:
            print(f'An error occurred: {e}')
            break

finally:
    driver.quit()
