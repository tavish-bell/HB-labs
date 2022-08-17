"""Generate sales report showing total melons each salesperson sold."""
import pandas

# ----------------------------- PROGRAM EXPLAINED -------------------------
# empty lists are created for collecting the names of salespeople and melons sold.
# the txt df is opened and read
# for each line in the txt df:
# strip extra space on right side
# split each line at the point of | and save this information
# inside of 'entries' variable
# the entries at index position 0 are the salespeople
# the entries at index position 2 are the number of melons sold
# as the for loop is iterating over the lines in the txt df,
# it adds salespeople and melons sold into the created lists at
# lines 4 & 5.
# if during this iteration process, the same salesperson is found
# (i.e. their name appears more than once in the txt df), then
# the program will locate the index position of their name within the
# salespeople list. This index position will be used to update the
# corresponding index position in the melons_sold list.
# ----------------------------------------------------------------------------
salespeople = []
melons_sold = []

# f = open("sales-report.txt")


# for line in f:
#     line = line.rstrip()
#     entries = line.split("|")
#     salesperson = entries[0]
#     melons = int(entries[2])

#     #

#     if salesperson in salespeople:
#         position = salespeople.index(salesperson)
#         melons_sold[position] += melons

#     else:
#         salespeople.append(salesperson)
#         melons_sold.append(melons)


# for i in range(len(salespeople)):
#     print(f"{salespeople[i]} sold {melons_sold[i]} melons")

# ------------------- HOW TO IMPROVE PROGRAM ------------------------
# There are several ways to make this program more efficient.
#
# One way to improve the program would be to create a dictionary
# where the key is represented by the name of the salesperson and
# the corresponding value is represented as the number of melons
# they sold.
#
# Another way to improve this program (my preferred method) would
# be to use the Pandas Library to create ........


# ------------------- IMPROVED PROGRAM USING PANDAS ----------------------
# EXPLAINED:
# when opening/reading the txt file with Pandas, separating items by | will  ensure each item separted by | is placed in its own column. Column names can be added to the file by using the .set_axis method.
#
# This method takes in three parameters - the labels for each column,the axis is set to 1 to identify where the label needs to be set, and finallyh adding True to inplace to indicate that these changes should be applied to the existing dataframe instead of creating a new one.
#
# the dataframe can be converted to a dictionary (line 73)


df = pandas.read_csv("sales-report.txt", sep="|")
df.set_axis(
    labels=["salesperson", "total_order_cost", "melons_sold"], axis=1, inplace=True
)
df.to_dict(orient="records")
print(df)
