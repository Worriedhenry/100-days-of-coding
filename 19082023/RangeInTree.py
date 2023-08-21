# You are given the root of the Binary Search Tree. You are also provided integers start and end.

# You have to return the sum of all the nodes that lie in the inclusive range of start and end.

# All the values in the tree are unique
# https://unstop.com/code/challange-asesment/250874?moduleId=372

n=int(input())
arr=list(map(int,input().split()))
rang=list(map(int,input().split()))
count=0
for i in arr:
  if i>=rang[0] and i<=rang[1]:
    count+=i
print(count)