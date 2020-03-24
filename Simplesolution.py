
def CheckPalindrome(array):
    lengthofarray = int(len(array))
    for i in range(lengthofarray // 2):
        if array[i] != array[lengthofarray - 1 - i]:
            return False
    else:
        return True


array1 = [1, 2, 3, 4, 2, 1]

array2 = [9000, 8000, 7000, 6000, 5000, 6000, 7000, 8000, 9000]

print(CheckPalindrome(array1))
print(CheckPalindrome(array2))




