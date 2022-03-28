from pprint import pprint

# """Название блюда
# Количество ингредиентов в блюде
# Название ингредиента | Количество | Единица измерения
# Название ингредиента | Количество | Единица измерения
# ..."""

cook_book = {}


def get_cook_book(file_path, encoding):
    with open(file_path, encoding=encoding) as file:
        while True:
            name_dish = file.readline().strip().lower()
            if name_dish.strip() == '':
                break
            count_ingredient = int(file.readline().strip())
            list_ingredient = []
            for i in range(count_ingredient):
                ingredient = file.readline().strip().split('|')
                ingredients = {'ingredient_name': ingredient[0], 'quantity': int(ingredient[1]), 'measure': ingredient[2]}
                list_ingredient.append(ingredients)
            cook_book.update({name_dish: list_ingredient})
            file.readline()


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_list = dict(ingredient)
            new_list['quantity'] *= person_count
            if new_list['ingredient_name'] not in shop_list:
                shop_list[new_list['ingredient_name']] = new_list
            else:
                shop_list[new_list['ingredient_name']]['quantity'] += new_list['quantity']
    return shop_list


def print_list(shop_list):
    for i in shop_list.values():
        print(f'{i["ingredient_name"]}, {i["quantity"]} {i["measure"]}')


def get_shop_list():
    person_count = int(input('Введите количество гостей: '))
    dishes = input('Введите список блюд через запятую: ').lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_list(shop_list)
    # pprint(shop_list)


if __name__ == '__main__':
    get_cook_book('data.txt', 'utf-8')
    get_shop_list()
    # pprint(cook_book)



import os
# Строка номер 1 файла номер 1
# Строка номер 2 файла номер 1

# Строка номер 1 файла номер 2
#
# 2.txt
# 1
# Строка номер 1 файла номер 2
# 1.txt
# 2
# Строка номер 1 файла номер 1
# Строка номер 2 файла номер 1


def get_list(file_path, encoding):
    file_list = os.listdir(file_path)
    # print(file_list)
    full_list = []
    for file in file_list:
        with open(file_path + '/' + file, encoding=encoding) as f:
            full_list.append([file, 0, []])
            for line in f:
                full_list[-1][2].append(line.strip())
                full_list[-1][1] += 1
    # print(full_list)
    return sorted(full_list, reverse=True)


def print_combined_txt(file_path, encoding):
    with open('combined.txt', 'w', encoding=encoding) as f:
         for file in get_list(file_path, encoding):
            f.write(f'File: {file[0]}\n')
            f.write(f'Length: {file[1]}\n')
            for string in file[2]:
                f.write(string + '\n')


if __name__ == '__main__':
    print_combined_txt('files', 'utf-8')





