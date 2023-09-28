# for converting
integer = eval(input("Enter Desired Second(s): "))
mns = integer // 60
scs = integer % 60

print(format(integer) + "seconds is " + format(mns) + " minute(s) and " + format(scs) + " second(s). ")
