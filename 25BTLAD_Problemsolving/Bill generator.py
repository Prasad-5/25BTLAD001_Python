print("===== BILL GENERATOR =====")
customer = input("Enter customer name: ")
 
# Number of items (ask again until a valid number is entered)
n = int(input("Enter number of items: "))
while n <= 0:
    print("Number of items must be greater than 0.")
    n = int(input("Enter number of items: "))
 
names = []
prices = []
quantities = []
 
# Read the details of every item using a loop
for i in range(1, n + 1):
    print(f"\nItem {i}")
    names.append(input("Enter item name: "))
 
    price = float(input("Enter price: "))
    while price <= 0:
        print("Price must be greater than 0.")
        price = float(input("Enter price: "))
    prices.append(price)
 
    qty = int(input("Enter quantity: "))
    while qty <= 0:
        print("Quantity must be greater than 0.")
        qty = int(input("Enter quantity: "))
    quantities.append(qty)
 
# Print the bill
print("\n" + "=" * 44)
print(f"{'BILL':^44}")
print("=" * 44)
print(f"Customer: {customer}")
print("-" * 44)
print(f"{'Item':<16}{'Qty':>5}{'Price':>11}{'Amount(₹)':>12}")
print("-" * 44)
 
subtotal = 0
for i in range(n):
    amount = prices[i] * quantities[i]
    subtotal += amount
    print(f"{names[i]:<16}{quantities[i]:>5}"
          f"{prices[i]:>11.2f}{amount:>12.2f}")
 
# 10% discount if subtotal >= 1000; GST is 5% of the discounted amount
if subtotal >= 1000:
    discount = subtotal * 0.10
else:
    discount = 0
gst = (subtotal - discount) * 0.05
grand_total = subtotal - discount + gst
 
print("-" * 44)
print(f"{'Subtotal':<32}{subtotal:>12.2f}")
print(f"{'Discount (10%)':<32}{-discount:>12.2f}")
print(f"{'GST (5%)':<32}{gst:>12.2f}")
print("=" * 44)
print(f"{'GRAND TOTAL (₹)':<32}{grand_total:>12.2f}")
print("=" * 44)
print(f"Thank you for shopping, {customer}!")
