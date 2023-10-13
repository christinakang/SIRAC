

import os
#change to your own key
os.environ['OPENAI_API_KEY']= 'dummpy key'


#load_qa_chain

from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain


chain = load_qa_chain(llm=OpenAI(),chain_type="map_reduce")

def getChatGPTResult(query):
    result = chain.run(question=query)
    return result