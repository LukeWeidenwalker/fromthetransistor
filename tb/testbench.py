from pathlib import Path
from cocotb_test.simulator import run

hdl_sources_dir = Path().parent / "hdl"

def test_quickstart_examples():
    run(
        verilog_sources=[hdl_sources_dir / "quickstart_examples/my_design.sv"], # sources
        toplevel="my_design",            # top level HDL
        module="tb.quickstart_examples.test_my_design"        # name of cocotb test module
    )

def test_gates():
    run(
        verilog_sources=[hdl_sources_dir / "01_gates/_not.v"], # sources
        toplevel="_not",            # top level HDL
        module="tb.01_gates.test_not"        # name of cocotb test module
    )