def skaitlis_to_pirmreizinataji(skaitlis):
    # no skaitļa izvada sarakstu ar tā pirmreizinātājiem
    pirmreizinataji = []
    pirmskaitli = [x for x in range(2, 1000) if all(x % y != 0 for y in range(2, x))]
    while skaitlis > 1:
        for pirmskaitlis in pirmskaitli:
            if skaitlis % pirmskaitlis == 0:
                pirmreizinataji.append(pirmskaitlis)
                skaitlis = skaitlis // pirmskaitlis
                break
    return pirmreizinataji

def list_to_set(list):
    edited_list = list[:]
    return set(edited_list)

def count_list_elem(list_of_lists, set):
    # returns a dictionary with key: string format for number: what is the lowest occurences of that item
    my_dict = {}
    for set_item in set:
        counts = []
        for lst in list_of_lists:
            counts.append(lst.count(set_item))
        my_dict[str(set_item)] = min(counts)
    return my_dict

def dict_to_pirmreizinataji(dictionary):
    # adds int value of key *distionary[key]* times
    lst = []
    for key in dictionary:
        for i in range(dictionary[key]):
            lst.append(int(key))
    # Multiply elements one by one
    return lst

def reiz(list):
    reizinajums = 1
    for elem in list:
        reizinajums *= elem
    return reizinajums

def LKD(dotais):
    list_of_pirmreizinataji = list(map(skaitlis_to_pirmreizinataji, dotais))
    list_of_sets = list(map(list_to_set, list_of_pirmreizinataji))
    set_of_kopigie_pirmreiznataji = list_of_sets[0].intersection(*list_of_sets[1:])
    dictionary_of_counts = count_list_elem(list_of_pirmreizinataji, set_of_kopigie_pirmreiznataji)
    list_of_kopigie_pirmreiznataji = dict_to_pirmreizinataji(dictionary_of_counts)
    atbilde = reiz(list_of_kopigie_pirmreiznataji)
    return atbilde


def MKD(dotais):
    return abs(reiz(dotais))//LKD(dotais)



print(LKD([3,4,5,6,7,8,9,90]))
print(MKD([1,9,2,4,6,7,8,10]))

