"""Console menu for the Pharma Distribution System."""
import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from domain import (
    Manufacturer, Medicine, Batch, Client, Order, OrderLine, 
    Payment, Invoice, Pharmacist, Doctor, Prescription
)
from exceptions import InsufficientStockException, PrescriptionRequiredException

def main_menu():
    print("=== Pharma Distribution CLI ===")
    
    # Setup dummy data
    mfg = Manufacturer("PharmaCorp", "Germany", "LIC-123")
    aspirin = Medicine("Aspirin", "500mg", "Tablet", requires_prescription=False)
    aspirin.set_price(10.50)
    mfg.add_medicine(aspirin)
    
    batch = Batch("B001", aspirin, 100, "2026-12-31")
    aspirin.attach_batch(batch)
    
    client = Client("City Hospital", "Hospital")
    pharmacist = Pharmacist("John Doe", "PH-999")
    
    while True:
        print("\n--- MAIN MENU ---")
        print("1. View Medicine Inventory")
        print("2. Place Order")
        print("3. Dispense Prescription")
        print("4. Exit")
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
            except InsufficientStockException as e:
                print(f"Error: {e}")
                
        elif choice == "3":
            try:
                doc = Doctor("Dr. Smith", "DOC-1")
                med = Medicine("Morphine", "10mg", "Liquid", requires_prescription=True)
                script = doc.write_prescription(med, "John Patient")
                pharmacist.dispense(script)
                print("Prescription dispensed successfully.")
            except PrescriptionRequiredException as e:
                print(f"Error: {e}")
                
        elif choice == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main_menu()