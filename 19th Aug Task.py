def is_valid_triangle(s1,s2,s3):
    if (s1 + s2 > s3) and (s2 + s3 > s1) and (s3 + s1 > s2) :
        print('Can form a valid Triangle')
        if s1 == s2 == s3:
            print('Equalateral Triangle')
        elif s1 == s2 or s2 == s3 or s3 == s1:
            print('Isosceles Triangle')
        else:
            print('Scalen Triangle')
        if (s1^2 + s2^2 == s3^2) or (s2^2 + s3^2 == s1^2) or (s1^2 + s3^2 == s2^2):
            print('Right angled Triangle')
        else:
            print('Not a right angled triangle')
    else:print ('Can not form a valid Triangle')
s1=int(input('Enter side1:'))
s2=int(input('Enter side2:'))
s3=int(input('Enter side3:'))
print(is_valid_triangle(s1,s2,s3))