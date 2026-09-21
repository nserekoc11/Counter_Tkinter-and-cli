# Counter App

A small desktop counter application built with Python and Tkinter. The app provides buttons to increase, decrease, or reset a numeric counter.

## Features

- Increment the counter with the `+` button.
- Decrement the counter with the `-` button.
- Reset the counter to `0` with the `Reset` button.
- Simple, fixed-size graphical interface.
- No external dependencies beyond Python's standard library.

## Requirements

- Python 3.6 or later
- Tkinter, which is included with most standard Python installations

## Getting Started

1. Clone or download this repository.
2. Open a terminal in the project directory.
3. Run the application:

   ```bash
   python counter.py
   ```

   On systems where Python is invoked as `python3`, use:

   ```bash
   python3 counter.py
   ```

## Usage

When the application starts, the counter displays `0`.

| Control | Action |
| --- | --- |
| `+` | Increases the counter by 1 |
| `-` | Decreases the counter by 1 |
| `Reset` | Sets the counter back to 0 |

The counter can become either positive or negative.

## Project Structure

```text
.
├── counter.py       # Tkinter application
└── README.md        # Project documentation
```

## How It Works

The `CounterApp` class:

- Creates the main Tkinter window and its controls.
- Stores the current value in `self.count`.
- Updates the displayed value through `_update_label()`.
- Connects each button to an operation:
  - `increment()` adds one.
  - `decrement()` subtracts one.
  - `reset()` sets the value to zero.

The Tkinter event loop keeps the window open and responds to button clicks.

## License

No license has been specified for this project.
