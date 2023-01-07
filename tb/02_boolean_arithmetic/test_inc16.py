from random import randint
import cocotb
from cocotb.triggers import Timer


@cocotb.test()
async def test_inc16(dut):
    for _ in range(512):
        in_a = randint(0, 0xFFFF)

        await Timer(time=1)

        dut.a.value = in_a

        await Timer(time=1)

        expected_value = int(bin(in_a + 1)[2:].zfill(16)[-16:], 2)

        actual_value = dut.out.value
        assert actual_value == expected_value, f"in_a: {bin(in_a)}, in_b: {bin(1)} Expected output: {expected_value}, actual output: {actual_value}, type_expected: {type(expected_value)}, type_Actual: {type(actual_value)}"
