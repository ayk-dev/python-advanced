def age_assignment(*names, **kwargs):
    names_and_ages = {}
    for name in names:
        age = kwargs[name[0]]
        names_and_ages[name] = age

    return names_and_ages


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
