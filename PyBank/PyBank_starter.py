# -*- coding: UTF-8 -*-
"""PyBank Homework Starter File."""

# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = r"C:\Repos\PyBankPyPoll\PyBank\Resources\budget_data.csv"
import os
print(f"Current Working Directory: {os.getcwd()}")

file_to_output = r"C:\Repos\PyBankPyPoll\PyBank\analysis\budget_analysis.txt"
try:
    with open(file_to_load) as financial_data:
        print("File opened successfully!")
        reader = csv.reader(financial_data)
        # Continue with your processing logic here
except FileNotFoundError:
    print("Error: The file was not found at the specified path.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


# Define variables to track the financial data
total_months = 0
total_net = 0
net_change_list = []  # List to store month-to-month changes in profit/losses
months = []  # List to track months corresponding to changes
greatest_increase = ["", 0]  # To track the month and value of greatest increase
greatest_decrease = ["", 0]  # To track the month and value of greatest decrease

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

    # Skip the header row
    header = next(reader)

    # Extract the first row to initialize variables
    first_row = next(reader)
    total_months += 1
    total_net += int(first_row[1])  # Add first month's profit/loss to total
    previous_net = int(first_row[1])  # Set this as the initial value for comparison

    # Process each row of data
    for row in reader:
        # Update total months and total net
        total_months += 1
        total_net += int(row[1])

        # Calculate the monthly change and add to the list
        net_change = int(row[1]) - previous_net
        net_change_list.append(net_change)
        months.append(row[0])  # Track the month for this change

        # Update previous net for the next iteration
        previous_net = int(row[1])

        # Calculate the greatest increase in profits
        if net_change > greatest_increase[1]:
            greatest_increase = [row[0], net_change]

        # Calculate the greatest decrease in losses
        if net_change < greatest_decrease[1]:
            greatest_decrease = [row[0], net_change]

# Calculate the average net change across the months
average_net_change = sum(net_change_list) / len(net_change_list)

# Generate the output summary
output = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total: ${total_net}\n"
    f"Average Change: ${average_net_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n"
)
import os

# Ensure the 'analysis' directory exists
os.makedirs("analysis", exist_ok=True)  # Creates the folder if it doesn't exist

# Print the output
print(output)

# Write the results to a text file
try:
    with open(file_to_output, "w") as txt_file:
        txt_file.write(output)
        print("File written successfully!")
except Exception as e:
    print(f"An error occurred while writing the file: {e}")
print(f"Writing to: {file_to_output}")

