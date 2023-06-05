import uuid

class Product:

    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price
        self.id = self.get_id()

    def __repr__(self):
        return (f"Product(product_name='{self.product_name}', price={self.price})")

    def get_id(self):
        random_id = str(uuid.uuid4())
        product_id = random_id.split('-')[-1]
        return product_id

class Warehouse:

    def __init__(self):
        self.products = []

    def add_product(self,product_name,price):
        for i in self.products:
            if i.product_name == product_name:
              print("Ez a product már szerepel a")
        product = Product(product_name, price)
        self.products.append(product)

    def remove_product(self,product_name):
        for i in self.products:
            if i.product_name == product_name:
                self.products.remove(i)

    def display_products(self):
        for product in self.products:
          print(f"Product(product_name='{product.product_name}', price={product.price}, id={product.id})")

    def sort_by_price(self,ascending=True):
        self.products.sort(key=lambda x: x.price, reverse = not ascending)
        return self.products


#Test
warehouse = Warehouse()
warehouse.add_product('Laptop', 3900.0)
warehouse.add_product('Mobile Phone', 1990.0)
warehouse.add_product('Camera', 2900.0)
warehouse.add_product('USB Cable', 24.9)
warehouse.add_product('Mouse', 49.0)
for product in warehouse.sort_by_price():
    print(product)

