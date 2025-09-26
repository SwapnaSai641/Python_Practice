def check_prime(num1):
    if num1 < 2:
        return False
    
    for i in range(2,int(num1**0.5)+1):
        if num1 % i == 0:
            return False
        
    return True

start=int(input('Enter starting range'))
end=int(input('Enter end range'))

for i in range(start,end+1):
    if check_prime(i):
        print(i)




