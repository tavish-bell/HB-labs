# variable that is storing the contents of a txt file
log_file = open("um-server-01.txt")

# function that takes the above variable as an argument. 
# for each line in the log file, the spaces are removed
# day variable contains targeted index positions
# if value of day variable is equal to "Tue", print statement will trigger
# call function and pass in argument
def generate_sales_reports(log_file):
    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Tue":
            print(line)


generate_sales_reports(log_file)
