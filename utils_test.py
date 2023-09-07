from utils import utils

# Test reversed
try:
    str_test = utils.reversed('234')
    print(str_test)
except:
    print("reversed function doesn't support string input")
    
try:
    int_test = utils.reversed(234)
    print(int_test)
except:
    print("reversed function doesn't support integer input")
    
try:
    float_test = utils.reversed(2.34)
    print(float_test)
except:
    print("reversed function doesn't support float input")   

# Test formatter
try:
    str_test = utils.formatter('234')
    print(str_test)
except:
    print("reversed function doesn't support string input")
    
try:
    int_test = utils.formatter(234)
    print(int_test)
except:
    print("reversed function doesn't support integer input")
    
try:
    float_test = utils.formatter(2.34)
    print(float_test)
except:
    print("reversed function doesn't support float input")     