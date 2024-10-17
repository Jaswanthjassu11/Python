# from python2 import reverse
#
# name = "String in doub'le quote"
#
# name2 = 'string in single quote'
#
# print(name)
#
# print(name[0])    #  accessing element through indexing
# print(len(name))  # -- length of the string- how many charcarers in a string
#
# print(name[-1])
#
#
# print(name[:23])
#
#
# name = "jaswanth"
# length = len(name)
# print(length)
# print(name[:8])
#
#
# print(name[::-1])
#
#
# #   built in functions
#
# #   1.reversed
#
# new_name = "".join(reversed(name))
# print(new_name)
#
#
# new_str = ""



def search(arr1, n1):
    sum_n = (n1 * (n1 +1))//2

    for num in arr1:
        sum_n -= num
    print(sum_n)

arr = [1, 2, 3, 4, 6]
n = 6
search(arr, n)
