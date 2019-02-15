#Syed M Rahman


#creating a tuple
course_tuple =[( "John", ("Physics", 80)) , ("Daniel", ("Science", 90)), ("John", ("Science", 95)), ("Mark",("Maths", 100)),
               ("Daniel", ("History", 75)), ("Mark", ("Social", 95))]

print("The following is a tuple:\n",course_tuple)
#creat an empty dictionary
my_dict = dict()

#if there is a duplicate key, it appends the values
[my_dict [t [0]].append(t [1]) if t [0] in list(my_dict.keys())
 else my_dict.update({t [0]: [t [1]]}) for t in course_tuple]




# for every key it sorts the values in ascending order
for key in my_dict.keys():
  my_dict[key].sort()



#prints the dictionary keys and sorts the subjects & scores in order
print("\nThis is a dictionary with keys as names and the subjects & scores in sorted order:")
print(my_dict)











