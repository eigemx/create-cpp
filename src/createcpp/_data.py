"""
Define the data to be written to files
"""


def cmake_file(project_name: str) -> str:
    cmake_file_data = f"""cmake_minimum_required(VERSION 3.20)
project({project_name} VERSION 0.0.1 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# if build type is not specified, default to release
if(NOT CMAKE_BUILD_TYPE)
    set(CMAKE_BUILD_TYPE Release)
endif()

# set compiler flags
set(CMAKE_CXX_FLAGS "-Wall -Wextra -Wpedantic -Werror")
set(CMAKE_CXX_FLAGS_DEBUG "-g")
set(CMAKE_CXX_FLAGS_RELEASE "-O2")"""

    cmake_file_data += """
# set output directories
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)
set(CMAKE_LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/lib)

# generate compile_commands.json to be used by clang-tidy
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

"""

    cmake_file_data += f"add_executable({project_name} src/main.cpp)"

    return cmake_file_data


def clang_tidy_file() -> str:
    return """Checks: 
        '-*,modernize-*, readability-*, performance-*, misc-*, cppcoreguidelines-*,
         -cppcoreguidelines-avoid-magic-numbers, 
         -modernize-use-nodiscard'
WarningsAsErrors: '*'"""


def clang_format_file() -> str:
    return """BasedOnStyle: Google
IndentWidth: 4
ColumnLimit: 98
AllowShortFunctionsOnASingleLine: Inline
AllowShortIfStatementsOnASingleLine: false
AllowShortLoopsOnASingleLine: false
AlignConsecutiveAssignments: false
AlignConsecutiveDeclarations: false
AlignTrailingComments: true
SpacesBeforeTrailingComments: 1
SpaceBeforeCpp11BracedList: true
SortIncludes: true
AccessModifierOffset: -4
KeepEmptyLinesAtTheStartOfBlocks: false
MaxEmptyLinesToKeep: 2
FixNamespaceComments: true
ReflowComments: false
BreakBeforeBraces: Custom
BraceWrapping:
  AfterCaseLabel:  false
  AfterClass:      false
  AfterControlStatement: false
  AfterEnum:       false
  AfterFunction:   false
  AfterNamespace:  false
  AfterObjCDeclaration: false
  AfterStruct:     false
  AfterUnion:      false
  BeforeCatch:     false
  BeforeElse:      false
  IndentBraces:    false
DerivePointerAlignment: false
PointerAlignment: Left
SortUsingDeclarationsOptions: true
AccessModifierOffset: -2

# https://stackoverflow.com/q/29483626/2839539
# Allow putting all parameters of a function declaration onto the next line 
# even if BinPackParameters is false.
AllowAllParametersOfDeclarationOnNextLine: false
ExperimentalAutoDetectBinPacking: false

# If false, a function call’s arguments will either be all on the same line 
# or will have one line each.
BinPackArguments: false
# If false, a function call’s arguments will either be all
# on the same line or will have one line each.
BinPackParameters: false"""


def gitignore_file() -> str:
    return """build/
.vscode/"""


def main_file() -> str:
    # return a Hello, World! program
    return """#include <iostream>

auto main() -> int {
    std::cout << "Hello, World!" << std::endl;
    return 0;
}
"""


def readme_file(project_name: str) -> str:
    return f"""# {project_name}
Hello, World!"""


file_to_function_map = {
    "CMakeLists.txt": {"func": cmake_file, "require_name": True},
    ".clang-tidy": {"func": clang_tidy_file, "require_name": False},
    ".clang-format": {"func": clang_format_file, "require_name": False},
    ".gitignore": {"func": gitignore_file, "require_name": False},
    "src/main.cpp": {"func": main_file, "require_name": False},
    "README.md": {"func": readme_file, "require_name": True},
}
