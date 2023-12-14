1. Always start with creating the SIMPLEST example first, for example when creating all the cells, start with creating one cell and check that it appears correctly, then implement a row, then implement the columns

2. Ur work approach should be:

- Create the grid and populate the cells variable
- Draw all the cells onto the screen so they are visible, ensure everything works
- Write an event that checks the distance between ur mouse when pressed and all the other cells, if any cell is within cell_width//2 it means that the mouse is inside a cell! (this is sometimes faulty, as for example when ur in the top left corner of a cell, but its a start that somewhat works and is simple)
- Print the cells x and y coordinates, ensure it makes sense!

When you have succesfully ensured you have clicked inside a cell and generated the grid, only first then proceed:

- Next up is to write that code that is called upon in the run_setup function, suggestively call upon another function called find_neighboring_bombs(). This function is meant to ensure that before even the game starts up, each cell knows how many neighboring cells contain a bomb. For example if i am a cell, i check each neighbour I have for if cell.bomb == true, if so I increment the cell.neighboring_bombs variable by 1. This means that after having checked all neighbors, you then know how many bombs are besides it (Warning: this is quite complex to do)

- Tip is to write something of a test to validify the above! Its the trickiest part of the assignment so make sure you get it right!

After having implemeneted this, we continue with the cursor operations:

- After having pressed a cell and confirmed you are pressing the correct one, set that cells self.selected variable to true

- In the draw function for each cell, add code that conditionally draws a letter or digit inside each cell, the code should draw a digit if the cell is not a bomb, displaying the amount of neighboring bombs. If it is a bomb it should instead draw the letter X

## Here you are basically done! The game is playable although there is no win/lose condition implemented. Here are some tips to build out the game:

## COMPLETELY OPTIONAL NOT REQUIRED FOR ASSIGNMENT
- Sort out any minor bugs, such as pressing in upper left area of a cell
- Implement a lose screen that appears when you press a bomb, allowing you to restart the program
- Implement a score counter
- Implement a "sprite" (image) that is a bomb instead of the X
- Implement a win mechanic for when you have correctly selected all none-bomb squares!
- Implement the functionality to leave a flag where the user suspect there might be a bomb, for example if they right click they place a warning flag as a reminder

There are ofc many more! These are just some ideas