def total_salary(path: str):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = [
                int(line.split(",")[1].strip())
                for line in f.readlines()
                if line.strip()
            ]

            if not data:
                return (0, 0)

            total = sum(data)
            average = round(total / len(data))

    except FileNotFoundError:
        return None

    except Exception:
        return None

    else:
        return (total, average)


result = total_salary("./salary_file.txt")
if result is None:
    print("Error: file not found or invalid format")
else:
    total, average = result
    print(f"The total salary: {total}, The average salary: {average}")
