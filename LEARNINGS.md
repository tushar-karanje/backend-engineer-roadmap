
Day 2:

Q1: A
Because we are printing A+B but not returning it hence x will be None

Q2: None
Because we are not returning anything.

Q3 : 10
We are printing the value of x outside function fun(). Hence the global value will be printed

Q4. [1,2,10]
Yes, because we are providing list named "numbers" as an argument and lst is the parameter. hence 10 will get appended to numbers

Q5.
I guess "def calculate(employee):" is better due to following reasons:
1. Readability : with calculate employee code is more readable and makes more sense that the function will take some employee related info as parameters
2. As everything is object in the Python, we can just add attributes to a object and send it as an argument
3. Maintainability : As there are less number of parameters, it is easier to maintain.



Problem:
def change(lst):
    lst.append(100)

numbers = [1, 2, 3]

change(numbers)

print(numbers)


Prediction


Why :
Because number is a list and we are sending it as an argument. lst is a parameter which has type list, so function change will add 100 to lst which is nothing but the reference of numbers

Prediction :
Output?
[1,2,3,100]

Reason
Why?

Because number is a list and we are sending it as an argument. lst is a parameter which has type list, so function change will add 100 to lst which is nothing but the reference of numbers


Confidence

8/10.