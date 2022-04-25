import requests as r
import json

class Getter:
    def __init__(self):
        self.key = 'qhqws47nyvgze2mq3qx4jadt'
        self.skuId = None
        self.productData = None
    
    def getSKUFromURL(self, best_buy_url):
        return best_buy_url.split('skuId=')[1]

    def getProductData(self):
        url = 'https://www.bestbuy.com/site/asus-rog-zephyrus-14-wqxga-120hz-gaming-laptop-amd-ryzen-9-16gb-ddr5-memory-amd-radeon-rx-6700s-1tb-pcie-4-0-ssd/6494638.p?skuId=6494638'
        skuId = self.getSKUFromURL(url)
        api_url = f'https://api.bestbuy.com/v1/products/{skuId}.json?apiKey={self.key}'
        page_json = r.get(api_url).text
        self.productData = json.loads(page_json)
        self.saveProductPrice()
        return self.productData
    
    def saveProductPrice(self):
        file = open('tracked_products.txt', 'a')
        file.write(f'name: {self.productData["name"]}\n')
        file.write(f'regularPrice: {self.productData["regularPrice"]}\n')
        file.write(f'salePrice: {self.productData["salePrice"]}\n')
        file.close()


