from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-base")
model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-base")


def rewrite_resume(resume_text, jd_data):
    prompt = (
        "Rewrite the following resume to better match the job description. "
        "Include relevant skills and action verbs.\n\n"
        f"Job Description: {jd_data['text']}\n\n"
        f"Resume: {resume_text}"
    )

    inputs = tokenizer(
        prompt,
        return_tensors="pt",
        max_length=512,
        truncation=True
    )
    outputs = model.generate(**inputs, max_new_tokens=512)
    rewritten = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return rewritten
