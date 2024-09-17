#question 2 task 1

service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def open_ticket(ticket_id, customer_name, issue_description):
    if ticket_id in service_tickets:
        print(f"This ticket ID {ticket_id} already exist please try again.")
    else:
        service_tickets[ticket_id] = {
            "Customer": customer_name,
            "Issue": issue_description,
            "Status": "open"
        }
        print(f"Ticket ID {ticket_id} opened.")

def update_ticket(ticket_id, ticket_status):
    if ticket_id in service_tickets:
        if ticket_status in ["open", "closed"]:
            service_tickets[ticket_id]["Status"] = ticket_status
            print(f"Ticket ID {ticket_id} updated to {ticket_status}.")
        else:
            print("Invalid option. Try 'open' or 'closed'.")
    else:
        print(f"Ticket {ticket_id} does not exist please try agian.")

def disply_tickets(status=None):
    for ticket_id, details in service_tickets.items():
        if status is None or details["Status"] == status:
            print(f"ID: {ticket_id}, Customer: {details['Customer']}, Issue: {details['Issue']}, Status: {details['Status']}")\
            
print("Displaying tickets:")
disply_tickets()

print("\n\nCreating a ticket:")
open_ticket("Ticket003", "Charlie", "Feature request")

print("\n\nUpdating ticket:")
update_ticket("Ticket001", "closed")

print("\\nDisplaying tickets:")
disply_tickets()

print("\n\nDisplaying only open tickets:")
disply_tickets("open")