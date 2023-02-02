import sys

input = sys.stdin.readline

n, m = map(int, input().split()) # 회의실 수, 예약된 회의 수
rooms = [input().rstrip('\n') for _ in range(n)]
reservation = [input().split() for _ in range(m)]

rooms.sort()
reservation.sort()

count = 0

def get_empty_time():
    global count
    empty_time = [True for _ in range(9)]

    while count < m:
        if room != reservation[count][0]:
            break
        for i in range(int(reservation[count][2]) - int(reservation[count][1])):
            empty_time[int(reservation[count][1])-9+i] = False
        count += 1

    return empty_time

def get_avail_time(empty_time_list):
    start_time = 0
    end_time = 0
    flag = False
    avali_time = []

    for i in range(9):
        if flag == False and empty_time_list[i] == True:
            flag = True
            start_time = i + 9
        if flag == True and empty_time_list[i] == False:
            flag = False
            end_time = i + 9
        if i == 8 and flag == True and empty_time_list[i] == True:
            end_time = i + 10
        if start_time != 0 and end_time != 0:
            avali_time.append([start_time, end_time])
            start_time = 0; end_time = 0
    return avali_time

for room in rooms:
    print(f'Room {room}:')
    
    avail_time_list = get_avail_time(get_empty_time())
    
    if len(avail_time_list):
        print(f'{len(avail_time_list)} available:')
        for start, end in avail_time_list:
            print(f'{str(start).zfill(2)}-{end}')
    else:
        print('Not available')

    if room != rooms[n-1]:
        print('-----')