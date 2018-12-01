def lenth(arr):
    if arr:
        return 1 + lenth(arr[1:])
    return 0
