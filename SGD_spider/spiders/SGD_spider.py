from scrapy import Spider
from budget.items import GeneItem

class BudgetSpider(Spider):
    name = "SGD_spider"
    allowed_urls = ['https://www.yeastgenome.org']
    start_urls = ['https://www.yeastgenome.org/locus/S000006000']

    def parse(self, response):

        # shell call rows = response.xpath('//*[@id="overview"]/div/dl/dd')
        StandardName = rows[0].xpath('./text()').extract_first().strip()
        SysName = rows[1].xpath('./text()').extract_first().strip()
        SGD_ID = rows[2].xpath('./text()').extract_first().strip()
        FeatureType = rows[4].xpath('./text()').extract_first().strip()
        Description = rows[5].xpath('./text()').extract_first().strip()
        NameDesc = rows[6].xpath('./text()').extract_first().strip()



# go = //*[@id="go"]/div/div[1]/dl/dd/ul/li
# go.xpath('./dl/dd/text()').extract_first().strip()

# go2 = response.xpath('//*[@id="go"]/div/div')
# go2_elements = go2.xpath('./dl/dd/ul/li/a/text()').extract()
# MolFunc, BioProc, CellComp = go2_elements
