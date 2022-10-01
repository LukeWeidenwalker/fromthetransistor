# test_my_design.py (extended)

import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_not(dut):
    dut.a.value = 0
    await Timer(time=1)

    dut._log.info(f"Not gate: a is {dut.a.value} and output y is {dut.y.value}")
    assert dut.y.value == 1, "y is 0 when it should be 1!"

