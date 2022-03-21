import scrapper


def iphone_13():
    links = {
        "amazon": "https://www.amazon.in/Apple-iPhone-13-128GB-Midnight/dp/B09G9HD6PD",
        "apple": "https://www.apple.com/in/shop/buy-iphone/iphone-13",
        "flipkart": "https://www.flipkart.com/apple-iphone-13-midnight-128-gb/p/itmca361aab1c5b0",
        "croma": "https://www.croma.com/apple-iphone-13-128gb-rom-mlpf3hn-a-midnight-black-/p/243459",
        "imagineonline": "https://imagineonline.store/products/iphone-13",
        "reliancedigital": "https://www.reliancedigital.in/apple-iphone-13-128-gb-midnight-black-/p/491997699"
    }
    for i in links:

        if "amazon" in links[i]:
            print("[₹{price}] Amazon".format(price=scrapper.amazon(links[i])))

        if "flipkart" in links[i]:
            print("[₹{price}] Flipkart".format(price=scrapper.flipkart(links[i])))

        if "imagineonline" in links[i]:
            print("[₹{price}] Imagineonline".format(price=scrapper.imagineonline(links[i])))

        if "reliancedigital" in links[i]:
            print("[₹{price}] Reliancedigital".format(price=scrapper.reliancedigital(links[i])))


# def iphone_13_pro():
#     links = {
#         "amazon": "https://www.amazon.in/Apple-iPhone-13-128GB-Midnight/dp/B09G9HD6PD",
#         "apple": "https://www.apple.com/in/shop/buy-iphone/iphone-13",
#         "flipkart": "https://www.flipkart.com/apple-iphone-13-midnight-128-gb/p/itmca361aab1c5b0",
#         "croma": "https://www.croma.com/apple-iphone-13-128gb-rom-mlpf3hn-a-midnight-black-/p/243459",
#         "imagineonline": "https://imagineonline.store/products/iphone-13",
#         "reliancedigital": "https://www.reliancedigital.in/apple-iphone-13-128-gb-midnight-black-/p/491997699"
#     }
