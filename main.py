import shop_data

chosen_case = []
chosen_ram = []
chosen_HDD = []
chosen_items = []
other_chosen_type = []


def chosen_category(category, item_code):
    return shop_data.Category[category][item_code]


def price_of_computer(chosen_items, no_of_other_items):
    total_sum = 0
    for item in chosen_items:
        total_sum = total_sum + item["Price"]
    print(f"Total price of your computer is ${total_sum:.2f}")
    if no_of_other_items == 1:
        discount_price = total_sum / 100 * 5
    elif no_of_other_items > 1:
        discount_price = total_sum / 100 * 10

    if no_of_other_items > 0:
        After_discount = (total_sum - discount_price)
        print(f"You saved {discount_price:.2f}")
        print(f"After Discount Total price of your computer is ${After_discount:.2f}")


def computer_selected(chosen_case, chosen_RAM, chosen_HDD):
    print("Chosen Case:")
    for item in chosen_case:
        print(f"\t{item['Description']} - ${item['Price']}")
    print("Chosen RAM:")
    for item in chosen_RAM:
        print(f"\t{item['Description']} - ${item['Price']}")
    print("Chosen Main Hard Disk Drive")
    for item in chosen_HDD:
        print(f"\t{item['Description']} - ${item['Price']}")


# Other items
def computer_other_items(other_chosen_items, other_chosen_type):
    for i in range(len(other_chosen_type)):
        print(f"Chosen {other_chosen_items[i]}:")
        print(f"\t{other_chosen_type[i].get('Description')} - ${other_chosen_type[i].get('Price')}")


print("\t\t---WELCOME TO ONLINE COMPUTER SHOP---")

total_price = 0
# Customer choosing
print(f"Case: \n\t{shop_data.Category["Case"]}")
case_type = input("What case type you want: ")
chosen_case.append(chosen_category("Case", case_type))

print(f"RAM: \n\t{shop_data.Category["RAM"]}")
RAM_type = input("What RAM type you want: ")
chosen_ram.append(chosen_category("RAM", RAM_type))

print(f"Main Hard Disk Drive:\n\t{shop_data.Category["Main Hard Disk Drive"]}")
HDD_type = input("What HDD type you want: ")
chosen_HDD.append(chosen_category("Main Hard Disk Drive", HDD_type))

# other items
choice = input("Do you want to purchase other item (yes\\no) :")
new_items = []
no_of_other_items = 0
if choice == "yes":
    print("Other Items: ")
    for item in shop_data.Category.keys():
        print(f"\t{item}")
    no_of_other_items = int(input(f"how many other items you want to purchase: "))
    for x in range(no_of_other_items):
        item_name = input("Enter the name of item: ")
        print(f"{item_name:}\n\t{shop_data.Category[item_name]}")
        new_item_type = input(f"What type of {item_name} you want: ")
        new_items.append(item_name)
        other_chosen_type.append(chosen_category(item_name, new_item_type))
        chosen_items = chosen_items + other_chosen_type

chosen_items = chosen_items + chosen_case + chosen_ram + chosen_HDD

# Computer Details
computer_selected(chosen_case, chosen_ram, chosen_HDD)
if choice == "yes":
    computer_other_items(new_items, other_chosen_type)

# price of computer
price_of_computer(chosen_items, no_of_other_items)
