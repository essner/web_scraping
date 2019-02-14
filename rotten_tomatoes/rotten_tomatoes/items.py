# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RottenTomatoesItem(scrapy.Item):
	# define the fields for your item here like:
	rating = scrapy.Field()
	genre = scrapy.Field()
	directors = scrapy.Field()
	writers = scrapy.Field()
	release = scrapy.Field()
	runtime = scrapy.Field()
	studio = scrapy.Field()
	box_office = scrapy.Field()
	faulty = scrapy.Field()
	title = scrapy.Field()
