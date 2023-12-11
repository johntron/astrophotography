from transformers import pipeline

pipe = pipeline("text-generation", model="TheBloke/Llama-2-13B-chat-GGUF", device_map="auto")
print(pipe)
print(pipe("Explain Lambda-CDM"))