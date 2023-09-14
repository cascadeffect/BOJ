def solution(id_list, report, k):

    rep_dict = {id: set() for id in id_list}
    cnt_dict = {id: 0 for id in id_list}    
    
    for row in set(report):
        key, val = map(str, row.split())
        rep_dict[key].add(val)
        cnt_dict[val] += 1
    
    rep_set = set(filter(lambda x: cnt_dict[x] >= k, id_list))

    return [len(val & rep_set) for val in rep_dict.values()]