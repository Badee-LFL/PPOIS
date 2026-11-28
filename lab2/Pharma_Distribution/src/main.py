from src.models import *

def main_menu():
    print("=== Pharma Distribution CLI ===")
    mfg = Manufacturer("PharmaCorp")
    client = Client("City Hospital")
    
    aspirin = Medicine("Aspirin", "500mg", False)
    aspirin.set_price(10.50)
    aspirin.attach_batch(Batch("B001", aspirin, 100, "2026-12-31"))

    while True:
        print("\n--- MAIN MENU ---")
        print("1. View Inventory")
        print("2. Place Order")
        print("3. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            print(f"{aspirin.name} | Stock: {aspirin.calculate_available_stock()} | Price: ${aspirin.price}")
                
        elif choice == "2":
            try:
                qty = int(input(f"Enter quantity of {aspirin.name}: "))
                order = Order(101, client)
                order.add_line(OrderLine(aspirin, qty))
                order.submit()
                client.place_order(order)
                aspirin.batches[0].deduct_quantity(qty)
                print(f"Order placed! Total: ${order.calculate_total():.2f}")
            except Exception as e:
                print(f"Failed: {e}")

        elif choice == "3":
            break

if __name__ == "__main__":
    main_menu()