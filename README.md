## About

A python script which automates the manual steps usually taken to setup a project. It generates a project folder, README, TODO and main.py with the appropriate details. The template files are included in the project to allow for easy modification to satisfy more specific use cases.

This script now includes a GUI.

This project now includes a CLI.

![Alt text](image.png)

## Table of Contents

- [Local Setup](#local-setup)
- [Status](#Status)
- [License](#license)

## Local Setup

Clone or Download the repository from Github

Install dependencies

`pip install -r requirements.txt`

Run the python script

`python auto_starter_gui.py`

A CLI has been added. Run with -p argument to create all the project files or the -r option to create a README.md only. For example,

`python auto_starter_cli.py -p C:\Users\Nattie project_name author`

will create a directory called project_name at the given location as well as the README.md, TODO.md and main.py files inside the project_name directory. 

## Status

Completed.

In the future I hope to add additional templates such as a Django project template.

## License

This project is licensed under the terms of the MIT license.

You can find the License for this project [here](LICENSE.md)