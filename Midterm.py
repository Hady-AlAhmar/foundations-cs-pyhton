import requests
import json
tabs = {}


open_tabs_order = []

# Added the ability to open a new tab and check if a tab is already open.

def open_tab(tab_name, tab_url, tabsList):
    new_tab = {"name": tab_name, "URL": tab_url}
    tabsList.append(new_tab)


def add_new_tab(tabsList):
    """Add a new tab with title and URL."""
    tab_name = input("Enter the title of the new tab: ")
    tab_url = input("Enter the URL of the new tab as following https://website.com: ")
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
    if not tabs:
        print("No tabs open.")
    else:
        print("All open tabs:")
        display_tabs_recursive(tabs, level=0)

def display_tabs_recursive(tabs, level):
    for tab in tabs:
        print("  " * level + f"{tab['title']}")
        if 'tabs' in tab:
            display_tabs_recursive(tab['tabs'], level + 1)

def display_tab_content(url):
    try:
        response = requests.get(url)
        html_content = response.text
        print(f"Displaying content from {url}:\n")
        print(html_content)
    except requests.RequestException as e:
        print(f"Error fetching content: {e}")
        
# Added the ability to open a nested tab under a parent tab.

def open_nested_tab():
    if not tabs:
        print("No tabs available to nest under.")
        return

    index = input("Enter the index of the parent tab: ")
    if not index.isdigit() or not (0 <= int(index) < len(tabs)):
        print("Invalid parent tab index.")
        return

    parent_tab = tabs[int(index)]

    nested_tabs = []
    num_nested_tabs = int(input("Enter the number of nested tabs to create: "))

    for _ in range(num_nested_tabs):
        nested_title = input("Enter nested tab title: ")
        nested_url = input("Enter nested tab URL: ")
        nested_tabs.append({'title': nested_title, 'url': nested_url})

    if 'tabs' not in parent_tab:
        parent_tab['tabs'] = []

    parent_tab['tabs'].extend(nested_tabs)
    print(f"Opened {num_nested_tabs} nested tab(s) under: {parent_tab['title']}")   
        
# Added the ability to close all open tabs.

def clear_all_tabs():
    global tabs
    tabs = []
    print("All tabs cleared.")
    
# Save the current tabs to a text file.

def save_tabs(file_path):
    with open(file_path, 'w') as file:
        json.dump(tabs, file, indent=2)
    print(f"Tabs saved to {file_path}")

# Import tabs from a text file.

def import_tabs(file_path):
    global tabs
    try:
        with open(file_path, 'r') as file:
            tabs = json.load(file)
        print(f"Tabs loaded from {file_path}")
    except FileNotFoundError:
        print("File not found. Please enter a valid file path.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    
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
    elif choice == '2':
        index = input("Enter tab index to close (optional): ")
        close_tab(int(index) if index.isdigit() else None)
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
    elif choice == '7':
        file_path = input("Enter file path to save tabs: ")
        save_tabs(file_path)
    elif choice == "8":
        filename = input("Enter the filename to import tabs from: ")
        import_tabs(filename)
    elif choice == "9":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 9.")
