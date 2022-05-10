from getter import Getter
from validators import url

def main():
    getter = Getter()
    user_input = input("Enter the best buy URL: ")
    valid_url = url(user_input)
    bb_url = user_input.__contains__("bestbuy")
    bb_item = user_input.__contains__("skuId")

    if valid_url and bb_url and bb_item:
        getter.getProductData(user_input)
    else:
        print("Please verify the url.")

if __name__ == '__main__':
    main()
