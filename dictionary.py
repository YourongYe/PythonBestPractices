d = {}
d[12345] = "yoyo"
d[242] = "mincong"
d[33] = "someone"

print(d)

num = 242
if num in d:
  print(d[242])
  
d = {1:"people1",2:"people2"}
d[12345] = "yoyo"
d[242] = "mincong"
d[33] = "someone"

print(d)

num = 242
if num in d:
  print(d[242])

num = 242
if num in d:
  print(d[num])
  
  
random_num = 1111111111
if random_num not in d:
  print(str(random_num)+" is not in the dictionary")
  
random_num = 0
if random_num not in d:
  print(str(random_num)+" is not in the dictionary")
  
  
d1 = {}
d1["APPL"] = "apple"
d1["GOOGL"] = "google"
d1["AMZN"] = "amazon"
d1["NFLX"] = "netflix"
d1["FB"] = "facebook"

print (d1["APPL"],d1["GOOGL"],d1["AMZN"])

if "BABA" not in d1:
  print("BABA is not in the dictionary")
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
