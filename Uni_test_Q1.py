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
