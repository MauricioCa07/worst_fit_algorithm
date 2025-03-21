def worst_fit(memory: list, requirement: int, index: int):
    if not memory:
        return None
    
    n = len(memory)
    start_index = index % n 
    bloques_circular = memory[start_index:] + memory[:start_index]
    
    max_limit = -1
    selected_block_index = None  
    
    for i, block in enumerate(bloques_circular):
        if block[1] >= requirement and block[1] > max_limit:
            max_limit = block[1]
            selected_block_index = i
    
    if selected_block_index is None:
        return None
    
    original_index = (start_index + selected_block_index) % n
    base, limit = memory[original_index]
    remaining = limit - requirement
    
    if remaining == 0:
        memory.pop(original_index)
        if original_index == len(memory):
            original_index = 0
        return (memory, base, requirement, original_index)
    else:
        memory.pop(original_index)
        memory.insert(original_index, (base + requirement, remaining))
        return (memory, base, requirement, original_index)

print(worst_fit([(0x00A00000, 0x000F0000)]
                ,0x000A0000,0))





   