score=input('★輸入你的成績:')
score=int(score)
if score>0 and score<=100:
    print('你的分數等級為:')
    if score>=90:
        print('A')
    elif score>=80:
        print('B')
    elif score>=70:
        print('C')
    elif score>=60:
        print('D')
    else:
        print('E')
else:
    print('error')