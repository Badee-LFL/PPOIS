import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from domain import Manufacturer, Medicine, Batch, Client, Order, OrderLine

def main():
    print("=== Pharma Distribution CLI ===")
    
    mfg = Manufacturer("PharmaCorp", "Germany")
    med = Medicine("Aspirin", "500mg", mfg)
    med.set_price(10.00)
    batch = Batch("B1", med, 100)
    med.attach_batch(batch)
    client = Client(1, "City Hospital")

    while True:
        print("\n1. View Inventory\n2. Place Order\n3. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            print(f"Medicine: {med.name} | Available: {med.get_total_available()} | Price: ${med.price}")
        elif choice == "2":
            try:
                qty = int(input("Enter quantity: "))
                order = Order(101, client)
                order.add_line(OrderLine(med, qty))
                order.submit()
                print(f"Order submitted! Total: ${order.calculate_total():.2f}")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "3":
            break

if __name__ == "__main__":
    main()