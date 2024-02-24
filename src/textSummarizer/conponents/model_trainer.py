from transformers import TrainingArguments, Trainer
from transformers import DataCollatorForSeq2Seq
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import load_dataset, load_from_disk
import torch
import os  # Module for interacting with the operating system
from src.textSummarizer.entity import ModelTrainerConfig  # Importing ModelTrainerConfig class


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config


    
    def train(self):
        
        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)
        
        #loading data 
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        


        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir,
            num_train_epochs=1,
            warmup_steps=500,
            per_device_train_batch_size=1,  # Reduced batch size to mitigate out-of-memory error
            per_device_eval_batch_size=1,   # Reduced batch size to mitigate out-of-memory error
            weight_decay=0.01,
            logging_steps=10,
            evaluation_strategy='steps',
            eval_steps=500,
            save_steps=1e6,
            gradient_accumulation_steps=16
        ) 
        # Assuming you have a tokenized dataset named tokenized_dataset

        # Select only the first 100 samples from the tokenized dataset
        tokenized_subset_test = dataset_samsum_pt["test"].select(range(100))
        tokenized_subset_val = dataset_samsum_pt["validation"].select(range(100))


        


        trainer = Trainer(model=model_pegasus, args=trainer_args,
                  tokenizer=tokenizer, data_collator=seq2seq_data_collator,
                  train_dataset=tokenized_subset_test, 
                  eval_dataset=tokenized_subset_val)
        
        trainer.train()

        ## Save model
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir,"pegasus-samsum-model"))
        ## Save tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.root_dir,"tokenizer"))
