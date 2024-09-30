class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop:
    __file_name = 'products.txt'

    def __init__(self):
        # Create the file if it doesn't exist
        with open(self.__file_name, 'a'):
            pass

    def get_products(self):
        products = []
        with open(self.__file_name, 'r') as products_file:
            for line in products_file:
                name, weight, category = line.strip().split(', ')
                products.append(Product(name, float(weight), category))
        return products

    def add(self, *products):
        existing_products = self.get_products()
        existing_names = {product.name for product in existing_products}

        for new_product in products:
            if new_product.name not in existing_names:
                with open(self.__file_name, 'a') as file:
                    file.write(f'{new_product}\n')
                print(f'Added: {new_product}')
            else:
                print(f'Продукт {new_product.name} уже есть в магазине')
                # Update the weight if the product exists but has a different weight
                existing_product = next(p for p in existing_products if p.name == new_product.name)
                if existing_product.weight != new_product.weight:
                    existing_product.weight = new_product.weight
                    print(f'Updated weight of {new_product.name} to {new_product.weight}')

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)
s1.add(p1, p2, p3)
