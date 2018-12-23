# 打开HTML文件，后面的'lxml'可以自己设置读取方式
soup = BeautifulSoup(open("Tencent_data/222.htm"),'lxml')

# 找节点
node = soup.find('div', 'box-etf') #此处会找到<div class="box-etf">这整个section并返回
node = soup.find(text="9000098") #也可以用text来查找，但是必须完全一致才能找到；会直接返回定位到的文字，然后可以用find_parent反查找
node1 = node.find_parent('div','c-box') #可以找到上段文字的第一个符合要求的父节点

# 返回节点和list的区别
find_all 和 find_parents 返回的是所有符合要求的节点组成的list
find 是在当前节点的子树里寻找第一个符合要求的节点，find_next是在当前节点往后找第一个符合要求的节点

