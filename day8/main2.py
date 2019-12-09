from functools import reduce

inp = list(open('input', 'r').read().rstrip())
pixels = 25 * 6

layers = [inp[n: n + pixels] for n in range(0, len(inp), pixels)]
transposed = map(list, zip(*layers))

def reducer(colour1, colour2):
    return colour1 if colour1 in ('0', '1') else colour2

result = [reduce(reducer, layer) for layer in transposed]

# christmassy printing
result = ['\033[92m#' if x == '1' else '\033[91m|' for x in result]
[print(''.join(result[n: n + 25])) for n in range(0, pixels, 25)]

