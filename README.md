# four-in-a-row

## Introduction:

This documentation provides an overview of the code implementation for a Four in a Row game. The game is implemented using Python and utilizes the Tkinter library for the graphical user interface (GUI) components. The game follows the traditional rules of Four in a Row, where players take turns dropping colored tokens into a grid to connect four tokens of their color in a row, either vertically, horizontally, or diagonally.
## Code Structure:

The code is structured into several functions and global variables to manage the game logic and GUI interactions. Here is a breakdown of the code structure:

### Import Statements:
The necessary libraries are imported at the beginning of the code. These include:
   - PIL (Python Imaging Library): Used for creating and manipulating images.
- ImageDraw module from PIL: Used for drawing on the image.
- lib.token module: Contains the implementation of the token class used in the game.

### Global Variables:
- current_token: Represents the current token being played.
- main_slate: Represents the game board.

### Utility Functions:
- clear_window(window): Clears the GUI window by destroying all its children widgets.
- create_board(output_path): Creates the game board image with holes and saves it as a PNG file.
- unbind_arrows(window): Unbinds arrow key events from the window.
- bind_arrows(window): Binds arrow key events to specific actions in the game.
- restricted_move(index): Moves the current token to a restricted index on the game board.
- validate_turn(window): Validates the current turn and updates the game state accordingly.
start_game(window): Initializes and starts the game.

### Game Initialization:
The Tkinter window and necessary variables are initialized.
Score labels, a restart button, and canvas for drawing the game board are created.
The game board image is generated and displayed in the canvas.
main_slate and current_token objects are created.
Arrow key events are bound to corresponding functions.


## Function Details:

- clear_window(window)
    - Parameters: window (Tkinter window object)
    - Description: This function clears the GUI window by destroying all its child widgets.

- create_board(output_path="src/img/board.png")
    - Parameters: output_path (string, optional)
    - Description: This function creates the game board image with holes using the PIL library and saves it as a PNG file. The default output path is "src/img/board.png".

- unbind_arrows(window)
   - Parameters: window (Tkinter window object)
  -  Description: This function unbinds arrow key events from the window to disable movement controls.

- bind_arrows(window)
  -  Parameters: window (Tkinter window object)
   - Description: This function binds arrow key events to corresponding functions to enable movement controls.

- restricted_move(index)
    - Parameters: index (integer)
  -   Description: This function restricts the movement of the current token to the specified index on the game board. It is called when the left or right arrow key is pressed.

- validate_turn(window)
   - Parameters: window (Tkinter window object)
  -  Description: This function validates the current turn and updates the game state accordingly. It is called when the down arrow key is pressed to drop the token into a column. It also handles the game outcome and updates the GUI elements accordingly.

- start_game(window)
    - Parameters: window (Tkinter window object)
    - Description: This function starts the game by initializing the necessary GUI elements and objects. It is called at the beginning and also when the restart button is clicked.

## Usage:

To use the Four in a Row game, follow these steps:

Ensure that you have the required libraries installed, including PIL and Tkinter.
Copy and paste the provided code into a Python script.
Run the script, and the game window will appear.
Play the game by using the left and right arrow keys to move the token and the down arrow key to drop it into a column.
The game outcome and scores will be displayed in the GUI.

Note: You can customize certain aspects of the game, such as the board size and colors, by modifying the relevant variables in the code.
## Conclusion:

This documentation provides an overview of the code implementation for a Four in a Row game. It explains the code structure, function details, and usage instructions. With this information, you should be able to understand and utilize the provided code to play the game or further modify it according to your requirements.