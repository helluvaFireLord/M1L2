import random
sym = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
u = int(input("сколько символов в пароль"))
res = ""
for x in range(u):
    res += random.choice(sym)
print(res)
