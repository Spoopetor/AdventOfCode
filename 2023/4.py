
with open("2023\inputs\input4.txt", 'r') as f:
    lines = f.readlines()

total = 0

for line in lines:
    this_total=0
    card = line.split(":")[1]
    have, win = card.split("|")
    
    have = have.split()
    win = win.split()


    wins = 0
    for i in have:
        if i in win:
            wins += 1
    
    if wins >= 1:
        this_total += 1
        if wins >= 2:
            this_total *= 2**(wins-1)

    total += this_total

print(total)