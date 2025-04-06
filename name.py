
def search(l, x, inf, sup):
    while inf <= sup:
        mid = (inf + sup) // 2
        if l[mid] == x:
            print("It exists")
            return
        elif l[mid] > x:
            sup = mid - 1
        else:
            inf = mid + 1
    print("It doesn't exist")

# Example usage:
l = [1, 2, 3, 4, 5, 6, 7]
search(l,7,0, len(l) - 1)
