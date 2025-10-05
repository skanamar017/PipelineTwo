# Exercise: Process store_sales.csv and calculate basic statistics
# Your task is to complete this outline with working code
#
# See ./Notes.md for some more instructions and explanations.
pass

# Import the csv module
import csv
# Import any other modules you need (e.g., collections for defaultdict)
from collections import defaultdict
from datetime import datetime

# Initialize data structures to hold our results
store_dict={'Store1':[0, 0, 0], 'Store2':[0, 0, 0], 'Store3':[0, 0, 0]}
# Hint: Consider using a dictionary with store_id as keys
# For each store, you'll need to track:
#   - Count of days
#   - Total items sold
#   - Total revenue
#   - Minimum revenue
#   - Maximum revenue

# Open the CSV file for reading
# Remember to use "with" to ensure the file gets closed properly
with open('/Users/saisarathkanamarlapudi/Documents/ZipCodeWilmington/PipelineTwo/store_sales.csv', mode='r') as file:

    # Create a CSV reader
    csv_reader = csv.reader(file)
    # Read the header row first
    header = next(csv_reader)
    # Loop through each row in the CSV file
    
    for row in csv_reader:
        # Extract values from each row (date, store_id, items_sold, revenue)
        # Convert numerical values to the right data types (int, float)
        #print(row)
        
        
        date, store_id, items_sold, revenue=datetime.strptime(row[0], "%Y-%m-%d").date(), str(row[1]), int(row[2]), float(row[3])
        #print(date, store_id, items_sold, revenue)
        # Update the appropriate store's statistics:
        #   - Increment day count
        
        if store_id not in store_dict:
            store_dict[store_id][0]=1
        else:
            store_dict[store_id][0]+=1
        #   - Add to total items
        if store_id not in store_dict:
            store_dict[store_id][1]=items_sold
        else:
            store_dict[store_id][1]+=items_sold
        #   - Add to total revenue
        if store_id not in store_dict:
            store_dict[store_id][2]=revenue
        else:
            store_dict[store_id][2]+=revenue
        #   - Update min revenue if current is lower
        if len(store_dict[store_id])<4:
            store_dict[store_id].append(revenue)
        else:
            if revenue<store_dict[store_id][3]:
                store_dict[store_id][3]=revenue

        #   - Update max revenue if current is higher
        if len(store_dict[store_id])<5:
            store_dict[store_id].append(revenue)
        else:
            if revenue>store_dict[store_id][4]:
                store_dict[store_id][4]=revenue

        
print(store_dict)
# Calculate averages for each store
for store_id in store_dict:
# For each store in your data structure:
    # Calculate average items per day (total_items / days)
    avg_items=store_dict[store_id][1]/store_dict[store_id][0]
    store_dict[store_id].append(avg_items)
    # Calculate average revenue per day (total_revenue / days)
    avg_revenue=store_dict[store_id][2]/store_dict[store_id][0]
    store_dict[store_id].append(avg_revenue)

# Determine which store had the highest average daily revenue
# Initialize variables to track best store and its revenue
# Loop through stores and compare average revenues
max_avg_rev=avg_revenue=store_dict['Store1'][2]/store_dict['Store1'][0]
max_store='Store1'

for store_id in store_dict:
    store_avg_rev=avg_revenue=store_dict[store_id][2]/store_dict[store_id][0]
    if store_avg_rev>max_avg_rev:
        max_avg_rev=store_avg_rev
        max_store=store_id

print("")
print(f"highest average daily revenue: {max_avg_rev} from {max_store}")

# Print a summary of statistics for each store
print("")
print(store_dict)
print("")
# Print which store had the highest average daily revenue
for store_id in store_dict:
    print(f"{store_id} count of days: {store_dict[store_id][0]}")
    print(f"{store_id} number of items: {store_dict[store_id][1]}")
    print(f"{store_id} total revenue: {store_dict[store_id][2]}")
    print(f"{store_id} minimum revenue: {store_dict[store_id][3]}")
    print(f"{store_id} maximum revenue: {store_dict[store_id][4]}")
    print(f"{store_id} average number of items: {store_dict[store_id][5]}")
    print(f"{store_id} average revenue: {store_dict[store_id][6]}")
    print("")


