def my_reduce(func, sequence, initial=None):
    if not sequence:
        if initial is None:
            raise TypeError("reduce() of empty sequence with no initial value")
        return initial
    
    iterator = iter(sequence)
    
    if initial is None:
        result = next(iterator)
    else:
        result = initial
    
    for item in iterator:
        result = func(result, item)
    
    return result
if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    total = my_reduce(lambda x, y: x + y, numbers)
    print(f"Сумма {numbers} = {total}")
    
    words = ["Функциональное", " ", "программирование"]
    text = my_reduce(lambda x, y: x + y, words)
    print(f"Текст: '{text}'")
