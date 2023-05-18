import scrapy


class ImagesSpider(scrapy.Spider):
    name = "images"
    start_urls = ["https://en.wikipedia.org/wiki/Colombia"]

    def parse(self, response):
        image_urls = response.css(".image img ::attr(src)").getall()
        clean_image_urls = []
        for img_url in image_urls:
            clean_image_urls.append(response.urljoin(img_url))

        yield {"image_urls": clean_image_urls}
