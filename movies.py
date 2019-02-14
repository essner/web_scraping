from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv
import re

# Initialize a chrome browser
driver = webdriver.Chrome()

# Set url page to scrape
driver.get("https://www.rottentomatoes.com/browse/dvd-streaming-all")

# Continue clicking the "Show More" button until all elements are shown
while True:
	try:
		wait_button = WebDriverWait(driver, 10)
		next_button = wait_button.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="show-more-btn"]/button')))
		next_button.click()
	except Exception as e:
		print(e)
		break

# Find all of the movies on the page
wait_movies = WebDriverWait(driver, 20)
movies = wait_movies.until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="content-column"]/div[2]/div[2]/div')))

csv_file = open('movies.csv', 'w', encoding='utf-8')
writer = csv.writer(csv_file)


for movie in movies:
	
	# Initialize an empty dictionary for each review
	movies_dict = {}

	# For each element, if the info does not exists than return ?
	try:
		title = movie.find_element_by_xpath('./div[2]/a/h3').text
	except:
		title = "?"
	try:
		rotten = movie.find_element_by_xpath('./div[2]/a/div/span[1]/span[2]').text
	except:
		rotten = "?"
	try:
		user = movie.find_element_by_xpath('./div[2]/a/div/span[2]/span[2]').text
	except:
		user = "?"
		
	movies_dict['title'] = title
	movies_dict['rotten_rating'] = rotten
	movies_dict['user_rating'] = user
	writer.writerow(movies_dict.values())

csv_file.close()
driver.close()

