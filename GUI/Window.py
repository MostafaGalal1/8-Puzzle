import tkinter as tk
from tkinter import ttk
from math import sqrt

from Algorithms.Algorithm_Factory import get_algorithm

BOARD_SIZE = 3
BOARD_DIMENSION = 584
BOARD_COLOR = "#202020"
FOCUSED_COLOR = "#ebb735"
BACKGROUND_COLOR = "#404040"
TRANSPARENT_COLOR = "#00000088"

def resize_image(photo_image, new_width, new_height):
    return photo_image.subsample(int(photo_image.width() / new_width), int(photo_image.height() / new_height))


def convert_int_to_state(state):
    state_str = str(state)
    if len(state_str) == 8:
        state_str = '0' + state_str

    state_board = []
    board_size = int(sqrt(len(state_str)))
    for i in range(board_size):
        row = []
        for j in range(board_size):
            row.append(int(state_str[i * board_size + j]))
        state_board.append(row)
    return state_board


class Window:
    def __init__(self):
        # initialize the window
        self.root = tk.Tk()
        self.root.title("8-Puzzle")
        self.root.iconbitmap('GUI/Assets/icon.ico')
        self.root.resizable(False, False)
        self.root.configure(background=BACKGROUND_COLOR)

        # Configure the style of the widgets
        self.style = ttk.Style()
        self.style.configure("Custom.TFrame", background=BACKGROUND_COLOR)
        self.style.configure("Custom.TCombobox", lightcolor=FOCUSED_COLOR)
        self.style.configure("Custom.TEntry", highlightcolor=FOCUSED_COLOR, foreground=FOCUSED_COLOR, lightcolor=FOCUSED_COLOR)
        self.style.configure("Custom.TButton", background=BACKGROUND_COLOR, color=BOARD_COLOR)
        self.style.configure("Custom.TLabel", background=BACKGROUND_COLOR, foreground="white", font=("Helvetica", 14))
        self.style.configure("Solution.TLabel", background=BACKGROUND_COLOR, foreground="white", font=("Helvetica", 12))

        # Create a side frame
        side_frame = ttk.Frame(self.root, style="Custom.TFrame")
        side_frame.pack(side=tk.LEFT, padx=10, pady=10, expand=True, fill="both")

        # Dropdown menu for selecting the search algorithm
        algorithm_label = ttk.Label(side_frame, text="Select Algorithm:", style="Custom.TLabel")
        algorithm_label.pack(pady=(8, 4))
        self.algorithm_var = tk.StringVar()
        algorithm_combobox = ttk.Combobox(side_frame, textvariable=self.algorithm_var,
                                          values=["DFS", "BFS", "A-Star (Manhattan)", "A-Star (Euclidean)"], state="readonly", style="Custom.TCombobox")
        algorithm_combobox.current(0)
        algorithm_combobox.pack(pady=(0, 68))

        # Input field for entering the initial state
        initial_state_label = ttk.Label(side_frame, text="Enter Initial State:", style="Custom.TLabel")
        initial_state_label.pack(pady=(8, 2))
        state_description_label = ttk.Label(side_frame, text="Write state in this form:\n    0,1,2,3,4,5,6,7,8", background=BACKGROUND_COLOR, foreground="white", font=("Helvetica", 10))
        state_description_label.pack(pady=(0, 4))
        self.initial_state_entry = ttk.Entry(side_frame, style="Custom.TEntry")
        self.initial_state_entry.pack(pady=(0, 8))

        # Solve button
        self.solve_button = ttk.Button(side_frame, text="Solve", style="Custom.TButton",command=lambda: self.sol())
        self.next_state_button = ttk.Button(side_frame, text="Next", command=lambda: self.display_next_state(), style="Custom.TButton")
        self.previous_state_button = ttk.Button(side_frame, text="Previous", command=lambda: self.display_previous_state(), style="Custom.TButton")

        self.solve_button.pack(pady=(0, 16))
        self.next_state_button.pack()
        self.previous_state_button.pack()

        self.current_state_label = ttk.Label(side_frame, text="Current State: 0", style="Solution.TLabel")
        self.current_state_label.pack(pady=(8, 2))

        self.solution_header_label = ttk.Label(side_frame, style="Solution.TLabel")
        self.solution_body_label = ttk.Label(side_frame, style="Solution.TLabel")

        self.canvas = tk.Canvas(self.root, width=BOARD_DIMENSION, height=BOARD_DIMENSION, highlightbackground=BACKGROUND_COLOR)
        self.canvas.pack()

        self.tile_images = None
        self.load_images()
        self.current_state_index = 0


        self.previous_state_button.configure(state="disabled")
        self.next_state_button.configure(state="disabled")



        #self.draw_board(self.states[0])
        self.root.mainloop()

    def load_images(self):
        self.tile_images = []
        for i in range(0, 8):
            tile_image = tk.PhotoImage(file=f"GUI/Assets/{i + 1}{i + 1}.png")
            tile_image = resize_image(tile_image, BOARD_DIMENSION / 3, BOARD_DIMENSION / 3)
            self.tile_images.append(tile_image)

    def display_next_state(self):
        self.previous_state_button.configure(state="normal")
        self.draw_board(self.states[self.current_state_index + 1])
        self.current_state_index += 1
        self.current_state_label.configure(text="Current State: " + str(self.current_state_index))
        if self.current_state_index + 1 >= len(self.states):
            self.next_state_button.configure(state="disabled")

    def display_previous_state(self):
        self.next_state_button.configure(state="normal")
        self.draw_board(self.states[self.current_state_index - 1])
        self.current_state_index -= 1
        self.current_state_label.configure(text="Current State: " + str(self.current_state_index))
        if self.current_state_index - 1 < 0:
            self.previous_state_button.configure(state="disabled")

    def draw_board(self, state):
        self.canvas.delete("all")
        cell_width = BOARD_DIMENSION / self.board_size
        cell_height = BOARD_DIMENSION / self.board_size

        for i in range(self.board_size):
            for j in range(self.board_size):
                value = state[i][j]
                if value != 0:
                    self.canvas.create_image(j * cell_width, i * cell_height, anchor=tk.NW, image=self.tile_images[value - 1])

    def sol(self):
        #reseting state buttons
        self.previous_state_button.configure(state="disabled")
        self.next_state_button.configure(state="disabled")

        #taking intial satate and turning it into 2d list
        initial = self.initial_state_entry.get()
        initial = initial.replace(',','')
        board = int(''.join([''.join(map(str, row)) for row in initial]))
        print(type(board),board)


        #taking the method
        method = self.algorithm_var.get()
        hur = None
        if (method[:6] == "A-Star"):
            hur = method[7:]
            method = method[:6]
            hur = hur[1:-1]

        #solving the board
        method_object = get_algorithm(board, method,hur)
        solution = method_object.solve()

        #checking if the board has a solution
        if(solution.solvable):
            self.current_state_index = 0
            self.current_state_label.configure(text="Current State: " + str(self.current_state_index))

            self.solution_header_label.configure(text="Solution exists!")
            self.solution_body_label.configure(text=solution.stringify())
            self.solution_header_label.pack(pady=(68, 8))
            self.solution_body_label.pack(pady=(0, 8))


            self.states = solution.path
            if len(self.states) > 1:
                self.next_state_button.configure(state="enabled")
            for state_index in range(len(self.states)):
                self.states[state_index] = convert_int_to_state(self.states[state_index])

            self.board_size = len(self.states[0])
            self.draw_board(self.states[0])
        else:
            self.solution_header_label.configure(text="No Solution :(")
            self.solution_body_label.configure(text=solution.stringify())
            self.solution_header_label.pack(pady=(68, 8))
            self.solution_body_label.pack(pady=(0, 8))

            self.board_size = len(board)
            self.draw_board(board)