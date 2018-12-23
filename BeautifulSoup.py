# 打开HTML文件，后面的'lxml'可以自己设置读取方式
soup = BeautifulSoup(open("Tencent_data/222.htm"),'lxml')

# 找节点
node = soup.find('div', 'box-etf') #此处会找到<div class="box-etf">这整个section并返回
node = soup.find_all(name='p',attrs={"class":"num"}) #不同的写法
node = soup.find(text="9000098") #也可以用text来查找，但是必须完全一致才能找到；会直接返回定位到的文字，然后可以用find_parent反查找
node1 = node.find_parent('div','c-box') #可以找到上段文字的第一个符合要求的父节点
text = parent_node.find_next('p','num').get_text() #下一个最近的符合参数的目标，并拿到text的内容
float_pnl_list = self.soup.select('p[class="num f-red"]') #select和find的用法类似，但可以多重导向定位；这里寻找的是<p class="num f-red">
float_pnl_list = self.soup.select('p [class="num f-red"]') #和上面的结果可能完全不同，寻找的是<p>里面的<span class="num f-red">
soup.select('div [class="float-l"] > span') #寻找的是div里的class="float-l"里面的span

# 返回节点和list的区别
find_all，select 和 find_parents 返回的是所有符合要求的节点组成的list
find 是在当前节点的子树里寻找第一个符合要求的节点，find_next是在当前节点往后找第一个符合要求的节点
find_sibling 是在当前节点的兄弟节点中找第一个符合要求的节点

# text的处理
text = parent_node.find_next('p','num').get_text() #get_text()返回的是当前节点内所有的文字内容，以string形式，空格隔开
比如：<span>泰康养老汇选悦泰 <b>9000054</b></span>
会得到：'泰康养老汇选悦泰 9000054'
split_txt = txt.split(' ')
txt1 = split_txt[0]




