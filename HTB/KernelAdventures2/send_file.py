FILENAME = "small.txt"
MAX_LEN = 950

with open(FILENAME, "r") as f:
    data = f.read()

arr = [data[i:i+MAX_LEN] for i in range(0, len(data), MAX_LEN)]
for s in arr:
    print(f"echo -n \"{s}\" >> exploit.gz")
    print()