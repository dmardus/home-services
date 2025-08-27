import os

def validate_directory(path: str):
    if not os.path.isdir(path):
        raise ValueError(f"❌ Data path '{path}' does not exist or is not a directory.")
