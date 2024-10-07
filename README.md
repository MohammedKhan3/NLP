### README for TechBot:
# Overview:
TechBot is an interactive Python program designed to assist users with a simulated tech shopping experience. It offers functionalities such as shopping for products, checking delivery status, managing payments, and managing a shopping cart.

# Features:
Shopping for Products: Users can view a list of tech products and add items to their shopping cart.
Managing the Cart: Users can add or remove products from their cart.
Checking Delivery Status: Users can check the delivery status of their order.
Payment: Users can make payments for the items in their cart by entering valid card details.
Exit: Users can exit the interaction by typing 'exit' or 'done.'

### Key Components:
Welcome Messages: Random welcome patterns are displayed when a user starts interacting with TechBot.
Product Catalog: A set of predefined tech products, each with a product number, description, and price.
Shopping Cart: Users can add or remove items from their cart, and the cart is cleared after successful payment.
Delivery Status: Random delivery statuses are generated to simulate tracking.
Payment System: A basic system that accepts card input (simulated by a 16-digit number) and processes the payment.
Goodbye Messages: When the user exits, a goodbye message is displayed.

### How it Works:
Initialization: When the TechBot is created, it initializes with predefined product details, welcome messages, and other interaction patterns.
Interaction: The user interacts with TechBot via text input. TechBot understands various commands such as shopping, payment, checking delivery status, and cart management based on user input.
Command Matching: The bot uses regex patterns to identify user intents and take corresponding actions like showing products, adding/removing items, processing payments, or providing a generic response when the input is not understood.
Loop: The program keeps running in a loop until the user types 'exit' or 'done' to terminate the interaction.

### Code Walkthrough:
greetUser(): Displays a random welcome message.
user_intents(user_input): Identifies user commands and directs them to the appropriate functionality (e.g., shop, payment, delivery).
show_products(): Displays the list of available tech products with their details.
addInCart(): Allows users to add products to their cart by entering the product number.
deleteFromCart(): Enables users to remove items from their cart.
defaultDelivery(): Randomly generates and displays a delivery status for the user.
paymentInfo(): Simulates a payment process by asking for a card number and processing the total cost.
generic(): Responds to unrecognized input with a generic response.
goodBye(): Displays a goodbye message when the user ends the session.

### Dependencies:
random and re for selecting random patterns and matching user input.
time to simulate delays (e.g., for loading products or processing payments).

### How to Run:
Instantiate the TechBot class.
The program starts by greeting the user and enters a loop, awaiting user input.
The user can interact with the bot by entering commands like 'shop,' 'payment,' 'delete,' 'delivery,' or 'exit.'

### Future Improvements:
Integrate real product data from an API or database.
Add more robust error handling for inputs.
Implement user authentication and order history tracking.
