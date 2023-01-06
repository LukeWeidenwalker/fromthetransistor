from random import randint
import cocotb
from cocotb.triggers import Timer

from collections import namedtuple


@cocotb.test()
async def test_add16(dut):
    for _ in range(512):
        in_a = randint(0, 0xFFFF)
        in_b = randint(0, 0xFFFF)

        await Timer(time=1)

        dut.a.value = in_a
        dut.b.value = in_b

        await Timer(time=1)

        expected_value = ~(in_a + in_b) & 0xFFFF
        actual_value = dut.out.value.integer
        assert actual_value == expected_value, f"in_a: {bin(in_a)}, in_b: {bin(in_b)} Expected output: {expected_value}, actual output: {actual_value}, type_expected: {type(expected_value)}, type_Actual: {type(actual_value)}"


