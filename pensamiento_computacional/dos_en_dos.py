# for i in range(10):
#     if i % 2 == 0:
#         print(i)
#     else:
#         continue

# 0
# 2
# 4
# 6
# 8
# pares = range(0, 101, 2)
# col = 1
# for i in pares:
#     if (col < 10):
#         print(f'{i}\t', end="")
#         col += 1
#     else:
#         print(i)
#         col = 1

impares = range(1, 101, 2)
col = 1
for i in impares:
    if (col < 10):
        print(f'{i}\t', end="")
        col += 1
    else:
        print(i)
        col = 1
