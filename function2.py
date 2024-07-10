def f(l: list, x: int) -> int:
    if all([i == 1 for i in l]):
        return x
    else:
        if l[0] == 1:
            i:int = 0
            while l[i] == 1:
                l[i] = x
                i += 1
            l[i]-=1
            return f(l,x)
        elif l[0]>1:
            l[0] -= 1
            return f(l,f(l,x))