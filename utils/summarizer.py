from transformers import pipeline

# Load summarizer pipeline (downloads model on first run)
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_report(text):
    # Hugging Face models have a max token limit (~1024 words), so we truncate if needed
    if len(text) > 1000:
        text = text[:1000]

    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']
