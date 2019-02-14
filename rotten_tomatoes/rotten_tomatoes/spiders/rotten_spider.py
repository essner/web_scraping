from scrapy import Spider
from rotten_tomatoes.items import RottenTomatoesItem
import re
import pandas as pd

with open('titles.txt', 'r') as f:
    lines = f.readlines()

lines = [word.strip() for word in lines]

class rottenSpider(Spider):
	name = 'rotten_spider'
	allowed_urls = ['https://www.rottentomatoes.com']
	handle_httpstatus_list = [404]
	start_urls = ['https://www.rottentomatoes.com/m/' + movie for movie in lines] 

	def parse(self, response):


		if response.status == 404:
			item = RottenTomatoesItem()
			item['faulty'] = response.url
			yield item

		else:
			temp = []
			rows = response.xpath('//section[@class="panel panel-rt panel-box movie_info media"]//ul/li')
			for row in rows:
				temp.append([row.xpath('./div[1]/text()').extract(),row.xpath('./div[2]//text()').extract()])

			for i in temp:
				i[1] = [x.rstrip() for x in i[1]]
				i[1] = [x for x in i[1] if x and x != ","]
				i[0] = [x.strip().replace(':', "") for x in i[0]]
				i[0] = i[0][0]

			df = pd.DataFrame(['Rating', 'Genre', 'Directed By', 'Written By','On Disc/Streaming','Runtime','Studio','Box Office'],columns = ['category'])
			temp_df = pd.DataFrame(temp,columns = ["category","info"])
			final_df = pd.merge(df,temp_df, left_on='category', right_on='category',how = 'left')
			

			item = RottenTomatoesItem()
			item['rating'] = final_df.loc[0, 'info']
			item['genre'] = final_df.loc[1, 'info']
			item['directors'] = final_df.loc[2, 'info']
			item['writers'] = final_df.loc[3, 'info']
			item['release'] = final_df.loc[4, 'info']
			item['runtime'] = final_df.loc[5, 'info']
			item['studio'] = final_df.loc[6, 'info']
			item['box_office'] = final_df.loc[7, 'info']
			item['title'] = response.url.split("/")[-1]

			yield item