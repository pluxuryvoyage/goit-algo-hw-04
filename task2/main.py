from pathlib import Path

def get_cats_info(path):
    try:
        with open (path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        if not lines:
            print("Файл порожній.")
            return []
        
        cats = []

        for line in lines:
            line = line.strip()
        
            if not line:
                    continue

            parts = line.split(',')
        
            try: 
                cat = {
                    "id": parts[0].strip(),
                    "name": parts[1].strip(),
                    "age": int(parts[2].strip()),
                }
                cats.append(cat)
            except (ValueError):
                continue

        return cats
    
    except FileNotFoundError:
        print("Файл відсутній.")
        return []
    except Exception as e:
        print(f"Виникла помилка: {e}")
        return []

if __name__ == "__main__":
    file_path = Path("C:/Homework/goit-algo-hw-04/task2/cats_file.txt")
    cats_info = get_cats_info(file_path)
print(cats_info)
