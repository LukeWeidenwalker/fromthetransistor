import cocotb
from cocotb.triggers import Timer
from random import randint

@cocotb.test()
async def test_not16(dut):
    for _ in range(0, 512):
        two_bytes = randint(0, 0xFFFF)
        await Timer(time=1)
        dut.in_a.value = two_bytes
        await Timer(time=1)

        # `& 0xFFFF` is to transform this from a signed into an unsigned integer
        assert dut.out_y.value == ~two_bytes & 0xFFFF, f"Input bytes: {bin(two_bytes)}, Expected output: {bin(~two_bytes)}, actual output: {dut.out_y.value}"
