def input_to_list(count):
    lines = []
    for _ in range(count):
        lines.append(input())

    return lines


def input_to_list_until_command(end_command):
    lines = []
    while True:
        command = input()
        if command == end_command:
            break
        else:
            lines.append(command)

    return lines


def is_vip(guest):
    return guest[0].isdigit()


def separator(guests):
    vip_guests = []
    regular_guests = []
    for guest in guests:
        if is_vip(guest):
            vip_guests.append(guest)
        else:
            regular_guests.append(guest)
    return sorted(vip_guests), sorted(regular_guests)


def print_result(guests):
    vip_guests, regular_guests = separator(guests)
    for guest in vip_guests:
        print(guest)

    for guest in regular_guests:
        print(guest)


n = int(input())

reservations = input_to_list(n)

guests_arrived = input_to_list_until_command('END')

guests_not_arrived = set(reservations).difference(guests_arrived)
print(len(guests_not_arrived))
print_result(guests_not_arrived)