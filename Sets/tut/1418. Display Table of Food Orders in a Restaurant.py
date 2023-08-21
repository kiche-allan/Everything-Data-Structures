# Given the array orders, which represents the orders that customers have done in a restaurant. More specifically orders[i]=[customerNamei,tableNumberi,foodItemi] where customerNamei is the name of the customer, tableNumberi is the table customer sit at, and foodItemi is the item customer orders.

# Return the restaurant's “display table”. The “display table” is a table whose row entries denote how many of each food item each table ordered. The first column is the table number and the remaining columns correspond to each food item in alphabetical order. The first row should be a header whose first column is “Table”, followed by the names of the food items. Note that the customer names are not part of the table. Additionally, the rows should be sorted in numerically increasing order.


# Example 1:

# Input: orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
# Output: [["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]] 
# Explanation:
# The displaying table looks like:
# Table,Beef Burrito,Ceviche,Fried Chicken,Water
# 3    ,0           ,2      ,1            ,0
# 5    ,0           ,1      ,0            ,1
# 10   ,1           ,0      ,0            ,0
# For the table 3: David orders "Ceviche" and "Fried Chicken", and Rous orders "Ceviche".
# For the table 5: Carla orders "Water" and "Ceviche".
# For the table 10: Corina orders "Beef Burrito". 

from typing import List

class Solution(object):
    def displayTable(self, orders):
        """
        :type orders: List[List[str]]
        :rtype: List[List[str]]
        """
        foods = set([])
        tables = collections.defaultdict(lambda :collections.defaultdict(int))
        for order in orders:
            foods.add(order[2])
            tables[int(order[1])][order[2]] += 1
        tables = sorted(tables.items(), key=lambda x:x[0])
        ans = [["Table"]]
        foods = sorted(list(foods))
        ans[0].extend(foods)
        for k, v in tables:
            cur_ans = [str(k)]
            for food in foods:
                cur_ans.append(str(v[food]))
            ans.append(cur_ans)
        return ans
    
#     The provided implementation uses a defaultdict to store table orders, where each table has its own dictionary to store food item counts. It also uses a set to keep track of unique food items.

# The implementation iterates through the orders list and populates the tables and foods data structures. It then sorts the tables dictionary by table number using the sorted() function with a lambda function as the key.

# Next, it initializes the ans (answer) list with a header row containing the string "Table" as the first element. It then extends the header row with the sorted food items.

# For each table in the sorted tables dictionary, it creates a row in the ans list. The table number is converted to a string and added as the first element of the row. It then iterates through the sorted food items and appends the corresponding food item count from the tables dictionary to the current row.

# Finally, it returns the ans list, which represents the restaurant's display table with the table number, food items, and their respective counts.

# Please note that this implementation assumes that the orders list contains valid input and does not include error handling for invalid or missing data. Additionally, it does not include a sorting order for the food items, as the problem statement does not specify a specific sorting order for them.