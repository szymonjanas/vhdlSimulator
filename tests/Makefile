TOPLEVEL_LANG=vhdl
SIM=ghdl
COMPILE_ARGS=--ieee=synopsys

PWD=$(shell pwd)

export PYTHONPATH := $(PWD)/../model:$(PYTHONPATH)

VHDL_SOURCES = $(PWD)/../hdl/licznik.vhdl

TOPLEVEL := licznik
MODULE   := test_licznik

include $(shell cocotb-config --makefiles)/Makefile.sim
