from ga_pid_const import MIN_POINTS_NUMBER, EPS, MAX_SCORE


def is_sample_ok(s, t):
    n = len(s)
    m = len(t)
    if n != m:
        return False
    if n < MIN_POINTS_NUMBER:
        return False
    if head_zeros_number(s, EPS) > (n // 4):
        return False
    return True


def head_zeros_number(s, eps):
    i = 0
    while i < len(s) and s[i] <= eps:
        i = i+1
    return i


def cut_queue_zeros(s, t, eps):
    while s[-1] <= eps:
        s.pop()
        t.pop()
    return s, t


def is_stable(s, eps):
    if len(s) <= 6:
        return False
    for i in range(1, 6):
        if s[-i] - s[-i-1] > eps:
            return False
    return True


def stat_error(s, instruction):
    return abs(s[-1] - instruction)


def overflow(s):
    stat_value = s[-1]
    return max_arr(s) - stat_value


def max_arr(s):
    max_value = s[0]
    for i in range(1, len(s)):
        if s[i] >= max_value:
            max_value = s[i]
    return max_value


def response_time(s, t):
    j = len(t)-1
    stat_value = s[-1]
    while stat_value * .95 < s[j] < stat_value * 1.05:
        j = j-1
        if j < 0:
            return -1
    return t[j+1]


def absolute_error(s, t, instruction):
    error = 0
    for i in range(1, len(t)):
        error += (abs(instruction - s[i]) + abs(instruction - s[i-1])) * (t[i] - t[i-1]) / 2
    return error


def score_mod(s, t, module, instruction):
    if not is_stable(s, EPS):
        return 0
    return module - (((3 * (stat_error(s, instruction) + absolute_error(s, t, instruction))) + 2 * (response_time(s, t) + overflow(s))) % module)
