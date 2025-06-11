import os
from flask import Flask, render_template, request
from image_generator import generate_image

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'templates'))
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'static'))
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

models = [
    "MoneyPrinterTurbo", "Anime Character Generator", "Jackey", "Polynate", "Memed",
    "Elixpo-Art", "MIDIjourney", "TurboReel", "StoryWeaver", "AI PPT Maker",
    "flux", "turbo"
]

themes = [
    "realistic landscape", "anime girl", "fantasy city", "3D robot", 
    "cyberpunk street", "pixel art dragon", "cartoon dog", "space station", "ancient ruins"
]

@app.route("/", methods=["GET", "POST"])
def index():
    image_path = None
    if request.method == "POST":
        prompt = request.form["prompt"]
        model = request.form["model"]
        theme = request.form["theme"]
        aspect_ratio = "1:1"  # We can upgrade later to allow selecting ratio

        final_prompt = f"{prompt}, {theme}"

        image_path = generate_image(final_prompt, model, aspect_ratio)

    return render_template("index.html", models=models, themes=themes, image_path=image_path)

if __name__ == "__main__":
    app.run(debug=True)
