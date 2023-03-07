spot = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

def is_not_empty(string)
    no_whitespace = string.strip()
    if no_whitespace != '':
        return True
    else:
        retrun False 
 

real_places = list(filter(is_not_empty, spot))
print(real_spot)