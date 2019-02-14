from scrapy import Spider, Request
from user_reviews.items import UserReviewsItem
import re
import pandas as pd

with open('titles_2.txt', 'r') as f:
	lines = f.readlines()

lines = [word.strip() for word in lines]

test = ["the_grinch","creed_ii"]

class userSpider(Spider):
	name = 'user_spider'
	allowed_urls = ['https://www.rottentomatoes.com']
	handle_httpstatus_list = [404]
	start_urls = ['https://www.rottentomatoes.com/m/{}/reviews/?page=1&type=user&sort='.format(x) for x in test]


	def parse(self, response):
		num_pages = re.sub('Page 1 of ', '', response.xpath('//div[@class="panel-body content_body"]//span[@class="pageInfo"]/text()').extract_first())
		review_urls = [response.url + '?page={}&sort='.format(x) for x in range(1, int(num_pages) + 1)]

		for url in review_urls:
			yield Request(url = url, callback = self.parse_user_page)

	def parse_user_page(self, response):
		rows = response.xpath('//div[@class="row review_table_row"]')

		for i in rows:
			score_list = []
			name = i.xpath('./div[1]/div[3]/a/span/text()').extract_first()
			score_list.append([len(i.xpath('./div[2]/span[1]/span')),i.xpath('./div[2]/span[1]/text()').extract()])
			text = i.xpath('./div[2]/div[1]/text()').extract()

			item = UserReviewsItem()
			item['name'] = name
			item['score'] = score_list
			item['text'] = text
			item['movie'] = response.url.split("/")[-3]

			yield item


