x= 10
if x>5:
    x = x * 2
else:
    x = x + 5
ENDIF

if x >= 15:
    x = x - 5
ENDIF
#What is the output of the following block?
status ="Member"
total = '100'

if status == "Member" and total >= 100:
    print("Discount Applied")
ELSE if status == "Member" OR total > 150 THEN
    print("Partial Discount")
else:
    print("No Discount")
ENDIF
#What is the value of result?
SET a = 5, b = 10, c = 15

if(a < b AND b > c) OR (c > a):
    SET result = "Condition A"
else:
    SET result = "Condition B"
ENDIF
#Evaluate the final value of score:
score = 50
if score != 50 THEN
    score = 0
else:
if score >= 50 THEN
        score = score + 10
    ENDIF
ENDIF
#What does this program print?
SET temperature = 30

if temperature > 25 THEN
    if temperature > 35 THEN
        print("Extreme Heat")
    else:
        print("Warm")
    ENDIF
else:
    print("Cool")
ENDIF
#How many times will "Hello" be printed?
FOR i FROM 1 TO 5
    FOR j FROM 1 TO 2
        PRINT "Hello"
    ENDFOR
ENDFOR
#What is the final value of sum?
SET sum = 0
SET k = 1

WHILE k < 5
    sum = sum + k
    k = k + 1
ENDWHILE
#What is the output of this loop?
SET count = 10

WHILE count > 0
    count = count - 3
ENDWHILE

PRINT count
# Trace the value of n:
SET n = 1

FOR i FROM 1 TO 4
    n = n * 2
ENDFOR
# What is the final value of x?
SET x = 0

FOR i FROM 1 TO 10
    IF i % 3 == 0 THEN
        x = x + 1
    ENDIF
ENDFOR
#What is the final value of total?
SET total = 0

FOR i FROM 1 TO 3
    FOR j FROM i TO 3
        total = total + 1
    ENDFOR
ENDFOR
The Step Counter

#Write a program that calculates the total distance walked over a set number of days.
The user provides the number of days and the steps taken each day.
For every 1,000 steps, the distance increases by 0.8 kilometers.

Test Case 1:
Input: Days = 2, Steps = [5000, 3000]
Output: 6.4 km

Test Case 2:
Input: Days = 1, Steps = [10000]
Output: 8.0 km

Problem 12: Finding the Evens

Given a starting number and an ending number, print how many even numbers exist within that inclusive range.

Test Case 1:
Input: Start = 1, End = 10
Output: 5

Test Case 2:
Input: Start = 7, End = 11
Output: 2
The Factorial Finder
#Write a program that takes a non-negative integer N and calculates its factorial (N!).
Note: 0! is defined as 1.

Test Case 1:
Input: N = 4
Output: 24

Test Case 2:
Input: N = 6
Output: 720
The "FizzBuzz" Sum
#Write a program that looks at all numbers from 1 to N:
If divisible by 3  add to sum
If divisible by 5 add to sum
If divisible by both  ignore

Print the absolute difference between sum and sum

Test Case:
Input: N = 10
Output: 3
The Square Border
#Write a program that takes an integer N and prints an N × N square of asterisks (*), but only the border.
The inside should be empty (spaces).

Test Case:
Input: N = 4

Output:

* * * *
*     *
*     *
* * * *

