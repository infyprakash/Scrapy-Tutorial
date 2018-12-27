import scrapy

class QuotesSpider(scrapy.Spider):
	name = "quotes"
	start_urls = [
	'http://quotes.toscrape.com/page/1/',
	'http://quotes.toscrape.com/page/2/',
	]

	def parse(self,response):
		for quote in response.css("div.quote"):
			yield {
			'Author' : quote.css("small.author::text").extract_first(),
			"quote" : quote.css("span.text::text").extract_first(),
			"Tags" : quote.css("div.tags a.tag::text").extract()
			}
		next_page = response.css("li.next a::attr(href)").extract()
		yield response.follow(next_page,callback=self.parse)

