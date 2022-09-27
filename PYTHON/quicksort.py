
import random


def get_random_list(maxLength):
    mylist=[number for number in range(0,maxLength)]
    random.shuffle(mylist)
    return mylist


def quicksortpartition(liste,low,high):
    pivot=liste[low]
    left=low

    for elem in range(low+1,high):
        if liste[elem] < pivot:
            liste[elem],liste[left]=liste[left],liste[elem]
            left+=1
    pivot,liste[left]=liste[left],pivot

    return left


def quicksort(liste,low,high):
    if low<high:
        pivotpos=quicksortpartition(liste,low,high)
        quicksort(liste,low,pivotpos)
        quicksort(liste,pivotpos,high)


def main():
    maxLength=100
    random_list=get_random_list(maxLength)
    print(quicksort(random_list,low=0,high=len(random_list)-1))
    

if __name__ == "__main__":
    main()