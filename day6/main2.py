from collections import defaultdict
import math

# o1 - orbitee: orbiter
# o2 - orbiter: orbitee
orbits = [l.strip() for l in open('input', 'r')]
o1 = defaultdict(list)
o2 = {}

for orbit in orbits:
    orbitee, orbiter = orbit.split(')')
    o1[orbitee].append(orbiter)
    o2[orbiter] = orbitee

seen = set()
distances = defaultdict(lambda: math.inf)
node = o2['YOU']
q = [(node, 0)]

while node != o2['SAN']:
    node, d = q[0]
    if node not in seen:
        seen.add(node)
        distances[node] = d
        if node in o2:
            q.append((o2[node], d + 1))

        if node in o1:
            for orbiter in o1[node]:
                q.append((orbiter, d + 1))

    q = q[1:] # pop

print(distances[o2['SAN']])
