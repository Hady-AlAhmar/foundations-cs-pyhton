
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

# Added the ability to display all open tabs.

def display_all_tabs():
    """Display all open tabs."""
    print("Open Tabs:")
    for tab in open_tabs_order:
        print(f"- {tab}")
        
# Added the ability to open a nested tab under a parent tab.

def open_nested_tab(parent_tab, nested_tab_name):
    """Open a nested tab under a parent tab."""
    if parent_tab in tabs:
        tabs[parent_tab][nested_tab_name] = {}
        print(f"Nested tab '{nested_tab_name}' opened under '{parent_tab}'.")
    else:
        print(f"Parent tab '{parent_tab}' not found.")       
        
# Added the ability to close all open tabs.

def clear_all_tabs():
    """Close all open tabs."""
    for tab in open_tabs_order.copy():
        close_tab(tab)
    print("All tabs closed.")
    
