# You are given a stream of records about a particular stock. Each record contains a timestamp and the corresponding price of the stock at that timestamp.

# Unfortunately due to the volatile nature of the stock market, the records do not come in order. Even worse, some records may be incorrect. Another record with the same timestamp may appear later in the stream correcting the price of the previous wrong record.

# Design an algorithm that:

# Updates the price of the stock at a particular timestamp, correcting the price from any previous records at the timestamp.
# Finds the latest price of the stock based on the current records. The latest price is the price at the latest timestamp recorded.
# Finds the maximum price the stock has been based on the current records.
# Finds the minimum price the stock has been based on the current records.
# Implement the StockPrice class:

# StockPrice() Initializes the object with no price records.
# void update(int timestamp, int price) Updates the price of the stock at the given timestamp.
# int current() Returns the latest price of the stock.
# int maximum() Returns the maximum price of the stock.
# int minimum() Returns the minimum price of the stock.

from collections import defaultdict
from sortedcontainers import SortedSet

class StockPrice:
    
    def __init__(self):
        #initialize the data structures here
        self.prices = defaultdict(int) #store prices as key-value pairs
        self.timestamps = SortedSet() #store timestamps in a sorted set
        
    def update(self, timestamp: int, price: int) -> None:
        
        #Update the price of the stock at the given timestamp.
        if timestamp in self.prices:
            self.timestamps.remove(timestamp) 
            
        #update price in prices dictionary   
        
        self.prices[timestamp] = price
        #add timestamp to sorted set
        self.timestamps.add(timestamp) 
        
        
    def current(self) -> int:
        #return the latest prices of the stock
        #get the latest timestamp from the sorted set
        latest_timestamp = self.timestamps[-1]
        return self.prices[latest_timestamp]
    
    def maximum(self) -> int:
        #return the maximum price of the stock
        #get the maximum price from the prices dictionary
        return max(self.prices.values())
        
    def minimum(self) -> int:
        #return the minimum price of the stock
        #get the minimum price from the prices dictionary
        return min(self.prices.values())

# In this block of code, we import the necessary modules, defaultdict from collections and SortedSet from sortedcontainers, to use in our implementation. Then we define the StockPrice class and initialize its instance variables prices and timestamps. prices is a defaultdict that will store the prices as key-value pairs, where the timestamp is the key and the price is the value. We use defaultdict(int) to automatically initialize new keys with a default value of 0. timestamps is a SortedSet that will store the timestamps in sorted order, allowing us to easily access the latest timestamp.
# The update() method takes in a timestamp and a price as arguments and updates the price of the stock at the given timestamp. If the timestamp already exists in self.prices, we remove it from self.timestamps so that we can update it later. Then, we update the price in self.prices by assigning the price to the corresponding timestamp key. Finally, we add the timestamp to self.timestamps to maintain the sorted order of timestamps.