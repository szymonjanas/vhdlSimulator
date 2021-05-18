import cocotb
from cocotb.triggers import Timer
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge

import random

async def CLEAR(DUT):
    RESET = 1
    DUT.reset <= RESET
    await RisingEdge(DUT.clk)
    RESET = 0
    DUT.reset <= RESET


@cocotb.test()
async def test_count_to_15(DUT):

    clock = Clock(DUT.clk, 10, units="us") # f = 1/10us = 100MHz
    cocotb.fork(clock.start())  

    DIR = 1
    DUT.dir <= DIR 
    RESET = 0
    DUT.reset <= RESET

    counterHistory = list()
    for num in range(0, 16):
        await RisingEdge(DUT.clk)
        counterHistory.append(int(DUT.led.value))
        outputLed = int(DUT.led.value)
        assert outputLed == num, "Counter error! Output value {} is not equal to {}!".format(outputLed, num)
    print("Test " + test_count_to_15.__name__ + ", Counter History: ", counterHistory)


@cocotb.test()
async def test_change_dir(DUT):
    """ 
    1. Count to 8. 
    2. Change DIR. 
    3. Count to 0.
    """

    clock = Clock(DUT.clk, 10, units="us") # f = 1/10us = 100MHz
    cocotb.fork(clock.start())  

    DIR = 1
    DUT.dir <= DIR 
    RESET = 0
    DUT.reset <= RESET

    CountTo = 8
    outputLed = None
    counterHistory = list()
    # 1. Count to 8
    for num in range(0, CountTo):
        await RisingEdge(DUT.clk)
        counterHistory.append(int(DUT.led.value))
        outputLed = int(DUT.led.value)
        assert outputLed == num, "Counter error! Output value {} is not equal to {}!".format(outputLed, num)
    
    # Test if counter value is equal 8
    outputLed = int(DUT.led.value)
    assert outputLed == CountTo-1, "Counter error! Output value {} is not equal to {}!".format(outputLed, CountTo-1)

    # 2. Change DIR
    DIR = 0
    DUT.dir <= DIR 

    # 3. Count to 0
    CountTo = outputLed+2
    for num in range(0, CountTo):
        await RisingEdge(DUT.clk)
        counterHistory.append(int(DUT.led.value))
        outputLed = int(DUT.led.value)
        assert outputLed == (CountTo - num-1), "Counter error! Output value {} is not equal to {}!".format(outputLed, (CountTo - num-1))
    print("Test " + test_change_dir.__name__ + ", Counter History: ", counterHistory)

@cocotb.test()
async def test_reset(DUT):
    """ 
        1. Count to 8. 
        2. Reset
        4. Count to 15.
    """

    clock = Clock(DUT.clk, 10, units="us") # f = 1/10us = 100MHz
    cocotb.fork(clock.start())  
    

    DIR = 1
    DUT.dir <= DIR 
    RESET = 0
    DUT.reset <= RESET
    await RisingEdge(DUT.clk)

    CountTo = 9
    outputLed = None
    counterHistory = list()
    # 1. Count to 8
    for num in range(0, CountTo):
        await RisingEdge(DUT.clk)
        counterHistory.append(int(DUT.led.value))
        outputLed = int(DUT.led.value)
        assert outputLed == num, "Counter error! Output value {} is not equal to {}!".format(outputLed, num)
    
    # 2. Reset
    RESET = 1
    DUT.reset <= RESET
    await RisingEdge(DUT.clk)
    RESET = 0
    DUT.reset <= RESET

    CountTo = 16
    # 1. Count to 8
    for num in range(0, CountTo):
        await RisingEdge(DUT.clk)
        counterHistory.append(int(DUT.led.value))
        outputLed = int(DUT.led.value)
        assert outputLed == num, "Counter error! Output value {} is not equal to {}!".format(outputLed, num)

    print("Test " + test_reset.__name__ + ", Counter History: ", counterHistory)

@cocotb.test()
async def test_count(DUT):

    clock = Clock(DUT.clk, 10, units="us") # f = 1/10us = 100MHz
    cocotb.fork(clock.start())  

    DIR = 1
    DUT.dir <= DIR 
    RESET = 0
    DUT.reset <= RESET

    counterHistory = list()
    for num in range(1, 40):
        await RisingEdge(DUT.clk)
        counterHistory.append(int(DUT.led.value))
    print("Test " + test_count.__name__ + ", Counter History: ", counterHistory)

@cocotb.test()
async def test_count_reverse(DUT):

    clock = Clock(DUT.clk, 10, units="us") # f = 1/10us = 100MHz
    cocotb.fork(clock.start())  

    DIR = 0
    DUT.dir <= DIR 
    RESET = 0
    DUT.reset <= RESET

    counterHistory = list()
    for num in range(1, 40):
        await RisingEdge(DUT.clk)
        counterHistory.append(int(DUT.led.value))
    print("Test " + test_count_reverse.__name__ + ", Counter History: ", counterHistory)
