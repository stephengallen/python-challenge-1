# python-challenge-1
## _Objective_

To design an interactive ordering system from a food truck menu, using the skills I've learned in Python so far.

## _Challenges_
- The most challenging part for me was using the if-else statement to check if menu_selection was in the menu_items keys.
- I also had a challenging time aligning the columns using string muliplication


## _Credits_
 - I asked ChatGTP for this bit of code from lines 98-105
 > if isinstance(value, dict):
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + " - " + key2)
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2:.2f}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2

## _What Did I Learn?_
 
 I learned that tackling the project in small portions works best. I would run the system to a certain point and then continue to work from there on the next steps until completion. This helped me avoid any confusion as the project grew. Early on I tried putting in code for parts that weren't ready yet, and that just led to errors and frustration.
