import sys

input = sys.stdin.readline

n = int(input()) # 지도 사이즈
input_map = [list(map(int, list("".join(input().split())))) for _ in range(n)] # 장애물-도로 지도
output_map = [[0 for _ in range(n)] for _ in range(n)] # 블록 번호 지도

def search(a, b):
    global count
    # 지도 범위 밖이거나 도로(0)거나 이미 방문했으면 리턴
    if a < 0 or a >= n or b < 0 or b >= n or input_map[a][b] == 0 or output_map[a][b] != 0:
        return False

    output_map[a][b] = answer # 장애물(1) => 블록 번호 표시 (방문)
    count += 1

    search(a, b+1)
    search(a-1, b)
    search(a+1, b)
    search(a, b-1)

    return True

count = 0 # 블록별 장애물 수
answer = 1 # 블록 번호 == 총 블록 수
answer_list = [] # 블록별 장애물 수 리스트

for i in range(n):
    for j in range(n):
        if search(i, j) == True:
            answer += 1
            answer_list.append(count)
            count = 0
    
answer_list.sort()

print(answer - 1)
for num in answer_list:
    print(num)