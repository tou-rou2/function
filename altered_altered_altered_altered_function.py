def S(t_n, h_f):#h_fは1変数関数
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
                if t_n == 1:
                    l_l[-2] -= 1
                    l_l[-1] = g(l_l)
                    l_l[-2] = 1
                    return g(l_l)
                elif t_n > 1:
                    l_l[-2] -= 1

                    def g2(x_n):#h_fに代入用
                        l_l[-1] = x_n
                        return g(l_l)

                    G_f = S(t_n - 1, g2)
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

            F_f = S(t_n, f2)
            return F_f(l_l[-1])
