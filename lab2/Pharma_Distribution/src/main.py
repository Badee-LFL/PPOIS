from src.models import *
from src.exceptions import *

def main_menu():
    print("=== Pharma Distribution CLI ===")
    mfg = Manufacturer("PharmaCorp", "Germany")
    client = Client("City Hospital", "Hospital")
    
    aspirin = Medicine("Aspirin", "500mg", False)
    aspirin.set_price(10.50)
    mfg.add_medicine(aspirin)
    aspirin.attach_batch(Batch("B001", aspirin, 100, "2026-12-31"))

    while True:
        print("\n--- MAIN MENU ---")
        print("1. View Inventory")
        print("2. Add New Medicine")
        print("3. Place Order")
        print("4. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            for med in mfg.medicines:
                print(f"{med.name} ({med.dosage}) | Stock: {med.calculate_available_stock()} | Price: ${med.price}")
                
        elif choice == "2":
            try:
                name = input("Enter medicine name: ")
                dosage = input("Enter dosage: ")
                price = float(input("Enter price: "))
                qty = int(input("Enter stock qty: "))
                
                new_med = Medicine(name, dosage, False)
                new_med.set_price(price)
                mfg.add_medicine(new_med)
                new_med.attach_batch(Batch(f"B{len(mfg.medicines)}", new_med, qty, "2027-12-31"))
                print(f"Added {new_med.name}!")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "3":
            med_name = input("Enter medicine name to order: ")
            target = next((m for m in mfg.medicines if m.name.lower() == med_name.lower()), None)
            if not target:
                print("Not found!")
                continue
            try:
                qty = int(input(f"Enter qty of {target.name}: "))
                order = Order(101, client)
                order.add_line(OrderLine(target, qty))
                order.submit()
                invoice = Invoice("INV-101", order)
                payment = Payment(invoice.total, "Credit Card")
                payment.process(invoice)
                client.place_order(order)
                target.batches[0].deduct_quantity(qty)
                print(f"Order placed! Total: ${order.calculate_total():.2f}")
            except Exception as e:
                print(f"Failed: {e}")

        elif choice == "4":
            break

if __name__ == "__main__":
    main_menu()