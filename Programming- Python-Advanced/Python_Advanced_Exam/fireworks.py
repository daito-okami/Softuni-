from collections import deque
firework_effect = deque([int(el) for el in input().split(", ")])
explosive_power = [int(el) for el in input().split(", ")]


perfect_show = False

palm_firework = 0
willow_firework = 0
crossette_firework = 0


while len(firework_effect) > 0 and len(explosive_power) > 0:
    current_firework_effect = firework_effect.popleft()
    current_explosive_power = explosive_power.pop()
    sum_of_both = current_explosive_power + current_firework_effect

    if current_firework_effect <= 0:
        explosive_power.append(current_explosive_power)
        continue
    if current_explosive_power <= 0:
        firework_effect.appendleft(current_firework_effect)
        continue
    if sum_of_both % 3 == 0 and not sum_of_both % 5 == 0:
        palm_firework += 1
    elif sum_of_both % 5 == 0 and not sum_of_both % 3 == 0:
        willow_firework += 1
    elif sum_of_both % 5 == 0 and sum_of_both % 3 == 0:
        crossette_firework += 1
    else:
        current_firework_effect -= 1
        firework_effect.append(current_firework_effect)
        explosive_power.append(current_explosive_power)

    if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
        perfect_show = True
        break


if perfect_show:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can’t make the perfect firework show.")

if len(firework_effect) > 0:
    print(f"Firework Effects left: {', '.join(str(el) for el in firework_effect)}")
if len(explosive_power) > 0:
    print(f"Explosive Power left: {', '.join(str(el) for el in explosive_power)}")

print(f"Palm Fireworks: {palm_firework}")
print(f"Willow Fireworks: {willow_firework}")
print(f"Crossette Fireworks: {crossette_firework}")