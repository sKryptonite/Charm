import scrapy
from ..items import FerganatutorialItem

class FerganatutorialSpider(scrapy.Spider):
    name = 'fergana'
    page_number = 2
    name2 = input("Search for: ")
    start_urls = [
        'https://fergana.agency/search/?search=%s' % name2
    ]

    def parse(self, response):

        items = FerganatutorialItem()
        all_div_quotes = response.css('div.news-list__content')

        for fergana in all_div_quotes:
            title = fergana.css('p::text').extract()
            date = fergana.css('.news-list__date::text').extract()

            items['title'] = title
            items['date'] = date

            yield items

        p_num = int(response.css('div.pagination__container  span::text')[0].extract())

        next_page = FerganatutorialSpider.start_urls[0] + '&n=' + str(FerganatutorialSpider.page_number)
        if FerganatutorialSpider.page_number-1 == p_num:
            yield response.follow(next_page, callback=self.parse)
            FerganatutorialSpider.page_number += 1