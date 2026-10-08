class Shoe:
    """Represents a shoe in the inventory."""

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = float(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        """Return the cost of the shoe."""
        return self.cost

    def get_quantity(self):
        """Return the quantity of the shoe in stock."""
        return self.quantity

    def __str__(self):
        """Return a string representation of the shoe."""
        return (
            f"Country: {self.country}, "
            f"Code: {self.code}, "
            f"Product: {self.product}, "
            f"Cost: ${self.cost:.2f}, "
            f"Quantity: {self.quantity}"
        )


shoes_list = []


def read_shoes_data():
    """Read shoe data from inventory.txt and create Shoe objects."""
    try:
        with open("/Users/abhishekdallakoti/VS code Dev/test/MT0307/inventory.txt", "r") as file:
            next(file)

            for line in file:
                data = line.strip().split(",")

                country = data[0]
                code = data[1]
                product = data[2]
                cost = data[3]
                quantity = data[4]

                shoe = Shoe(country, code, product, cost, quantity)
                shoes_list.append(shoe)

    except FileNotFoundError:
        print("Error: inventory.txt could not be found.")

    except ValueError:
        print("Error: There was a problem with the data in inventory.txt.")

    except IndexError:
        print("Error: A line in inventory.txt has missing information.")


def capture_shoes():
    """Allow the user to enter a new shoe and add it to the inventory."""
    country = input("Enter the country: ")
    code = input("Enter the shoe code: ")
    product = input("Enter the shoe product: ")
    cost = float(input("Enter the cost: "))
    quantity = int(input("Enter the quantity: "))

    shoe = Shoe(country, code, product, cost, quantity)
    shoes_list.append(shoe)

    print("Shoe successfully added.")


def view_all():
    """Display all shoes currently stored in the inventory."""
    if len(shoes_list) == 0:
        print("There are no shoes in the inventory.")
        return

    print("\n--- ALL SHOES ---")

    for shoe in shoes_list:
        print(shoe)


def re_stock():
    """Find the shoe with the lowest quantity and update its stock."""
    if len(shoes_list) == 0:
        print("There are no shoes in the inventory.")
        return

    lowest_quantity_shoe = shoes_list[0]

    for shoe in shoes_list:
        if shoe.get_quantity() < lowest_quantity_shoe.get_quantity():
            lowest_quantity_shoe = shoe

    print("\nShoe requiring restock:")
    print(lowest_quantity_shoe)

    choice = input(
        "Would you like to add stock to this shoe? (yes/no): "
    ).lower()

    if choice == "yes":
        amount = int(input("How many shoes would you like to add? "))

        lowest_quantity_shoe.quantity += amount

        # Rewrite the inventory file with the updated quantity.
        with open("inventory.txt", "w") as file:
            file.write("Country,Code,Product,Cost,Quantity\n")

            for shoe in shoes_list:
                file.write(
                    f"{shoe.country},"
                    f"{shoe.code},"
                    f"{shoe.product},"
                    f"{shoe.cost},"
                    f"{shoe.quantity}\n"
                )

        print("Stock successfully updated.")
        print(lowest_quantity_shoe)

    else:
        print("No stock was added.")


def search_shoe():
    """Search for a shoe using its shoe code."""
    code = input("Enter the shoe code to search for: ")

    for shoe in shoes_list:
        if shoe.code == code:
            print("\nShoe found:")
            print(shoe)
            return shoe

    print("Shoe not found.")
    return None


def value_per_item():
    """Calculate and display the total value of each shoe in stock."""
    print("\n--- INVENTORY VALUE ---")

    for shoe in shoes_list:
        value = shoe.get_cost() * shoe.get_quantity()

        print(
            f"{shoe.product}: "
            f"Cost = ${shoe.get_cost():.2f}, "
            f"Quantity = {shoe.get_quantity()}, "
            f"Total Value = ${value:.2f}"
        )


def highest_qty():
    """Find and display the shoe with the highest quantity."""
    if len(shoes_list) == 0:
        print("There are no shoes in the inventory.")
        return

    highest_quantity_shoe = shoes_list[0]

    for shoe in shoes_list:
        if shoe.get_quantity() > highest_quantity_shoe.get_quantity():
            highest_quantity_shoe = shoe

    print("\n--- SHOE FOR SALE ---")
    print(
        f"The shoe with the highest quantity is "
        f"{highest_quantity_shoe.product}."
    )
    print(highest_quantity_shoe)


# Load the inventory when the program starts.
read_shoes_data()


while True:
    print("\n================================")
    print("       SHOE INVENTORY MENU")
    print("================================")
    print("1. View all shoes")
    print("2. Capture a new shoe")
    print("3. Restock shoe")
    print("4. Search for a shoe")
    print("5. Calculate inventory value")
    print("6. Find shoe with highest quantity")
    print("7. Exit")
    print("================================")

    choice = input("Please select an option: ")

    if choice == "1":
        view_all()

    elif choice == "2":
        capture_shoes()

    elif choice == "3":
        re_stock()

    elif choice == "4":
        search_shoe()

    elif choice == "5":
        value_per_item()

    elif choice == "6":
        highest_qty()

    elif choice == "7":
        print("Thank you for using the Shoe Inventory System.")
        break

    else:
        print("Invalid choice. Please select a number from 1 to 7.")