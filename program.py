def add_random_list (list=[]):
    import random
    for i in range (0, random.randint(0,20)):
        list.append(random.randint(0,100))
    print("Ваш список:", list, sep="\n")
    print("\n")
    return list

def reverse(list, K, M):
    if M==K:
        print(list)
        return list
    if M-K==1:
        k=list[K]
        list[K]=list[M]
        list[M]=k
        print(list)
        return list
    k=list[K]
    list[K]=list[M]
    list[M]=k
    return reverse(list,K+1,M-1)
    reverse(list, K+1)

list=add_random_list()
K=int(input("Введите номер первого элемента в массиве дле ревераса: "))
M=int(input("Введите номер последнего элемента в массиве дле ревераса: "))
reverse(list,K,M)
