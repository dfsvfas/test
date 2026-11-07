# -*- coding:utf-8 -*-
"""
奶茶点单
========
奶茶店的点单程序。前三杯已经定好，第 4 杯从键盘读入。
每一杯写成「杯型 甜度 饮品」，按杯型算价钱，最后打出合计和叫号。

前三杯：
    第 1 杯  珍珠奶茶，杯型和甜度都用默认的
    第 2 杯  杨枝甘露，超大杯
    第 3 杯  生椰拿铁，小杯，三分糖

运行后应看到（样例：第 4 杯输入 芋泥波波，杯型直接回车）：

    第4杯喝什么：芋泥波波
    杯型（直接回车就是中杯）：

    ══════ 奶茶点单 ══════
    1. 中杯 七分糖 珍珠奶茶 15 元
    2. 超大杯 七分糖 杨枝甘露 21 元
    3. 小杯 三分糖 生椰拿铁 12 元
    4. 中杯 七分糖 芋泥波波 15 元
    合计：63 元
    请 12 号取餐
    call_number 的返回值： None

第 4 杯的杯型输入 大杯，第 4 行应是「4. 大杯 七分糖 芋泥波波 18 元」，合计 66 元。

函数清单（名字照写）：
1. make_cup(drink, size="中杯", sugar="七分糖")
   return「杯型 甜度 饮品」这一句。make_cup("珍珠奶茶") 是「中杯 七分糖 珍珠奶茶」。
2. cup_price(size="中杯")
   小杯 12 元，中杯 15 元，大杯 18 元，超大杯 21 元。return 价钱。
3. call_number(no)
   只 print「请 12 号取餐」这样一句。不要写 return。

要求：
1. 三个函数写在最上面，点单写在它们下面。还没定义就调用，会报 NameError。
2. 第 1 杯只传饮品名。第 2 杯传饮品名和杯型。第 3 杯三项都传。
3. 第 4 杯用 input 读入饮品名和杯型。杯型直接回车时，input 拿到的是空字符串 ""，这时只传饮品名，用默认的中杯。
4. 合计 = 四杯价钱相加。样例应是 63。
5. 最后写 result = call_number(12)，再打印 result。call_number 没有 return，所以打出来是 None。
"""
# TODO ① 定义 make_cup、cup_price、call_number
def make_cup(drink,size="中杯", sugar="七分糖"):
    return size+"  "+drink+"  "+sugar

def cup_price(size="中杯") :
    if size=="小杯":
        return 12
    elif size=="大杯":
        return 18
    elif size=="超大杯":
        return 21
    else:
        return 15

def call_number(no):
   print("请"+str(no)+"号取餐")
total_price=cup_price()+cup_price("超大杯")+cup_price("小杯")+cup_price()

# TODO ② 读入第 4 杯的饮品名和杯型
drinks=input("点单：")
types=input("杯型：")

if types=="":
    cup4 = make_cup(drinks)
    price4 = cup_price()

else:
    cup4 = make_cup(drinks,types )
    price4 = cup_price(types)

 # TODO ③ 打印四杯和合计
print("=" * 6+"奶茶点单"+"=" * 6)
print("1.",make_cup("珍珠奶茶"),cup_price(),"元")
print("2.",make_cup("杨枝甘露","超大杯"),cup_price("超大杯"),"元")
print("3.",make_cup("生椰拿铁","小杯","三分糖"),cup_price("小杯"),"元")
print("4.", cup4 ,price4,"元")
total_price=cup_price()+cup_price("超大杯")+cup_price("小杯")+price4
print("合计："+str(total_price),"元")

# TODO ④ 调用 call_number(12)，打印它的返回值
result = call_number(12)
print(result)
#