from math import sqrt, isinf, isnan

eps = 1e-14


def solve(a: float, b: float, c: float) -> list:
    if any(map(isinf, [a, b, c])):
        raise ValueError("Coefficients must be differ from a infinity.")

    if any(map(isnan, [a, b, c])):
        raise ValueError("Coefficients must be differ from a nan.")

    if -eps < a < eps:
        raise ValueError("Coefficient 'a' must be differ from a zero.")

    d: float = b * b - 4 * a * c

    if -eps < d < eps:
        return [-b / 2 / a, ]
    elif d < eps:
        return []
    else:
        return [
            (-b + sqrt(d)) / 2 / a,
            (-b - sqrt(d)) / 2 / a
        ]
