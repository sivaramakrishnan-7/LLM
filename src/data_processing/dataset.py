import re 
import os 
import urllib
from torch.utils.data import Dataset, DataLoader
from tqdm import tqdm

if not os.path.exists("../data/the-verdict.txt"):
    url = ("https://raw.githubusercontent.com/rasbt/"
           "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
           "the-verdict.txt")
    file_path = "../data/the-verdict.txt"
    urllib.request.urlretrieve(url,file_path)
    
class LLMDataset(Dataset):
       
       def __init__(self, tokenizer, text, max_length:int, stride:int):
              
             self.tokenizer = tokenizer
             self.token_ids = tokenizer.encode(text)
             self.max_length = max_length
             self.stride = stride
             
                    
       def __len__(self):
              return ((len(self.token_ids) - self.max_length)//self.stride) + 1
        
       
       def __getitem__(self, index):
             input_ids = self.token_ids[index*self.stride: index*self.stride + self.max_length]
             target_ids = self.token_ids[index*self.stride+1:index*self.stride+self.max_length+1]
             if len(target_ids) < self.max_length:
                   target_ids = target_ids + [self.tokenizer.pad_token_id]*(self.max_length - len(target_ids)) 
             return {"input":input_ids,"targets":target_ids}
       
       
                    
                    
                    
             
    
    
    



    
