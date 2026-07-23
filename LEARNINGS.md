Day 4:




Day 3:

Exercise 1:
employees is a list object.
Yes I can append,search and remove elements from list.
If I append Tushar again, it will allow because list allows duplicate elements.

Exercise 2:
employees is a set object.
Set is like list but the only difference is that set does not allow duplicates
If we try to append "Tushar" again in set, it will not throw any error but it will not insert "Tushar" again as it is already present in employees


Exercise 3:
employees is a dict object.
employees[2] will be 'Amit'

Reason why searching in a dict is faster than lists is because list starts element from the 0th index and it has to gone through end if element is not present.
If list is having small number of elements like 10-50 then we will not be able to see any difference but if list is having millions of records and if we provide any element which is either at last or not present , then search will be inefficient.
Also, list allows duplicates, due to this also list become inefficient to search the elements




Interview Questions
Q1.

Predict:
Output : {'Tushar', 'Amit'}

Reason:
Because employees is the set object. 
Sets does not allow duplicates.


Q2.

Predict:
Output: 400000

Complexity : average O(1) 
Note : I don't know how to calculate the complexity. But yes I want to learn it.



Complexity for 
number.pop(0)

I am bit confused here.
I think here pop function will act as remove function but with index.
So I believe, the complexity will be O(n) , because if we remove 0th element, all other elements needs to be placed again by reducing the index by 1. Due to which python needs to work a lot.

Also another possibility is that pop(0) will remove first element. Hence, python knows the current size of list "numbers", so it may simply moves 0th for the next memory location



 



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