from collections import defaultdict
from math import ceil

recipes = dict()
def parse(lines):
    for line in lines:
        lhs, rhs = line.split(' => ')
        inputs = { x.split(' ')[1]: int(x.split(' ')[0]) for x in lhs.split(', ') }
        val, out = map(lambda x: x.rstrip(), rhs.split(' '))
        recipes[out] = (int(val), inputs)

parse(open('input').readlines())
print(recipes)


ingredients = defaultdict(int)
q = list(ingredients.keys())
required_amount = 1
ingredients['FUEL'] = required_amount

while len(q) != 0 and q[0] != 'ORE':
    ingredient, quantity, constituents = q[0], ingredients[q[0][0]], ingredients[q[0][1]]
    # I can't create partial multiple of outputs, so round up to factor of required_amount
    factor_required_amount = ceil(quantity / required_amount)
    # total
    ingredients[ingredient] -= required_amount * factor_required_amount

    # produce the required amount of each constituent
    for i, q in constituents.items():
        ingredients[i] += q * factor_required_amount
        q.append(i)

    # pop item
    q = q[1:]

print(ingredients['ORE'])



