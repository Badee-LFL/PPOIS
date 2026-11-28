from src.models import *

def main_menu():
    print("=== Pharma Distribution CLI ===")
    
    mfg = Manufacturer("PharmaCorp")
    client = Client("City Hospital")
    
    # Pre-load Aspirin
    aspirin = Medicine("Aspirin", "500mg", False)
    aspirin.set_price(10.50)
    aspirin.attach_batch(Batch("B001", aspirin, 100, "2026-12-31"))
    mfg.add_medicine(aspirin)

    while True:
        print("\n--- MAIN MENU ---")
        print("1. View Inventory")
        print("2. Place Order")
        print("3. Add New Medicine")
        print("4. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            print("\n--- INVENTORY ---")
            for med in mfg.medicines:
                print(f"{med.name} ({med.dosage}) | Stock: {med.calculate_available_stock()} | Price: ${med.price}")
                
        elif choice == "2":
            print("\n--- PLACE ORDER ---")
            # 1. Ask for Medicine Name FIRST
            med_name = input("Enter medicine name: ").strip()
            
            target_med = next((m for m in mfg.medicines if m.name.lower() == med_name.lower()), None)
            
            if not target_med:
                print(f"Medicine '{med_name}' not found!")
                continue
                
            # 2. Ask for Quantity SECOND
            try:
                qty = int(input(f"Enter quantity of {target_med.name}: "))
                order = Order(101, client)
                order.add_line(OrderLine(target_med, qty))
                order.submit()
                client.place_order(order)
                target_med.batches[0].deduct_quantity(qty)
                print(f"Order placed for {qty} {target_med.name}! Total: ${order.calculate_total():.2f}")
            except Exception as e:
                print(f"Order Failed: {e}")
                
        elif choice == "3":
            try:
                name = input("Enter medicine name: ")
                dosage = input("Enter dosage: ")
                price = float(input("Enter price: "))
                qty = int(input("Enter initial stock quantity: "))
                
                new_med = Medicine(name, dosage, False)
                new_med.set_price(price)
                new_med.attach_batch(Batch(f"B{len(mfg.medicines)+1}", new_med, qty, "2027-12-31"))
                mfg.add_medicine(new_med)
                print(f"Successfully added {new_med.name}!")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "4":
            print("Goodbye.")
            break

if __name__ == "__main__":
    main_menu()