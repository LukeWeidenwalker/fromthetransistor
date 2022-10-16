import cocotb
from cocotb.triggers import Timer
from random import randint

import logging

logger = logging.getLogger(__name__)

@cocotb.test()
async def test_or8way(dut):
    for _ in range(0, 512):
        in_a = randint(0, 0xFF)

        await Timer(time=1)
        dut.in_a.value = in_a
        await Timer(time=1)

        expected_output = 1 if in_a > 0 else 0
        assert dut.out_y.value == expected_output, f"in_a: {bin(in_a)} Expected output: {bin(expected_output)}, actual output: {bin(dut.out_y.value)}"
