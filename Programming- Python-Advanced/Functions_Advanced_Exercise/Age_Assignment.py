def age_assignment(*names, **kwargs):
    assignment = {}
    for name in names:
        for letter, age in kwargs.items():
            if name.startswith(letter):
                assignment[name] = age
    return assignment


print(age_assignment("Peter", "George", G=26, P=19))