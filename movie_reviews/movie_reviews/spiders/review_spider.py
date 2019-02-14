from scrapy import Spider, Request
from movie_reviews.items import MovieReviewsItem
import re
import pandas as pd

with open('movies_final.txt', 'r') as f:
    lines = f.readlines()

lines = [word.strip() for word in lines]

class reviewSpider(Spider):
	name = 'review_spider'
	allowed_urls = ['https://www.rottentomatoes.com']
	handle_httpstatus_list = [404]
	start_urls = ['https://www.rottentomatoes.com/m/{}/reviews/?page=1&sort='.format(x) for x in lines]

	def parse(self, response):
		num_pages = re.sub('Page 1 of ', '', response.xpath('//div[@class="panel-body content_body"]//span[@class="pageInfo"]/text()').extract_first())
		review_urls = [response.url + '?page={}&sort='.format(x) for x in range(1, int(num_pages) + 1)]

		for url in review_urls:
			yield Request(url = url, callback = self.parse_review_page)

	def parse_review_page(self, response):
		rows = response.xpath('//div[@class="row review_table_row"]')

		for i in rows:
			critic = i.xpath('./div[1]/div[3]/a/text()').extract_first()
			source = i.xpath('./div[1]/div[3]/a/em/text()').extract_first()
			score = i.xpath('.//div[@class="review_area"]/div[2]/div[2]/text()').extract()
			text = i.xpath('.//div[@class="review_area"]/div[2]/div[1]/text()').extract()

			item = MovieReviewsItem()
			item['critic'] = critic
			item['source'] = source
			item['score'] = score
			item['text'] = text
			item['movie'] = response.url.split("/")[-3]

			yield item
