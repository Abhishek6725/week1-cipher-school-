n=5
for i in  range(n):
  for j in range(n):
    print(i,end=" ")
  print()

n=5
for i in  range(n):
  for j in range(n):
    print(i,end=" ")
  #print()

n=5
for i in  range(n):
  for j in range(n):
    print(i,end=" ")
  print('\n')

n=5
for i in  range(n):
  for j in range(n):
    print(j,end=" ")
  print()

n=5
for i in  range(n):
  for j in range(n):
    print(max(i,j),end=" ")
  print()

#n-i is giving distance from bottom
n=5
for i in  range(n):
  for j in range(n):
    print(n-i,end=" ")
  print()

#n-j is giving distance from right 
n=5
for i in  range(n):
  for j in range(n):
    print(n-j,end=" ")
  print()

n=5
for i in  range(n):
  for j in range(n):
    print(max(n-i,n-j),end=" ")
  print()

#i+1 is giving distance from bottom
n=5
for i in  range(n):
  for j in range(n):
    print(i+1,end=" ")
  print()

#j+1 is giving distance from right 
n=5
for i in  range(n):
  for j in range(n):
    print(j+1,end=" ")
  print()

n=5
for i in  range(n):
  for j in range(n):
    print(n-i-1,end=" ")
  print()

n=5
for i in  range(n):
  for j in range(n):
    print(n-j-1,end=" ")
  print()

n=5
for i in  range(n):
  for j in range(n):
    print(max(n-i-1,n-j-1),end=" ")
  print()

"""#write the question for these solution"""

#ist method
n=5
for i in  range(n):
  for j in range(n):
    print(max(i+1,j+1,n-i,n-j),end=" ")
  print()

#2nd method
n=5
for i in  range(n):
  for j in range(n):
    print(max(max(i+1,j+1),max(n-i-1+1,n-j-1+1)),end=" ")
  print()

"""#write the question for these solution"""

n=7
for i in  range(n):
  for j in range(n):
    print(max(i+1,j+1,n-i,n-j),end=" ")
  print()

n=7
for i in  range(n):
  for j in range(n):
    print((i,j),end=" ")
  print()

#sum doesn't take n number of output
#print(sum(1,2,3,4,5,6,7,8,9,0))

#sum take an array
print(sum([1,2,3,4,5,6,7,8,9,0]))
