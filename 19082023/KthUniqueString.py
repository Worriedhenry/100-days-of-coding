# Ashish is provided with a collection of n strings in which some strings are of repeating nature but he has been given with a number k. His task is to find the kth unique string. Also before finding the kth unique string he has to sort each individual string beforehand. If there are fewer unique strings than k return empty string. As his best friend, your task is to help Ashish in accomplishing the task.

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
arr=[]
for i in range(n):
  s=input()
  # res = ''.join(sorted(s))
  arr.append(s)
k=int(input())
vis=[]
for a in arr:
  if arr.count(a)==1:
    k-=1
    if not k:
      print(a)
      break
print("")
    

