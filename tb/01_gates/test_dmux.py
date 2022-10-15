import cocotb
from cocotb.triggers import Timer

from collections import namedtuple


TruthTableEntry = namedtuple("TruthTableEntry", ["in_a", "sel", "out_x", "out_y"])

truth_table = [
    TruthTableEntry(in_a=0, sel=0, out_x=0, out_y=0),
    TruthTableEntry(in_a=1, sel=0, out_x=1, out_y=0),
    TruthTableEntry(in_a=0, sel=1, out_x=0, out_y=0),
    TruthTableEntry(in_a=1, sel=1, out_x=0, out_y=1),
]


@cocotb.test()
async def test_dmux(dut):
    for entry in truth_table:
        await Timer(time=1)

        dut.in_a.value = entry.in_a
        dut.sel.value = entry.sel

        await Timer(time=1)

        assert dut.out_x.value == entry.out_x
        assert dut.out_y.value == entry.out_y
