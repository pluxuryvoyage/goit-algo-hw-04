from pathlib import Path

def total_salary(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        if not lines:
            print("Файл порожній.")
            return (0, 0)
        
        total = 0
        count = 0

        for line in lines:
            line = line.strip()
        
            if not line or line.startswith('_'):
                    continue

            parts = line.split(',')
            if len(parts) == 2:
                try:
                    salary = float(parts[1].strip())
                    total += salary
                    count += 1
                except ValueError:
                    continue

        average = total / count if count > 0 else 0
        return (total, average)
    
    except FileNotFoundError:
        print("Файл відсутній.")
        return (0, 0)
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return (0, 0)

if __name__ == "__main__":
    file_path = Path("C:/Homework/goit-algo-hw-04/task1/salary_file.txt")
    total, average = total_salary(file_path)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")