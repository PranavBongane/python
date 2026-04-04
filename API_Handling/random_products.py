import requests
def get_random_products():
    url = "https://api.freeapi.app/api/v1/public/randomproducts/product/random"
    response = requests.get(url).json()
    if response["statusCode"] == 200:
        data = response["data"]
        id = data["id"]
        title = data["title"]
        price = data["price"]
        discountper = data["discountPercentage"]
        rating = data["rating"]
        stock = data["stock"]
        brand = data["brand"]
        category = data["category"]
        images = data["images"]
        return f"Product ID: {id} titled: '{title}' \nfrom brand: {brand} falls under: {category} category, \npriced at {price} with a discount of {discountper}%, has a rating: {"*"*int(rating)}, and {stock} items left in stock.",images
    else:
        print("API NOT WORKING...🦩")


def main():
    sentence,images=get_random_products()
    print(sentence)

    for img in images:
        print(img)

if __name__=="__main__":
    main()