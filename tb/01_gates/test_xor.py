import cocotb
from cocotb.triggers import Timer

from collections import namedtuple


TruthTableEntry = namedtuple("TruthTableEntry", ["input_1", "input_2", "output"])

truth_table = [
    TruthTableEntry(input_1=0, input_2=0, output=0),
    TruthTableEntry(input_1=1, input_2=0, output=1),
    TruthTableEntry(input_1=0, input_2=1, output=1),
    TruthTableEntry(input_1=1, input_2=1, output=0),
]


@cocotb.test()
async def test_xor(dut):
    for entry in truth_table:
        await Timer(time=1)

        dut.a.value = entry.input_1
        dut.b.value = entry.input_2

        await Timer(time=1)

        assert dut.y.value == entry.output
