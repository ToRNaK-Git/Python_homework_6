arr = []
if len(arr) > 0:
    a = [arr[-1]]
    new_arr1 = arr.pop(-1)
    new_arr2 = a + arr
else:
    new_arr2 = []
print(new_arr2)
