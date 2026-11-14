from .domain import *

def main_menu():
    print("=== Pharma Distribution CLI ===")
    mfg = Manufacturer("PharmaCorp", "Germany", "LIC-123")
    aspirin = Medicine("Aspirin", "500mg", "Tablet", requires_prescription=False)
    aspirin.set_price(10.50)
    mfg.add_medicine(aspirin)
    batch = Batch("B001", aspirin, 100, "2026-12-31")
    aspirin.attach_batch(batch)
    client = Client("City Hospital", "Hospital")

    while True:
        print("\n--- MAIN MENU ---")
        print("1. View Medicine Inventory")
        print("2. Place Order")
        print("3. Exit")
        choice = input("Select an option: ").strip()

        if choice == "1":
            stock = aspirin.calculate_available_stock()
            print(f"\nMedicine: {aspirin.name} | Available: {stock} | Price: ${aspirin.price}")
        elif choice == "2":
            try:
                qty = int(input("Enter quantity: "))
                order = Order(101, client)
                order.add_line(OrderLine(aspirin, qty))
                order.submit()
                invoice = Invoice("INV-101", order)
                payment = Payment(invoice.total, "Credit Card")
                payment.process(invoice)
                client.place_order(order)
                batch.deduct_quantity(qty)
                print(f"Order placed! Total: ${order.calculate_total():.2f} | Paid: {invoice.is_paid}")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main_menu()