from abc import ABC, abstractmethod

# -------------------------
# Base Abstract Class
# -------------------------
class Person(ABC):
    """Abstract base class representing a Domino's employee."""

    def __init__(self, name, age, contact_info, gender, employee_id):
        self.name = name
        self.age = age
        self.__contact_info = contact_info  # private
        self.gender = gender
        self.employee_id = employee_id

    def update_contact_info(self, new_contact):
        self.__contact_info = new_contact

    def get_contact_info(self):
        return self.__contact_info

    @abstractmethod
    def display_info(self):
        pass


# -------------------------
# Delivery Staff
# -------------------------
class DeliveryStaff(Person):
    """Represents Domino's delivery employees."""

    def __init__(self, name, age, contact_info, gender, employee_id, area, shift_timing, license_number):
        super().__init__(name, age, contact_info, gender, employee_id)
        self.area = area
        self.shift_timing = shift_timing
        self.__license_number = license_number

    @property
    def license_number(self):
        return self.__license_number

    def update_shift(self, new_shift):
        self.shift_timing = new_shift

    def display_info(self):
        return (f"[Delivery Staff] Name: {self.name}, Age: {self.age}, Contact: {self.get_contact_info()}, "
                f"Gender: {self.gender}, ID: {self.employee_id}, Area: {self.area}, "
                f"Shift: {self.shift_timing}, License: {self.license_number}")


# -------------------------
# Cashier / Kitchen Staff
# -------------------------
class Staff(Person):
    """Represents Cashiers or Kitchen staff at Domino's."""

    def __init__(self, name, age, contact_info, gender, employee_id, role):
        super().__init__(name, age, contact_info, gender, employee_id)
        self.role = role

    def display_info(self):
        return (f"[Staff] Name: {self.name}, Age: {self.age}, Contact: {self.get_contact_info()}, "
                f"Gender: {self.gender}, ID: {self.employee_id}, Role: {self.role}")


# -------------------------
# Chef
# -------------------------
class Chef(Person):
    """Represents a Chef specializing in pizza preparation."""

    def __init__(self, name, age, contact_info, gender, employee_id, specialization, shift):
        super().__init__(name, age, contact_info, gender, employee_id)
        self.specialization = specialization
        self.shift = shift

    def update_shift(self, new_shift):
        self.shift = new_shift

    def display_info(self):
        return (f"[Chef] Name: {self.name}, Age: {self.age}, Contact: {self.get_contact_info()}, "
                f"Gender: {self.gender}, ID: {self.employee_id}, Specialization: {self.specialization}, Shift: {self.shift}")


# -------------------------
# Menu Item (Pizza)
# -------------------------
class Pizza:
    def __init__(self, name, size, price, ingredients):
        self.name = name
        self.size = size
        self.price = price
        self.ingredients = ingredients

    def display_pizza(self):
        return f"{self.name} ({self.size}) - ₹{self.price} | Ingredients: {', '.join(self.ingredients)}"


# -------------------------
# Domino Management
# -------------------------
class DominoManagement:
    employees = []
    menu = []
    orders = []

    @classmethod
    def register_employee(cls, employee):
        cls.employees.append(employee)

    def list_all_employees(self):
        if not self.employees:
            print("No employees registered.")
        else:
            for emp in self.employees:
                print(emp.display_info())

    def find_employee_by_id(self, emp_id):
        for emp in self.employees:
            if emp.employee_id == emp_id:
                return emp.display_info()
        return "Employee not found."

    @classmethod
    def add_pizza(cls, pizza):
        cls.menu.append(pizza)

    def show_menu(self):
        print("\n--- Domino's Menu ---")
        for idx, pizza in enumerate(self.menu, start=1):
            print(f"{idx}. {pizza.display_pizza()}")

    def place_order(self, pizza_index, customer_name):
        if 0 < pizza_index <= len(self.menu):
            selected_pizza = self.menu[pizza_index - 1]
            self.orders.append((customer_name, selected_pizza))
            print(f"✅ Order placed: {customer_name} ordered {selected_pizza.name} ({selected_pizza.size})")
        else:
            print("❌ Invalid menu choice.")

    @staticmethod
    def generate_report():
        return f"Total Employees: {len(DominoManagement.employees)} | Menu Items: {len(DominoManagement.menu)} | Orders Placed: {len(DominoManagement.orders)}"


# -------------------------
# CLI
# -------------------------
def main():
    system = DominoManagement()

    # ✅ Add default menu
    default_menu = [
        Pizza("Margherita", "Medium", 199, ["Cheese", "Tomato"]),
        Pizza("Farmhouse", "Large", 399, ["Cheese", "Onion", "Capsicum", "Mushroom"]),
        Pizza("Pepperoni", "Medium", 299, ["Cheese", "Pepperoni"]),
        Pizza("Veggie Supreme", "Small", 149, ["Cheese", "Onion", "Tomato", "Capsicum"])
    ]
    for p in default_menu:
        DominoManagement.add_pizza(p)

    # ✅ Add some employees
    default_employees = [
        DeliveryStaff("Ravi Kumar", 25, "9876543210", "Male", "D001", "Madhapur", "Morning", "LIC12345"),
        Staff("Anita Sharma", 28, "8765432109", "Female", "S001", "Cashier"),
        Chef("Suresh Reddy", 35, "7654321098", "Male", "C001", "Baking", "Evening")
    ]
    for emp in default_employees:
        DominoManagement.register_employee(emp)

    # CLI menu
    while True:
        print("\n========= Domino's Management System =========")
        print("1. Register New Employee")
        print("2. List All Employees")
        print("3. Find Employee by ID")
        print("4. Show Menu")
        print("5. Place Order")
        print("6. Generate Report")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\na. Delivery Staff\nb. Staff\nc. Chef")
            sub_choice = input("Enter your choice: ")

            name = input("Enter name: ")
            age = int(input("Enter age: "))
            gender = input("Enter gender: ")
            contact = input("Enter contact info: ")
            emp_id = input("Enter employee ID: ")

            if sub_choice == "a":
                area = input("Enter delivery area: ")
                shift = input("Enter shift timing: ")
                license_no = input("Enter license number: ")
                emp = DeliveryStaff(name, age, contact, gender, emp_id, area, shift, license_no)

            elif sub_choice == "b":
                role = input("Enter role (Cashier/Kitchen): ")
                emp = Staff(name, age, contact, gender, emp_id, role)

            elif sub_choice == "c":
                specialization = input("Enter specialization: ")
                shift = input("Enter shift timing: ")
                emp = Chef(name, age, contact, gender, emp_id, specialization, shift)

            else:
                print("Invalid choice.")
                continue

            DominoManagement.register_employee(emp)
            print("✅ Employee registered successfully!")

        elif choice == "2":
            system.list_all_employees()

        elif choice == "3":
            emp_id = input("Enter employee ID to search: ")
            print(system.find_employee_by_id(emp_id))

        elif choice == "4":
            system.show_menu()

        elif choice == "5":
            system.show_menu()
            idx = int(input("Enter pizza number to order: "))
            customer = input("Enter customer name: ")
            system.place_order(idx, customer)

        elif choice == "6":
            print(DominoManagement.generate_report())

        elif choice == "7":
            print("Exiting system... Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
