from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

class OpusEnFrServices():
    @staticmethod
    def translate(english_text: str) -> str:
        tokenizer = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-fr")
        model = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-fr")

        inputs = tokenizer.encode(english_text, return_tensors="pt", truncation=True)

        outputs = model.generate(inputs, max_length=200, num_beams=4, early_stopping=True)

        translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

        return translated_text
