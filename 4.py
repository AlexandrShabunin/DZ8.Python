import json


def write_order_to_json(item, quantity, price, buyer, date):
    raw = {
        'item': item,
        'quantity': quantity,
        'price': price,
        'buyer': buyer,
        'date': date,
    }
    with open('orders.json', 'w') as write_json:
        json.dump(raw, write_json, indent=4)


write_order_to_json(
    item=['pen', 'pensil', 'ruller'],
    quantity=[7, 8, 9],
    price=[130, 19, 234],
    buyer=['Petrovich'],
    date=['19.02.2023'])
