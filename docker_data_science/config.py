import transformers

"""
DEVICE = "cuda"
MAX_LEN = 64
TRAIN_BATCH_SIZE = 8
VALID_BATCH_SIZE = 4
EPOCHS = 10
BERT_PATH = "bert-base-uncased"
MODEL_PATH = "/root/docker_data/model.bin"
TRAINING_FILE = "/root/docker_data/train.csv"
TOKENIZER = transformers.BertTokenizer.from_pretrained(BERT_PATH, do_lower_case=True)
"""

DEVICE = "cpu"
MAX_LEN = 64
TRAIN_BATCH_SIZE = 8
VALID_BATCH_SIZE = 4
EPOCHS = 10
BERT_PATH = "bert-base-uncased"  # download in docker container
MODEL_PATH = "/root/docker_data/model.bin"  # docker 컨테이너 어디에 모델을 저장할건지
TRAINING_FILE = "/root/docker_data/train.csv"
TOKENIZER = transformers.BertTokenizer.from_pretrained(BERT_PATH, do_lower_case=True)
