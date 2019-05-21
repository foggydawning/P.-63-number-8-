def add_random_list (list=[]):
    import random
    for i in range (0, random.randint(0,20)):
        list.append(random.randint(0,100))
    print("Ваш список:", list, sep="\n")
    print("\n")
    return list

list=add_random_list()
