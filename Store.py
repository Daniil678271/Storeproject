class Store:
    def __init__(self):
        self.inventory = {}
        self.sales_log = []

    def add_product(self, name, price, quantity):
        if name in self.inventory:
            self.inventory[name]['quantity'] += quantity
        else:
            self.inventory[name] = {'price': price, 'quantity': quantity}
        print(f"Додано {quantity} одиниць товару '{name}' за ціною {price} грн.")

    def remove_product(self, name, quantity):
        if name in self.inventory:
            if self.inventory[name]['quantity'] >= quantity:
                self.inventory[name]['quantity'] -= quantity
                print(f"Видалено {quantity} одиниць товару '{name}'.")
                if self.inventory[name]['quantity'] == 0:
                    del self.inventory[name]
                    print(f"Товар '{name}' повністю видалено з інвентарю.")
            else:
                print(f"Помилка: недостатньо товару '{name}' на складі")
        else:
            print(f"Помилка: товар '{name}' не знайдено.")

    def self_product(self, name, quantity):
        if name in self.inventory and self.inventory[name]['quantity'] >= quantity:
            total_price = self.inventory[name]['price'] * quantity
            self. remove_product (name, quantity)
            self.sales_log.append({'product': name, 'quantity': quantity, 'total_price': total_price})
            print (f"Продано {quantity} одиниць товару '{name}' на суму {total_price} грн.")
        else:
            print(f"Помилка: неможливо продати товар '{name}' у такій кількості.")

    def show_inventory (self):
        if not self. inventory:
            print ("Інвентар порожній.")
        else:
            print ("\nПоточний інвентар:")
            for name, details in self.inventory.items():
                print (f"Товар: ({name}, Ціна: {details['price']} грн, Кількість: {details['quantity']}")
    def total_inventory_value (self):
        total = sum(details['price'] * details ['quantity'] for details in self. inventory.values)
        print(f"Загальна вартість товарів на складі: {total} грн.")
        return total
    def show_sales (self):
        if not self.sales_log:
            print ("Продажів ще не було.")
        else:
            print("\nІсторія продажів:")
            for sale in self. sales_log:
                print (f"Товар: {sale['product']}, Кількість: {sale['quantity']}, Сума: {sale['total_price']} грн.")
    def main(self):
        store = Store()

        while True:
            print ("\nМеню магазину:")
            print ("1. Додати товар") 
            print("2. Видалити товар") 
            print("3. Продати товар")
            print("4. Показати інвентар") 
            print("5. Показати загальну вартість інвентарю") 
            print("6. Показати історію продажів")
            print("7.Вихід")

            try:
                choice = int(input("Виберіть опцію (1-7): "))
            except ValueError:
                print ("Будь ласка, введіть ціле число.")
                continue


            if choice == 1:
                name = input ("Введіть назву товару: ")
                try:
                    price = float(input("Введіть ціну товару:"))
                    quantity = int(input ("Введіть кількість: "))
                    store.add_product (name, price, quantity)
                except ValueError:
                    print ("Помилка: ціна та кількість повинні бути числовими значеннями.")
                    
            elif choice == 2:
                name = input ("Введіть назву товару: ")
                try:
                    quantity = int(input("Введіть кількість для видалення: "))
                    store. remove_product (name, quantity)
                except ValueError:
                    print ("Помилка: кількість повинна бути цілим числом.")

            elif choice == 3:
                name = input ("Введіть назву товару: ")
                try:
                    quantity = int(input("Введіть кількість для продажу: "))
                    store.sell_product(name, quantity)
                except ValueError:
                    print ("Помилка: кількість повинна бути цілим числом.")

            elif choice == 4:
                store.show_inventory()

            elif choice == 5:
                store. total_inventory_value()

            elif choice == 6:
                store.show_sales()

            elif choice == 7:
                print("Вихід з програми.")
                break

            else:
                print("Невірний вибір. Введіть число від 1 до 7.")

if __name__ == "__main__":
    store = Store()
    store.main()