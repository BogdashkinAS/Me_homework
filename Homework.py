def cookbook():
    cook_book = {}
    book = []
    with open('recipes.txt', 'r', encoding='utf8') as file:
        for l in file:
            name = l.strip()
            employees_count = file.readline()
            for i in range(int(employees_count)):
                emp = file.readline()
                ingredient_name, quantity, measure = emp.strip().split(' | ')
                book.append({'ingredient_name': ingredient_name,
                                     'quantity': quantity,
                                     'measure': measure})
            blank_line = file.readline()
            cook_book.setdefault(name, book)
            book = []
    return cook_book

def get_shop_list_by_dishes(dishes, count):
    book = cookbook()
    shop_list = {}
    all_mass = {}
    mass2 = {}
    error = 0
    # name_error = []
    # asb2 = 0
    # asb3 = 0
    for i in range(len(dishes)):
        if dishes[i] in book:
            a = book.get(dishes[i])
            for i2 in range(len(a)):
                b = a[i2]
                ingredient_name = b.get('ingredient_name')
                measure = b.get('measure')
                quantity = b.get('quantity')
                mass2.setdefault('measure', measure)
                if ingredient_name in all_mass:
                    name_ingredient = ingredient_name
                    error += 1
                    name_quantity = quantity
                mass2.setdefault('quantity', int(quantity) * count)
                all_mass.setdefault(ingredient_name, mass2)
                measure = ''
                quantity = 0
                mass2 = {}
        else:
            print('Такого блюда нет')
    shop_list = all_mass
            
    if error > 0:
        asb = shop_list.get(name_ingredient)
        set = asb.get('quantity')
        del(asb['quantity'])
        asb.setdefault('quantity', int(name_quantity) * count + set)
        del(shop_list[name_ingredient])
        shop_list.setdefault(name_ingredient, asb)
    print(shop_list)

get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)

def txt_file():
    i1 = 0
    i2 = 0
    i3 = 0
    i = {}
    i_list = {}

    with open('1.txt', encoding='utf8') as file:
        content1 = file.readline()
        while len(content1) > 0:
            i1 += 1
            content1 = file.readline()
        i.setdefault(i1, '1.txt')

    with open('2.txt', encoding='utf8') as file:
        content2 = file.readline()
        while len(content2) > 0:
            i2 += 1
            content2 = file.readline()
        i.setdefault(i2, '2.txt')

    with open('3.txt', encoding='utf8') as file:
        content3 = file.readline()
        while len(content3) > 0:
            i3 += 1
            content3 = file.readline()
        i.setdefault(i3, '3.txt')

    i_list = i
    i = sorted(i)
    for set in i:
        f = open(i_list.get(set), encoding='utf8')
        a = f.read()
        f.close()
        mail_file = open('4.txt', 'a', encoding='utf8')
        mail_file.write(i_list.get(set) + '\n')
        mail_file.write(str(set) + '\n')
        mail_file.write(a + '\n')
        mail_file.close()

txt_file()