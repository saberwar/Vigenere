import sys
# 字母表
world = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# 引入密文
passStr = "OCWYIKOOONIWUGPMXWKTZDWGTSSAYJZWYEMDLBNQAAAVSUWDVBRFLAUPLOOUBFGQHGCSCMGZLATOEDCSDEIDPBHTMUOVPIEKIFPIMFNOAMVLPQFXEJSMXMPGKCCAYKWFZPYUAVTELWHRHMWKBBNGTGUVTEFJLODFEFKVPXSGRSORVGTAJBSAUHZRZALKWUOWHGEDEFNSWMRCIWCPAAAVOGPDNFPKTDBALSISURLNPSJYEATCUCEESOHHDARKHWOTIKBROQRDFMZGHGUCEBVGWCDQXGPBGQWLPBDAYLOOQDMUHBDQGMYWEUIK"
# 计算密文长度
passStr_len = len(passStr)
# 设定猜测密钥长度
n = 6
print("秘钥长度为:",n)
# 分解源字符串,并按行存储
str_list = []
# 开始分解
#记录坐标
x = 0
while x<passStr_len:
    line = [] #记录每一行
    line.append(passStr[x:x+n])
    x+=n
    str_list.append(line)
# 计算重合指数,计算每列重合指数，以及平均重合指数
ic = []
# 如果最后一行不够n ，则不计入
m = 0  #列数
if passStr_len % n !=0:
    m = len(str_list)-1
else:
    m = len(str_list)
#按给定n,按列分解
col = []
for x in range(0,n):
    c = []  #记录每一列

    for y in range(0,m):
        c.append(str_list[y][0][x])
    col.append(c)

#循环计算重合指数
for x in range(0,n):
    col_ic = 0
    up = 0
    for y in range(0,26):
        float_m = float(m)
        up+= (col[x].count(world[y])*(col[x].count(world[y])-1))
    col_ic=up/(float_m*(float_m-1))
    ic.append(col_ic)
#计算平均ic
sum=0
for z in ic:
    sum+=z
ave = sum/n
print("平均重合指数为：",ave)
# 计算秘钥
f_world = [0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015, 0.06094, 0.06966, 0.00153, 0.00772, 0.04025,
         0.02406, 0.06749, 0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758, 0.00978, 0.02360, 0.00150,
         0.01974, 0.00074]
# 拟重合指数
count = [] # 记录字符出现次数
reic = []
passKey = []
for cv in range(0,6):
    p =[]
    for v in range(0,26):
        p.append(col[cv].count(world[v]))
    count.append(p)
for time in range(0,n):
    for hy in range(0, 26):
        re_ic = 0
        for hj in range(0, 26):
            if (hj + hy) < 26:
                re_ic += (count[time][hj + hy] * f_world[hj]) / m
            else:
                re_ic += (count[time][hj + hy - 26] * f_world[hj]) / m
        reic.append(re_ic)

    #print(reic.index(max(reic)))
    passKey.append(reic.index(max(reic)))
    reic=[]
print("秘钥为：",passKey)
# 开始翻译
text=""
for len_x in range(0,m):
    for len_y in range(0,n):
        index_w=world.index(str_list[len_x][0][len_y])-passKey[len_y]
        if index_w<0:
            text+=world[index_w+26]
        else:
            text+=world[index_w]
print("明文为：",text.lower())








'''for cv in range(0,6):
    p =[]
    for v in range(0,26):
        p.append(col[cv].count(world[v]))
    count.append(p)
for hy in range(0,26):
    re_ic = 0
    for hj in range(0,26):
       if (hj+hy)<26:
            re_ic += (count[2][hj+hy] * f_world[hj]) / m
       else:
           re_ic += (count[2][hj + hy-26] * f_world[hj]) / m
    reic.append(re_ic)
print(reic.index(max(reic)))'''






















