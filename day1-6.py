Eng=float(input('★輸入你的英文成績:'))
Math=float(input('★輸入你的數學成績:'))
if Eng>=90 and Math>=90:
    print('Great job!有獎品唷~')
elif Eng<60 and Math<60:
    print('有懲罰喔!')
elif Eng<60 or Math<60:
    print('再接再厲~')
else:
    print('Fighting~')