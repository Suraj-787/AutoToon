# from google import genai
# from google.genai import types
# from PIL import Image
# from io import BytesIO
# import base64
# import os

# # === Initialize Gemini client ===
# api_key = "AIzaSyDaihqh33um9Allf3iss95g-Hxr7hdIlC8"
# client = genai.Client(api_key=api_key)

# # === Input your story here ===

# story = """
# The Clockmaker's Apprentice

# In the quiet town of Windmere, where time seemed to stroll rather than run, there lived an old clockmaker named Elias. His shop, nestled between a bakery and a bookshop, was filled with the gentle ticking of countless timepieces. Clocks of all shapes and sizes adorned the walls—grandfather clocks, cuckoos, pocket watches, even a mysterious clock with no hands.

# Elias worked alone until one day, a curious teenager named Lila walked in, her eyes wide with wonder.

# "Can you teach me how to fix time?" she asked, half-joking.

# Elias chuckled. "Time doesn't need fixing. But clocks? That's another story."

# He took her under his wing, teaching her not just the mechanics of gears and springs, but patience, precision, and respect for the invisible rhythm that ruled the world.

# As weeks passed, Lila noticed something odd. The handless clock ticked faster whenever someone lied nearby. It slowed when someone was sad. One evening, she confronted Elias.

# "That clock... it's alive, isn't it?"

# The old man sighed, then nodded. "It was my first invention—a truth clock. It doesn't tell time; it tells people."

# Years later, Elias passed on, leaving the shop to Lila. She kept fixing clocks, but the handless one remained untouched in the corner, quietly ticking away secrets of those who entered.

# And the townspeople of Windmere? They never knew that in a little shop of ticking hearts, time and truth quietly danced together.
# """

# def init_client(api_key):
#     return genai.Client(api_key=api_key)

# def split_story_into_scenes(story, max_words_per_scene=35):
#     sentences = story.strip().split('. ')
#     scenes = []
#     current_scene = ""
    
#     for sentence in sentences:
#         sentence += "." if not sentence.endswith('.') else ""
#         if len((current_scene + sentence).split()) < max_words_per_scene:
#             current_scene += sentence + " "
#         else:
#             scenes.append(current_scene.strip())
#             current_scene = sentence + " "
#     if current_scene:
#         scenes.append(current_scene.strip())
#     return scenes

# def generate_style_guide(client, story):
#     response = client.models.generate_content(
#         model="gemini-2.0-flash",
#         contents=[
#             "Create a detailed visual style guide for consistent comic generation including:",
#             "1. Character designs",
#             "2. Environment details",
#             "3. Key objects",
#             "4. Color palette recommendations",
#             "5. Consistent art style description",
#             f"Story: {story}"
#         ]
#     )
#     return ''.join(part.text for part in response.candidates[0].content.parts)

# def generate_panel_prompts(client, scenes, style_guide):
#     panel_prompts = []
#     for idx, scene in enumerate(scenes, 1):
#         response = client.models.generate_content(
#             model="gemini-2.0-flash",
#             contents=[
#                 "Generate a detailed comic panel description that:",
#                 "- Strictly follows the style guide",
#                 "- Maintains character/environment continuity",
#                 "- Includes specific visual elements",
#                 "- Always generate square images",
#                 f"Style Guide: {style_guide}",
#                 f"Current Panel ({idx}/{len(scenes)}): {scene}",
#                 "Previous Panel Summary: " + ("None" if idx==1 else panel_prompts[-1][:500]),
#                 "Output format: Detailed description focusing on visual consistency"
#             ]
#         )
#         panel_prompt = ''.join(part.text for part in response.candidates[0].content.parts)
#         panel_prompts.append(panel_prompt)
#     return panel_prompts

# def generate_comic_panels(client, panel_prompts):
#     """Generate images from panel prompts"""
#     cnt = 0
#     image_paths = []
    
#     for idx, prompt in enumerate(panel_prompts, 1):
#         try:
#             response = client.models.generate_content(
#                 model="gemini-2.0-flash-exp-image-generation",
#                 contents=prompt,
#                 config=types.GenerateContentConfig(
#                     response_modalities=['TEXT', 'IMAGE']
#                 )
#             )

#             for part in response.candidates[0].content.parts:
#                 if part.inline_data and part.inline_data.data:
#                     image_data = base64.b64decode(part.inline_data.data)
#                     image = Image.open(BytesIO(image_data))
#                     path = f"scene_{cnt}.png"
#                     image.save(path)
#                     image_paths.append(path)
#                     cnt += 1
#         except Exception as e:
#             print(f"Error generating scene {idx}: {str(e)}")
    
#     return image_paths

# def create_comic_pdf(image_paths, dpi=100):
#     """Create PDF from generated images"""
#     try:
#         scene_images = [Image.open(img).convert('RGB') for img in image_paths]
        
#         if not scene_images:
#             raise ValueError("No images generated")
        
#         width, height = scene_images[0].size
#         standardized_images = [img.resize((width, height)) for img in scene_images]

#         output_path = "comic_book.pdf"
#         standardized_images[0].save(
#             output_path,
#             save_all=True,
#             append_images=standardized_images[1:],
#             resolution=dpi,
#             quality=95,
#             optimize=True
#         )
#         return output_path
        
#     except Exception as e:
#         print(f"PDF creation error: {str(e)}")
#         return None









# from google import genai
# from google.genai import types
# from PIL import Image
# from io import BytesIO
# import base64
# from concurrent.futures import ThreadPoolExecutor
# import os

# # === Initialize Gemini client ===
# def init_client(api_key):
#     if not api_key or not isinstance(api_key, str):
#         raise ValueError("Invalid API key provided")
#     try:
#         return genai.Client(api_key=api_key)
#     except Exception as e:
#         raise ValueError(f"Failed to initialize Gemini client: {str(e)}")

# # === Split story into scenes ===
# def split_story_into_scenes(story, max_words_per_scene=35):
#     sentences = story.strip().split('. ')
#     scenes = []
#     current_scene = ""
#     for sentence in sentences:
#         sentence += "." if not sentence.endswith('.') else ""
#         if len((current_scene + sentence).split()) < max_words_per_scene:
#             current_scene += sentence + " "
#         else:
#             scenes.append(current_scene.strip())
#             current_scene = sentence + " "
#     if current_scene:
#         scenes.append(current_scene.strip())
#     return scenes

# # === Generate style guide with user-selected theme ===
# def generate_style_guide(client, story, user_style):
#     response = client.models.generate_content(
#         model="gemini-2.0-flash",
#         contents=[
#             "Create a detailed visual style guide for consistent comic generation including:",
#             "1. Character designs",
#             "2. Environment details",
#             "3. Key objects",
#             "4. Color palette recommendations",
#             "5. Consistent art style description",
#             f"User selected style: {user_style}",
#             f"Story: {story}"
#         ]
#     )
#     return ''.join(part.text for part in response.candidates[0].content.parts)

# # === Prompt generation in parallel ===
# def generate_single_panel_prompt(args):
#     idx, scene, style_guide, prev_scene, client, user_style = args
#     try:
#         response = client.models.generate_content(
#             model="gemini-2.0-flash",
#             contents=[
#                 f"Generate a detailed comic panel description in the style: {user_style}",
#                 "Strictly follow the provided visual style guide and maintain visual continuity across panels.",
#                 "Include:",
#                 "- Specific character/environment details",
#                 "- Important objects or scene elements",
#                 "- Emotion or action cues",
#                 "- Panel should be designed for a square image format",
#                 f"Style Guide: {style_guide}",
#                 f"Current Panel ({idx}): {scene}",
#                 f"Previous Panel Summary: {prev_scene or 'None'}",
#                 "Output: A richly detailed visual description matching the selected art style"
#             ]
#         )
#         return ''.join(part.text for part in response.candidates[0].content.parts)
#     except Exception as e:
#         print(f"[Prompt Error] Scene {idx}: {e}")
#         return ""

# def generate_panel_prompts_parallel(client, scenes, style_guide, user_style):
#     args = []
#     for idx, scene in enumerate(scenes, 1):
#         prev_scene = scenes[idx - 2] if idx > 1 else None
#         args.append((idx, scene, style_guide, prev_scene, client, user_style))
#     with ThreadPoolExecutor(max_workers=5) as executor:
#         return list(executor.map(generate_single_panel_prompt, args))

# # === Image generation in parallel ===
# def generate_single_comic_panel(args):
#     idx, prompt, client = args
#     try:
#         response = client.models.generate_content(
#             model="gemini-2.0-flash-exp-image-generation",
#             contents=prompt,
#             config=types.GenerateContentConfig(response_modalities=['TEXT', 'IMAGE'])
#         )

#         for part in response.candidates[0].content.parts:
#             if hasattr(part, "inline_data") and part.inline_data and part.inline_data.data:
#                 image_data = base64.b64decode(part.inline_data.data)
#                 image = Image.open(BytesIO(image_data))
#                 path = f"image/scene_{idx}.png"
#                 image.save(path)
#                 return path
#     except Exception as e:
#         print(f"[Image Error] Scene {idx}: {e}")
#     return None

# def generate_comic_panels_parallel(client, panel_prompts):
#     args = [(i, prompt, client) for i, prompt in enumerate(panel_prompts)]
#     with ThreadPoolExecutor(max_workers=4) as executor:
#         return list(filter(None, executor.map(generate_single_comic_panel, args)))

# # === Compile final PDF ===
# def create_comic_pdf(image_paths, dpi=100):
#     try:
#         scene_images = [Image.open(img).convert('RGB') for img in image_paths]
#         if not scene_images:
#             raise ValueError("No images generated")
#         width, height = scene_images[0].size
#         standardized_images = [img.resize((width, height)) for img in scene_images]
#         output_path = "image/comic_book.pdf"
#         standardized_images[0].save(
#             output_path,
#             save_all=True,
#             append_images=standardized_images[1:],
#             resolution=dpi,
#             quality=95,
#             optimize=True
#         )
#         return output_path
#     except Exception as e:
#         print(f"PDF creation error: {str(e)}")
#         return None

# # === Exported functions ===
# __all__ = [
#     "init_client",
#     "split_story_into_scenes",
#     "generate_style_guide",
#     "generate_panel_prompts_parallel",
#     "generate_comic_panels_parallel",
#     "create_comic_pdf"
# ]


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
        st.error(f"❌ Failed to initialize Gemini client: {str(e)}")
        raise ValueError(f"Failed to initialize Gemini client: {str(e)}")

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
        st.error(f"❌ Error generating style guide: {e}")
        return ""

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
    except Exception as e:
        st.error(f"[Prompt Error] Scene {idx}: {e}")
        return ""

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
                path = f"image/scene_{idx}.png"
                image.save(path)
                return path
    except Exception as e:
        st.error(f"[Image Error] Scene {idx}: {e}")
    return None

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
        output_path = "image/comic_book.pdf"
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
        st.error(f"❌ PDF creation error: {str(e)}")
        return None

# === Exported functions ===
__all__ = [
    "init_client",
    "split_story_into_scenes",
    "generate_style_guide",
    "generate_panel_prompts_parallel",
    "generate_comic_panels_parallel",
    "create_comic_pdf"
]
