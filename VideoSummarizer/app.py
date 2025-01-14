import streamlit as st
from phi.model.google import Gemini
from phi.agent import Agent
from phi.tools.duckduckgo import DuckDuckGo
from google.generativeai import upload_file, get_file
import google.generativeai as genai
import time
from pathlib import Path
import tempfile
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)
else:
    st.error("Please set your GOOGLE_API_KEY in the .env file")
    st.stop()

# Page configuration
st.set_page_config(
    page_icon="",
    page_title="Multimodal AI Agent",
    layout="wide"
)

st.title("Phidata Video AI Summarizer Agent")
st.header("Powered by Gemini 2.0 Flash Exp")

@st.cache_resource
def initialize_agent():
    return Agent(
        name="Video AI Summarizer",
        model=Gemini(id="gemini-2.0-flash-exp"),
        tools=[DuckDuckGo()],
        markdown=True
    )

multimodal_agent = initialize_agent()

video_file = st.file_uploader(
    "Upload a video file",
    type=["mp4", 'mov', 'avi'],
    help="Upload a video for AI Analysis"
)

if video_file:
    # Create a temporary file and save the uploaded video
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video:
        temp_video.write(video_file.read())
        video_path = temp_video.name

    # Display the video
    st.video(video_path, format="video/mp4", start_time=0)

    user_query = st.text_area(
        "What insights are you seeking from the video?",
        placeholder="Ask anything about the video content. The AI agent will analyze and gather the information",
        help="Please provide specific questions or insights you want from the video."
    )

    if st.button("Analyze Video", key='analyze_video_button'):
        if not user_query:
            st.warning("Please enter a question or insights to analyze the video.")
        else:
            try:
                with st.spinner("Processing Video and gathering insights... "):
                    # Upload the temporary file instead of the UploadedFile object
                    processed_video = upload_file(video_path)
                    
                    # Wait for processing to complete
                    while processed_video.state.name == "PROCESSING":
                        time.sleep(1)
                        processed_video = get_file(processed_video.name)

                    analysis_prompt = f"""
                    Analyze the uploaded video for content and context.
                    Respond to the following query using video insights and supplementary web research:
                    {user_query}
                    Provide a detailed, user-friendly, and actionable response.
                    """

                    response = multimodal_agent.run(analysis_prompt, videos=[processed_video])
                
                    st.subheader("Analysis Result")
                    st.markdown(response.content)

            except Exception as error:
                st.error(f"An error occurred during analysis: {str(error)}")
            finally:
                # Clean up the temporary file
                try:
                    Path(video_path).unlink()
                except Exception as e:
                    st.warning(f"Could not delete temporary file: {str(e)}")
else:
    st.info("Upload a video to begin")