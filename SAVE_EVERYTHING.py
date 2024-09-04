#!/usr/bin/env python3
# Welcome degenerate! This script will download all of your favorite hentai from nhentai.net and save them as PDFs.
# Please enter the following into your command line (CMD) to run this script:
# 1. pip install -r /path/to/requirements.txt
# 2. python SAVE_EVERYTHING.py
# Do note that manual login is required as you will have to complete the captcha

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import requests
import os
from fpdf import FPDF
import shutil
from PIL import Image
import re

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

def compress_to_pdf(img_paths, title):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=0)

    # Get PDF page dimensions
    pdf_width = pdf.w - 2 * pdf.l_margin  # Width minus margins
    pdf_height = pdf.h - 2 * pdf.t_margin  # Height minus margins

    for img_path in img_paths:
        pdf.add_page()
        # pdf.image(img_path)

        with Image.open(img_path) as img:
            img_width, img_height = img.size
            
            # Calculate aspect ratios
            img_aspect = img_width / img_height
            pdf_aspect = pdf_width / pdf_height

            # Resize the image while maintaining aspect ratio
            if img_aspect > pdf_aspect:  # Image is wider than PDF
                new_width = pdf_width
                new_height = int(pdf_width / img_aspect)
            else:  # Image is taller than or fits within PDF
                new_height = pdf_height
                new_width = int(pdf_height * img_aspect)

            # Add the image to the PDF with calculated dimensions
            pdf.image(img_path, x=pdf.l_margin, y=pdf.t_margin, w=new_width, h=new_height)

    try:
        pdf_file_path = f'C:/Users/Jamie/Downloads/{title}.pdf'
        pdf.output(pdf_file_path)
        print(f'PDF saved to {pdf_file_path}')
    except Exception as e:
        print(f"Error saving PDF: {e}")

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
            # image_element.screenshot(screenshot_name)
            driver.find_element(By.XPATH, '/html/body/div[2]/section[3]/a').click()
            i = i + 1
        except NoSuchElementException:
            print('end of hentai')
            break
    driver.back()
    driver.back()
    driver.back()
    compress_to_pdf(img_paths, TITLE)
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