#서울에서 김서방 찾기
#https://programmers.co.kr/learn/courses/30/lessons/12919

def solution(seoul):
    for i, k in enumerate(seoul):
        if k=="Kim":
            answer = "김서방은 "+str(i)+"에 있다"
            print(answer)
    return answer
