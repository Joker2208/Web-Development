def format_count(count):
    if count >=1000000:
            final = count/1000000
            return f"{final}M"
    
    elif count >= 1000:
        final = count/1000
        return f"{final}K"
    else: 
         return count