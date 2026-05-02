import os
import re
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def ask_gemini(prompt):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )
    return response.text


def clean_output(text):
    text = text.strip()

    remove_phrases = [
        "Certainly!",
        "Here is the final answer:",
        "Here is the revised version:",
        "Final answer:",
        "Final Output:",
        "Conclusion:",
    ]

    for phrase in remove_phrases:
        text = text.replace(phrase, "")

    text = re.sub(r"\s+", " ", text)
    return text.strip()


def generate_content(topic):
    research_prompt = f"""
    Give exactly 5 simple bullet points about: {topic}

    Rules:
    - No introduction
    - No heading
    - No explanation
    - Only 5 bullet points
    """

    research = ask_gemini(research_prompt)

    writing_prompt = f"""
    Convert the following bullet points into ONE clean paragraph:

    {research}

    Rules:
    - No heading
    - No bullet points
    - No numbering
    - No explanation
    - Only one professional paragraph
    """

    paragraph = ask_gemini(writing_prompt)

    review_prompt = f"""
    Clean and improve this paragraph:

    {paragraph}

    Rules:
    - Return only the final paragraph
    - No heading
    - No explanation
    - No extra text
    """

    final_output = ask_gemini(review_prompt)

    return clean_output(final_output)