
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


