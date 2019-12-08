inp = list(open('input', 'r').read().rstrip())
pixels = 25 * 6

layers = [inp[n: n + pixels] for n in range(0, len(inp), pixels)]

min_layer = min(layers, key=lambda x: x.count('0'))

print(min_layer.count('1') * min_layer.count('2'))
