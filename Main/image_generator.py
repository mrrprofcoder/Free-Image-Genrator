import urllib.parse

# Map models to pollinations codes if needed
model_mapping = {
    "Elixpo-Art": "boltning",
    "flux": "flux",
    "turbo": "turbo"
}

def generate_image(prompt, model, aspect_ratio):
    base_url = "https://image.pollinations.ai/prompt/"
    encoded_prompt = urllib.parse.quote(prompt)

    model_code = model_mapping.get(model, None)

    if model_code:
        url = f"{base_url}{encoded_prompt}?model={model_code}&aspectRatio={aspect_ratio}"
    else:
        url = f"{base_url}{encoded_prompt}?aspectRatio={aspect_ratio}"

    return url
