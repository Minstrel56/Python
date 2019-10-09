#----
# Ctrl+/ for block comment in pycharm
#----
def find_uniq(arr):
    c=1
    for i in arr[1:-1]:
        if i != arr[c-1] and i != arr[c+1]:
            return i
        c+=1
    if arr[0] != arr[-1] and arr[0] == arr[1]:
        return arr[-1]
    else:
        return arr[0]