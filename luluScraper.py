class ProductDetails(scrapy.Item):
    itemName = scrapy.Field()
    brandName = scrapy.Field()
    priceAED = scrapy.Field()
    stockAvailability = scrapy.Field()
    prodDescr = scrapy.Field()
    imageLinks = scrapy.Field()

class LuluSprider(scrapy.Spider):

   #name of spider
    name = 'luluscraper'

    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'lulu.csv'
    }

   #list of allowed domains
    allowed_domains = ['www.luluhypermarket.com']
   #starting url
    start_urls = ['https://www.luluhypermarket.com/en-ae/fresh-food-grocery/c/HY00216086?q=%3Arelevance&page={pageNumber}'.format(pageNumber=page) for page in range(1,3)]
   

    def scrape_product(self, response):
        item = response.css('h1.pdp-productname::text').extract()
        brand = response.css('strong label::text').extract()
        stock = response.css('span.stock-available::text').extract()
        price = response.css('.prod-price span::text').extract()
        productDescription = response.css('.description ul li::text').extract()
        image_url = response.css('.item img.lazyOwl::attr(src)').extract()
        yield ProductDetails(itemName = item, brandName = brand, priceAED = price, stockAvailability = stock, prodDescr = productDescription, imageLinks = image_url)
   
    def parse(self, response):

        brand = response.css('div.plp-prod-name::text').extract()
        product_url = response.css('a.js-gtm-product-link::attr(href)').extract()
        for pro in product_url:
            final_url = response.urljoin(pro)
            yield scrapy.Request(url=final_url, callback = self.scrape_product)
