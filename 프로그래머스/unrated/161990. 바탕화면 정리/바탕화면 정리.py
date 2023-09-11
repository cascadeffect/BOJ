def solution(wallpaper):
    rotation = list(zip(*wallpaper))
    
    s = {'lux': -1, 'luy': -1}
    e = {'rdx': -1, 'rdy': -1}
    
    for i in range(len(wallpaper)):
        if wallpaper[i].find('#') != -1:
            s['lux'] = i
            break
    for i in range(len(wallpaper)-1, -1, -1):
        if wallpaper[i].find('#') != -1:
            e['rdx'] = i+1
            break
    for i in range(len(rotation)):
        if '#' in rotation[i]:
            s['luy'] = i
            break
    for i in range(len(rotation)-1, -1, -1):
        if '#' in rotation[i]:
            e['rdy'] = i+1
            break
            
    answer = [s.get('lux'), s.get('luy'), e.get('rdx'), e.get('rdy')]
    
    return answer