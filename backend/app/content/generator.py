from app.services.llm_service import generate_document_content

def generate_text_from_prompt(prompt: str, max_output_tokens: int = 1024) -> str:
    return generate_document_content(prompt, max_output_tokens=max_output_tokens)
