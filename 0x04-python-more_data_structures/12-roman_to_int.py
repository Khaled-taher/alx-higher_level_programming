def roman_to_int(roman_string):
    if type(roman_string) == str:
        num = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum_r = 0

        for j in range(len(roman_string)):

            if j == len(roman_string) - 1:
                sum_r = num[roman_string[i]] + sum_r

            elif num[roman_string[i + 1]] <= num[roman_string[i]]:
                sum_r = num[roman_string[i]] + sum_r

            else:
                sum_r = num[roman_string[i]] - sum_r

        return (sum_r)
    else:
        return (0)
