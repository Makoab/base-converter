# Base Converter (Number System Converter)

This project is a simple **Base Converter** that converts numbers between different numeral systems (bases) ranging from **2 to 36** using **Python** and **Tkinter** for the GUI.

## Features
- Converts numbers between bases **2 to 36**.
- Supports both numeric digits and alphabetic characters for bases higher than 10.
- **User-friendly GUI** created with Tkinter.
- Displays error messages for invalid inputs.

## How It Works
1. The user inputs:
   - A **number** (e.g., `1a3f` for hexadecimal).
   - The **original base** (e.g., `16`).
   - The **target base** (e.g., `10`).
2. The program converts the number to **decimal** first, then converts it to the target base.
3. The result is displayed in a popup window.

## Installation & Usage
1. **Ensure Python 3 is installed** on your system.
2. Clone or download the repository.
3. Run the script using:
   ```sh
   python main.py
   ```
4. Enter the number and its bases, then click **Convert**.

## Example Conversions
| Input Number | From Base | To Base | Output |
|-------------|----------|--------|--------|
| 1011        | 2        | 10     | 11     |
| 1A3F        | 16       | 10     | 6719   |
| 6719        | 10       | 16     | 1A3F   |

## Code Structure
- `convert(number, from_base, to_base)`: Handles conversion between bases.
- `run_app()`: Initializes the Tkinter GUI.
- `on_convert()`: Validates input and triggers conversion.

## Error Handling
- Ensures bases are within **valid range (2-36)**.
- Displays a message if invalid characters are entered.
- Uses `try-except` to prevent crashes.

## License
This project is **open-source** and can be modified for learning purposes.

---
### Note:
This converter follows **case-insensitive** input handling (e.g., `A` and `a` are treated equally in base 16).

