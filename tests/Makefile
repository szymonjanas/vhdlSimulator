TOPLEVEL_LANG=vhdl
SIM=ghdl
COMPILE_ARGS=--ieee=synopsys
# COMPILE_ARGS=--ieee=standard
# COMPILE_ARGS+=-fexplicit
# COMPILE_ARGS+=-fsynopsys

# COMPILE_ARGS+=-fsynopsys
PWD=$(shell pwd)

export PYTHONPATH := $(PWD)/../model:$(PYTHONPATH)

VHDL_SOURCES = $(PWD)/../hdl/licznik.vhdl

TOPLEVEL := licznik
MODULE   := test_licznik

include $(shell cocotb-config --makefiles)/Makefile.sim
