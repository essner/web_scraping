# -*- coding: utf-8 -*-


BOT_NAME = 'movie_reviews'

SPIDER_MODULES = ['movie_reviews.spiders']
NEWSPIDER_MODULE = 'movie_reviews.spiders'
ROBOTSTXT_OBEY = False
ITEM_PIPELINES = {'movie_reviews.pipelines.WriteItemPipeline': 300}
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 3
