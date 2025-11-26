import tkinter as tk
import random

secret = random.randint(1, 20)
attempts = 0

ghost_hints_high = [
    "👻 A cold whisper: 'Too high… the spirits float lower.'",
    "🕯️ The candle flickers: 'Your number is above the dead… come down.'"
]

ghost_hints_low = [
    "👻 A hollow moan: 'Too low… deeper… darker… higher you must go.'",
    "🕯️ Something crawls on the floor: 'That number lies beneath the grave… rise.'"
]

def check_guess():
    global attempts
    attempts += 1

    try:
        guess = int(entry.get())
    except ValueError:
        message.set("☠️ The ghost snarls: 'Speak in numbers… or be silent forever…'")
        return

    if guess == secret:
        message.set(f"💀 The ghost shrieks!\nYou solved it in {attempts} attempts.\n"
                    "But something is standing behind you…")
        entry.config(state="disabled")
        button.config(state="disabled")

    elif guess > secret:
        message.set(random.choice(ghost_hints_high))
    else:
        message.set(random.choice(ghost_hints_low))


root = tk.Tk()
root.title("Haunted Guessing Game")
root.geometry("430x360")
root.configure(bg="#240a0a")   

title = tk.Label(
    root,
    text="👻 Haunted Number Hallway 👻",
    font=("Chiller", 28, "bold"),  
    bg="#0a0a0a",
    fg="#b30000"
)
title.pack(pady=10)

message = tk.StringVar()
message.set("A ghost has chosen a number (1–20)…\nGuess it… if you dare…")

msg_label = tk.Label(
    root,
    textvariable=message,
    wraplength=380,
    font=("Georgia", 12),
    bg="#0a0a0a",
    fg="#e6e6e6",
    justify="center"
)
msg_label.pack(pady=10)

entry = tk.Entry(
    root,
    font=("Georgia", 16),
    justify="center",
    width=8,
    bg="#1a1a1a",
    fg="#ff0000",
    relief="flat"
)
entry.pack(pady=10)

button = tk.Button(
    root,
    text="Summon Ghost",
    command=check_guess,
    font=("Georgia", 14),
    bg="#4d0000",
    fg="white",
    relief="flat",
    padx=10,
    pady=5
)
button.pack(pady=18)

root.mainloop()


