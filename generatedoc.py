import random
import pandas as pd

# Generate dummy data for the table
table_data = []
for _ in range(5):
    row = [random.randint(1, 100) for _ in range(20)]
    table_data.append(row)

# Create a DataFrame from the dummy data
df = pd.DataFrame(table_data)

# Display the DataFrame
print(df)