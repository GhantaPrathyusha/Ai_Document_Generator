from app.config import settings

import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=settings.GOOGLE_API_KEY)

def generate_document_content(prompt: str) -> str:
    """
    Proper Gemini call — ALWAYS returns real text.
    """
    try:
        model = genai.GenerativeModel(settings.GEMINI_MODEL)

        response = model.generate_content(prompt)

        # Correct way to extract text
        if hasattr(response, "text") and response.text:
            return response.text

        # Some SDK versions return candidates
        if hasattr(response, "candidates") and response.candidates:
            part = response.candidates[0].content.parts[0]
            return part.text

        return "⚠️ Gemini returned an empty response."

    except Exception as e:
        raise RuntimeError(f"Gemini generation failed: {str(e)}")
