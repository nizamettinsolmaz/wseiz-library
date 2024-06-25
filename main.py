from store import Store
from item import Item
from customer import Customer

# Mağazayı oluşturup ismini göstermek
our_store = Store('Tech Store', 'Rejtana 17, Warsaw')
print("Store Name: ", our_store.name)

# Bir ürün eklemek
our_item = Item('Laptop', 1200, 'Electronics', 'TechBrand', '1234-5678')
our_store.add_item(our_item)

# Bir müşteri eklemek
customer = Customer('John', 'Doe', '001')
print(f"Customer: {customer.first_name} {customer.last_name}, ID: {customer.id}")
