import cocotb
from cocotb.triggers import Timer
from random import randint

import logging

logger = logging.getLogger(__name__)

@cocotb.test()
async def test_and16(dut):
    for _ in range(0, 512):
        in_a = randint(0, 0xFFFF)
        in_b = randint(0, 0xFFFF)

        await Timer(time=1)
        dut.in_a.value = in_a
        dut.in_b.value = in_b

        await Timer(time=1)

        assert dut.out_y.value == in_a & in_b, f"in_a: {bin(in_a)}, in_b: {bin(in_b)} Expected output: {bin(in_a & in_b)}, actual output: {dut.out_y.value}"
