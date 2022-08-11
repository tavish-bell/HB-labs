"""
Create function that makes generating daily reports more efficient
"""


def melon_counter(day_num, file_path):
    """input day number & file path

    returns report of how many melons delivered, type, and total cost
    """
    the_file = open("um-deliveries-day-1.txt")
    with open(file_path) as contents:
        delivery_log = contents.read()

    for line in delivery_log:
        line = line.rstrip()
        word = line.split("|")

        melon = word[0]
        count = word[1]
        cost = word[2]

        print(f"{day_num}: Delivered {count} {melon}s for total of ${cost}")


melon_counter(
    day_num="day_1", file_path="open("um-deliveries-day-1.txt")"
)


# print("Day 1")
# the_file = open("um-deliveries-day-1.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[1]
#     amount = words[2]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()


# print("Day 2")
# the_file = open("um-deliveries-day-2.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()


# print("Day 3")
# the_file = open("um-deliveries-day-3.txt")
# for line in the_file:
#     line = line.rstrip()
#     words = line.split('|')

#     melon = words[0]
#     count = words[0]
#     amount = words[0]

#     print(f"Delivered {count} {melon}s for total of ${amount}")
# the_file.close()
