inp = int(input())
h = inp / 3600
s = inp % 3600
m = s / 60
s = s % 60
print("{}:{}:{}".format(int(h),int(m),int(s)))