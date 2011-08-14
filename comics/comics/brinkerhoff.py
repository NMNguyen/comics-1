from comics.aggregator.crawler import CrawlerBase, CrawlerImage
from comics.meta.base import MetaBase

class Meta(MetaBase):
    name = 'Brinkerhoff'
    language = 'en'
    url = 'http://www.brinkcomic.com/'
    active = False
    start_date = '2006-01-02'
    end_date = '2009-12-30'
    rights = 'Gabe Strine'

class Crawler(CrawlerBase):
    def crawl(self, pub_date):
        pass # Comic no longer published
