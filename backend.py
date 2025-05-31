from google import genai
from google.genai import types
from PIL import Image
from io import BytesIO
import base64
from concurrent.futures import ThreadPoolExecutor
import os
import streamlit as st


# === Initialize Gemini client ===
def init_client(api_key):
    if not api_key or not isinstance(api_key, str):
        raise ValueError("Invalid API key provided")
    try:
        return genai.Client(api_key=api_key)
    except Exception as e:
        raise ValueError(f"❌ Failed to initialize Gemini client: {str(e)}")

# === Split story into scenes ===
def split_story_into_scenes(story, max_words_per_scene=35):
    sentences = story.strip().split('. ')
    scenes = []
    current_scene = ""
    for sentence in sentences:
        sentence += "." if not sentence.endswith('.') else ""
        if len((current_scene + sentence).split()) < max_words_per_scene:
            current_scene += sentence + " "
        else:
            scenes.append(current_scene.strip())
            current_scene = sentence + " "
    if current_scene:
        scenes.append(current_scene.strip())
    return scenes

# === Generate style guide with user-selected theme ===
def generate_style_guide(client, story, user_style):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[
                "Create a detailed visual style guide for consistent comic generation including:",
                "1. Character designs",
                "2. Environment details",
                "3. Key objects",
                "4. Color palette recommendations",
                "5. Consistent art style description",
                f"User selected style: {user_style}",
                f"Story: {story}"
            ]
        )
        return ''.join(part.text for part in response.candidates[0].content.parts)
    except Exception as e:
        return ""  # Don't use st.error here, handle outside

# === Prompt generation in parallel ===
def generate_single_panel_prompt(args):
    idx, scene, style_guide, prev_scene, client, user_style = args
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=[
                f"Generate a detailed comic panel description in the style: {user_style}",
                "Strictly follow the provided visual style guide and maintain visual continuity across panels.",
                "Include:",
                "- Specific character/environment details",
                "- Important objects or scene elements",
                "- Emotion or action cues",
                "- Panel should be designed for a square image format",
                f"Style Guide: {style_guide}",
                f"Current Panel ({idx}): {scene}",
                f"Previous Panel Summary: {prev_scene or 'None'}",
                "Output: A richly detailed visual description matching the selected art style"
            ]
        )
        return ''.join(part.text for part in response.candidates[0].content.parts)
    except Exception:
        return ""  # Skip this prompt on error

def generate_panel_prompts_parallel(client, scenes, style_guide, user_style):
    args = []
    for idx, scene in enumerate(scenes, 1):
        prev_scene = scenes[idx - 2] if idx > 1 else None
        args.append((idx, scene, style_guide, prev_scene, client, user_style))
    with ThreadPoolExecutor(max_workers=5) as executor:
        return list(executor.map(generate_single_panel_prompt, args))

# === Image generation in parallel ===
def generate_single_comic_panel(args):
    idx, prompt, client = args
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash-exp-image-generation",
            contents=prompt,
            config=types.GenerateContentConfig(response_modalities=['TEXT', 'IMAGE'])
        )

        for part in response.candidates[0].content.parts:
            if hasattr(part, "inline_data") and part.inline_data and part.inline_data.data:
                image_data = base64.b64decode(part.inline_data.data)
                image = Image.open(BytesIO(image_data))
                path = f"scene_{idx}.png"
                image.save(path)
                return path
    except Exception:
        return None  # Skip image on error

def generate_comic_panels_parallel(client, panel_prompts):
    args = [(i, prompt, client) for i, prompt in enumerate(panel_prompts)]
    with ThreadPoolExecutor(max_workers=4) as executor:
        return list(filter(None, executor.map(generate_single_comic_panel, args)))

# === Compile final PDF ===
def create_comic_pdf(image_paths, dpi=100):
    try:
        scene_images = [Image.open(img).convert('RGB') for img in image_paths]
        if not scene_images:
            raise ValueError("No images generated")
        width, height = scene_images[0].size
        standardized_images = [img.resize((width, height)) for img in scene_images]
        output_path = "comic_book.pdf"
        standardized_images[0].save(
            output_path,
            save_all=True,
            append_images=standardized_images[1:],
            resolution=dpi,
            quality=95,
            optimize=True
        )
        return output_path
    except Exception as e:
        return None  # Handle error in app

# === Exported functions ===
__all__ = [
    "init_client",
    "split_story_into_scenes",
    "generate_style_guide",
    "generate_panel_prompts_parallel",
    "generate_comic_panels_parallel",
    "create_comic_pdf"
]
