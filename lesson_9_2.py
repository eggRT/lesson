filename = "lesson.txt"
n_array = []

with open(filename, encoding="utf8") as file:
    for obj in file:
        str_arr = []
        for el in obj.split(','):
            str_arr.append(el.replace(' ', '')[:3])
        if(int(str_arr[3]) == 720):
            n_array.append(obj)
print(n_array)