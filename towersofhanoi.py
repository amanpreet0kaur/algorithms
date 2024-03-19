import random
import time
import matplotlib.pyplot as plt
listx=[]
listy=[]
def selection_sort(arr, n):
  for ind in range(n):
    min=ind
    for j in range(ind+1,n):
       if arr[j] < arr[min]:
                min = j
         # swapping the elements to sort the array
                (arr[ind], arr[min]) = (arr[min], arr[ind])
  return arr
def towers(x,f,u,t):
  if(n>=1):
    towers(n-1,f,t,u)
    print("move")
    towers(n-1,u,f,t)


def random_generator(n):
  arr=[0]*n
  a=1
  for i in range(n):
    arr[i]=(random.randint(a, n))
  return arr

n=3
while(n<=3):
  arr=random_generator(n)
  t_start= time.time()
  for i in range (10):
    towers(n,1,2,3)
  t_end=time.time()
  avg_time=(t_end-t_start)/10
  print(avg_time, n)
  listx.append(avg_time*1000)
  listy.append(n)
  n=n+1

plt.scatter(listy,listx)
