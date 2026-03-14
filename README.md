# digitalfrontdesk
Python Script that handles guest reservations and guest arrivals

Project: "Digital Front Desk"
Part A: Build a script that handles a Restaurant Reservations.
Part B: Build a script that handles a guest's arrival.

Part A: 
1. Asks the guest for their full name, email address & phone number.
2. Asks the guest for the number in their party and reservation time.
3. Cleans the all the data so it is properly formatted. Remove spaces, capitalized, establish AM vs PM
4. Print a formal confirmation message.

Part B:
1. Asks the guest for their full name.
Asks the guest if they have a table preference

2. Asks the guest for their favorite table number.
3. Cleans the name so it is properly capitalized (e.g., "john doe" becomes "John Doe") even if the guest is messy with their typing.
4. Removes any accidental spaces before or after the name.
5. Prints a professional welcome message: "Welcome to Our Restaurant, [Name]. We have reserved Table [Number] for you."

Pseudocode

Part A: The Reservation Logic
Goal: Gather, sanitize, and validate contact, booking, and dietary details.

1. Define a main function: Orchestrate the flow by capturing returned data from Part A and passing it to Part B.
2. Input & Sanitize (Strings):
*Name: Prompt for names. Strip whitespace and use .title() for proper casing.
*Email: Prompt for email. Strip whitespace and use .lower(). Validate that it contains an "@" and a "." in the correct order.
*Phone: Prompt for digits. Use .isdigit() to ensure it's a valid number string without losing leading zeros.
3. Input & Validation (Numbers/Exceptions):
*Start a Loop: Use while True to ask for adults and children.
*Try/Except: Attempt to convert inputs to int. If a ValueError occurs, print a helpful message and restart the loop.
4. Input & Formatting (Date/Time/Allergies):
*Date: Prompt for YYYY-MM-DD. Use datetime logic to ensure the date actually exists.
*Time: Prompt for HH:MM. Include logic to automatically add a leading "0" if the user types a 4-digit time (like 9:00).
*Allergies: Start a Nested Loop. Ask if allergies exist. If "yes," allow the user to keep adding items to a List until they type "done."
5. Output:
*Print a formatted summary using f-strings. Include a special conditional "Alert" if the allergy list is not empty.

Part B: The Arrival Logic
Goal: Handle the physical check-in, verify party changes, and enforce table rules.

1. Define handle_arrival: Accept the variables (Name, Party Size, Allergies) passed from Part A.
2. Verify & Alert:
*Immediately print a "Kitchen Alert" if any allergies were passed in the data.
*Start a Loop: Ask if the party size is still the same.
*If "no": Use a Try/Except block to collect and update the new total_guests.
3. Conditionals & Nested Validation (Tables):
*Ask: "Do you have a table preference? (yes/no)".
*If "yes":
    -Start a Nested Loop: Prompt for a table number.
    -Range Check: Use an if statement to ensure the number is strictly between 1 and 99.
    -Try/Except: Ensure the input is a valid integer. If it fails the range or the type, keep the user inside this nested loop.
*Else ("no"):
    -Use the random library to pick a table number between 1 and 99 automatically.
4. Final Output:
*Print the professional welcome message: "Thanks for joining us [Name], we have Table [Table Number] ready for your party of [Total]."
