def count_ways_to_sum(dice_left, target_sum, faces=6, memo=None):
    if memo is None:
        memo = {}
    

    if dice_left == 0:
        return 1 if target_sum == 0 else 0
    
    if target_sum < 0:
        return 0

    if (dice_left, target_sum) in memo:
        return memo[(dice_left, target_sum)]
    
    ways = 0
    for face_value in range(1, faces + 1):
        ways += count_ways_to_sum(dice_left - 1, target_sum - face_value, faces, memo)
    
    memo[(dice_left, target_sum)] = ways
    return ways

dice_count = 5
target_sum = 20
result = count_ways_to_sum(dice_count, target_sum)
print(f"Nombre de façons d'obtenir {target_sum} avec {dice_count} dés : {result}")
