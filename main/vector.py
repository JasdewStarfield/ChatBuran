import numpy as np
from langchain.vectorstores import Chroma

from langchain_community.embeddings import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='main/models/text2vec/text2vec-base-chinese')


if __name__ == '__main__':
    sentence1 = "我喜欢小狗。"
    sentence2 = "我喜欢小动物。"
    sentence3 = "我今天心情很差。"

    embedding1 = embedding.embed_query(sentence1)
    embedding2 = embedding.embed_query(sentence2)
    embedding3 = embedding.embed_query(sentence3)

    print(np.dot(embedding1, embedding2))
    print(np.dot(embedding1, embedding3))
    print(np.dot(embedding2, embedding3))
    print(embedding1)
