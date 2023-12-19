from math import copysign, fabs, floor, isfinite, modf


def float_to_bin_fixed(f):
    if not isfinite(f):
        return repr(f)  # inf nan

    sign = '-' * (copysign(1.0, f) < 0)
    frac, fint = modf(fabs(f))  # split on fractional, integer parts
    n, d = frac.as_integer_ratio()  # frac = numerator / denominator
    assert d & (d - 1) == 0  # power of two
    return f'{sign}{floor(fint):b}.{n:0{d.bit_length() - 1}b}'


def bin_to_float_fixed(binary_str):
    if binary_str.lower() in ('inf', '-inf', 'nan'):
        return float(binary_str)

    sign = -1 if binary_str[0] == '-' else 1
    binary_str = binary_str.lstrip('-')
    integer_part, frac_part = binary_str.split('.')

    int_part_dec = int(integer_part, 2)
    frac_part_dec = int(frac_part, 2) / (2 ** len(frac_part))

    return sign * (int_part_dec + frac_part_dec)
