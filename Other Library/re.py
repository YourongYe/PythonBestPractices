# 在string中找到所有符合某种pattern的字符，并且以list形式返回
re.findall(r'\d.\d\d', string)
example：
string = '我今天拿了100.23元出门，花了55.33元'
re.findall(r'\d.\d\d', string) # 会返回['100.23', '55.33']

# 在string中找到所有符合pattern的字符，然后用repl代替，并返回
re.sub(pattern, repl, string, count=0, flags=0)
example:
string = '100abc'
re.sub("\D", "", string) # \D表示非数字的字符，此处会返回‘100’
