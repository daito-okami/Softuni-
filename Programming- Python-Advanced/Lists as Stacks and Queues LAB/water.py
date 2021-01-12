from collections import deque

END_COMMAND = "End"
START_COMMAND = "Start"
REFILL_COMMAND = "refill"

dispenser = int(input())

people = deque()


while True:
    command = input()
    if command == START_COMMAND:
        break
    people.append(command)


while True:
    command = input()
    if command == END_COMMAND:
        print(f"{dispenser} liters left")
        break
    if command.startswith(REFILL_COMMAND):
        command_param = command.split(" ")
        refilled_liters = int(command_param[1])
        dispenser += refilled_liters
    else:
        person = people.popleft()
        person_litters = int(command)
        if person_litters <= dispenser:
            dispenser -= person_litters
            print(f"{person} got water")
        else:
            print(f"{person} must wait")