
import re 

# """Decode
#     >>> decipher_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka")
#     "A wise old owl lived in an oak"
# """


def decipher_this(string):
    word_list = string.split(' ')
    nums = []
    for words in word_list:
        for n in words:
            if n.isnumeric() ==  True:
                print(n)

    temp = re.compile("([a-zA-Z]+)([0-9]+)") 
    res = temp.match(string).groups() 
    print(res)
    
decipher_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka")





# Test.assert_equals(decipher_this("65 119esi 111dl 111lw 108dvei 105n 97n 111ka"), "A wise old owl lived in an oak")
# Test.assert_equals(decipher_this("84eh 109ero 104e 115wa 116eh 108sse 104e 115eokp"), "The more he saw the less he spoke")
# Test.assert_equals(decipher_this("84eh 108sse 104e 115eokp 116eh 109ero 104e 104dare"), "The less he spoke the more he heard")
# Test.assert_equals(decipher_this("87yh 99na 119e 110to 97ll 98e 108eki 116tah 119esi 111dl 98dri"), "Why can we not all be like that wise old bird")
# Test.assert_equals(decipher_this("84kanh 121uo 80roti 102ro 97ll 121ruo 104ple"), "Thank you Piotr for all your help")

# if __name__ == '__main__':
#     import doctest
#     if doctest.testmod().failed == 0:
#         print("\n*** ALL TESTS PASSED ***\n")