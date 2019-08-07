import factorial

def test_1():
    nine_factorial=362880  #expected value for 9!
    True_Val = factorial.fac1(9)
    assert nine_factorial==True_Val
    print("test_1 success")
    
def test_2():
    t=9
    assert factorial.fac2(t) == 362880
    print("test_2 success")
    return

def test_3():
    ten_factorial=3628800  #expected value for 10!
    True_Val = factorial.fac3(10)
    assert ten_factorial==True_Val
    
    t=10
    assert factorial.fac3(t) == 3628800
    print("test_3 success")
    return
    
    
test_1()
test_2()
test_3()