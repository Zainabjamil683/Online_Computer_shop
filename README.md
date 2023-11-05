# Online_Computer_shop
This Python code represents an online computer shop application where a user can choose components for a computer, such as a case, RAM, and hard disk drive, and optionally select other items. The code uses a predefined shop_data module to store information about available items and their prices. The user's choices are stored in lists, and the total price of the selected components is calculated, taking into account any discounts for additional items.
Here's a brief explanation:
The code initializes empty lists to store chosen components (case, RAM, HDD, and others).
The chosen_category function retrieves the details of a selected item based on its category and code from the shop_data module.
The user is prompted to choose a case, RAM, and HDD, with the choices stored in corresponding lists.
If the user decides to purchase other items, they can choose the type and quantity of additional items, and the details are added to the other_chosen_type list.
The selected items are then combined into the chosen_items list.
The computer_selected function prints the details of the chosen case, RAM, and HDD.
If the user has selected other items, the computer_other_items function prints the details of those items.
The price_of_computer function calculates the total price of the selected components and applies a discount based on the number of additional items. The final price, along with the discount information, is then displayed.
The main part of the code takes user input, processes choices, and prints the selected components and their prices.
