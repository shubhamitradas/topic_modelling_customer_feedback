import openai
import streamlit as st


    
class ml_backend:
        
    openai.api_key = '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' #st.secrets["key"]
    

    def get_review_category(self,review):
        """Returns the key topics in the input text"""
  
        prompt_text= "Feedback: More lesson and interacting with the class.  As this is the first module and everyone has come into being extremely nervous the amount of support provided has been limited. The first lesson was spent with 140 people waiting for the tutor to talk 1 person through tech issues! She then ran through the assignment in less the ten mins. I assumed from speaking with the sales rep we would have done a bit of learning rather then all by ourselves. Being in a whatsapp group with 100 other students everyone is feeling the same and disappointed. I would highly recommend watching the online lesson back.\n\nKey topics:\n1. Limited support provided \n2. Too few opportunities to learn from the class; \n3. Feeling overwhelmed and frustrated with the class; \n4. Limited opportunity to ask questions or get help from the tutor; \n5. Disappointed with the amount of learning available in the class;  \n\nFeedback: "       
        response = openai.Completion.create(
        model="text-davinci-002",
        prompt= prompt_text + review + "\n",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0 
       )
        return response.choices[0].text
    
    
    
    def get_improvement_steps(self,review):
        """Returns some potential improvement steps"""
  
        prompt_text= "\n\n This is a negative review of a customer.\nLet's think step by step to improve this.\n "
        response = openai.Completion.create(
        model="text-davinci-002",
        prompt= review + prompt_text,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0 
       )
        return response.choices[0].text
    
    def get_review_mood(self,review):
        """Returns sentiment analysis of the review"""
  
        prompt_text= "Customer Feedback: "
        question = "\nWhat is the mood of the review?\n"
        response = openai.Completion.create(
        model="text-davinci-002",
        prompt= prompt_text + review + question,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0 
       )
        return response.choices[0].text
    