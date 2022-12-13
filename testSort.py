tab = [24, 12, 33, 42, 16, 73, 91]
def bubbleSort(tab):    
    for i in range(len(tab)):
        for j in range(0, len(tab) - i - 1):
            if tab[j] > tab[j+1]:
                temp = tab[j]
                tab[j] = tab[j+1]
                tab[j+1] = temp
bubbleSort(tab)
print(tab)