from lambdafunction.simplefunction import *
import pytest

def test_sum():
    assert sumnumbers(10, 2) == 12

def test_multiply():
    assert mutiplynumbers(10, 2) == 20

def test_sub():
    assert subnumbers(10, 2) == 8

def test_div():
    assert divisionnumbers(10, 2) == 5

def test_sum1():
    assert sumnumbers(10, 4) == 14

def test_multiply1():
    assert mutiplynumbers(10, 4) == 40

def test_sub1():
    assert subnumbers(10, 4) == 6

def test_div1():
    assert divisionnumbers(10, 4) == 2

def test_sum2():
    assert sumnumbers(56, 34) == 90

def test_multiply2():
    assert mutiplynumbers(56, 34) == 1904

def test_sub2():
    assert subnumbers(56, 34) == 22

def test_div2():
    assert divisionnumbers(56, 34) == 1

def test_sum3():
    assert sumnumbers(564, 344) == 908

def test_multiply3():
    assert mutiplynumbers(564, 344) == 194016

def test_sub3():
    assert subnumbers(564, 344) == 220

def test_div3():
    assert divisionnumbers(564, 344) == 1

def test_sum4():
    assert sumnumbers(5646, 3446) == 9092

def test_multiply4():
    assert mutiplynumbers(5646, 3446) == 19456116

def test_sub4():
    assert subnumbers(5646, 3446) == 2200

def test_div4():
    assert divisionnumbers(5646, 3446) == 1