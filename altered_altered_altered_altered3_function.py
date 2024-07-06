def T(A_ls,h_f):#h_fは1変数関数
    def g(l_l):
        if len(l_l) == 1 or all([i == 1 for i in l_l[:-1]]):
            return h_f(l_l[-1])
        else:
            if l_l[-2] == 1:
                i = -2
                while l_l[i] != 1:
                    i -= 1
                l_l[i] -= 1
                i += 1
                while i < -1:
                    l_l[i] = l_l[-1]
                    i += 1
                return g(l_l)
            elif l_l[-2] > 1:
                if all([all([j == 1 for j in i]) for i in A_ls]):
                    l_l[-2] -= 1
                    l_l[-1] = g(l_l)
                    l_l[-2] = 1
                    return g(l_l)
                elif A_ls[-1][-1] == 1:
                    i = -1
                    while all([j == 1 for j in A_ls[i]]):
                        i -= 1
                    j = -1
                    while A_ls[i][j] == 1:
                        j -= 1
                    A_ls[i][j] -= 1
                    j += 1
                    while j < 0:
                        A_ls[i][j] = l_l[-1]
                        j += 1
                    i += 1
                    while i < 0:
                        A_ls[i] = [l_l[-1]] * l_l[-1]
                        i += 1
                    l_l[-2] -= 1
                elif A_ls[-1][-1] > 1:
                    A_ls[-1][-1] -= 1
                    l_l[-2] -= 1

                def g2(x_n):#h_fに代入用
                    l_l[-1] = x_n
                    return g(l_l)

                G_f = T(g2, A_ls)
                return G_f(l_l[-1])

    def gx(x_n):
        return g([x_n] * x_n)

    return gx


def f(t_n, l_l):
    if len(l_l) == 1 or all([i == 1 for i in l_l[:-1]]):
        return l_l[-1] + 1
    else:
        if l_l[-2] == 1:
            i = -2
            while l_l[i] != 1:
                i -= 1
            l_l[i] -= 1
            i += 1
            while i < -1:
                l_l[i] = l_l[-1]
                i += 1
            return f(t_n, l_l)
        elif l_l[-2] > 1:
            l_l[-2] -= 1

            def f2(x_n):#h_fに代入用
                l_l[-1] = x_n
                return f(t_n, l_l)

            F_f = T(f2, [[l_l[-1]] * l_l[-1] for i in range(l_l[-1])])
            return F_f(l_l[-1])
