def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for num in numbers:
        try:
            result += num
        except TypeError:
            incorrect_data += 1

    return result, incorrect_data

def calculate_average(numbers):
    try:
        if not isinstance(numbers, (list, tuple, set)):
            raise TypeError

        total_sum, incorrect_data = personal_sum(numbers)
        count = len(numbers) - incorrect_data

        if count == 0:
            return 0

        average = total_sum / count
        return average
    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None
print(calculate_average([1, 2, 3, 4, 5]))
print(calculate_average([1, 2, 'a', 4]))
print(calculate_average([]))
print(calculate_average(123))
print(calculate_average({1, 2, 3, 4, 5}))