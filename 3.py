russian = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('wow.txt', 'r') as file_obj1:
    # content = file_obj1.read().split('\n')
    for i in file_obj1:
        i = i.split(' ', 1)
        new_file.append(russian[i[0]] + '  ' + i[1])
    print(new_file)

with open('wow_new.txt', 'w') as file_obj_2:
    file_obj_2.writelines(new_file)
