l = list(map(str, input().split()))
cnt_upper = 0
cnt_lower = 0
f_l = [w[0] for w in l]
for i in f_l:
    if 65 <= ord(i) - 32 <= 90:
        cnt_lower += 1
    elif 97 <= ord(i) + 32 <= 122:
        cnt_upper += 1
print(f"Number of lower : {cnt_lower}, Number of upper : {cnt_upper}")

# 65-90
# 97-122
