import math

import conv_to_bin


def F(F_prev, q, G_prev):
    return round(F_prev + q * G_prev, 8)


def G(p, G_prev):
    return round(p * G_prev, 8)


def cumulative_probability(probabilities, n):
    sum = 0
    for i in range(n):
        sum += probabilities[i]
    return round(sum, 8)


def calc_all_cumulative_probabilities(probabilities):
    q = []
    for i in range(len(probabilities)):
        q.append(cumulative_probability(probabilities, i))
    return q


def coding(probabilities, s):
    F_S = []
    F_S.append(0)
    G_S = []
    G_S.append(1)

    q = calc_all_cumulative_probabilities(probabilities)

    str_res = ""

    str_res += f"\nq_Sm = p1 + p2 + ... + p_m-1\nF(S_ik) = F(S_ik-1) + q(S_i)*G(S_ik-1)\nG(S_ik) = P(S_i)*G(S_ik-1)\n\n"

    for i in range(len(probabilities)):
        str_res += f"p(s{i + 1}) = {probabilities[i]}  q(s{i + 1}) = {q[i]}\n"

    str_res += f"\nШаг 0\ns_i = - | S_ik = - | p(S_i) = - | q(S_i) = - | F(S_ik) = {F_S[0]} | G(S_ik) = {G_S[0]}\n"
    S_ik = ""

    for i in range(len(s)):
        S_ik += "s" + str(s[i])
        p = probabilities[s[i] - 1]
        F_S.append(F(F_S[i], q[s[i] - 1], G_S[i]))
        G_S.append(G(p, G_S[i]))
        str_res += f"Шаг {i + 1}\ns_i = s{s[i]} | S_ik = {S_ik} | p(S_i) = {p} | q(S_i) = {q[s[i] - 1]} | F(S_ik) = {F_S[i + 1]:.8f} | G(S_ik) = {G_S[i + 1]:.8f}\n"

    tmp = get_code_word(F_S[len(s)], G_S[len(s)])
    str_res += tmp[0]
    x = tmp[1]
    return str_res, x, q, F_S, G_S


def get_code_word(F_S_ik, G_S_ik):
    tmp = get_code_len(G_S_ik)
    str = tmp[0]
    L = tmp[1]
    str += f"\nx = bin({F_S_ik:.8f} + {G_S_ik:.8f}/2) = "
    x = F_S_ik + G_S_ik / 2
    str += f"bin({x:.8f}) = "
    x = conv_to_bin.float_to_bin_fixed(x)[:L + 2]
    str += f"{x}_2\n"
    x = x[2:L + 2]
    str += f"x = {x}\n"
    return str, x


def get_code_len(G_S_ik):
    L = round(-math.log2(G_S_ik), 6)
    str = f"\nL = ⌈-log_2({G_S_ik:.8f})⌉ + 1 = ⌈{L}⌉ + 1 = "
    L = math.ceil(L) + 1
    str += f"{L}\n"
    return str, L
