
tabs = {}


open_tabs_order = []

# Added the ability to open a new tab and check if a tab is already open.

def open_tab(tab_name):
    """Open a new tab."""
    if tab_name not in tabs:
        tabs[tab_name] = {}
        open_tabs_order.append(tab_name)
        print(f"Tab '{tab_name}' opened successfully.")
    else:
        print(f"Tab '{tab_name}' is already open.")

# Added the ability to close an open tab.

def close_tab(tab_name):
    """Close an open tab."""
    if tab_name in tabs:
        del tabs[tab_name]
        open_tabs_order.remove(tab_name)
        print(f"Tab '{tab_name}' closed successfully.")
    else:
        print(f"Tab '{tab_name}' is not open.")

# Added the ability to switch to a different tab.

def switch_tab(tab_name):
    """Switch to a different tab."""
    if tab_name in tabs:
        print(f"Switched to tab '{tab_name}'.")
    else:
        print(f"Tab '{tab_name}' is not open.")
        