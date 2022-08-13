SOURCE = 'R;crc75ihl`cNYe`]m%50gYhugow~34i'
results1 = []

for i in range(0, 19):
    res = SOURCE[i:19] + SOURCE[19:] + SOURCE[:i]
    results1.append(res)

results2 = []
for res in results1:
    m = ""
    for i in range(len(res) // 2):
        m += chr(ord(res[i]) - 3 * int(i/-2))
    for j in range(len(res) // 2, len(res)):
        m += chr(ord(res[j]) - int(j/6))
    results2.append(m)

results3 = []
for res in results2:
    m = ""
    for i in range(len(res) // 2):
        m += res[i+len(res) // 2] + res[i]
    results3.append(m)

for r in results3:
    if "shell" in r:
        print(r)
        break