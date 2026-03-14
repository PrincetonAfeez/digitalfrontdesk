import datetime  # Import the library to handle dates and times
import random    # Import the library to generate random numbers (for tables)

# The main function is the 'brain' of the program. It controls the order of events.
def main():
    print("\n--- Part A: Reservation InTake---\n")
    
    # We call get_resy_details() and 'catch' the 5 pieces of info it returns.
    # The order here must match the return order at the end of that function.
    first_name, last_name, head_count, children, allergies = get_resy_details()
    
    # We pass those 5 pieces of info into the next function as 'arguments'.
    handle_arrival(first_name, last_name, head_count, children, allergies)

# This function collects all the data needed to make a reservation.
def get_resy_details():
    print("\n--- Thanks for calling MyRestaurant to make a Reservation ---")
    
    # Use helper functions to get clean, validated text data
    first_name = get_name("First Name: ")
    last_name = get_name("Last Name: ")
    email = get_email("Email Address: ")

    # Loop until the user provides a valid phone number (digits only)
    while True:
        phone_number = input("Phone Number (digits only): ").strip()
        if phone_number.isdigit(): # Checks if the string contains only 0-9
            break
        print("Invalid input. Please enter numbers only.")

    # Loop for party size. We use 'try/except' to prevent the program from 
    # crashing if the user accidentally types letters instead of numbers.
    while True:
        try:
            head_count = int(input("How many adults? "))
            children = int(input("How many children? "))
            break
        except ValueError:
            print("Please enter a valid number.")

    # Get date and time using helper functions that talk to the 'datetime' library
    date = get_date("Reservation Date (YYYY-MM-DD): ")
    resy_time = get_time("Reservation Time (HH:MM): ")
    
    # Call the allergy collector
    allergies = get_allergies()

    # Final Confirmation print-out using f-strings for easy formatting
    print("\n--- Reservation Confirmed ---")
    print(f"Guest: {first_name} {last_name}")
    print(f"Contact: {email} | {phone_number}")
    print(f"Booking: {date} at {resy_time}")
    print(f"Group: You have {head_count} adults and {children} children.")
    
    # Only print the allergy alert if the list isn't empty
    if allergies:
        # ', '.join() takes a list like ['A', 'B'] and makes it 'A, B'
        print(f"!!! DIETARY ALERT: {', '.join(allergies)} !!!")
        
    print("-" * 29)
    print("--- Thanks for your reservation. ---")
    print("--- We look forward to seeing you ---")

    # Send the data back to main() so it can be used in Part B
    return first_name, last_name, head_count, children, allergies

# This function simulates the guest physically walking into the restaurant.
def handle_arrival(first_name, last_name, head_count, children, allergies):
    print(f"\n--- Part B: Guest Arrival ---")
    print(f"\n--- Welcome to MyRestaurant ---")
    print(f"Thanks for joining us: {first_name} {last_name}")
    print(f"Original Party Size: {head_count} Adults, {children} Children")
    
    # Immediately notify the host of any kitchen/allergy risks
    if allergies:
        print(f"\n*** KITCHEN ALERT: Guest has noted allergies: {', '.join(allergies)} ***")
        print("Ensure server & kitchen are notified before water service.")

    # Confirm if the party size has changed since the phone call
    while True:
        confirm = input("Is the party size still the same? (y/n): ").strip().lower()
        if confirm in ["y", "yes"]:
            total_guests = head_count + children # Add adults + children
            break
        elif confirm in ["n", "no"]:
            try:
                new_adults = int(input("Updated adult count: "))
                new_kids = int(input("Updated children count: "))
                total_guests = new_adults + new_kids
                break
            except ValueError:
                print("Please enter numbers only.")
        else:
            print("Please enter 'y' or 'n'.")
    
    # Assign a table using the get_table helper
    table_num = get_table()

    # Final professional greeting
    print(f"Thanks for joining us {first_name}, we have Table {table_num} ready for your party of {total_guests}.")

# --- HELPER FUNCTIONS ---
# These are small "tools" that do one specific job over and over again.

def get_allergies():
    """Asks if allergies exist, then builds a list of them."""
    allergies_list = []
    while True:
        choice = input("Any food allergies? (yes/no): ").strip().lower()
        if choice in ["n", "no"]:
            return [] # Return an empty list if no allergies
        elif choice in ["y", "yes"]:
            print("Enter allergies one by one (type 'done' when finished):")
            while True:
                item = input("> ").strip().title()
                if item.lower() == "done":
                    return allergies_list
                if item: # Don't add empty strings
                    allergies_list.append(item)
        else:
            print("Please answer 'yes' or 'no'.")

def get_table():
    """Handles the table preference and ensures the number is between 1 and 99."""
    while True:
        pref = input("Do you have a table preference? (yes/no): ").strip().lower()
        
        if pref in ["yes", "y"]:
            while True:
                try:
                    table = int(input("Enter Table Number (1-99): "))
                    if 1 <= table <= 99: # Logical check for range
                        return table
                    else:
                        print("Error: Table must be between 1 and 99.")
                except ValueError:
                    print("Error: Please enter a numeric value.")
                
        elif pref in ["no", "n"]:
            # Pick a random number between 1 and 99 inclusive
            selected = random.randint(1, 99)
            print(f"No problem! We've assigned you Table {selected}.")
            return selected
        else:
            print("Please answer with 'yes' or 'no'.")

def get_name(prompt):
    """Ensures names are not empty and only contain letters/spaces."""
    while True:
        # .title() makes 'john' become 'John'
        name = input(prompt).strip().title()
        if not name:
            continue
        # all() checks if every single character follows the rules provided
        if all(char.isalpha() or char in ["'", " "] for char in name):
            return name
        print("Invalid name format. Use letters, spaces, and apostrophes only.")

def get_email(prompt):
    """Checks for a basic email structure (contains @ and a dot)."""
    while True:
        email = input(prompt).strip().lower()
        # Basic logical check to see if '@' exists and comes before the '.'
        if "@" in email and "." in email and email.find("@") < email.rfind("."):
            return email
        print("Invalid email format.")

def get_date(prompt):
    """Uses the datetime library to ensure the date is real (e.g. rejects Feb 30)."""
    while True:
        try:
            # fromisoformat expects exactly YYYY-MM-DD
            return datetime.date.fromisoformat(input(prompt).strip())
        except ValueError:
            print("Use YYYY-MM-DD format.")

def get_time(prompt):
    """Ensures time is valid and automatically fixes 4-digit inputs like 9:00."""
    while True:
        try:
            time_input = input(prompt).strip()
            
            # If user types 1:30, we turn it into 01:30 so the computer understands it
            if len(time_input) == 4 and ":" in time_input and time_input.find(":") == 1:
                time_input = "0" + time_input 
            
            return datetime.time.fromisoformat(time_input)
        except ValueError:
            print("Use HH:MM format (24h).")

# This boilerplate code ensures main() only runs if the script is played directly, 
# not if it's imported as a library into another file.
if __name__ == "__main__":
    main()
