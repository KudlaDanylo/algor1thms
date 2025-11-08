from functools import reduce

prise = [12, 5, 14, 87, 52]

total_price = reduce(lambda x, y: x + y, prise)

average_price = total_price / len(prise)

print(average_price)