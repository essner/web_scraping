# -*- coding: utf-8 -*-

# Scrapy settings for rotten_tomatoes project

BOT_NAME = 'rotten_tomatoes'
SPIDER_MODULES = ['rotten_tomatoes.spiders']
NEWSPIDER_MODULE = 'rotten_tomatoes.spiders'
ROBOTSTXT_OBEY = False
ITEM_PIPELINES = {'rotten_tomatoes.pipelines.WriteItemPipeline': 300}
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 3

