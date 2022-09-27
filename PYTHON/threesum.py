arr=[6,4,7,9,3,12]
pair_sum=13


def twosumfinder(arr, pair_sum):
    for elem in range(len(arr)):
        for obj in range(elem, len(arr)):
            for item in range(obj, len(arr)):
                if arr[elem]+arr[obj]+arr[item]==pair_sum:
                    print(f"first: {arr[elem]} sec: {arr[obj]} third: {arr[item]}.")


twosumfinder(arr,pair_sum)