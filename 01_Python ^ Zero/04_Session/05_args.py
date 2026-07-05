def calc(offer, *args):
    outputs = []

    for price in args:
        price_offer = round((price * offer / 100))
        final_price = price - price_offer
        outputs.append((price_offer, final_price))

    return outputs


prices = [100_000, 200_000, 250_000]
cart = calc(25, *prices)


for idx, (price_offer, final_price) in enumerate(cart):
    print(f"{idx + 1} - Price offer: {price_offer}\t Final price: {final_price}")