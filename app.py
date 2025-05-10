# # import streamlit as st
# # import time
# # from backend import (
# #     init_client,
# #     split_story_into_scenes,
# #     generate_style_guide,
# #     generate_panel_prompts,
# #     generate_comic_panels,
# #     create_comic_pdf
# # )

# # def main():
# #     st.set_page_config(page_title="AI Comic Generator", layout="wide")
# #     st.title("AutoToon")
    
# #     # Sidebar controls
# #     with st.sidebar:
# #         st.header("Settings")
# #         api_key = st.text_input("Gemini API Key", type="password")
# #         max_words = st.slider("Words per Scene", 20, 50, 35)
# #         dpi = st.select_slider("PDF Quality", options=[72, 150, 300], value=150)
    
# #     # Main content
# #     story = st.text_area("Enter your story:", height=400)
    
# #     if st.button("Generate Comic") and story and api_key:
# #         with st.status("Generating...", expanded=True) as status:
# #             try:
# #                 # Validate API key
# #                 try:
# #                     client = init_client(api_key)
# #                 except Exception as e:
# #                     st.error("Invalid API key. Please check your Gemini API key and try again.")
# #                     st.stop()
                
# #                 st.write("1️⃣ Splitting story into scenes...")
# #                 scenes = split_story_into_scenes(story, max_words)
                
# #                 st.write("2️⃣ Creating style guide...")
# #                 style_guide = generate_style_guide(client, story)
                
# #                 st.write("3️⃣ Generating panel prompts...")
# #                 panel_prompts = generate_panel_prompts(client, scenes, style_guide)
                
# #                 st.write("4️⃣ Drawing comic panels...")
# #                 image_paths = generate_comic_panels(client, panel_prompts)
                
# #                 if not image_paths:
# #                     st.error("Failed to generate any comic panels. Please try again.")
# #                     st.stop()
                
# #                 st.write("5️⃣ Compiling PDF...")
# #                 pdf_path = create_comic_pdf(image_paths, dpi)
                
# #                 if not pdf_path:
# #                     st.error("Failed to create PDF. Please try again.")
# #                     st.stop()
                
# #                 status.update(label="Done!", state="complete")
                
# #                 # Display results
# #                 st.success("Comic generated successfully!")
# #                 cols = st.columns(3)
# #                 for i, img_path in enumerate(image_paths):
# #                     with cols[i % 3]:
# #                         st.image(img_path, caption=f"Panel {i+1}")
                
# #                 with open(pdf_path, "rb") as f:
# #                     st.download_button(
# #                         "Download PDF",
# #                         f,
# #                         file_name="my_comic.pdf",
# #                         mime="application/pdf"
# #                     )
                
# #             except Exception as e:
# #                 st.error(f"Error: {str(e)}")
# #                 st.stop()

# # if __name__ == "__main__":
# #     main()




# # import streamlit as st
# # import time
# # from backend import (
# #     init_client,
# #     split_story_into_scenes,
# #     generate_style_guide,
# #     generate_panel_prompts_parallel,
# #     generate_comic_panels_parallel,
# #     create_comic_pdf
# # )

# # def main():
# #     st.set_page_config(page_title="AI Comic Generator", layout="wide")
# #     st.title("AutoToon")

# #     # Sidebar controls
# #     with st.sidebar:
# #         st.header("Settings")
# #         api_key = st.text_input("Gemini API Key", type="password")
# #         max_words = st.slider("Words per Scene", 20, 50, 35)
# #         dpi = st.select_slider("PDF Quality", options=[72, 150, 300], value=150)

# #     # Main content
# #     story = st.text_area("Enter your story:", height=400)

# #     if st.button("Generate Comic") and story and api_key:
# #         with st.status("Generating Comic...", expanded=True) as status:
# #             try:
# #                 # Validate API key
# #                 try:
# #                     client = init_client(api_key)
# #                 except Exception as e:
# #                     st.error("Invalid API key. Please check your Gemini API key and try again.")
# #                     st.stop()

# #                 st.write("1️⃣ Splitting story into scenes...")
# #                 scenes = split_story_into_scenes(story, max_words)

# #                 st.write(f"✂️ Detected {len(scenes)} scenes.")

# #                 st.write("2️⃣ Creating style guide...")
# #                 style_guide = generate_style_guide(client, story)

# #                 st.write("3️⃣ Generating panel prompts (parallel)...")
# #                 panel_prompts = generate_panel_prompts_parallel(client, scenes, style_guide)

# #                 st.write("4️⃣ Drawing comic panels (parallel)...")
# #                 image_paths = generate_comic_panels_parallel(client, panel_prompts)

# #                 if not image_paths:
# #                     st.error("Failed to generate any comic panels. Please try again.")
# #                     st.stop()

# #                 st.write("5️⃣ Compiling PDF...")
# #                 pdf_path = create_comic_pdf(image_paths, dpi)

# #                 if not pdf_path:
# #                     st.error("Failed to create PDF. Please try again.")
# #                     st.stop()

# #                 status.update(label="✅ Comic Generation Complete!", state="complete")

# #                 # Display results
# #                 st.success("🎉 Comic generated successfully!")
# #                 cols = st.columns(3)
# #                 for i, img_path in enumerate(image_paths):
# #                     with cols[i % 3]:
# #                         st.image(img_path, caption=f"Panel {i+1}")

# #                 with open(pdf_path, "rb") as f:
# #                     st.download_button(
# #                         "📥 Download Comic PDF",
# #                         f,
# #                         file_name="my_comic.pdf",
# #                         mime="application/pdf"
# #                     )

# #             except Exception as e:
# #                 st.error(f"❌ Error: {str(e)}")
# #                 st.stop()

# # if __name__ == "__main__":
# #     main()



# import streamlit as st
# import time
# from backend import (
#     init_client,
#     split_story_into_scenes,
#     generate_style_guide,
#     generate_panel_prompts_parallel,
#     generate_comic_panels_parallel,
#     create_comic_pdf
# )

# def main():
#     st.set_page_config(page_title="AI Comic Generator", layout="wide")
#     st.title("AutoToon")

#     # Sidebar controls
#     with st.sidebar:
#         st.header("Settings")
#         api_key = st.text_input("Gemini API Key", type="password")
#         if not api_key:
#             st.warning("⚠️ Please enter a valid Gemini API key.")
#         max_words = st.slider("Words per Scene", 20, 50, 35)
#         dpi = st.select_slider("PDF Quality", options=[72, 150, 300], value=150)
#         style = st.selectbox("Choose Comic Art Style", [
#             "2D (Flat Art)",
#             "Manga Style",
#             "Vector Art",
#             "Painted / Watercolor Style",
#             "3D Rendered (Stylized)",
#             "Grayscale / Black & White",
#             "Ink & Brush (Traditional Inking)"
#         ])

#     # Main content
#     story = st.text_area("Enter your story:", height=400)

#     if st.button("Generate Comic") and story and api_key:
#         with st.status("Generating Comic...", expanded=True) as status:
#             try:
#                 # Validate API key
#                 try:
#                     client = init_client(api_key)
#                 except Exception as e:
#                     st.warning("⚠️ Invalid API key. Please check your Gemini API key and try again.")
#                     st.stop()

#                 st.write("1️⃣ Splitting story into scenes...")
#                 scenes = split_story_into_scenes(story, max_words)

#                 st.write(f"✂️ Detected {len(scenes)} scenes.")

#                 st.write("2️⃣ Creating style guide...")
#                 style_guide = generate_style_guide(client, story, style)

#                 st.write("3️⃣ Generating panel prompts (parallel)...")
#                 panel_prompts = generate_panel_prompts_parallel(client, scenes, style_guide)

#                 st.write("4️⃣ Drawing comic panels (parallel)...")
#                 image_paths = generate_comic_panels_parallel(client, panel_prompts)

#                 if not image_paths:
#                     st.error("Failed to generate any comic panels. Please try again.")
#                     st.stop()

#                 st.write("5️⃣ Compiling PDF...")
#                 pdf_path = create_comic_pdf(image_paths, dpi)

#                 if not pdf_path:
#                     st.error("Failed to create PDF. Please try again.")
#                     st.stop()

#                 status.update(label="✅ Comic Generation Complete!", state="complete")

#                 # Display results
#                 st.success("🎉 Comic generated successfully!")
#                 cols = st.columns(3)
#                 for i, img_path in enumerate(image_paths):
#                     with cols[i % 3]:
#                         st.image(img_path, caption=f"Panel {i+1}")

#                 with open(pdf_path, "rb") as f:
#                     st.download_button(
#                         "📥 Download Comic PDF",
#                         f,
#                         file_name="my_comic.pdf",
#                         mime="application/pdf"
#                     )

#             except Exception as e:
#                 st.error(f"❌ Error: {str(e)}")
#                 st.stop()

# if __name__ == "__main__":
#     main()



import streamlit as st
import time
from backend import (
    init_client,
    split_story_into_scenes,
    generate_style_guide,
    generate_panel_prompts_parallel,
    generate_comic_panels_parallel,
    create_comic_pdf
)

def main():
    st.set_page_config(page_title="AI Comic Generator", layout="wide")
    st.title("AutoToon")

    # Sidebar controls
    with st.sidebar:
        st.header("Settings")
        api_key = st.text_input("Gemini API Key", type="password")
        if not api_key:
            st.warning("⚠️ Please enter a valid Gemini API key.")
        max_words = st.slider("Words per Scene", 20, 50, 35)
        dpi = st.select_slider("PDF Quality", options=[72, 150, 300], value=150)
        style = st.selectbox("Choose Comic Art Style", [
            "2D (Flat Art)",
            "Manga Style",
            "Vector Art",
            "Painted / Watercolor Style",
            "3D Rendered (Stylized)",
            "Grayscale / Black & White",
            "Ink & Brush (Traditional Inking)"
        ])

    # Main content
    story = st.text_area("Enter your story:", height=400)

    if st.button("Generate Comic") and story and api_key:
        with st.status("Generating Comic...", expanded=True) as status:
            try:
                # Validate API key
                try:
                    client = init_client(api_key)
                except Exception as e:
                    st.warning("⚠️ Invalid API key. Please check your Gemini API key and try again.")
                    st.stop()

                st.write("1️⃣ Splitting story into scenes...")
                scenes = split_story_into_scenes(story, max_words)

                st.write(f"✂️ Detected {len(scenes)} scenes.")

                st.write("2️⃣ Creating style guide...")
                style_guide = generate_style_guide(client, story, style)

                st.write("3️⃣ Generating panel prompts (parallel)...")
                panel_prompts = generate_panel_prompts_parallel(client, scenes, style_guide, style)

                st.write("4️⃣ Drawing comic panels (parallel)...")
                image_paths = generate_comic_panels_parallel(client, panel_prompts)

                if not image_paths:
                    st.error("Failed to generate any comic panels. Please try again.")
                    st.stop()

                st.write("5️⃣ Compiling PDF...")
                pdf_path = create_comic_pdf(image_paths, dpi)

                if not pdf_path:
                    st.error("Failed to create PDF. Please try again.")
                    st.stop()

                status.update(label="✅ Comic Generation Complete!", state="complete")

                # Display results
                st.success("🎉 Comic generated successfully!")
                cols = st.columns(3)
                for i, img_path in enumerate(image_paths):
                    with cols[i % 3]:
                        st.image(img_path, caption=f"Panel {i+1}")

                with open(pdf_path, "rb") as f:
                    st.download_button(
                        "📥 Download Comic PDF",
                        f,
                        file_name="my_comic.pdf",
                        mime="application/pdf"
                    )

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.stop()

if __name__ == "__main__":
    main()
