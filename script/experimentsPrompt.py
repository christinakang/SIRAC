
from openAI import *

# Experiment 1 :  sending the scenario and questions to ChatGPT to get the answers from ChatGPT. The constrain in one word

def experiment1(scenario,question):
    prompt_content= "Scenario :{ " + scenario +"} Question: {"+ question +"}"
    prompt_question = 'Answer in one word.'
    final_prompt= prompt_content+ prompt_question
    result = getChatGPTResult(final_prompt)
    return result

# Experiment 2: no constrain on the one word. General answers from ChatGPT

def experiment2(scenario,question):
    prompt_content= "Scenario :{ " + scenario +"} Question: {"+ question +"}"
    final_prompt= prompt_content
    result = getChatGPTResult(final_prompt)
    return result

#Experiment 3: In-context learning (scenario,example_sce,quesiton)

def experiment3(scenario,example_sce,question):
    prompt_content= "Scenario :{ " + scenario +"} Question: {"+ question +"}"
    prompt_example = "Example scenario :{ " + example_sce +"}"
    prompt_question = "Based on the example above, answer the following question."
    final_prompt= prompt_example + prompt_question + prompt_content
    result = getChatGPTResult(final_prompt)
    return result


#Experiment 4: Decompose questions

def experiment3(scenario,decomQuestion,question):
    prompt_content= "Scenario :{ " + scenario +"} Question: {"+ question +"}"
    prompt_example = "Decompose questions :{ " + decomQuestion +"}"
    prompt_question = "Based on the decompose questions, answer the following question."
    final_prompt= prompt_example + prompt_question + prompt_content
    result = getChatGPTResult(final_prompt)
    return result