# import required modules

import argparse
from main import create_project_dir, create_project_files, create_readme_from_template


def call_create_readme(args):
    
    location = args.readme[0]
	
    project = args.readme[1]
     
    author = args.readme[2]
    create_readme_from_template(location, project, author)

def call_create_project(args):

    location = args.project[0]
	
    project = args.project[1]
     
    author = args.project[2]

    project_path = create_project_dir(name=project, location=location)
    create_project_files(project=project, author=author, project_path=project_path)

def main():
    # create the parser

    parser = argparse.ArgumentParser(description="An auto project starter")

    # two arguments, create project files, create readme only
    # readme only
    parser.add_argument("-r", "--readme", type=str, nargs=3,
                        metavar=("location","project", "author"), 
                        help="Create a README at the specified location with the given project and author name")
    
    
    parser.add_argument("-p", "--project", type=str, nargs=3,
                        metavar=("location","project", "author"),
                        help="Create project directory and project files: README.md, TODO.md and main.py")
    # parse the arguments from the input
    args = parser.parse_args()

    if args.readme !=None:
        call_create_readme(args)
    elif args.project !=None:
        call_create_project(args)


if __name__ == "__main__":
    main()