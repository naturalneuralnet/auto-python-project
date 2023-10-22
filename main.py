import os
import re
from mdutils.mdutils import MdUtils
import time
from jinja2 import Template
import codecs
# repeatedly ask the user until a valid input is acheived
# suggest a better name to the user - will do this later
# exit after three attempts

unix_time = str(int(time.time()))


def get_project_name():
    print(type(unix_time))
    valid_count = 0
    while valid_count < 3:
        print(valid_count)
        project_name = input("What is the name of the project?")
        # project_name = "TestProject" + unix_time
        print(project_name)
    # this regex limits the characters ^ indicates to the regex to check from the start of the string
    # and everyhting in [] brackets is whats permitted
    # a-z, A-Z, 0-9, - are all permitted, the dash is its own thing
    # then there is {1, 40} which limits the character lenght
    # $ dollar sign at the end to mark the end of whats allowed.
        if not re.match("^[a-zA-Z0-9-]{1,40}$", project_name):
            print("Invalid Project name. Try Again")
            valid_count += 1
        else:
            valid_count = 3
            return project_name


def get_project_author_name():
    valid_count = 0
    while valid_count < 3:
        print(valid_count)
        author_name = input("What is the name of the author?")
        # author_name = "Nattie"
        if not re.match("^[a-zA-Z0-9]{1,40}$", author_name):
            print("Invalid Author Name. Try Again")
            valid_count += 1
        else:
            valid_count = 3
        return author_name


project = get_project_name()
author = get_project_author_name()

print(f"The name of the project is: {project}")
print(f"The author of the project is: {author}")


def create_project_dir(name, location):
    path = location + name
    os.mkdir(path)
    print(f"Project directory {name} created at: {path}")
    return path


project_path = create_project_dir(
    project, "C:/Users/POWEHI/Desktop/Projects/autoProjectStarter/")


def create_readme(project, author, location):
    # create a README file with the project and author name
    path = location + '/README.md'
    print(path)
    print(project)
    mdFile = MdUtils(file_name=path)

    # Add Headings to the md file
    mdFile.new_header(level=1, title=project)
    mdFile.new_header(level=2, title='About')
    mdFile.write('EHLLO')

    mdFile.new_header(level=2, title="Installation")
    mdFile.write(' \n')
    mdFile.new_header(level=2, title="How to Run Locally")
    mdFile.write(' \n')
    mdFile.new_header(level=2, title="Author")
    mdFile.write(' \n')
    mdFile.write(f'The author of this project is {author}')
    mdFile.new_header(level=2, title="License")
    mdFile.write(' \n')
    mdFile.new_table_of_contents(table_title='Contents', depth=2)
    # THIS NEEDS TO BE LAST
    mdFile.create_md_file()


# create_readme(project, author, project_path)


def create_readme_from_template():
    # render the template
    with open('README.template.md', 'r') as file:
        template = Template(file.read(), trim_blocks=True)
    rendered_file = template.render(name=project, author=author)

    # output the file
    path = project_path + "/README.md"
    output_file = codecs.open(path, "w", "utf-8")
    output_file.write(rendered_file)
    output_file.close()


def create_todo_from_template():
    # render the template
    with open('ToDo.template.md', 'r') as file:
        template = Template(file.read(), trim_blocks=True)
    rendered_file = template.render(name=project, author=author)

    # output the file
    path = project_path + "/TODO.md"
    output_file = codecs.open(path, "w", "utf-8")
    output_file.write(rendered_file)
    output_file.close()


def create_main_from_template():
    # render the template
    with open('main.template.md', 'r') as file:
        template = Template(file.read(), trim_blocks=True)
    rendered_file = template.render(name=project, author=author)

    # output the file
    path = project_path + "/main.py"
    output_file = codecs.open(path, "w", "utf-8")
    output_file.write(rendered_file)
    output_file.close()


# create_readme_from_template()
# create_todo_from_template()
# create_main_from_template()


def create_file_from_template(template_file, template_params, output_file_path):
    # render the template
    with open(template_file, 'r') as file:
        template = Template(file.read(), trim_blocks=True)
    rendered_file = template.render(
        name=template_params['project'], author=template_params['author'])
    # output the file

    output_file = codecs.open(output_file_path, "w", "utf-8")
    output_file.write(rendered_file)
    output_file.close()


# create_file_from_template(
#     template_file='README.template.md',
#     template_params={"project": project, "author": author},
#     output_file_path=project_path + "/README.md"
# )
# create_file_from_template(
#     template_file='ToDo.template.md',
#     template_params={"project": project, "author": author},
#     output_file_path=project_path + "/TODO.md"
# )
# create_file_from_template(
#     template_file='main.template.md',
#     template_params={"project": project, "author": author},
#     output_file_path=project_path + "/main.py"
# )

create_file_from_template(
    template_file='README.template.md',
    template_params={"project": project, "author": author},
    output_file_path=project_path + "/README.md"
)
