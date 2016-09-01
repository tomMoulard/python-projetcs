#-*-coding:utf8;-*-
#qpy:3
#qpy:console
#made by moular_b

def powPlusUn(x, alpha):
    po, div, res = x, 1, 1
    for i in range (1, 43):
        print(res)
        res += (alpha * po) / div
        alpha *= (alpha - i)
        po *= x
        div *= i
    return res
x = int(input("x = "))
alpha = int(input("alpha = "))
print(powPlusUn(x, alpha))