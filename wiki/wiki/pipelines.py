from scrapy.pipelines.images import ImagesPipeline


class CustomWikiImagesPipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        return request.url.split("/")[-1]
