def fft(minutes):
    ft_count = 0
    possible_hours = [i if i != 0 else 12 for i in range(12)]
    hour_index = 0
    min = 0
    while minutes:
        if min + 1 == 60:
            hour_index = (hour_index + 1) % len(possible_hours)
            min = 0
        else:
            min += 1
        time = str(possible_hours[hour_index]) + ":" + str(min).zfill(2)
        digits = [int(d) for d in time if d.isnumeric()]
        dif = digits[1] - digits[0]
        for i in range(1, len(digits) - 1):
            if digits[i + 1] - digits[i] != dif:
                break
        else:
            ft_count += 1
        minutes -= 1
    return ft_count

minutes = input()
print(fft(int(minutes)))
