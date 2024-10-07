import random
import re
import time

class TechBot:
    def __init__(self):
        self.welcome_patterns = (
            "Welcome to TechBot! How can I assist you today? Please choose from the following options: 1️⃣ Shop for tech products, 2️⃣ Check delivery status, 3️⃣ Manage payments",
            "Hi there! I'm TechBot, here to help with all your tech needs. You can: 🛍️ Browse our tech shop, 🚚 Track your delivery, 💳 Get help with payment options",
            "Hello! TechBot at your service. What would you like to do today? 🔍 Shop for new gadgets, 📦 Check the delivery of your order, 💰 Make a payment or review payment details"
        )
        self.generic_responses = (
            "I'm sorry, I didn't quite catch that. Can you please rephrase?",
            "Sure! Let me help you with that.",
            "Please wait a moment while I retrieve that information for you.",
            "If you need further assistance, feel free to ask me anytime!"
        )
        self.menuPatterns = (
            "What would you like to do next? Choose from the following options: 1️⃣ Shop more 🛍️, 2️⃣ Delete items 🗑️, 3️⃣ Proceed to payment 💳, 4️⃣ Check delivery status 🚚, or type 'exit' to leave.",
            "Please select an option: 1️⃣ Continue shopping 🛒, 2️⃣ Remove items from cart ❌, 3️⃣ Make a payment 💸, 4️⃣ Track your delivery 📦, or type 'exit' to end the session.",
            "Here’s what you can do: 1️⃣ Shop for more products 🛍️, 2️⃣ Delete items from cart 🗑️, 3️⃣ Proceed to payment 💳, 4️⃣ Check delivery 🚚. Type 'exit' to leave.",
            "Your options: 1️⃣ Shop more 🛍️, 2️⃣ Delete from cart ❌, 3️⃣ Payment 💸, 4️⃣ Delivery status 🚚. Type 'exit' to quit.",
            "What would you like to do? 1️⃣ Shop 🛒, 2️⃣ Remove items 🗑️, 3️⃣ Payment 💳, 4️⃣ Delivery status 🚚, or type 'exit' to leave."
        )

        self.delivery_responses = [
            "Your package is out for delivery and will arrive today! 🚚",
            "Your order has been delayed due to weather conditions. Expected delivery tomorrow. ☁️",
            "Your package is in transit and should arrive within 2 days. 📦",
            "Your order has been shipped and is on its way. Estimated delivery: 3 days. 🚀",
            "Your order is being processed. We will notify you once it ships. 📬"
        ]
        self.tech_products = (
            (101, "A powerful smartphone with 128GB storage and 5G capability", "Smartphone X", 699),
            (102, "High-performance laptop with 16GB RAM and 512GB SSD", "Laptop Pro", 1299),
            (103, "Wireless noise-cancelling over-ear headphones", "Headphones Elite", 199),
            (104, "Smartwatch with fitness tracking and heart rate monitor", "Smartwatch 360", 249),
            (105, "4K Ultra HD smart TV with HDR and voice control", "Smart TV Ultra", 999),
            (106, "Compact wireless Bluetooth speaker with deep bass", "Bluetooth Speaker", 149)
        )
        self.goodbye_patterns = (
            "Goodbye! Thanks for using TechBot, have a great day! 👋",
            "It was a pleasure assisting you. See you next time! 😊",
            "Take care! Don’t hesitate to return if you need any tech help! 💻",
            "Goodbye! If you need more assistance, TechBot will be here! ✨",
            "Thank you for visiting! Stay tech-savvy and come back soon! 🙌",
            "Farewell! I’ll be ready to help whenever you need me again. 🎉"
        )

        self.cart = []
        self.paid = False
        self.pattern = {
            "shop": r"\b(shop|add)\b",
            "delivery": r"\bdelivery|track your delivery| track order| delivery status\b",
            "payment": r"\b(payment|pay)\b",
            "exit": r"\b(exit|goodbye|bye|leave)\b",
            "delete": r"\b(delete|remove)\b"
        }
    def showMenuPatterns(self):
        menu = random.choice(self.menuPatterns)
        print(menu)

    def greetUser(self):
        welcome = random.choice(self.welcome_patterns)
        print(welcome)

    def defaultDelivery(self):
        print("Checking Status....")
        time.sleep(2)
        delivery = random.choice(self.delivery_responses)
        print(delivery)
        self.showMenuPatterns()

    def show_products(self):
        print("Loading Products...")
        time.sleep(1)
        print("Available Products:")
        for p in self.tech_products:
            print(f"Product Number: {p[0]} \nName: {p[2]}\nDescription: {p[1]}\nPrice: ${p[3]}\n")
            time.sleep(1)

    def goodBye(self):
        bye = random.choice(self.goodbye_patterns)
        print(bye)

    def user_intents(self, user_input):
        if re.search(self.pattern["shop"], user_input, re.IGNORECASE):
            self.show_products()
            self.addInCart()
        elif re.search(self.pattern["delivery"], user_input, re.IGNORECASE):
            self.defaultDelivery()
        elif re.search(self.pattern["payment"], user_input, re.IGNORECASE):
            self.paymentInfo()
        elif re.search(self.pattern["delete"], user_input, re.IGNORECASE):
            self.deleteFromCart()
        elif re.search(self.pattern["exit"], user_input, re.IGNORECASE):
            self.goodBye()
        else:
            self.generic()

    def paymentInfo(self):
        if self.paid:
            print("Payment has already been completed for this order.")
            return

        if not self.cart:
            print("Your cart is empty. Add items to your cart before making a payment.")
            return

        total = sum(item[3] for item in self.cart)
        order_number = random.randint(1000, 9999)
        print(f"Your total is ${total}. Your order number is {order_number}.")

        while True:
            card_input = input("Please enter your card details (format 16 digits): ")
            if re.match(r"^\d{16}$", card_input):
                print("Card accepted. Processing payment...")
                time.sleep(2)
                self.paid = True
                print("Payment successful! Thank you for your purchase.")
                self.cart = []  # Clear the cart after payment
                break
            else:

                print("Invalid card details. Please try again.")
        self.showMenuPatterns()


    def addInCart(self):
        while True:
            print("Enter product number to add to the cart (or type 'done' to finish): ")
            p_num = input("You: ").lower()
            if p_num == 'done':
                break
            try:
                p_num = int(p_num)
                product_found = False
                for p in self.tech_products:
                    if p_num == p[0]:
                        self.cart.append(p)
                        print(f"Product '{p[2]}' added to the cart.")
                        product_found = True
                        break
                if not product_found:
                    print("Product not available.")
            except ValueError:
                print("Invalid input. Please enter a valid product number.")
        self.showMenuPatterns()

    def deleteFromCart(self):
        while True:
            if not self.cart:
                print("Your cart is empty.")
                break
            print("Your current cart:")
            for item in self.cart:
                print(f"Product Number: {item[0]} - {item[2]} - ${item[3]}")
            print("Enter the product number to delete (or type 'done' to finish):")
            p_num = input("You: ").lower()
            if p_num == 'done':
                break
            try:
                p_num = int(p_num)
                product_found = False
                for p in self.cart:
                    if p_num == p[0]:
                        self.cart.remove(p)
                        print(f"Product '{p[2]}' removed from the cart.")
                        product_found = True
                        break
                if not product_found:
                    print("Product not found in the cart.")
            except ValueError:
                print("Invalid input. Please enter a valid product number.")
        self.showMenuPatterns()

    def generic(self):
        response = random.choice(self.generic_responses)
        print(response)


# Sample interaction with TechBot
bot = TechBot()
bot.greetUser()

while True:
    user_input = input("You: ").lower()
    if re.search(r"(exit|done)", user_input):
        bot.goodBye()
        break
    else:
        bot.user_intents(user_input)
