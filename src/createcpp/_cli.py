import os
import sys

from ._data import (clang_format_file, clang_tidy_file, cmake_file,
                    gitignore_file, main_file, readme_file)


def main():
    # check fir project name in args
    if len(sys.argv) < 2:
        print("Please provide a project name")
        return

    project_name = sys.argv[1]

    # try to create project folder
    try:
        os.mkdir(project_name)
    except FileExistsError:
        print("Project folder already exists")
        return

    except OSError:
        print("Error creating project folder")
        return

    # create src folder
    os.mkdir(f"{project_name}/src")

    # create project files
    try:
        with open(f"{project_name}/CMakeLists.txt", "w") as f:
            f.write(cmake_file(project_name))

        with open(f"{project_name}/.clang-format", "w") as f:
            f.write(clang_format_file())

        with open(f"{project_name}/.clang-tidy", "w") as f:
            f.write(clang_tidy_file())

        with open(f"{project_name}/.gitignore", "w") as f:
            f.write(gitignore_file())

        with open(f"{project_name}/src/main.cpp", "w") as f:
            f.write(main_file())
        
        with open(f"{project_name}/README.md", "w") as f:
            f.write(readme_file(project_name))

    except OSError:
        print("Error creating project files")
        return

    print("Project created successfully")

if __name__ == "__main__":
    main()