from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

from utils.lazylogger import logger
from utils.mlloader import ModelLoader

tokenizer, model = ModelLoader("facebook/m2m100_418M","models", M2M100Tokenizer, M2M100ForConditionalGeneration).retrieve()

def translator(*, text: str, src_lang: str="da", target_lang: str="en") -> str:
    tokenizer.src_lang = src_lang
    encoded_hi = tokenizer(text, return_tensors="pt")
    generated_tokens = model.generate(**encoded_hi, forced_bos_token_id=tokenizer.get_lang_id(target_lang))
    return tokenizer.batch_decode(generated_tokens, skip_special_tokens=True).pop()



if __name__ == '__main__':  
    
    text = "Janteloven er en række love der bygger på ideen om, at alle er lige i det danske samfund, og at man derfor ikke skal tro at man er bedre end andre mennesker"
    print(f"Original: {text}")
    translated_text = translator(text=text, src_lang="da", target_lang="en")
    print(f"Translated: {translated_text}")