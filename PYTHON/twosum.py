
arr=[3,5,2,-4,8,11]
pair_sum=7


def twosumfinder(arr, pair_sum):
    for elem in range(len(arr)):
        for obj in range(elem, len(arr)):
            if arr[elem]+arr[obj]==pair_sum:
                print(f"first: {arr[elem]}. sec: {arr[obj]}.")


twosumfinder(arr,pair_sum)