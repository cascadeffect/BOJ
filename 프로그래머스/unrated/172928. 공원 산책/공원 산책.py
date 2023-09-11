def solution(park, routes):
    answer = [] # 도착 좌표
    h = len(park)
    w = len(park[0])
    directions = ['N', 'S', 'E', 'W']
    dx = dict(zip(directions, [-1, 1, 0, 0]))
    dy = dict(zip(directions, [0, 0, 1, -1]))
    
    # 시작지점 좌표 구하기
    for x in range(h):
        y = park[x].find('S')
        if (y != -1):
            answer = [x, y]
            break
    
    for route in routes:
        direction, distance = map(str, route.split())
        distance = int(distance)
        nx = answer[0] + dx[direction] * distance
        ny = answer[1] + dy[direction] * distance
        if (0 <= nx < h and 0 <= ny < w):
            # 북 (N)
            if direction == 'N':
                tmp = [park[answer[0]-i][answer[1]] for i in range(1, distance+1)]
                if 'X' in tmp:
                    continue
            # 서 (W)
            elif direction == 'W':
                if 'X' in park[answer[0]][ny:answer[1]]:
                    continue
            # 동 (E)
            elif direction == 'E':
                if 'X' in park[answer[0]][answer[1]+1:ny+1]:
                    continue
            # 남 (S)
            elif direction == 'S':
                tmp = [park[answer[0]+i][answer[1]] for i in range(1, distance+1)]
                if 'X' in tmp:
                    continue
            answer = [nx, ny]
    return answer