import random

#lottos생성

listA=list(range(1,46))
random.shuffle(listA)

lottos=listA[0:6]

num=random.randint(0,6)
tryy=0
while tryy!=num:
    lottos[tryy]=0
    tryy=tryy+1
print(num,lottos)

#win_nums생성

listB=list(range(1,46))
random.shuffle(listB)
win_nums=listB[0:6]
print(win_nums)

#최고순위와 최저순위 판단
def solution(lottos,win_nums):
    max_num=0
    min_num=0
    for i in lottos:
        if i==0:
                max_num=max_num+1
        else:
            for k in win_nums:
                if i==k:
                    max_num=max_num+1
                    min_num= min_num+1
    print(max_num, min_num)
    
    if  min_num==2:
        min_grade=5
    elif  min_num==3:
        min_grade=4
    elif  min_num==4:
        min_grade=3
    elif  min_num==5:
        min_grade=2
    elif min_num==6:
        min_grade=1
    else:
        min_grade=6
        
    if  max_num==2:
        max_grade=5
    elif  max_num==3:
        max_grade=4
    elif  max_num==4:
        max_grade=3
    elif  max_num==5:
        max_grade=2
    elif max_num==6:
        max_grade=1
    else:
        max_grade=6 
        
    answer=[max_grade,min_grade]
    
    return answer
