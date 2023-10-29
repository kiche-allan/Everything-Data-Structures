def birthdayCakeCandles(candles):
    # Find the maximum height of the candles
    max_height = max(candles)
    
    # Count how many candles have the maximum height
    count = candles.count(max_height)
    
    return count