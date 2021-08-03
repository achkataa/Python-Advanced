words = {w: len(w) for w in input().split(", ")}

print(', '.join('{} -> {}'.format(k,v) for k,v in words.items()))