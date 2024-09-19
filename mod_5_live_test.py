def ticket_price_calculator(age, showtime):

    if age <= 10:
        ticket_price = 300
    elif 11 <= age <= 25:
        ticket_price = 500
    elif 26 <= age <= 60:
        ticket_price = 800
    elif age > 60:
        ticket_price = 400
    else:
        return "Age must be a positive integer number."
    
    discount = 0

    if showtime < 1700:
        discount = ticket_price * 0.10

    discount_price = ticket_price - discount

    outcome = f"Ticket price: {ticket_price}\n"
    outcome += f"Discount: {discount}\n"
    outcome += f"Discounted price: {discount_price}\n"

    return outcome

try:
    age = int(input("Age: "))
    if age <= 0:
        print("Age must be above zero.")
    
    showtime = input("Showtime (HHMM): ")
    if len(showtime) != 4 or not showtime.isdigit():
        print("Enter showtime in correct format (HHMM)")

    int_showtime = int(showtime)

    if int_showtime < 0 or int_showtime >= 2400 or int(showtime[:2]) > 23 or int(showtime[2:]) > 59:
        print("Invalid time input.")
    
    result = ticket_price_calculator(age,int_showtime)

    print("\nYour ticket details are:\n````````````````````````")
    print(result)

except ValueError:
    print("Invalid input. Enter correct formatted value.")