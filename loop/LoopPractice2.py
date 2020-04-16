#4,5,6,7   xxx
for a in range(4,8):
    for b in range(4,8):
        for c in range(4, 8):
            if a!=b and b!=c and c!=a:
                print(f'{a}{b}{c}')