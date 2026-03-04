"""

def print_numbers(n):
    for i in range(1,n+1):
        print(i)
def main():
    n=int(input("enter the number:"))
    prime_numbers(n)

__name__=="___main___"
    
main()





def calculate_sum(n):
    total=0
    for i in range(1, n+1):
        total+=i
    return total



#sum of numbers

def main():
    n=int(input("enter the number:"))
    result= calculate_sum(n)
    print("sum of numbers up to ", n ,"is", result)

if __name__=="__main__":
        main()
"""




"""

def Find_minimum(arr):
    minimum=arr[0]

    for i in range(1,len(arr)):
        if arr[i] < minimum:
            minumum=arr[i]
            
    return minimum 



# finnd miinimum number

def find_minimum(arr):
    
    minimum = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]
    return minimum       

arr=[2,3,5,1]
result=find_minimum(arr)
print(result)


# find max number

def find_maximum(arr):
    maximum=arr[0]
    for num in arr:
        if num > maximum:
            maximum = num
    return maximum            
arr=[1,2,4,5,8]
result=find_maximum(arr)
print(result)


#count of even numbers

def count_even(arr):
    count=0
    for i in arr:
        if i%2==0:
            count+=1
    return count
arr=[1,2,3,4,5,6,7,8,9]
result=print(count_even(arr))
"""

#reverse of array
def reverse_arr(arr):
    left=0
    right=len(arr)-1

    while left<right:
       arr[left],arr[right]=arr[right],arr[left]
       left+=1
       right-=1
        
    return arr

arr=[1,2,3,4,5,6]
print(reverse_arr(arr))

























