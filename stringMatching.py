def compute_border_function(pattern):
    m = len(pattern)
    border = [0] * m
    j = 0  # Length of previous longest prefix suffix
    
    for i in range(1, m):
        # Handle the case where pattern[i] != pattern[j]
        while j > 0 and pattern[i] != pattern[j]:
            j = border[j - 1]
        
        # Handle the case where pattern[i] == pattern[j]
        if pattern[i] == pattern[j]:
            j += 1
            border[i] = j
        else:
            border[i] = 0
            
    return border

def KMP_search(text, pattern):
    n = len(text)
    m = len(pattern)
    border = compute_border_function(pattern)
    result = []
    
    i = 0  # Index for text
    j = 0  # Index for pattern
    
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == m:
            result.append(i - j)
            j = border[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = border[j - 1]
            else:
                i += 1
                
    return result[0]