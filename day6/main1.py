from collections import defaultdict

def count_indirects(orbiter):
    orbitee = o2[orbiter]
    if orbitee not in o2:
        return 0
    return 1 + count_indirects(orbitee)

# o1 - orbitee: orbiter
# o2 - orbiter: orbitee
orbits = [l.strip() for l in open('input', 'r')]
o1 = defaultdict(list)
o2 = {}

for orbit in orbits:
    orbitee, orbiter = orbit.split(')')
    o1[orbitee].append(orbiter)
    o2[orbiter] = orbitee


directs = len(orbits)
indirects = sum(count_indirects(o) for o in o2)

print(f'Directs: {directs}')
print(f'Directs: {indirects}')
print(f'Total: {directs + indirects}')
