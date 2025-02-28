# Delivery Management System

# Customer Class
class Customer:
    #Represents a customer in the delivery management system.

    def __init__(self, customer_id, name, email, phone_number, address, registration_date):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.registration_date = registration_date

    # Setters and Getters
    def setCustomerId(self, customer_id):
        self.customer_id = customer_id

    def getCustomerId(self):
        return self.customer_id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

    def setPhoneNumber(self, phone_number):
        self.phone_number = phone_number

    def getPhoneNumber(self):
        return self.phone_number

    def setAddress(self, address):
        self.address = address

    def getAddress(self):
        return self.address

    def setRegistrationDate(self, registration_date):
        self.registration_date = registration_date

    def getRegistrationDate(self):
        return self.registration_date

    # Display function
    def displayCustomerInfo(self):
        print(
            f"Customer ID: {self.customer_id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone_number}, Address: {self.address}, Registered: {self.registration_date}")


# Order Class
class Order:
    #Represents an order placed by a customer.

    def __init__(self, order_id, order_date, status, total_amount, customer_id):
        self.order_id = order_id
        self.order_date = order_date
        self.status = status
        self.total_amount = total_amount
        self.customer_id = customer_id

    # Setters and Getters
    def setOrderId(self, order_id):
        self.order_id = order_id

    def getOrderId(self):
        return self.order_id

    def setOrderDate(self, order_date):
        self.order_date = order_date

    def getOrderDate(self):
        return self.order_date

    def setStatus(self, status):
        self.status = status

    def getStatus(self):
        return self.status

    def setTotalAmount(self, total_amount):
        self.total_amount = total_amount

    def getTotalAmount(self):
        return self.total_amount

    def setCustomerId(self, customer_id):
        self.customer_id = customer_id

    def getCustomerId(self):
        return self.customer_id

    # Display function
    def displayOrderInfo(self):
        print(
            f"Order ID: {self.order_id}, Date: {self.order_date}, Status: {self.status}, Total: {self.total_amount}, Customer ID: {self.customer_id}")


# Item Class
class Item:
    #Represents an item in an order.

    def __init__(self, item_id, item_name, item_description, price, quantity, order_id):
        self.item_id = item_id
        self.item_name = item_name
        self.item_description = item_description
        self.price = price
        self.quantity = quantity
        self.order_id = order_id

    # Setters and Getters
    def setItemId(self, item_id):
        self.item_id = item_id

    def getItemId(self):
        return self.item_id

    def setItemName(self, item_name):
        self.item_name = item_name

    def getItemName(self):
        return self.item_name

    def setItemDescription(self, item_description):
        self.item_description = item_description

    def getItemDescription(self):
        return self.item_description

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price

    def setQuantity(self, quantity):
        self.quantity = quantity

    def getQuantity(self):
        return self.quantity

    def setOrderId(self, order_id):
        self.order_id = order_id

    def getOrderId(self):
        return self.order_id

    # Display function
    def displayItemInfo(self):
        print(
            f"Item ID: {self.item_id}, Name: {self.item_name}, Description: {self.item_description}, Price: {self.price}, Quantity: {self.quantity}, Order ID: {self.order_id}")


# Payment Class
class Payment:
    #Represents a payment transaction for an order.

    def __init__(self, payment_id, amount, payment_method, payment_status, order_id):
        self.payment_id = payment_id
        self.amount = amount
        self.payment_method = payment_method
        self.payment_status = payment_status
        self.order_id = order_id

    # Setters and Getters
    def setPaymentId(self, payment_id):
        self.payment_id = payment_id

    def getPaymentId(self):
        return self.payment_id

    def setAmount(self, amount):
        self.amount = amount

    def getAmount(self):
        return self.amount

    def setPaymentMethod(self, payment_method):
        self.payment_method = payment_method

    def getPaymentMethod(self):
        return self.payment_method

    def setPaymentStatus(self, payment_status):
        self.payment_status = payment_status

    def getPaymentStatus(self):
        return self.payment_status

    def setOrderId(self, order_id):
        self.order_id = order_id

    def getOrderId(self):
        return self.order_id

    # Display function
    def displayPaymentInfo(self):
        print(
            f"Payment ID: {self.payment_id}, Amount: {self.amount}, Method: {self.payment_method}, Status: {self.payment_status}, Order ID: {self.order_id}")


# Delivery Class
class Delivery:
    #Represents the delivery details of an order.

    def __init__(self, tracking_number, delivery_status, delivery_date, order_id, courier_name, delivery_address):
        self.tracking_number = tracking_number
        self.delivery_status = delivery_status
        self.delivery_date = delivery_date
        self.order_id = order_id
        self.courier_name = courier_name
        self.delivery_address = delivery_address

    # Setters and Getters

    def setTrackingNumber(self, tracking_number):
        self.tracking_number = tracking_number

    def getTrackingNumber(self):
        return self.tracking_number

    def setDeliveryStatus(self, delivery_status):
        self.delivery_status = delivery_status

    def getDeliveryStatus(self):
        return self.delivery_status

    def setDeliveryDate(self, delivery_date):
        self.delivery_date = delivery_date

    def getDeliveryDate(self):
        return self.delivery_date

    def setOrderId(self, order_id):
        self.order_id = order_id

    def getOrderId(self):
        return self.order_id

    def setCourierName(self, courier_name):
        self.courier_name = courier_name

    def getCourierName(self):
        return self.courier_name

    def setDeliveryAddress(self, delivery_address):
        self.delivery_address = delivery_address

    def getDeliveryAddress(self):
        return self.delivery_address

    # Display function
    def displayDeliveryInfo(self):
        print(
            f"Tracking Number: {self.tracking_number}, Status: {self.delivery_status}, Date: {self.delivery_date}, Order ID: {self.order_id}, Courier: {self.courier_name}, Address: {self.delivery_address}")


#  Testing the Classes (Creating Two Objects Per Class):

# Printing Delivery Note Message
print("Delivery Note:")
print()
print("Thank you for using our delivery service! Please print your delivery reciept and present it upon recieving your items.")
print()
print("Recipient Details:")
# Testing Customer Class
customer1 = Customer("CUST001", "Sarah Johnson", "sarah.johnson@example.com", "0551234567",
                     "45 Knowledge Avenue, Dubai, UAE", "2025-01-01")
customer2 = Customer("CUST002", "Maha Alhosani", "Maha.Alhosani@example.com", "0557654321", "Khalifa City, Abu Dhabi, UAE",
                     "2025-02-15")

customer1.displayCustomerInfo()
customer2.displayCustomerInfo()
print()  # Spacing for clarity

print("Delivery Information:")
# Testing Order Class
order1 = Order("ORD001", "2025-01-25", "Shipped", 283.50, "CUST001")
order2 = Order("ORD002", "2025-02-10", "Processing", 150.00, "CUST002")

order1.displayOrderInfo()
order2.displayOrderInfo()
print()  # Spacing for clarity

print("Summary of items Delivered:")
# Testing Item Class
item1 = Item("ITM001", "Wireless Keyboard", "Compact keyboard", 100.00, 1, "ORD001")
item2 = Item("ITM002", "Laptop Stand", "Adjustable stand for laptop", 75.00, 2, "ORD002")

item1.displayItemInfo()
item2.displayItemInfo()
print()  # Spacing for clarity

print("Payment:")
# Testing Payment Class
payment1 = Payment("PAY001", 283.50, "Credit Card", "Completed", "ORD001")
payment2 = Payment("PAY002", 150.00, "Cash on Delivery", "Pending", "ORD002")

payment1.displayPaymentInfo()
payment2.displayPaymentInfo()
print()  # Spacing for clarity

print("Delivery Status:")
# Testing Delivery Class
delivery1 = Delivery("DEL123456789", "Out for Delivery", "2025-01-25", "ORD001", "DHL",
                     "45 Knowledge Avenue, Dubai, UAE")
delivery2 = Delivery("DEL987654321", "Delivered", "2025-02-12", "ORD002", "FedEx", "Khalifa City, Abu Dhabi, UAE")

delivery1.displayDeliveryInfo()
delivery2.displayDeliveryInfo()
print()  # Spacing for clarity


