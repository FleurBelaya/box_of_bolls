import json
import os


def default_data():
    return {
        "background": "",
        "pattern": "Обычный",
        "balls": []
    }


def project_file_path(folder):
    return os.path.join(folder, "project.json")


def create_project(folder):
    path = project_file_path(folder)
    if not os.path.exists(folder):
        os.makedirs(folder, exist_ok=True)
    if not os.path.exists(path):
        data = default_data()
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    return path

