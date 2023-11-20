import customtkinter

from main import create_project_dir, create_project_files, create_readme_from_template


# calls function to create project folder and files
def call_create_all_files():
    location = location_entry.get()

    project = project_entry.get()

    author = author_entry.get()

    if not location or not project or not author:

        warning = customtkinter.CTkLabel(master=frame, text="Please enter a file path!", font=("Courier", 18), text_color="red")

        warning.grid(row=12, column=0, pady=12, padx=10)
    else:
        success = customtkinter.CTkLabel(master=frame, text="Folder created", font=("Courier", 18), text_color="green")

        success.grid(row=12, column=0, pady=12, padx=10)
        project_path = create_project_dir(name=project, location=location)

        create_project_files(project=project, author=author, project_path=project_path)

       
        success_files_msg = customtkinter.CTkLabel(master=frame, text="README.md, TODO.md and main.py created!", font=("Courier", 18), text_color="green")

        success_files_msg.grid(row=13, column=0, pady=12, padx=10)
    

# calls function to create readme only
def call_create_readme():

    location = location_entry.get()
    project = project_entry.get()
    author = author_entry.get()

    if not location or not project or not author:

        warning = customtkinter.CTkLabel(master=frame, text="Please enter a file path!", font=("Courier", 18), text_color="red")

        warning.grid(row=12, column=0, pady=12, padx=10)

    else:
        
        create_readme_from_template(project, author, location)

        success_msg = customtkinter.CTkLabel(master=frame, text="README.md created!", font=("Courier", 18), text_color="green")

        success_msg.grid(row=13, column=0, pady=12, padx=10)

# set customtkinter theme
customtkinter.set_appearance_mode("dark")

customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()

root.maxsize(1000, 1000)

root.title("Auto Project Starter")

frame = customtkinter.CTkFrame(master=root, width=800, height=700)

frame.grid(row=0, column=0, padx=10, pady=10)





title=customtkinter.CTkLabel(master=frame, text="Auto Project Starter", font=("Courier", 24) )

title.grid(row=1, column=0, pady=12, padx=10 )

## Could make this into a for loop eventually
## LOCATION
location_label= customtkinter.CTkLabel(master=frame, text="Project location:", font=("Courier", 18))

location_label.grid(row=2, column=0, pady=12, padx=0,  )

location_entry = customtkinter.CTkEntry(width=220, master=frame)

location_entry.grid(row=3, column=0, pady=12, padx=10,  )



## PROJECT NAME
project_label= customtkinter.CTkLabel(master=frame, text="Project name:", font=("Courier", 18))

project_label.grid(row=4, column=0, pady=12, padx=10)

project_entry = customtkinter.CTkEntry(width=220, master=frame)

project_entry.grid(row=5, column=0, pady=12, padx=10)


## PROJECT AUTHOR
author_label= customtkinter.CTkLabel(master=frame, text="Project author:", font=("Courier", 18))

author_label.grid(row=6, column=0, pady=12, padx=10)

author_entry = customtkinter.CTkEntry(width=220, master=frame)

author_entry.grid(row=7, column=0, pady=12, padx=10)

## BUTTONS
sort_button = customtkinter.CTkButton(master=frame, text="Create project folder & files", command=(call_create_all_files), font=("Courier", 18))

sort_button.grid(row=10, column=0, pady=10, padx=10, sticky="nswe")

readme_button = customtkinter.CTkButton(master=frame, text="Create README only", command=(call_create_readme), font=("Courier", 18))

readme_button.grid(row=11, column=0, pady=10, padx=10, sticky="nswe")

root.mainloop()

