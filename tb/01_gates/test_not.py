import cocotb
from cocotb.triggers import Timer

from collections import namedtuple

TruthTableEntry = namedtuple("TruthTableEntry", ["input", "output"])

truth_table = [
    TruthTableEntry(input=0, output=1),
    TruthTableEntry(input=1, output=0),
]

@cocotb.test()
async def test_not(dut):
    for entry in truth_table:
        await Timer(time=1)
        dut.a.value = entry.input
        await Timer(time=1)

        assert dut.y.value == entry.output, f"Expected output: {entry.output}, actual output: {dut.y.value}"
