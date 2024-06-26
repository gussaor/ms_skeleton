import shutil
import os
import sys

def eliminate_skip_directory() -> None:
    """
    Eliminates a directory named 'skip' along with its contents.
    """
    decision: bool = {{ cookiecutter.include_optional_dir }}
    c2: str = "{{ cookiecutter.optional_dir }}"
    c1: str = "{{ cookiecutter.project_slug }}"
    directory: str = f"{c1}\{c2}"
    if decision==False:
        try:
            sys.stdout.write(f"{directory}\n")
            skip_dir = os.path.join(os.getcwd(), c2)
            sys.stdout.write(f"trying to eliminate path :{skip_dir}\n")
            if os.path.exists(skip_dir):
                shutil.rmtree(skip_dir)
                sys.stdout.write(f"Path eliminated\n")
            else:
                sys.stdout.write(f"Path does not exist\n")
        except:
            sys.stdout.write(f"Failed to enter conditional\n")

def main():
    eliminate_skip_directory()
    return

if __name__ == "__main__":
    main()