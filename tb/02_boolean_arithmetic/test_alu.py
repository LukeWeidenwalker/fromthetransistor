from random import randint
import cocotb
from cocotb.triggers import Timer
from cocotb.binary import BinaryValue, BinaryRepresentation
from collections import namedtuple

configRow = namedtuple("configRow", ["zx", "nx", "zy", "ny", "f", "no", "out"])

test_configs = [
    configRow(1, 0, 1, 0, 1, 0, lambda x, y: 0),
    configRow(1, 1, 1, 1, 1, 1, lambda x, y: 1),
    configRow(1, 1, 1, 0, 1, 0, lambda x, y: -1),
    configRow(0, 0, 1, 1, 0, 0, lambda x, y: x),
    configRow(1, 1, 0, 0, 0, 0, lambda x, y: y),
    configRow(0, 0, 1, 1, 0, 1, lambda x, y: ~x),
    configRow(1, 1, 0, 0, 0, 1, lambda x, y: +y),
    configRow(0, 0, 1, 1, 1, 1, lambda x, y: -x),
    configRow(1, 1, 0, 0, 1, 1, lambda x, y: -y),
    configRow(0, 1, 1, 1, 1, 1, lambda x, y: x+1),
    configRow(1, 1, 0, 1, 1, 1, lambda x, y: y+1),
    configRow(0, 0, 1, 1, 1, 0, lambda x, y: x-1),
    configRow(1, 1, 0, 0, 1, 0, lambda x, y: y-1),
    configRow(0, 0, 0, 0, 1, 0, lambda x, y: x+y),
    configRow(0, 1, 0, 0, 1, 1, lambda x, y: x-y),
    configRow(0, 0, 0, 1, 1, 1, lambda x, y: y-x),
    configRow(0, 0, 0, 0, 0, 0, lambda x, y: x&y),
    configRow(0, 1, 0, 1, 0, 1, lambda x, y: x|y)
]

@cocotb.test()
async def test_alu(dut):
    for _ in range(512):
        in_x = randint(0, 0xFFFF)
        in_y = randint(0, 0xFFFF)

        for i, row in enumerate(test_configs):
            print(f"Now running test {i}")
            await Timer(time=1)
            dut.x.value = in_x
            dut.y.value = in_y
            dut.zx.value = row.zx
            dut.nx.value = row.nx
            dut.zy.value = row.zy
            dut.ny.value = row.ny
            dut.f.value = row.f
            dut.no.value = row.no
            
            await Timer(time=1)
            actual_value = dut.out.value.binstr

            expected_value = bin(((1 << 16) - 1) & row.out(in_x, in_y))[2:].zfill(16)

            assert actual_value == expected_value, f"Test {i}: in_a: {bin(in_x)}, \n\
                in_b: {bin(in_y)} \n\
                Expected output: {expected_value}, \n\
                actual output: {actual_value} \n"

            