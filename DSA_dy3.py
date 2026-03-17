"""
#count of even 
def count_even(n):
    count = 0
    for i in range(1,n+1):
        if i % 2 != 0:
            count += 1
    
    return count

n =int(input("enter the number:"))
print(count_even(n))





#countof positive numbers
def count_positive(numbers):
    count=0
    for num in numbers:
        if num > 0:
            count+=1
    return count
numbers=[1,2,3,-2,-4,5]
print(count_positive(numbers))

#linarsearch
def search_index(arr, target):
    for i in range(len(arr)):
        
        if arr[i]== target:
            return i
    else:
         return ("-1")
arr=[1,2,3,5,8]
print(search_index(arr,8))
    

def search_index(arr,target):
    for index ,value in enumerate(arr):
        if value == target:
            return index
    else:
        return("-1")
arr=[1,2,3,4,6,9]
print(search_index(arr,9))
"""

#













