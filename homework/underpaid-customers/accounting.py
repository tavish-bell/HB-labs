# """
# invoicing program that uses txt file to
# track customer orders and calculate if
# customer overpaid or underpaid for their
# order
# """

# import pandas

# MELON_COST = 1


# def payment_status(customer_orders):
#     """
#     takes txt file as input

#     returns data for customers who overpaid or underpaid
#     """
#     invoice = pandas.read_csv(customer_orders, sep="|", index_col=0)


#     customer = invoice.customer
#     total_cost = invoice.expected
#     expected_pymt = MELON_COST * total_cost
#     total_paid = invoice.paid

#     # --- customers who underpaid ---
#     # identify customers who underpaid by looping through data
#     # put tthis information into a new dataframe and export csv

#     # -- customers who overpaid --
#     # same as above

#     print(invoice)

#     # print(total_cost)

#     # customer underpaid
#     if total_cost > total_paid:
#         print(f"{customer} paid ${expected_pymt}\nexpected ${total_cost}")

#     # customer overpaid
#     if total_paid > total_cost:
#         print(f"{customer} paid ${expected_pymt}\nexpected ${total_cost}")


# payment_status(customer_orders="customer-orders.txt")


MELON_COST = 1.00


def payment_status(payment_data_filename):
    """Calculate cost of melons and determine who has underpaid."""

    payment_data = open(payment_data_filename)  # open the file

    # Iterate over lines in file
    for line in payment_data:
        # Split line by '|' to get a list of strings
        order = line.split("|")

        # Get customer's full name
        full_name = order[1]
        print(order)
        # Split `customer_name` by space (' ') to get
        # a list of [first_name, last_name].
        #
        # Then, assign first name (at index 0) to `customer_first`
        # first_name = full_name.split(" ")[0]

        # Get no. of melons in the order and amount customer paid
        # melons_qty = float(order[2])  # also ok to typecast melons_qty as an int
        # amt_paid = float(order[3])

        # # Calculate expected price of customer's order
        # expected_price = melons_qty * MELON_COST

        # # Print general payment info
        # print(f"{full_name} paid ${amt_paid:.2f}, expected", f"${expected_price:.2f}")

        # Print payment status
        #
        # If customer overpaid, print that they've overpaid for their melons. If
        # customer underpaid, print that they've underpaid for their melons.
        # if expected_price < amt_paid:
        #     print(f"{first_name} has overpaid for their melons.")

        # elif expected_price > amt_paid:
        #     print(f"{first_name} has underpaid for their melons.")

    # Close the file
    payment_data.close()


# Call the function
payment_status("customer-orders.txt")
