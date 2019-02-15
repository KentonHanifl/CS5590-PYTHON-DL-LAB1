import operator
course_tuple = [("John",("Physics",80)), ("Mushfiq",("Social",100)), ("Daniel", ("Science", 90)), ("John",("Science",95)),
            ("Daniel", ("History", 75)),("Mushfiq",("Math",75))]

my_dict = dict()

[my_dict [t [0]].append(t [1]) if t [0] in list(my_dict.keys())
 else my_dict.update({t [0]: [t [1]]}) for t in course_tuple]

sorted_dictionary_byvalue = sorted(my_dict.items(), key=operator.itemgetter(0))

print(sorted_dictionary_byvalue)









