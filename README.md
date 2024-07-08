# 🎮 Roblox Cookie Checker

This script checks the validity of `.ROBLOSECURITY` cookies for Roblox accounts. It uses the `requests` library to send HTTP requests to the Roblox API and `curses` to provide a text-based progress interface. Valid and invalid cookies are stored in separate files for later review.

## ✨ Features

- ✅ Checks the validity of Roblox `.ROBLOSECURITY` cookies.
- 🗂 Logs valid and invalid cookies into separate files.
- 📊 Provides a progress bar and real-time status updates using `curses`.
- 🔔 Optionally sends successful login information to a Discord webhook.

## 📋 Requirements

- 🐍 Python 3.x
- 📦 `requests` library
- 📟 `curses` library (usually included with Python on Unix-based systems)

## 🛠 Installation

1. 📥 Clone this repository or download the script files.

2. 📦 Install the required Python libraries using pip:

    ```sh
    pip install requests
    ```

3. Ensure you have the `curses` library. This is typically included with Python on Unix-based systems. On Windows, you may need to install a package like `windows-curses`:

    ```sh
    pip install windows-curses
    ```

## 🚀 Usage

1. 📝 Create a file named `cookies.txt` in the same directory as the script. Add your Roblox cookies (one per line) to this file.

2. If you want to enable Discord webhook notifications, add your webhook URL to the `webhook_url` variable in the script and set `webhookenabled` to `True`.

3. ▶️ Run the script:

    ```sh
    python main.py
    ```

## 📜 Script Overview

The script reads cookies from `cookies.txt`, checks their validity by attempting to access the Roblox profile page, and logs valid and invalid cookies into `work.txt` and `invalid.txt` respectively. It uses the `curses` library to display a progress bar and status updates in the terminal.

### 🔍 check_cookie Function

- Takes a `.ROBLOSECURITY` cookie as input.
- Sends a request to the api to check if cookie is valid
- Returns the username and user ID if the cookie is valid.

### 🖥 main Function

- Initializes the `curses` interface.
- Reads cookies from `cookies.txt`.
- Iterates over each cookie, checking its validity.
- Updates the progress bar and status messages in the terminal.
- Logs valid and invalid cookies to respective files.

## 📝 Notes

- Ensure your `cookies.txt` file is formatted correctly, with one cookie per line.
- If using on Windows, you may need additional steps to install and configure `curses`.

## ⚠️ Disclaimer

This script is for educational purposes only. Use it responsibly and do not violate Roblox's terms of service.

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
