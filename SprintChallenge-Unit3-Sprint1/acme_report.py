import acme
from random import choice, uniform

possible_adj = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
possible_noun = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    for i in range(num_products):
        name = f'{choice(possible_adj)} {choice(possible_noun)}'
        weight = acme.randint(5, 101)
        price = acme.randint(5, 101)
        flammability = uniform(0.0, 2.5)
        product = acme.Product(name, price, weight, flammability)
        products.append(product)

    return products


def inventory_report(products):
    unique_names, prices, weights, flammabilities = [], [], [], []

    for product in products:
        prices.append(product.price)
        weights.append(product.weight)
        flammabilities.append(product.flammability)

        if product.name not in unique_names:
            unique_names.append((product.name))

    print(f"""OFFICIAL ACME INVENTORY REPORT
There are {len(unique_names)} unique names with the following averages:
Price - {get_avgs(prices)}
Weight - {get_avgs(weights)}
Flammability - {get_avgs(flammabilities)}
""")


def get_avgs(lst):
    return sum(lst) / len(lst)


if __name__ == '__main__':
    inventory_report((generate_products()))
