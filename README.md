# PaPiRus-boardGames
This project is aimed at bringing board games to the PaPiRus zero screen for the raspberry pi

# Making games with library

Import the file "screenTester"
Commands:

button( index ) -- Is button <index> down?
  Returns a bool

update() -- Updates the screen to the changes you made

clear() -- Clears the screen from all objects (doesen't update after)

rectangle(first_x, first_y, end_x, end_y, fill) -- Draws a rectangle at (first_x,first_y) to the point (end_x,eny_y). Fill is if you want the rectangle to be filled or not

circle(pos_x, pos_y, radius, fill) -- Draws a circle with the center (pos_x,posy) and the radius <radius>. Im pretty sure you know what fill means so i won't keep explainng it!

line(first_x,first_y,end_x,end_y) -- Draws a line from (first_x,first_y) to the point (end_x,end_y)

text(pos_x,pos_y,text) -- Draws text at the position (pos_x,pos_y) with the text <text>

image(pos_x,pos_y,path) -- Draws a image at the position (pos_x,pos_y) and drawing the image from the path <path>

# Using the library

In your program you should try to use a while loop and call the function updateLoop as much as you can since this deals with events and if you are testing with the tester script it will update the tkinter window so it doesen't freeze

If you find it annoying programming buttons you can bind a function to be called when a button is pressed or let go, simply change the list 'downBind' or 'upBind' to bind a function to each button.
e.g.

  downBind[0] = sayHello() -- Bind the button at the very left to call the function as soon as it is pressed
  
  upBind[4] = shutdown() -- Bind the button at the very right to call the function as soon as the button is let go

All of the functions and variables mentioned will be in the library screenTester when imported.

# Making a game

Games made must be a python script in the "games" directory followed by its icon screen which should be EXACTLY the same name as the script (apart from the extention) with the extention .png in the "gameIcons" directory.

When you have put the two files in, inside your game you need to make a class called "Main". Inside your new class put an __init__ function inside and two paramiters will be required, the first is a pointer to the screen library thing mentioned on how to use obove, the second is a pointer to a function that when called, exits the game back to the main screen.

In your class you need to have a function named "loop", no paramiters. This will be called in a while loop to run the game.
