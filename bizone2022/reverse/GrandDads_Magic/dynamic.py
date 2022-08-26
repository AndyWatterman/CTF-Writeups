from unicorn import *
from unicorn.x86_const import *

FILENAME = "backup/magic_2.img.726782296e7a15b416d4d21529853b90"

INT_PRINT = 0x10
INT_READ = 0x16
INT_DISK = 0x13

PASSWORD = b"n0t_th3fl@gst1ll"
curr_sym = 0

binary = b""
read_data = b""

def hook_intr(mu, intno, user_data):
    global curr_sym, binary, read_data

    ah = mu.reg_read(UC_X86_REG_AH)
    al = mu.reg_read(UC_X86_REG_AL)
    dh = mu.reg_read(UC_X86_REG_DH)
    dl = mu.reg_read(UC_X86_REG_DL)
    cl = mu.reg_read(UC_X86_REG_CL)
    ch = mu.reg_read(UC_X86_REG_CH)
    bx = mu.reg_read(UC_X86_REG_BX)

    if intno == INT_PRINT:
        if ah == 0x0e:
            print(chr(al), end='')

    elif intno == INT_READ:
        if (curr_sym >= len(PASSWORD)):
            print("The end :-)")
            exit(0)

        mu.reg_write(UC_X86_REG_AL, PASSWORD[curr_sym])
        print(chr(PASSWORD[curr_sym]), end='')
        curr_sym += 1

    elif intno == INT_DISK:
        if ah == 0x2:
            n_sectors = al
            head = dh
            drive = dl
            sector = cl
            cylinder = ch

            lba_start = (cylinder * 16 + head) * 63 + (sector - 1)
            lba_end = (cylinder * 16 + head) * 63 + ((sector + n_sectors) - 1)

            start_offset = lba_start * 512
            end_offset = lba_end * 512

            # get results
            print(f"Read from {hex(start_offset)} to {hex(end_offset)}")
            read_data = binary[start_offset:end_offset]

            print(f"Write to {hex(bx)}, {hex(len(read_data))} bytes")
            mu.mem_write(bx, read_data)

            mu.reg_write(UC_X86_REG_AL, 0)
            mu.reg_write(UC_X86_REG_AH, 0)

            eflags = mu.reg_read(UC_X86_REG_EFLAGS)
            mu.reg_write(UC_X86_REG_EFLAGS, eflags & ~(1 << 0))

        if ah == 0x3:
            n_sectors = al
            head = dh
            drive = dl
            sector = cl
            cylinder = ch

            lba_start = (cylinder * 16 + head) * 63 + (sector - 1)
            lba_end = (cylinder * 16 + head) * 63 + ((sector + n_sectors) - 1)

            start_offset = lba_start * 512
            end_offset = lba_end * 512

            # get results
            sz = end_offset - start_offset
            read_data = bytes(mu.mem_read(bx, sz))
            print(f"Read from {hex(bx)}")
            print(read_data[:16])
            print(f"Write sectors to {hex(start_offset)}-{hex(end_offset)}")
            mu.mem_write(start_offset, read_data)

            mu.reg_write(UC_X86_REG_AL, 0)
            mu.reg_write(UC_X86_REG_AH, 0)

            eflags = mu.reg_read(UC_X86_REG_EFLAGS)
            mu.reg_write(UC_X86_REG_EFLAGS, eflags & ~(1 << 0))


def hook_code(mu, address, size, user_data):
    al = mu.reg_read(UC_X86_REG_AL)
    if address == 0xE0CF:
        print(chr(al), end='')
    elif address == 0xE0DD or address == 0xE0BB or address == 0xE014:
        print()

    #print(hex(address))

def main() -> None:
    global binary

    with open(FILENAME, "rb") as f:
        binary = f.read()

    img_base = 0x7c00
    entry_point = img_base

    try:
        # Initialize emulator in X86-16bit mode
        mu = Uc(UC_ARCH_X86, UC_MODE_16)

        # map 8KB memory for this emulation
        mem_size = len(binary)
        mu.mem_map(0, mem_size)

        # write machine code to be emulated to memory
        mu.mem_write(img_base, binary[:512])

        mu.hook_add(UC_HOOK_CODE, hook_code)
        mu.hook_add(UC_HOOK_INTR, hook_intr)

        # emulate machine code in infinite time
        mu.emu_start(entry_point, 0, count=0x7000)

        print(">>> Emulation done. Below is the CPU context")
    except UcError as e:
        print("ERROR: %s" % e)

if __name__ == '__main__':
    main()