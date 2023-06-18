from PIL import Image, ImageDraw
from lib.token import *

# * variables
current_token = None
main_slate = None


# * methods
def clear_window(window):
    for widget in window.winfo_children():
        widget.destroy()


def create_board(output_path="src/img/board.png"):
    width = N * 100
    height = M * 100
    image = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    # Draw the main rectangle
    draw = ImageDraw.Draw(image)
    draw.rectangle([(0, 0), (width, height)], fill=board_color)
    # Draw the holes
    for row in range(M):
        for column in range(N):
            draw.ellipse(
                [
                    (column * 100 + 10, row * 100 + 10),
                    (column * 100 + 90, row * 100 + 90),
                ],
                fill=(0, 0, 0, 0),
            )
    # Save the image as PNG
    image.save(output_path, "PNG")


def unbind_arrows(window):
    window.unbind("<KeyPress-Left>")
    window.unbind("<KeyPress-Right>")
    window.unbind("<KeyPress-Down>")


def bind_arrows(window):
    window.bind(
        "<KeyPress-Left>", lambda e: restricted_move(current_token.position - 1)
    )
    window.bind(
        "<KeyPress-Right>", lambda e: restricted_move(current_token.position + 1)
    )
    window.bind("<KeyPress-Down>", lambda e: validate_turn(window))
    window.restart_button.bind("<Button>", lambda e: start_game(window))


def restricted_move(index):
    unbind_arrows(window)
    current_token.move_to(index)
    bind_arrows(window)


def validate_turn(window):
    global current_token
    if not main_slate.add_token(current_token.position, current_token.turn):
        return
    unbind_arrows(window)
    global raw_red_score, raw_yellow_score
    current_token.put_down(main_slate.peaks[current_token.position] - 1)
    if main_slate.state == on_going:
        current_token = token(window, not current_token.turn)
        bind_arrows(window)
    elif main_slate.state == red_won:
        window.announcement.set("red has won")
        window.win_message.config(fg="red")
        raw_red_score += 1
        window.red_score.set(str(raw_red_score))
    elif main_slate.state == yellow_won:
        window.announcement.set("yellow has won")
        window.win_message.config(fg="yellow")
        raw_yellow_score += 1
        window.yellow_score.set(str(raw_yellow_score))
    else:
        window.announcement.set("DRAW")
        window.win_message.config(fg="white")


def start_game(window):
    window.announcement.set("")
    WIDTH = N * 100 + 200
    HEIGHT = M * 100 + 200
    window.geometry(str(WIDTH) + "x" + str(HEIGHT))
    window.canvas.delete("all")
    window.canvas.configure(width=WIDTH, height=HEIGHT)
    create_board()
    window.board_img = tk.PhotoImage(file="src/img/board.png")
    window.board = window.canvas.create_image(
        100, 100, anchor=tk.NW, image=window.board_img
    )
    global main_slate, current_token
    main_slate = slate()
    current_token = token(window, Yellow_turn)
    bind_arrows(window)


# * start
window = tk.Tk()
window.red_score = tk.StringVar()
window.yellow_score = tk.StringVar()
raw_red_score = 0
raw_yellow_score = 0
window.red_score.set(str(raw_red_score))
window.yellow_score.set(str(raw_yellow_score))
window.announcement = tk.StringVar()
window.canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg=BG_color)
window.win_message = tk.Label(
    window, textvariable=window.announcement, font=("Bitter 40 bold"), bg=BG_color
)
window.restart_button = tk.Button(
    window, font=("Bitter 35 bold"), fg="purple", bg=BG_color, text="restart"
)
window.restart_button.place(relx=0.25, rely=0.98, anchor=tk.S)
scoreboard = tk.Frame(window)
tk.Label(
    scoreboard,
    textvariable=window.red_score,
    font=("Bitter 50 bold"),
    fg="red",
    bg=BG_color,
).pack(side="left")
tk.Label(scoreboard, text="-", font=("Bitter 50 bold"), fg="purple", bg=BG_color).pack(
    side="left"
)
tk.Label(
    scoreboard,
    textvariable=window.yellow_score,
    font=("Bitter 50 bold"),
    fg="yellow",
    bg=BG_color,
).pack(side="left")
scoreboard.place(relx=0.5, rely=0.875, anchor=tk.N)
window.win_message.place(relx=0.5, rely=25 / WIDTH, anchor=tk.N)
window.canvas.pack()
start_game(window)
window.resizable(False, False)
window.mainloop()
