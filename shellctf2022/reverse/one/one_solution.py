from qiling import *
from qiling.const import *
from qiling.extensions import pipe

import sys, string

TASK_PATH = "one"
ROOTFS = r"/qiling/examples/rootfs/x8664_linux"

ENTRY_POINT = 0x00005555555551C9
FLAG_LEN = 0x2F

class Solver:
    def __init__(self):
        self.ql = Qiling([TASK_PATH], ROOTFS, profile="/qiling/qiling/profiles/linux.ql", verbose=QL_VERBOSE.OFF)

        self.ql.os.stdin = pipe.SimpleInStream(sys.stdin.fileno())

        # stop at main()
        self.ql.run(end=ENTRY_POINT)
        self.replay_starts = self.ql.arch.regs.arch_pc

        # end replay on this condition
        # if ( v16 == 0x5D ) <---- here we stop
        #     puts("you're good at this!");
        self.replay_ends = 0x000055555555586F

        # save current state
        self.jumpstart = self.ql.save() or {}

    def __run(self, input: bytes):
        self.ql.os.stdin.write(input + b'\n')

        # resume emulation till function returns
        self.ql.run(begin=self.replay_starts, end=self.replay_ends)

    def save_to_file(self, data):
        self.f.write(data)

    def replay(self, input: bytes) -> bool:
        self.ql.restore(self.jumpstart)
        self.__run(input)

        rsp = self.ql.arch.regs.read("RSP")
        mem = self.ql.mem.read(rsp+0x40, 0x2f4)

        exp_mem = mem[:0x5d*4]
        res_mem = mem[0x180:0x180+0x5d*4]

        count = 0
        for i in range(0, len(exp_mem), 4):
            if exp_mem[i:i+4] == res_mem[i:i+4]:
                count += 1
            else:
                break

        return count

    def solve(self, input: bytes, count: int):
        ALLOWED_CHARS = string.ascii_letters + string.digits + r"""!_{}"""
        for ch in ALLOWED_CHARS:
            next_str = input + bytes([ord(ch)])
            curr_count = self.replay(next_str)
            if curr_count >= 0x5d:
                print(b"***FLAG***: " + next_str)
                exit(0)
            if curr_count > count:
                print(r"{}({})".format(next_str, count))
                self.solve(next_str, curr_count)


def progress(msg: str) -> None:
    print(msg, end='\r', file=sys.stderr, flush=True)

def main():
    solver = Solver()
    solver.solve(b"", 0)

if __name__ == "__main__":
    main()

