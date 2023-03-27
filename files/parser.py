#!/usr/bin/env python3

import os
import csv
from rich.console import Console
from rich.prompt import Prompt
from rich.table import Table
from rich.style import Style
from rich.columns import Columns

# Specify the path to the CSV file
csv_dir = "CHANGE ME!"

# Create a new console for displaying the menu and table
console = Console()

# Create an empty list to store the menu items
menu_items = []

# Iterate through all CSV files in the directory
for file_name in os.listdir(csv_dir):
    if file_name.endswith(".csv"):
        # Load the CSV file into a rich table
        file_path = os.path.join(csv_dir, file_name)
        with open(file_path, "r") as csv_file:
            csv_reader = csv.reader(csv_file)
            header = next(csv_reader)
            table = Table(title=file_name[:-4], show_header=True, header_style=Style(color="cyan", bold=True))
            table.add_column(header[0], style=Style(color="white"))
            table.add_column(header[1], style=Style(color="white"))
            for row in csv_reader:
                if len(row) >= 2:
                    table.add_row(row[0], row[1])
        # Add the table as a menu item
        menu_items.append({"title": file_name[:-4], "table": table})

# Display the numbered menu
console.print("Select a CSV file:")
for index, item in enumerate(menu_items, start=1):
    console.print(f"{index}> {item['title']}")

# Ask the user to select a number
selected_index = Prompt.ask("Enter the number of your choice:", choices=[str(i) for i in range(1, len(menu_items) + 1)])

# Display the selected table
selected_item = menu_items[int(selected_index) - 1]
console.print(selected_item["table"], style=Style(bgcolor="black"))
