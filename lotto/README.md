# Lotto Game

This project is based on the Italian lotto game.  
It will consist of 3 learning paths.  
For more info on the rules visit: https://www.sisal.it/lotto/come-si-gioca  

## Learning Path 1

In this brach there is the first level, where a lottery ticket will be generated based
on the wheel name, type of bet and numbers to be generated entered by the user.

### Structure

**How to launch the program:**  
start the program from the file lotto_game.py present here.  
At the command line enter "-n" followed by the number of tickets to generate

**lotto folder:**  
This folder contains all the classes used in the program:  

- bet_type.py  
Contains the BetType class, where general information on the type of bet is contained. Inside we find:
    - is_bet_type_valid  
    which takes care of validating the user's choice
    
    - bet_index  
     which takes care of transforming the numerical value entered by the user into the corresponding name

- city.py  
Contains the City class, where there is general information on "ruota" names. Inside we find:
    - is_city_valid  
    which takes care of validating the user's choice
    
    - city_index  
    which takes care of transforming the numerical value entered by the user into the corresponding name
    
- lotto.py  
It manages the logic of the program. Inside we find:
    - choose_city  
    Asks the user for input for the name of the "ruota" on which the ticket is to be generated
    
     - choose_bet_type  
     Asks the user as input for the type of bet to be made
    
    - choose_numbers  
    Asks the user how many numbers to randomly generate for the single ticket (from 1 to 10)
    
    - print_ticket  
    Print the ticket on the screen
    
- lotto_helper.py  
It takes care of the printing functions.

-