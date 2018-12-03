"""
Unit test script for Lab 8

Authors: Walker M. White (wmw2), Lillian Lee (ljl2)
Date:    October 10, 2017 (Python 3 Version)
"""
import cornell
import lab08


def test_numberof():
    """
    Tests for function numberof
    """
    mylist = [5, 3, 3455, 74, 74, 74, 3]
    cornell.assert_equals(0, lab08.numberof([],4))
    cornell.assert_equals(1, lab08.numberof([4],4))
    cornell.assert_equals(3, lab08.numberof(mylist,74))
    cornell.assert_equals(2, lab08.numberof(mylist,3))
    cornell.assert_equals(0, lab08.numberof(mylist,4))


def test_replace():
    """
    Tests for function replace
    """
    mylist = [5, 3, 3455, 74, 74, 74, 3]
    cornell.assert_equals([],  lab08.replace([], 1, 2))
    cornell.assert_equals([4], lab08.replace([5],5,4))
    cornell.assert_equals([5, 20, 3455, 74, 74, 74, 20], lab08.replace(mylist,3, 20))
    cornell.assert_equals([5, 3, 3455, 74, 74, 74, 3],   lab08.replace(mylist, 1, 3))
    
    # test for whether the code is really returning a copy of the original list
    cornell.assert_equals([5, 3, 3455, 74, 74, 74, 3], mylist)
    cornell.assert_equals(False, mylist is lab08.replace(mylist, 1, 3))


def test_remove_dups():
    """
    Tests for function remove_dups
    """
    mylist = [1,2,2,3,3,3,4,5,1,1,1]
    cornell.assert_equals([],  lab08.remove_dups([]))
    cornell.assert_equals([3], lab08.remove_dups([3,3]))
    cornell.assert_equals([4], lab08.remove_dups([4]))
    cornell.assert_equals([5], lab08.remove_dups([5, 5]))
    cornell.assert_equals([1,2,3,4,5,1], lab08.remove_dups(mylist))
    
    # test for whether the code is really returning a copy of the original list
    cornell.assert_equals([1,2,2,3,3,3,4,5,1,1,1], mylist)
    cornell.assert_equals(False, mylist is lab08.remove_dups(mylist))


def test_oddsevens():
    """
    Tests for function oddsevens
    """
    mylist = [1,2,3,4,5,6]
    cornell.assert_equals([],     lab08.oddsevens([]))
    cornell.assert_equals([3],    lab08.oddsevens([3]))
    cornell.assert_equals([3,4],  lab08.oddsevens([4,3]))
    cornell.assert_equals([-1,1,2,0],    lab08.oddsevens([-1,0,1,2]))
    cornell.assert_equals([1,3,5,6,4,2], lab08.oddsevens(mylist))
    
    # test for whether the code is really returning a copy of the original list
    cornell.assert_equals([1,2,3,4,5,6], mylist)
    cornell.assert_equals(False, mylist is lab08.oddsevens(mylist))


### OPTIONAL EXERCISES ###

# Sequences Examples #

def test_number_not():
    """
    Tests for function number_not
    """
    mylist = [5, 3, 3455, 74, 74, 74, 3]
    cornell.assert_equals(0, lab08.number_not([],4))
    cornell.assert_equals(0, lab08.number_not([4],4))
    cornell.assert_equals(4, lab08.number_not(mylist,74))
    cornell.assert_equals(5, lab08.number_not(mylist,3))
    cornell.assert_equals(7, lab08.number_not(mylist,4))


def test_remove_first():
    """
    Tests for function remove_first
    """
    cornell.assert_equals([],  lab08.remove_first([],3))
    cornell.assert_equals([],  lab08.remove_first([3],3))
    cornell.assert_equals([3], lab08.remove_first([3],4))
    cornell.assert_equals([3, 4, 4, 5],    lab08.remove_first([3, 4, 4, 4, 5],4))
    cornell.assert_equals([3, 5, 4, 4, 4], lab08.remove_first([3, 4, 5, 4, 4, 4],4))
 

def test_histogram():
    """
    Tests for function histogram
    """
    cornell.assert_equals({}, lab08.histogram(''))
    cornell.assert_equals({'a':1}, lab08.histogram('a'))
    cornell.assert_equals({'a':1,'b':1,'c':1}, lab08.histogram('abc'))
    cornell.assert_equals({'a':3}, lab08.histogram('aaa'))
    cornell.assert_equals({'s':1, 'a':1, 'm':1, 'p':1, 'l':1, 'e':1}, lab08.histogram('sample'))
    cornell.assert_equals({'a':5, 'b':2, 'c':1, 'd':1, 'r':2}, lab08.histogram('abracadabra'))


def test_flatten():
    """
    Tests for function flatten
    """
    cornell.assert_equals([],  lab08.flatten([]))
    cornell.assert_equals([3], lab08.flatten([3]))
    cornell.assert_equals([3], lab08.flatten([[3]]))
    cornell.assert_equals([1,2,3,4], lab08.flatten([[1,2],[3,4]]))
    cornell.assert_equals([1,2,3,4,5,6,7], lab08.flatten([[1,[2,3]],[[4,[5,6]],7]]))
    cornell.assert_equals([1,2,3], lab08.flatten([1,2,3]))
    cornell.assert_equals([],  lab08.flatten([[[]],[]]))


def test_sum_list():
    """
    Tests for function sum_list
    """
    cornell.assert_equals(0,  lab08.sum_list([]))
    cornell.assert_equals(34, lab08.sum_list([34]))
    cornell.assert_equals(46, lab08.sum_list([7,34,1,2,2]))


def test_sum_to():
    """
    Tests for function sum_to
    """
    cornell.assert_equals(1,  lab08.sum_to(1))
    cornell.assert_equals(6,  lab08.sum_to(3))
    cornell.assert_equals(15, lab08.sum_to(5))


def test_num_digits():
    """
    Tests for function num_digits
    """
    cornell.assert_equals(1, lab08.num_digits(0))
    cornell.assert_equals(1, lab08.num_digits(3))
    cornell.assert_equals(2, lab08.num_digits(34))
    cornell.assert_equals(4, lab08.num_digits(1356))


def test_sum_digits():
    """
    Tests for function sum_digits
    """
    cornell.assert_equals(0,  lab08.sum_digits(0))
    cornell.assert_equals(3,  lab08.sum_digits(3))
    cornell.assert_equals(7,  lab08.sum_digits(34))
    cornell.assert_equals(12, lab08.sum_digits(345))


def test_number2():
    """
    Tests for function number2
    """
    cornell.assert_equals(0, lab08.number2(0))
    cornell.assert_equals(1, lab08.number2(2))
    cornell.assert_equals(2, lab08.number2(232))
    cornell.assert_equals(0, lab08.number2(333))
    cornell.assert_equals(3, lab08.number2(234252))


def test_into():
    """
    Tests for function into
    """
    cornell.assert_equals(0, lab08.into(5, 3))
    cornell.assert_equals(1, lab08.into(6, 3))
    cornell.assert_equals(2, lab08.into(9, 3))
    cornell.assert_equals(2, lab08.into(18, 3))
    cornell.assert_equals(4, lab08.into(3*3*3*3*7,3))


# Script Code
if __name__ == '__main__':
    test_numberof()
    test_replace()
    test_remove_dups()
    test_oddsevens()
    
    # UNCOMMENT ANY OPTIONAL ONES YOU DO
    #test_number_not()
    #test_remove_first()
    #test_sum_list()
    #test_histogram()
    #test_flatten()
    #test_sum_to()
    #test_num_digits()
    #test_sum_digits()
    #test_number2()
    #test_into()
    print('Module lab08 is working correctly')