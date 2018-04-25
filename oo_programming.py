Object-oriented programming （面向对象编程）是编程的一种方式，class就属于OO programming
其他的方式还有函数式（Eg.function）和面向过程（要进行运算操作的编程，比如main（）里的代码）

区别：OO programming是一种编程方式，class是一种代码方式，而dictionary是一种数据结构

class是框架，在创建一个object时需要定义一系列的参数。比如定义一个人：身高，年龄，体重，性别 等等这些参数加起来就构成class，这些参数就被封装在class中
class中可以有多种不同的数据结构:string,int,dictionary  等等。

一个class里面可以有很多很多object，在每个维度上设置不同的参数，组合起来就是不同的object
所有class就是框架，你写class的variables的时候就是在确定：定义一个object要有哪些参数

而且你还可以定义新的class封装已有的class，

比如一开始有 class student

class school 包含 student
class city 包含 school
class country 包含 city
