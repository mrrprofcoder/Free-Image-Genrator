import json

def load_styles():
    with open("static/style_presets.json", "r") as file:
        return json.load(file)
