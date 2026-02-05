import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECTS_DIR = os.path.join(BASE_DIR, "projects")


def ensure_dir():
    if not os.path.exists(PROJECTS_DIR):
        os.makedirs(PROJECTS_DIR, exist_ok=True)


def project_path(name):
    ensure_dir()
    safe_name = "".join(c for c in name if c not in "\\/:*?\"<>|")
    return os.path.join(PROJECTS_DIR, safe_name + ".json")


def list_projects():
    ensure_dir()
    result = []
    for file_name in os.listdir(PROJECTS_DIR):
        if file_name.lower().endswith(".json"):
            result.append(os.path.splitext(file_name)[0])
    result.sort()
    return result


def create_default_project():
    return {
        "background": "",
        "pattern": "Обычный",
        "balls": []
    }


def load_project(name):
    path = project_path(name)
    if not os.path.exists(path):
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return None


def save_project(name, data):
    path = project_path(name)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

