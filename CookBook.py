with open('recipes.txt', 'rt', encoding='utf-8') as f:

    def create_cook_book():
        cook_book = dict()
        def add_dishes():
            ingr_count = dict()
            ingr_list = list()
            name = f.readline().strip()
            b = list(range(0, int(f.readline())))

            for lines in b:
                a = f.readline().split('|')
                ingr_count['ingredient_name'] = a[0]
                ingr_count['quantity'] = int(a[1])
                ingr_count['measure'] = a[2].strip()
                ingr_list.append(ingr_count.copy())
                cook_book[name] = ingr_list

        add_dishes()
        while f.readline() == '\n':
            add_dishes()

        return cook_book

    def get_shop_list_by_dishes(dishes, person_count):
        cook_book = create_cook_book()
        a = list(dishes)
        order = dict()
        ingr_order = dict()
        for dishes in a:
            order[dishes] = cook_book[dishes]

        for ingr in order.values():
            for content in ingr:
                if ingr_order.get(content['ingredient_name']) == None:
                    ingr_order[content['ingredient_name']] = content.copy()
                else:
                    ingr_order[content['ingredient_name']]['quantity'] += content['quantity']
        for ingrs in ingr_order.values():
            ingrs['quantity'] = ingrs['quantity'] * int(person_count)
            del(ingrs['ingredient_name'])


        print(ingr_order)



    get_shop_list_by_dishes(['Салат', 'Жаркое'], 5)
