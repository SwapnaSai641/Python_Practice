#Built in functions of string

str1 = " swaPna"
print(str1.capitalize()) #converts first char to caps
print(str1.lower())  #converts all to lower case
print(str1.upper())  #converts all to upper
print(str1.swapcase()) #swaps upper to lower lower to upper
print(str1.title())


print(str1.count('d'))
print(str1.find('a')) #returns its first occured index -1 otherwise
print(str1.index('s')) #same as find but gives error if not present
print(str1.startswith('sa')) #gives op as true por false
print(str1.endswith('sa'))

print(str1.split())
print(str1.join('sai'))#.....

print(str1.splitlines('sa'))
print(str1.strip())

#Built in functions of sets

set1 = {5,7,9,4,2,1,6}
print(len(set1))
print(max(set1))
print(min(set1))
print(sum(set1))
print(sorted(set1))
list1=[3,8,9,5]
print(set(list1))

set1.add(10)
set1.update(list1)
set1.remove(10)
set1.discard(6)
set1.pop()
set1.clear

print(set1)










