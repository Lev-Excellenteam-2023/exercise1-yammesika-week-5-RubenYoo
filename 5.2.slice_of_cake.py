def get_recipe_price(prices: dict, optionals: list = None, **ingredient) -> int:
    if optionals is None:
        optionals = []
    price = 0
    for ing in ingredient:
        if ing not in optionals:
            price += prices[ing]/100 * ingredient[ing]
    return int(price)


print(get_recipe_price({'chocolate': 18, 'milk': 8}, chocolate=200, milk=100))
print(get_recipe_price({'chocolate': 18, 'milk': 8}, optionals=['milk'], chocolate=300))
print(get_recipe_price({}))
