def create_passport(name, birth_date, birth_place, height, nationality):
    passport = {str(name), str(birth_date), str(birth_place), float(height), str(nationality)}
    return passport


sebastian = create_passport("sebastian", "04-09-2021", "liverpool", 1.8, "nederlands")

print(type(sebastian))

# Comprehension = [os.path.join(cache_folder, file) for file in os.listdir(cache_folder)]
#     return abs_path_list


def return_absolute_path():
    abs_path_list = []
    for file in os.listdir(cache_folder):
        create_path = os.path.join(cache_folder, file)
        abs_path_list.append(create_path)
    return abs_path_list
