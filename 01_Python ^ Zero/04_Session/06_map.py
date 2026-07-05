offer = 25

def calc(price):
    price_offer = round((price * offer / 100))
    final_price = price - price_offer
    return final_price

prices = [100_000, 200_000, 150_000]



# outputs = [calc(price)[1] for price in prices]

outputs = map(calc, prices)
print(list(outputs))


