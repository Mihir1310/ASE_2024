import math
from DATA import DATA
from COLS import COLS
from ROW import ROW
# Test Case 1
def testcase_1():
    data = DATA([])
    data.cols = COLS(ROW(['Marks', 'Age', 'Year']))
    data.add([26, 18, 2023])
    data.add([28, 20, 2025])
    data.add([30, 22, 2027])
    print(data.stats())

def testcase_2():
    data = DATA([])
    data.cols = COLS(ROW(['GPA', 'Month', 'Rank']))
    data.add([9, 5, 10])
    data.add([8, 2, 18])
    data.add([10, 8, 5])
    print(data.stats())

def testcase_3():
    data = DATA([])
    data.cols = COLS(ROW(['Number', 'Height', 'Weight']))
    data.add([1, 168, 150])
    data.add([2, 175, 202])
    data.add([3, 171, 175])
    print(data.stats())

testcase_1()
testcase_2()
testcase_3()