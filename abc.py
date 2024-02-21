
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target_element = 5
result = linear_search(my_array, target_element)
if result != -1:
    print(f"Element {target_element} found at index {result}.")
else:
    print(f"Element {target_element} not found in the array.")