# 한줄같은 두줄...
# min(arr)을 먼저 저장해 놓지 않으면 O(n^2)가 되어서 테케 통과를 못함..
def solution(arr): m = min(arr); return [x for x in arr if x != m] if len(arr)>1 else [-1]
