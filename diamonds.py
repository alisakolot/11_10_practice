#  *
# ***
#  *
""" 
>>> diamond(3)
 *
***
 *

>>> diamond(5)
  *
 ***
*****
 ***
  *
"""

def diamond(n):
    # if n > 2 and n % 2 != 0:
    #     for n in range(n):
    #         if n % 2 == 0 :
    #             print('*' * (n+1))

    #ascending and descending list of numbers
    asc = []
    for x in range(n+1):
        if x % 2 != 0:
            asc.append(x)
    
    rev_lst = asc[::-1] + asc[1::]
    # print(rev_lst)
    lst = asc[:-1:] + asc[::-1]
    # print(lst)
    
    for n in lst:
        print(' ' * -(n-2) + "*" * n)
    
 
    # dstr = []
    # for n in rev_lst:
    #     print('#' * (n-1) + '*' * n)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n✨ ALL TESTS PASSED!\n')