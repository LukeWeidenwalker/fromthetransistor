import cocotb
from cocotb.triggers import Timer
from random import randint

import logging

logger = logging.getLogger(__name__)

@cocotb.test()
async def test_dmux4way(dut):
    for _ in range(0, 512):
        sel = randint(0, 3)
        in_ = randint(0, 1)

        await Timer(time=1)
        dut.in_.value = in_
        dut.sel.value = sel
        await Timer(time=1)

        if sel == 0:
            assert dut.out_a.value == in_
            assert dut.out_b.value == 0
            assert dut.out_c.value == 0
            assert dut.out_d.value == 0
        elif sel == 1:
            assert dut.out_a.value == 0
            assert dut.out_b.value == in_
            assert dut.out_c.value == 0
            assert dut.out_d.value == 0        
        elif sel == 2:
            assert dut.out_a.value == 0
            assert dut.out_b.value == 0
            assert dut.out_c.value == in_
            assert dut.out_d.value == 0    
        elif sel == 3:
            assert dut.out_a.value == 0
            assert dut.out_b.value == 0
            assert dut.out_c.value == 0
            assert dut.out_d.value == in_
            