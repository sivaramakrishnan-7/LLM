from byo_llm.src.data_processing.dataset import LLMDataset
import tiktoken 
tokenizer =  tiktoken.get_encoding('gpt2')
text = "Hello, World"
data = LLMDataset(tokenizer,text,max_length=5,stride=2)

print(data[0])