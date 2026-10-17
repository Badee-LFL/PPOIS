from Vector import Vector3D 


def get_vector(prompt: str) -> Vector3D:
    while True:
        try:
            return Vector3D.from_string(input(prompt))
        except (TypeError, ValueError) as error:
            print(f"Invalid vector: {error}")


def main_menu() -> None:
    print("Enter two vectors to start (for example: 1,2,3)")
    first = get_vector("First vector: ")
    second = get_vector("Second vector: ")

    while True:
        print("\n--- SELECT AN OPTION ---")
        print("1. Enter two new vectors")
        print("2. Add the vectors")
        print("3. Subtract the vectors")
        print("4. Dot product")
        print("5. Cross product")
        print("6. Show the vectors' lengths")
        print("7. Find the cosine between the vectors")
        print("8. Exit\n")

        choice = input("Choose an option: ").strip()

        if not choice:
            continue

        try:
            if choice == "1":
                first = get_vector("First vector: ")
                second = get_vector("Second vector: ")
                input("\nVectors updated successfully! Press Enter to continue...")
            elif choice == "2":
                print("\nResult:", first + second)
                input("\nPress Enter to return to menu...")
            elif choice == "3":
                print("\nResult:", first - second)
                input("\nPress Enter to return to menu...")
            elif choice == "4":
                print("\nResult:", first.dot(second))
                input("\nPress Enter to return to menu...")
            elif choice == "5":
                print("\nResult:", first.cross(second))
                input("\nPress Enter to return to menu...")
            elif choice == "6":
                print("\nFirst Vector Length:", first.length())
                print("Second Vector Length:", second.length())
                input("\nPress Enter to return to menu...")
            elif choice == "7":
                print("\nCosine:", first.cosine_with(second))
                input("\nPress Enter to return to menu...")
            elif choice == "8":
                print("Goodbye.")
                break
            else:
                print("Please choose a number from 1-8.")
                input("\nPress Enter to try again...")
        except (TypeError, ValueError, ZeroDivisionError) as error:
            print(f"Could not perform that operation: {error}")
            input("\nPress Enter to return to menu...")


if __name__ == "__main__":
    main_menu()
