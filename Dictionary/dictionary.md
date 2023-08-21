A dictionary in data structure is an unordered collection of key-pair where each value is unique and used to map a corresponding value. Its like a real-world dictionary where you have a word and its definition. Dictionaries allow you to look up a value based on its associated key in constant time. They are implemented as hash tables and commonly used for tasks such as counting word frequencies, grouping data or indexing data for quick search. In programming, dictionaries are supported by many programming languages and have different names such as maps, hashes or associative arrays. 

Python dictionaries are implemented using hash tables. A hash table is a way of doing key-value lookups. You store the values in an array and then use a hash function to find the index of the array cell that corresponds to your key value pair


Dictionaries Vs Lists

--------Dictionary--------------------                            -----List--------------------
Unordered                                                               Ordered
Acess via keys                                                          Access via index
Collection of key value pairs                                          Collection of elements
Preffered when you have unique key values                               Preferrred when you have ordered data
No duplicate members                                                    Allow duplicate members

Time and space complexity in Python Dictionary

Operation ------------------------------------------Time Complexity-----------------------------------Space Complexity

Creating a Dictionary------------------------0(len(dict)-----------------------------------0(n)
Inserting a value in a Dictionary----------------0(1)/0(n)-----------------------------------0(n)
Traversing a given Dictionary--------------------0(n)-----------------------------------0(1)
Accessing a given cell --------------------------0(1)-----------------------------------0(1)
Searching a given value -----------------------0(n)-----------------------------------0(1)
Deleting a given value--------------------------0(1)-----------------------------------0(1)