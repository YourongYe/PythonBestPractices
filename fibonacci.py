#用for循环写fibonacci数列，计算不会重复
def fib(n):
  #print("getting fibonacci["+str(n)+"]")
  
  if(n<0):
    return 0
  if(n==0):
    return 0
  if(n==1):
    return 1
    
  n -= 2
  prev = 0 
  cur = 1 
  next = prev+cur
  while n>=0:
    next = prev+cur
    prev = cur
    cur = next
    n-=1
    
  return next
  
print(fib(9))

#函数自己调用（call）自己，递归（recursion），适用于递推数列
def fib2(n):
  #print("getting fibonacci["+str(n)+"]")
  
  if(n<0):
    return 0
  if(n==0):
    return 0
  if(n==1):
    return 1
    
  return fib2(n-1)+fib2(n-2)
  
print(fib2(6))
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
