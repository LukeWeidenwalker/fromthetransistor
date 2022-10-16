import cocotb
from cocotb.triggers import Timer
from random import randint

import logging

logger = logging.getLogger(__name__)

@cocotb.test()
async def test_mux16(dut):
    for _ in range(0, 512):
        sel = randint(0, 1)
        in_a = randint(0, 0xFFFF)
        in_b = randint(0, 0xFFFF)

        await Timer(time=1)
        dut.in_a.value = in_a
        dut.in_b.value = in_b
        dut.sel.value = sel

        await Timer(time=1)
        expected_output = in_b if sel else in_a
        # `& 0xFFFF` is to transform this from a signed into an unsigned integer
        assert dut.out_y.value == expected_output, f"in_a: {bin(in_a)}, in_b: {bin(in_b)} Expected output: {bin(expected_output)}, actual output: {dut.out_y.value}"