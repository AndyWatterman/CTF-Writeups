import time

# e8030000 759f3103 e9030000 6764b72a
HASH_USER = 0x03319f75
HASH_ADMIN = 0x2ab76467

for i in range(256):
    print(f"[+] {i} - {int(time.process_time())}s")
    for j in range(256):
        #print(f"[++] {j} - {int(time.process_time())}s")
        for k in range(256):
            for l in range(256):
                hash = 0

                ch_o = i
                if ch_o > 0x7f:
                    ch_o = 0xFFFFFF00 | ch_o
                pre_hash = (0x401 * (hash + ch_o)) & 0xFFFFFFFF
                hash = (ch_o ^ (pre_hash >> 6) ^ pre_hash) & 0xFFFFFFFF

                ch_o = j
                if ch_o > 0x7f:
                    ch_o = 0xFFFFFF00 | ch_o
                pre_hash = (0x401 * (hash + ch_o)) & 0xFFFFFFFF
                hash = (ch_o ^ (pre_hash >> 6) ^ pre_hash) & 0xFFFFFFFF

                ch_o = k
                if ch_o > 0x7f:
                    ch_o = 0xFFFFFF00 | ch_o
                pre_hash = (0x401 * (hash + ch_o)) & 0xFFFFFFFF
                hash = (ch_o ^ (pre_hash >> 6) ^ pre_hash) & 0xFFFFFFFF

                ch_o = l
                if ch_o > 0x7f:
                    ch_o = 0xFFFFFF00 | ch_o
                pre_hash = (0x401 * (hash + ch_o)) & 0xFFFFFFFF
                hash = (ch_o ^ (pre_hash >> 6) ^ pre_hash) & 0xFFFFFFFF

                if hash == HASH_USER:
                    s = bytes([i, j, k, l])
                    print(f"[!!!] FOUND: {s.hex()}")
                    exit(0)