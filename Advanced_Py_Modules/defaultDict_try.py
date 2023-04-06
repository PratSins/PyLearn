from collections import defaultdict

d = defaultdict(lambda: 0)
print("d = ",d,end="\n\n")

d['CORRECT'] = 110
print("d = ", d,end="\n\n")

print("d['WRONG'] = ",d['WRONG'])
print("d = ", d,end="\n\n")