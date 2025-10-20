def get_cats_info(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            cats_info = []

            for line in f.readlines():
                if not line.strip():
                    continue

                row_data = line.strip().split(",")
                id_, name, age = row_data
                cats_info.append({"id": id_, "name": name, "age": age})

    except FileNotFoundError:
        return None

    except Exception:
        return None

    else:
        return cats_info

cats_info = get_cats_info("./cats_file.txt")
print(cats_info)
