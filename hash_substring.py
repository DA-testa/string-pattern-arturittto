# Artūrs Čubukovs 16.grupa 221RDB127

def read_input():
    choice = input().strip()
    if choice == 'I':
        pattern = input().strip()
        text = input().strip()
    else:
        with open(f"tests/06", "r") as f:
            lines = f.readlines()
            pattern = lines[0].strip()
            text = lines[1].strip()
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    prime = 1000000007
    multiplier = 31
    p_len = len(pattern)
    t_len = len(text)
    pattern_hash = 0
    text_hash = 0
    match_positions = []
    
    for i in range(p_len):
        pattern_hash = (pattern_hash * multiplier + ord(pattern[i])) % prime
        text_hash = (text_hash * multiplier + ord(text[i])) % prime
    
    for i in range(t_len - p_len + 1):
        if pattern_hash == text_hash and pattern == text[i:i+p_len]:
            match_positions.append(i)
        if i < t_len - p_len:
            text_hash = (multiplier * (text_hash - ord(text[i]) * pow(multiplier, p_len-1, prime)) + ord(text[i+p_len])) % prime
            if text_hash < 0:
                text_hash += prime
    
    return match_positions

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
