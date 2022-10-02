from pathlib import Path
from cocotb_test.simulator import run

hdl_sources_dir = Path().parent / "hdl"


def test_quickstart_examples():
    run(
        verilog_sources=[
            hdl_sources_dir / "00_quickstart_examples/my_design.sv"
        ],  # sources
        toplevel="my_design",  # top level HDL
        module="tb.00_quickstart_examples.test_my_design",  # name of cocotb test module
    )


def test_not():
    run(
        verilog_sources=[hdl_sources_dir / "01_gates/gates.v"],  # sources
        toplevel="_not",  # top level HDL
        module="tb.01_gates.test_not",  # name of cocotb test module
    )


def test_and():
    run(
        verilog_sources=[hdl_sources_dir / "01_gates/gates.v"],  # sources
        toplevel="_and",  # top level HDL
        module="tb.01_gates.test_and",  # name of cocotb test module
    )
