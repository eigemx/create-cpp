import os
import sys

from ._data import file_to_function_map


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
        for file_name, file_info in file_to_function_map.items():
            file_path = f"{project_name}/{file_name}"
            with open(file_path, "w") as f:
                if file_info["require_name"]:
                    f.write(file_info["func"](project_name))
                else:
                    f.write(file_info["func"]())
    except OSError as e:
        print("Error creating project files")
        print("Error:", e)
        return

    print("Project created successfully")


if __name__ == "__main__":
    main()
