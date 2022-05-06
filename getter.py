from os.path import exists
import requests as r
import json
from os.path import exists


class Getter:
    def __init__(self):
        self.key = 'qhqws47nyvgze2mq3qx4jadt'
        self.skuId = None

    def getSKUFromURL(self, best_buy_url):
        return best_buy_url.split('skuId=')[1]

    def getProductData(self, url):
        skuId = self.getSKUFromURL(url)
        api_url = f'https://api.bestbuy.com/v1/products/{skuId}.json?apiKey={self.key}'
        page_json = r.get(api_url).text
        productData = json.loads(page_json)
        self.saveProductPrice(productData)

    def check_in_file(self, sku):
        with open("tracked_products.json", 'r') as file:
            data = json.loads(file.read())

            for items in data['products']:
                if sku in items.values():
                    return True

    def add_to_file(self, stuff):
        with open("tracked_products.json", 'r+') as item_file:
            file_data = json.load(item_file)
            file_data['products'].append(stuff)
            item_file.seek(0)
            json.dump(file_data, item_file, indent=4)

    def saveProductPrice(self, data):
        # Set product info in json format with 'products' as the key.
        # 'products' is the key, and the item information is a
        # list of values.
        product_info = {
            'products': [
                {
                    'name': data['name'],
                    'sku':data['sku'],
                    'On_Sale': data['onSale'],
                    'clearance': data['clearance'],
                    'regularPrice': data['regularPrice'],
                    'salePrice': data['salePrice']
                }
            ]
        }

        # chicking if the file exists.
        # if the file exist, we continue and check if the item
        # is already in the file.
        if exists("tracked_products.json"):
            if self.check_in_file(data['sku']):
                print("Item already in file.")
            else:
                # if item is not on the list, we add it.
                # format the information as a dictionary
                # wtihout the key ('products')
                # so we can add it as a value to 'products'.
                new_product ={
                    'name': data['name'],
                    'sku':data['sku'],
                    'On_Sale': data['onSale'],
                    'clearance': data['clearance'],
                    'regularPrice': data['regularPrice'],
                    'salePrice': data['salePrice']
                }
                self.add_to_file(new_product)
                print("added new item to file")
        # If the file does not exist, it will create the file
        # with the item entered.
        else:
            with open("tracked_products.json", "w") as outfile:
                json.dump(product_info, outfile, indent=4)

    def del_entry(self, sku):
        with open("tracked_products.json", "r+") as item_file:
            file = json.load(item_file)
            for item in range(len(file['products'])):
                if file['products'][item]['sku'] == sku:
                    file['products'].pop(item)
                    print('deleted')
                    open('tracked_products.json', 'w').write(json.dumps(file, indent=4))
                    break

