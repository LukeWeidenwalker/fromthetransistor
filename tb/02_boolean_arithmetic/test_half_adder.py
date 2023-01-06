import cocotb
from cocotb.triggers import Timer

from collections import namedtuple


TruthTableEntry = namedtuple("TruthTableEntry", ["input_1", "input_2", "sum", "carry"])

truth_table = [
    TruthTableEntry(input_1=0, input_2=0, sum=0, carry=0),
    TruthTableEntry(input_1=1, input_2=0, sum=1, carry=0),
    TruthTableEntry(input_1=0, input_2=1, sum=1, carry=0),
    TruthTableEntry(input_1=1, input_2=1, sum=0, carry=1),
]


@cocotb.test()
async def test_half_adder(dut):
    for entry in truth_table:
        await Timer(time=1)

        dut.a.value = entry.input_1
        dut.b.value = entry.input_2

        await Timer(time=1)

        assert dut.carry.value == entry.carry
        assert dut.sum.value == entry.sum

