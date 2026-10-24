"""Console menu for the Polynomial class."""
try:
    from .Polynomial import Polynomial
except ImportError:
    from Polynomial import Polynomial


def get_polynomial(prompt: str) -> Polynomial:
    while True:
        try:
            raw_input = input(prompt).strip()
            if not raw_input:
                raise ValueError("Input cannot be empty.")
            parts = [float(num.strip()) for num in raw_input.split(",")]
            return Polynomial(*parts)
        except (TypeError, ValueError) as error:
            print(f"Invalid polynomial: {error}")


def main_menu() -> None:
    print(
        "Enter two polynomials to start by providing coefficients "
        "in ascending power order."
    )
    print("Example: entering '1,2,3' creates 3.0x^2 + 2.0x + 1.0")
    print("-" * 75)
    first = get_polynomial("First polynomial coefficients: ")
    second = get_polynomial("Second polynomial coefficients: ")

    while True:
        print("\n--- SELECT AN OPTION ---")
        print("1. Enter two new polynomials")
        print("2. Add the polynomials")
        print("3. Subtract the polynomials")
        print("4. Multiply the polynomials")
        print("5. Divide the first by the second (exact division)")
        print("6. Show the polynomials' degrees")
        print("7. Evaluate the first polynomial at a point x")
        print("8. Negate the first polynomial")
        print("9. Exit\n")

        choice = input("Choose an option: ").strip()

        if not choice:
            continue

        try:
            if choice == "1":
                first = get_polynomial("First polynomial coefficients: ")
                second = get_polynomial("Second polynomial coefficients: ")
                input("\nPolynomials updated. Press Enter...")
            elif choice == "2":
                print("\nResult:", first + second)
                input("\nPress Enter to return to menu...")
            elif choice == "3":
                print("\nResult:", first - second)
                input("\nPress Enter to return to menu...")
            elif choice == "4":
                print("\nResult:", first * second)
                input("\nPress Enter to return to menu...")
            elif choice == "5":
                print("\nResult:", first / second)
                input("\nPress Enter to return to menu...")
            elif choice == "6":
                print("\nFirst Polynomial Degree:", first.degree)
                print("Second Polynomial Degree:", second.degree)
                input("\nPress Enter to return to menu...")
            elif choice == "7":
                try:
                    x_val = float(
                        input("Enter a real number value for x: ").strip()
                    )
                    print(
                        f"\nResult of evaluation at x={x_val}:",
                        first(x_val),
                    )
                except ValueError:
                    print("\nInvalid number provided for x.")
                input("\nPress Enter to return to menu...")
            elif choice == "8":
                print("\nNegated Result:", -first)
                input("\nPress Enter to return to menu...")
            elif choice == "9":
                print("Goodbye.")
                break
            else:
                print("Please choose a number from 1-9.")
                input("\nPress Enter to try again...")
        except (TypeError, ValueError, ZeroDivisionError) as error:
            print(f"Error: {error}")
            input("\nPress Enter to return to menu...")


if __name__ == "__main__":
    main_menu()