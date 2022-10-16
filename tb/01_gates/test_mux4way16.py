import cocotb
from cocotb.triggers import Timer
from random import randint

import logging

logger = logging.getLogger(__name__)

@cocotb.test()
async def test_mux4way16(dut):
    for _ in range(0, 512):
        sel = randint(0, 3)
        in_a = randint(0, 0xFFFF)
        in_b = randint(0, 0xFFFF)
        in_c = randint(0, 0xFFFF)
        in_d = randint(0, 0xFFFF)

        await Timer(time=1)
        dut.in_a.value = in_a
        dut.in_b.value = in_b
        dut.in_c.value = in_c
        dut.in_d.value = in_d
        dut.sel.value = sel
        await Timer(time=1)

        if sel == 0:
            expected_output = in_a
        elif sel == 1:
            expected_output = in_b
        elif sel == 2:
            expected_output = in_c      
        elif sel == 3:
            expected_output = in_d

        assert dut.out_y.value == expected_output, f"sel: {bin(sel)}, in_a: {bin(in_a)}, in_b: {bin(in_b)}, in_c: {bin(in_c)}, in_d: {bin(in_d)} Expected output: {bin(expected_output)}, actual output: {bin(dut.out_y.value)}"
