from random import randint
import cocotb
from cocotb.triggers import Timer

from collections import namedtuple

configRow = namedtuple("configRow", ["zx", "nx", "zy", "ny", "f", "no", "zr", "ng", "out"])

row1 = configRow(1, 0, 1, 0, 1, 0, 1, 0, lambda x, y: 0)

@cocotb.test()
async def test_alu(dut):
    for _ in range(512):
        in_x = randint(0, 0xFFFF)
        in_y = randint(0, 0xFFFF)

        await Timer(time=1)
        dut.x.value = in_x
        dut.y.value = in_y
        dut.zx.value = row1.zx
        dut.nx.value = row1.nx
        dut.zy.value = row1.zy
        dut.ny.value = row1.ny
        dut.f.value = row1.f
        dut.no.value = row1.no
        
        await Timer(time=1)

        actual_value = dut.out.value

        expected_value = int(bin(row1.out(in_x, in_y))[2:].zfill(16)[-16:], 2)
        assert actual_value == expected_value, f"in_a: {bin(in_x)}, in_b: {bin(in_y)} Expected output: {expected_value}, actual output: {actual_value}, type_expected: {type(expected_value)}, type_Actual: {type(actual_value)}"
        