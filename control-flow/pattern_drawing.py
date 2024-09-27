def draw_pattern():
    """
    Draws a square pattern of asterisks (*) based on user input.
    """
    
    # Prompt user for pattern size
    while True:
        try:
            size = int(input("Enter the size of the pattern: "))
            if size <= 0:
                print("Please enter a positive integer.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    # Draw the pattern
    for i in range(size):
        for j in range(size):
            print("*", end=" ")
        print()

        
        

        


