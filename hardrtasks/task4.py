def filter_file_data(filename, condition):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            line_number = 0
            for line in file:
                line_number += 1
                cleaned_line = line.strip()
                if condition(cleaned_line, line_number):
                    yield cleaned_line, line_number
    except FileNotFoundError:
        print(f"Файл '{filename}' не найден")
        return

def demonstrate_file_filter():
    
    print("=== Фильтрация данных из файла через генератор ===\n")
    
    print("Строки содержащие 'Python':")
    python_lines = filter_file_data('test_data.txt', 
                                  lambda line, num: 'Python' in line)
    
    for line, line_num in python_lines:
        print(f"Строка {line_num}: {line}")
    
    print("\nСтроки длиннее 8 символов:")
    long_lines = filter_file_data('test_data.txt', 
                                lambda line, num: len(line) > 8)
    
    for line, line_num in long_lines:
        print(f"Строка {line_num}: {line}")

if __name__ == "__main__":
    demonstrate_file_filter()
