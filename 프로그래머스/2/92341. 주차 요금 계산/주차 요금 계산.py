import math

def solution(fees, records):
    parking_lot = dict()
    parking_time = dict()
    answer = []
    
    for record in records:
        time, car, sign = map(str, record.split())
        if sign == 'IN':
            parking_lot[car] = int(time[:2]) * 60 + int(time[3:])
        else:
            time = int(time[:2]) * 60 + int(time[3:]) - parking_lot[car]
            del parking_lot[car]
            if car in parking_time:
                parking_time[car] += time
            else:
                parking_time[car] = time
    
    for car, time in parking_lot.items():
        time = 23 * 60 + 59 - time
        if car in parking_time:
            parking_time[car] += time
        else:
            parking_time[car] = time
    
    parking_time = sorted(parking_time.items(), key = lambda x : x[0])
    
    for car, time in parking_time:
        if time > fees[0]:
            answer.append(fees[1] + math.ceil((time-fees[0])/fees[2])*fees[3])
        else:
            answer.append(fees[1])
    
    return answer