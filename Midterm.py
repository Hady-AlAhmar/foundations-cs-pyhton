import requests

tabs = {}


open_tabs_order = []

# Added the ability to open a new tab and check if a tab is already open.

def open_tab(tab_name, tab_url, tabsList):
    new_tab = {"name": tab_name, "URL": tab_url}
    tabsList.append(new_tab)


def add_new_tab(tabsList):
    """Add a new tab with title and URL."""
    tab_name = input("Enter the title of the new tab: ")
    tab_url = input("Enter the URL of the new tab: ")
    open_tab(tab_name, tab_url, tabsList)
        
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
    print(f"Tab '{tab_name}' closed successfully.")

# Added the ability to switch to a different tab.

def switch_tab(index=None):
    if not tabs:
        print("No tabs to switch.")
        return

    if index is None:
        index = len(tabs) - 1
    elif not 0 <= index < len(tabs):
        print("Invalid tab index.")
        return

    tab = tabs[index]
    print(f"Switched to tab {index + 1}: {tab['title']}")
    display_tab_content(tab['url'])

def display_tab_content(url):
    try:
        response = requests.get(url)
        html_content = response.text
        print(f"Displaying content from {url}:\n")
        print(html_content)
    except requests.RequestException as e:
        print(f"Error fetching content: {e}")

# Added the ability to display all open tabs.

def display_all_tabs():
    """Display all open tabs."""
    print("Open Tabs:")
    for tab in open_tabs_order:
        print(f"- {tab}")
        
# Added the ability to open a nested tab under a parent tab.

def open_nested_tab(parent_tab_index):
    """Open a nested tab under a parent tab."""
    parent_tab = open_tabs_order[parent_tab_index]
    if parent_tab:
        parent_tab["tabs"] = []
        add_new_tab(parent_tab["tabs"])
        # print(f"Nested tab '{nested_tab_name}' opened under '{parent_tab}'.")
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

    if choice == "1":
        add_new_tab(open_tabs_order)
    elif choice == "2":
        tab_name = int(input("Enter the name of the tab to close: "))
        close_tab(tab_name)
    elif choice == '3':
            index = input("Enter tab index to switch (optional): ")
            switch_tab(int(index) if index.isdigit() else None)
    elif choice == "4":
        display_all_tabs()
    elif choice == "5":
        parent_tab_index = int(input("Enter the index of the parent tab: "))
        open_nested_tab(parent_tab_index)
    elif choice == "6":
        clear_all_tabs()
    elif choice == "7":
        filename = input("Enter the filename to save tabs to: ")
        save_tabs(filename)
    elif choice == "8":
        filename = input("Enter the filename to import tabs from: ")
        import_tabs(filename)
    elif choice == "9":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 9.")
