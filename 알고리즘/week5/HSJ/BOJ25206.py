score = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
m = a = 0
for i in range(20):
    sub, c, g = input().split()
    if g == 'P':
        continue
    else:
        m += float(c) * score[g]
        a += float(c)
result = m/a
print(result)