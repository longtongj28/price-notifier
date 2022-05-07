from getter import Getter


def main():
    getter = Getter()
    user_input = input("Enter the best buy URL: ")
    if "bestbuy" in user_input.split() and "skuId=" in user_input.split():
        getter.getProductData(user_input)
    else:
        print("Please enter a valid Best Buy ulr.")

if __name__ == '__main__':
    main()