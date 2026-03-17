"""
try:
    num=int(input("enter the number:"))
    result=10 /num
    print("Result:", result)
    
except ZeroDivisionError:
    print("Error: cannot divide by 0")
except ValueError:
    print("Incorrect value")
finally:
    print("program ended")




#printing even and odd

    
def check_num(n):
    if n% 2 == 0:
        print("Even number")
    else:
        print("Odd number")
        
def main():
    n= int(input("enter the number:"))
    check_num(n)
main()


#check maximum number

def find_maximum(arr):
    maximum=arr[0]
    for num in arr:
        if num > maximum:
            maximum = num
    return maximum            
arr=[1,2,4,5,567]
result=find_maximum(arr)
print(result)


num1=int(input("enter the number:"))
num2=int(input("enter the number:"))
if num1 > num2:
    print(f"{num1} is maxuimum")
else:
    print(f"{num2} is maximum")

"""




def exam(marks):
    if marks > 90:
        print("O")
    elif marks >80:
        print("A+")
    elif marks > 70:
        prints("B+")
    elif marks >50:
        print("C")
    else:
        print("FAAAAAHHHHHHHHHH")
        
def main():
    marks=int(input("enter the marks:"))
    exam(marks)
main()




def fee_calculator(course,marks):
    course=course.strip().lower()

    if course == "AI":
        print("Fee:50000")
    elif course == "web":
        print("Fee:60000")
    elif course =="Data science":
        print("Fee:20000")

        if 



























