import cocotb
from cocotb.triggers import Timer

from collections import namedtuple


TruthTableEntry = namedtuple("TruthTableEntry", ["a", "b", "c", "sum", "carry"])

truth_table = [
    TruthTableEntry(a=0, b=0, c=0, sum=0, carry=0),
    TruthTableEntry(a=0, b=0, c=1, sum=1, carry=0),
    TruthTableEntry(a=0, b=1, c=0, sum=1, carry=0),
    TruthTableEntry(a=0, b=1, c=1, sum=0, carry=1),
    TruthTableEntry(a=1, b=0, c=0, sum=1, carry=0),
    TruthTableEntry(a=1, b=0, c=1, sum=0, carry=1),
    TruthTableEntry(a=1, b=1, c=0, sum=0, carry=1),
    TruthTableEntry(a=1, b=1, c=1, sum=1, carry=1),
]


@cocotb.test()
async def test_half_adder(dut):
    for entry in truth_table:
        await Timer(time=1)

        dut.a.value = entry.a
        dut.b.value = entry.b
        dut.c.value = entry.c

        await Timer(time=1)

        assert dut.carry.value == entry.carry
        assert dut.sum.value == entry.sum

