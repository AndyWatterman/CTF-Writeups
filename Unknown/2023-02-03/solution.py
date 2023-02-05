from malduck import aes

PRINTABLE = b"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"

ENC_DATA = bytes.fromhex("efe0acb2b8648a0cc3125e23e3ee4318")
KEY_PART_1 = b"JiQ0pMZ8DOQ8iwpldfCEGJ7EA"
KEY_PART_2 = b"ytWHy"
IV = b'\0'*16

for b1 in PRINTABLE:
    for b2 in PRINTABLE:
        key = KEY_PART_1 + bytes([b1]) + KEY_PART_2 + bytes([b2])
        ciphertext = aes.cbc.decrypt(key, IV, ENC_DATA)

        try:
            print(f"DATA: {ciphertext.decode('utf-8')}")
            print(f"KEY: {key}")

            password = chr(key[len(KEY_PART_1)]) + chr(key[-1])
            print(f"Password: {password}")

            exit(0)
        except Exception as ex:
            pass

