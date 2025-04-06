from graphics import Canvas
import time

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def main():
    # Create canvas
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Draw blue cells
    for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
        for col in range(0, CANVAS_WIDTH, CELL_SIZE):
            canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, 'blue')
    
    # Wait for user click to place eraser
    canvas.wait_for_click()
    eraser_x, eraser_y = canvas.get_last_click()
    
    # Create eraser
    eraser = canvas.create_rectangle(eraser_x, eraser_y, eraser_x + ERASER_SIZE, eraser_y + ERASER_SIZE, 'pink')
    
    # Move eraser and erase cells
    while True:
        # Move eraser to mouse position
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        canvas.moveto(eraser, mouse_x, mouse_y)
        
        # Erase cells that eraser touches
        for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
            for col in range(0, CANVAS_WIDTH, CELL_SIZE):
                if col <= mouse_x <= col + ERASER_SIZE and row <= mouse_y <= row + ERASER_SIZE:
                    canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, 'white')
        
        # Small delay
        time.sleep(0.05)

if __name__ == '__main__':
    main()
