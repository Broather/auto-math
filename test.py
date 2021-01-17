# 8, 12,16

a = [2,2,2]
b = [2,2,3]
c = [2,2,2,2]

my_list = [a]+[b]+[c]

# make each of the lists into sets
def list_to_set(list):
    edited_list = list[:]
    for i in range(len(edited_list)):
        edited_list[i] = set(edited_list[i])
    return edited_list
my_set = list_to_set(my_list)
# do the .intersection function on all of them, find out which numbers appear on all of them
unique_numbers = my_set[0].intersection(*my_set[1:])

# count how many of the number each list has and add the lowest amount to me list
def the_thing(list_of_lists, set):
    # returns a dictionary with key: string format for number: what is the lowest occurences of that item
    my_dict = {}
    for set_item in set:
        counts = []
        for lst in list_of_lists:
            counts.append(lst.count(set_item))
        my_dict[str(set_item)] = min(counts)
    return my_dict

my_dictionary = the_thing(my_list, unique_numbers)

def dict_to_answer(dictionary):
    # adds int value of key *distionary[key]* times
    lst = []
    for key in dictionary:
        for i in range(dictionary[key]):
            lst.append(int(key))
    # Multiply elements one by one
    result = 1
    for x in lst:
         result = result * x 
    return result 
        

print(dict_to_answer(my_dictionary))