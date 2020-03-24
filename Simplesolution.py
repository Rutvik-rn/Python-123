import time

def treepalindrome():

    palindrometree = ['5000',[['9000',[],[]],['8000',[],[]],['7000',[],[]],['6000',[],[]]],[['6000',[],[]],['7000',[],[]],['8000',[],[]],['9000',[],[]]]]
    print('Left side=', palindrometree[1])
    print('root=', palindrometree[0])
    print('right side=', palindrometree[2])


def CheckPalindrome(array):
    start_time = time.time()
    lengthofarray = int(len(array))
    for i in range(lengthofarray // 2):
        if array[i] != array[lengthofarray - 1 - i]:
            end_time = time.time()
            print("time=", end_time - start_time)
            return False
    else:
        start_time = time.time()
        treepalindrome()
        end_time = time.time()
        print("time=", end_time - start_time)
        return True


array1 = [1, 2, 3, 4, 2, 1]

array2 = [9000, 8000, 7000, 6000, 5000, 6000, 7000, 8000, 9000]

array3 = [99, 98, 97, 96, 95, 94]

array4 = [11, 22, 33, 44, 55, 66, 11]

array5 = [2, 3, 5, 7, 9]

print(CheckPalindrome(array1))
print("                     ")
print(CheckPalindrome(array2))
print("                     ")
print(CheckPalindrome(array3))
print("                     ")
print(CheckPalindrome(array4))
print("                     ")
print(CheckPalindrome(array5))



