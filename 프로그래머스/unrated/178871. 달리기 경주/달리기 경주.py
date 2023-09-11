def solution(players, callings):
    
    player_by_rank = {rank+1 : player for rank, player in enumerate(players)}
    rank_by_player = {player : rank+1 for rank, player in enumerate(players)}
    
    for calling in callings:
        before_rank = rank_by_player[calling]
        after_rank = before_rank - 1
        prev_player = player_by_rank[after_rank]
        
        player_by_rank[before_rank] = prev_player
        player_by_rank[after_rank] = calling
        rank_by_player[prev_player] = before_rank
        rank_by_player[calling] = after_rank
    
    return list(player_by_rank.values())