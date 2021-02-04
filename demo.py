'''
name = '张三'
print(name)

res = (1+2+352/(4*2))%3
print(res)

input('请输入：')

b = ("麻麻","巴巴","二货")
a = (1,2,3,4,"哈哈","嘻嘻",None,True,b)
print(a[-1][2])
print(a[-1].index("二货"))

b = ("麻麻","巴巴","二货")
a = [1,2,3,4,"哈哈","嘻嘻",None,True,b]

name = input("请输入你的名字：")
a.append(name)
a.insert(3,name)
print(a)
c = ["今天","明天","后天"]
a.extend(c)
print(a)
'''

d = [2,5,7,9,1]
d.reverse()
d.remove(2)
print(d)
