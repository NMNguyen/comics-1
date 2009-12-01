from comics.aggregator.crawler import BaseComicCrawler
from comics.meta.base import BaseComicMeta

class ComicMeta(BaseComicMeta):
    name = "Sherman's Lagoon"
    language = 'en'
    url = 'http://www.slagoon.com/'
    start_date = '1991-05-13'
    history_capable_days = 32
    schedule = 'Mo,Tu,We,Th,Fr,Sa,Su'
    time_zone = -5
    rights = 'Jim Toomey'

class ComicCrawler(BaseComicCrawler):
    def crawl(self):
        self.url = 'http://www.slagoon.com/dailies/SL%(date)s.gif' % {
            'date': self.pub_date.strftime('%y%m%d'),
        }