
tabs = {}


open_tabs_order = []

# Added the ability to open a new tab and check if a tab is already open.

def add_new_tab():
    """Add a new tab with title and URL."""
    tab_name = input("Enter the title of the new tab: ")
    tab_url = input("Enter the URL of the new tab: ")
    open_tab(tab_name, tab_url)
        
# Added the ability to close an open tab.

def close_tab(index=None):
    """Close an open tab."""
    if not open_tabs_order:
        print("No tabs are open.")
        return

    if index is None:
 # If no index is provided, close the last opened tab
        tab_name = open_tabs_order.pop()
    else:
        try:
 # close the tab at the specified index
            tab_name = open_tabs_order.pop(index)
        except IndexError:
            print(f"Invalid index: {index}. No such tab.")
            return

    del tabs[tab_name]
    print(f"Tab '{tab_name}' closed successfully.")


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
    
# Save the current tabs to a text file.

def save_tabs(filename):
    """Save the current tabs to a text file."""
    with open(filename, 'w') as file:
        for tab_name in open_tabs_order:
            file.write(tab_name + '\n')
    print(f"Tabs saved to '{filename}'.")

# Import tabs from a text file.

def import_tabs(filename):
    """Import tabs from a text file."""
    global tabs, open_tabs_order
    with open(filename, 'r') as file:
        tab_names = [line.strip() for line in file.readlines()]
        tabs = {tab_name: {} for tab_name in tab_names}
        open_tabs_order = list(tabs.keys())
    print(f"Tabs imported from '{filename}'.")
    
while True:
    print("\nBrowser Tabs Simulation Menu:")
    print("1. OpenTab")
    print("2. CloseTab")
    print("3. SwitchTab")
    print("4. DisplayAllTabs")
    print("5. OpenNestedTab")
    print("6. ClearAllTabs")
    print("7. SaveTabs")
    print("8. ImportTabs")
    print("9. Exit")

    choice = input("Enter your choice (1-9): ")

    if choice == '1':
        add_new_tab()
    elif choice == '2':
        tab_name = input("Enter the name of the tab to close: ")
        close_tab(tab_name)
    elif choice == '3':
        tab_name = input("Enter the name of the tab to switch to: ")
        switch_tab(tab_name)
    elif choice == '4':
        display_all_tabs()
    elif choice == '5':
        parent_tab = input("Enter the name of the parent tab: ")
        nested_tab_name = input("Enter the name of the nested tab to open: ")
        open_nested_tab(parent_tab, nested_tab_name)
    elif choice == '6':
        clear_all_tabs()
    elif choice == '7':
        filename = input("Enter the filename to save tabs to: ")
        save_tabs(filename)
    elif choice == '8':
        filename = input("Enter the filename to import tabs from: ")
        import_tabs(filename)
    elif choice == '9':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 9.")
