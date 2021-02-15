from collections import deque

bomb_effect = deque([int(el) for el in input().split(",")])
bomb_casing = [int(el) for el in input().split(",")]

is_pouched_filled = False

datura_bombs = 0
cherry_bombs = 0
smoke_decoy_bombs = 0


while len(bomb_casing) > 0 and len(bomb_effect) > 0:
    current_effect = bomb_effect.popleft()
    current_casing = bomb_casing.pop()
    value_of_bombs = current_casing + current_effect
    if value_of_bombs == 40:
        datura_bombs += 1
    elif value_of_bombs == 60:
        cherry_bombs += 1
    elif value_of_bombs == 120:
        smoke_decoy_bombs += 1
    else:
        current_casing -= 5
        bomb_effect.insert(0, current_effect)
        bomb_casing.append(current_casing)
    if datura_bombs >= 3 and cherry_bombs >= 3 and smoke_decoy_bombs >= 3:
        is_pouched_filled = True
        break
if is_pouched_filled:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")

if bomb_effect:
    print(f"Bomb Effects: {', '.join(str(el) for el in bomb_effect)}")
else:
    print("Bomb Effects: empty")

if bomb_casing:
    print(f"Bomb Casings: {', '.join(str(el) for el in bomb_casing)}")
else:
    print("Bomb Casings: empty")


print(f"Cherry Bombs: {cherry_bombs}")
print(f"Datura Bombs: {datura_bombs}")
print(f"Smoke Decoy Bombs: {smoke_decoy_bombs}")