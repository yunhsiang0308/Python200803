height=float(input('★輸入你的身高:'))
weight=float(input('★輸入你的體重:'))
BMI=(weight/height**2)
print('★你的BMI為:',BMI)
if BMI<18.5:
    print('→體重不足')
elif BMI<24:
    print('→正常')
elif BMI<27:
    print('→過重')
elif BMI<30:
    print('→輕度肥胖')
elif BMI<35:
    print('→重度肥胖')
else:
    print('→重度肥胖')