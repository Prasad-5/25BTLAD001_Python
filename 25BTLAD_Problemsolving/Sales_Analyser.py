products = {"Notebook": [20, 45.0], "Pen": [50, 10.0], "File": [15, 30.0]}
 
while True:
    print("\n===== SALES DATA ANALYZER =====")
    ch = input("1.Add/Update  2.Display  3.Summary  4.Exit: ")
 
    if ch == "1":
        name = input("Product name: ").strip().title()
        try:
            qty = int(input("Quantity sold: "))
            price = float(input("Unit price (Rs.): "))
            if not name or qty < 0 or price < 0:
                raise ValueError
            products[name] = [qty, price]
            print("Record saved.")
        except ValueError:
            print("Invalid input.")
 
    elif ch == "2":
        print(f"{'Product':<12}{'Qty':>6}{'Price':>9}{'Revenue':>10}")
        for n, (q, p) in products.items():
            print(f"{n:<12}{q:>6}{p:>9.2f}{q * p:>10.2f}")
 
    elif ch == "3":
        rev = {n: q * p for n, (q, p) in products.items()}
        print("Total quantity :", sum(q for q, p in products.values()))
        print(f"Total revenue  : Rs. {sum(rev.values()):.2f}")
        print("Best seller    :", max(products, key=lambda n: products[n][0]))
        print("Top revenue    :", max(rev, key=rev.get))
 
    elif ch == "4":
        break
    else:
        print("Invalid choice.")
