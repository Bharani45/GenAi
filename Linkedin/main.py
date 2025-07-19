import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post
import json

# Options
length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]
tone_options = ["Professional", "Casual", "Funny"]

image_dict = {
    "Mental Health": "🧠",
    "Productivity": "⏱️",
    "Leadership": "📈",
    "Motivation": "💪",
    "Career": "🎯"
}

# Initialize session state
if 'rating' not in st.session_state:
    st.session_state.rating = 3
if 'post' not in st.session_state:
    st.session_state.post = ""

def main():
    st.set_page_config(page_title="LinkedIn Post Generator", layout="wide")
    st.title("LinkedIn Post Generator ✍️")

    # Layout
    col1, col2, col3, col4 = st.columns(4)
    fs = FewShotPosts()
    tags = fs.get_tags()

    with col1:
        selected_tag = st.selectbox("Topic", options=tags)

    with col2:
        selected_length = st.selectbox("Length", options=length_options)

    with col3:
        selected_language = st.selectbox("Language", options=language_options)

    with col4:
        selected_tone = st.selectbox("Tone", options=tone_options)

    if st.button("Generate"):
        st.session_state.post = generate_post(
            selected_length, selected_language, selected_tag, selected_tone
        )

    # Show result if post exists
    if st.session_state.post:
        st.subheader("Generated Post ✨")
        st.text_area("Preview", value=st.session_state.post, height=200)

        st.markdown(f"**Suggested Emoji/Icon:** {image_dict.get(selected_tag, '💬')}")

        st.download_button("Download Post", st.session_state.post, file_name="linkedin_post.txt")

        st.session_state.rating = st.slider("Rate this post", 1, 5, key="rating_slider")

        if st.button("Submit Feedback"):
            with open("feedback.json", "a", encoding="utf-8") as f:
                json.dump({
                    "post": st.session_state.post,
                    "rating": st.session_state.rating
                }, f)
                f.write("\n")

            st.success("Thanks for your feedback!")

            # Reset session state
            for key in st.session_state.keys():
                del st.session_state[key]

            st.rerun()


if __name__ == "__main__":
    main()
