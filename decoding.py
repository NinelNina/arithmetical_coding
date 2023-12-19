from conv_to_bin import bin_to_float_fixed


def decoding(probabilities, q, x, n, F_k, G_k):
    str_res = f"x = {x} ->"
    x = "0." + x
    x_f = round(bin_to_float_fixed(x), 8)
    str_res += f"{x}_2 = {x_f}_10\n"
    s = ""

    for i in range(n):
        str_res += f"Шаг {i + 1}\nF_k = {F_k[i]} | G_k = {G_k[i]} | Проверка F_k + q_i * G_k < x:\n"
        result_s = ""
        for j in range(len(probabilities)):
            q_i = q[j]
            tmp = round(F_k[i] + q_i * G_k[i], 8)
            str_res += f'Гипотеза s_i: s{j + 1} | q = {q_i} | {f"{tmp} < x" if tmp < x_f else f"{tmp} > x"}\n'
            if tmp >= x_f and result_s == "":
                result_s = f"s{j}"
        if result_s == "":
            result_s = f"s{len(probabilities)}"
        s += result_s
        str_res += f"Решение s_i: {result_s} | p(s_i) = {probabilities[int(result_s[1:]) - 1]}\ns = {s}\n"
    return str_res
