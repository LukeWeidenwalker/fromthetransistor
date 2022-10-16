import cocotb
from cocotb.triggers import Timer
from random import randint

@cocotb.test()
async def test_not16(dut):
    for _ in range(0, 512):
        in_a = randint(0, 0xFFFF)
        await Timer(time=1)
        dut.in_a.value = in_a
        await Timer(time=1)

        # `& 0xFFFF` is to transform this from a signed into an unsigned integer
        assert dut.out_y.value == ~in_a & 0xFFFF, f"Input bytes: {bin(in_a)}, Expected output: {bin(~in_a)}, actual output: {dut.out_y.value}"
