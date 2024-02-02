'''Question text
Students have done two tests, each marked out of 50. Grades are awarded on the basis of the combined total (the scores on both tests added together) as follows:

 0 -  49  Fail
50 -  69  Pass
70 - 100  Distinction
A lecturer wishes to be able to put the students' marks into a computer, like this:

Next student (first test): 29
(second test): 34
Next student (first test): 13
(second test): 10
Next student (first test): 36
(second test): 45
(...)


and so on, ending with 51 and 51 to indicate the end of the data; and have the computer output the number of distinctions, the number of passes, and the number of failures, in that order. Write a Python program to do this. (You may assume that the lecturer enters the data correctly, i.e., all values are integers between 0 and 51.)
'''

#Question 1

count_distinctions=0
count_pass=0
count_fail=0

while True:

    first_test=int(input('Next student (first test): '))
    second_test=int(input('(second test): '))

    total_score = first_test + second_test
    
    if first_test==51:
        break
    
    if total_score>=70 and total_score<=100:
        count_distinctions=count_distinctions+1
           
    elif total_score>=50 and total_score<=69:
        count_pass=count_pass+1
        
    elif total_score>=0 and total_score<=49:
        count_fail=count_fail+1
        

print('\n')        
print('no of disctinctions: ', count_distinctions)
print('no of passes: ', count_pass)
print('no of failures: ', count_fail)