# NHentai Favorites Archiver

> Note that this is still a work in progress.

This repository contains a script that uses Selenium to go through every single one of your favorites!
While this script only converts your files into .cbz, there are plans to convert it into other ebook-compatible file formats such as .epub, .mobi, etc.
Do note that you will have to manually login so that it is possible to bypass the Captcha.
MAKE SURE YOU HAVE FIREFOX INSTALLED!

## Guide
Firstly, install all the necessary packages.
`pip install -r /path/to/requirements.txt`

Next, inside `SAVE_EVERYTHING.py` (Line 6), define the output directory of where your precious assets will be stored.
e.g: OUTPUT_FOLDER = 'C:/Users/Username/Downloads'

Run `python SAVE_EVERYTHING.py`

Manually login and let the script handle the rest.
