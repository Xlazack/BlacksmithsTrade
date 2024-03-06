import os

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')
        
def wait_for_key_press():
    input("Press Enter to continue...")
    clear_screen()
