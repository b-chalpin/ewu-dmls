import sys
import os
import shutil

def main() -> None:
    if len(sys.argv) != 2:
        print("Error: Expected only one argument <model_name>")
        exit(1)

    new_model_name = sys.argv[1]

    if new_model_name in os.listdir("../models"):
        print(f"Error: Model with name {new_model_name} already exists. Please choose a different name")
        exit(1)

    new_model_dir = f"../models/{new_model_name}"

    os.mkdir(new_model_dir)
    shutil.copytree(src="../common/template", dst=new_model_dir, dirs_exist_ok=True)

    print(f"New model template created at {os.path.abspath(new_model_dir)}")

if __name__ == "__main__":
    main()
