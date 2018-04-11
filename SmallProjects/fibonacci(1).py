def fib(x):
  #find the largest fib no. smaller than x and the smallest fib no. larger than x
  if (x<=0):
    return "none"
    
  prev=0
  cur=1
  while True:
    next=prev+cur
    subs=prev
    prev=cur
    cur=next
    if (cur>x):
      if (x==prev):
        return subs,cur
      if (x>prev):
        return prev,cur
    

print (fib(9))
