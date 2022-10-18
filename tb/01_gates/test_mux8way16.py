import cocotb
from cocotb.triggers import Timer
from random import randint

import logging

logger = logging.getLogger(__name__)

@cocotb.test()
async def test_mux8way16(dut):
    for _ in range(0, 512):
        sel = randint(0, 7)
        in_a = randint(0, 0xFFFF)
        in_b = randint(0, 0xFFFF)
        in_c = randint(0, 0xFFFF)
        in_d = randint(0, 0xFFFF)
        in_e = randint(0, 0xFFFF)
        in_f = randint(0, 0xFFFF)
        in_g = randint(0, 0xFFFF)
        in_h = randint(0, 0xFFFF)

        await Timer(time=1)
        dut.in_a.value = in_a
        dut.in_b.value = in_b
        dut.in_c.value = in_c
        dut.in_d.value = in_d
        dut.in_e.value = in_e
        dut.in_f.value = in_f
        dut.in_g.value = in_g
        dut.in_h.value = in_h
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
        elif sel == 4:
            expected_output = in_e
        elif sel == 5:
            expected_output = in_f      
        elif sel == 6:
            expected_output = in_g
        elif sel == 7:
            expected_output = in_h
            
        assert dut.out_y.value == expected_output
