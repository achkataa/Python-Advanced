def age_assignment(*args, **kwargs):
    for el in args:
        for key in kwargs:
            if el[0] == key:
                kwargs[el] = kwargs.pop(key)
    return kwargs
print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
