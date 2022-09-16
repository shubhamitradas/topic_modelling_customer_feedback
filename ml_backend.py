import openai
import streamlit as st


    
class ml_backend:
        
    openai.api_key = "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" #st.secrets["key"]
    

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
    
    def get_positve_negative_aspects(self,review):
        """Returns postive and negative aspects from the review."""
  
        #prompt_text= "Extract positive and negative aspects from the text :\n "
        prompt_text = "Feedback: This new edition of the course has been very much a disappointment for me. The one I started in December 2020 was much more straightforward.  The contents are not complete and all this interactivity just makes the theory like a game.   The platform is confusing, things are not in the right place and it seems that information shared about where to look re the assessment results.   Each time I finish a topic, I need to come back to the dashboard to be able to continue another thing/ consult another topic.  The shared PowerPoint do not point well what is required in the assessments criteria.  I am very disappointed.\n\npositive: \n-December 2020 course was much more straightforward.\n\nnegative: \n-The contents are not complete \n-Too much interactivity just makes the theory like a game.\n-The platform is confusing, \n-Too many back-and-forth operations between course and dashboard.\n-Assessment criteria in the PowerPoint are not clear. \n\nFeedback: The Tutor support sessions frequency should be increased and the span of control for a tutor should not be more than 50-70 students.\n\npositive:\n-\nnegative:\n-Frequency of tutor support sessions is lesser.\n-Span of control for a tutor is too high.\n\nFeedback: "
        response = openai.Completion.create(
        model="text-davinci-002",
        prompt=  prompt_text + review,
        temperature=0.35,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0 
       )
        return response.choices[0].text
    
    
    def is_customer_polite(self,review):
        """Returns a text which shows if the customer is polite or not."""
  
        prompt_text= "Is the customer polite in the following customer feedback? :\n "
        response = openai.Completion.create(
        model="text-davinci-002",
        prompt=  prompt_text + review,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0 
       )
        return response.choices[0].text
    
    def compose_response(self,review):
        """Returns a response text for the feedback.."""
  
        prompt_text= "Write a polite response for the following customer feedback.\n "
        response = openai.Completion.create(
        model="text-davinci-002",
        prompt=  prompt_text + review,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0 
       )
        return response.choices[0].text
    
    def auto_tag(self,review):
        """Returns a response text for the feedback.."""
  
        prompt_text= "Feedback:This new edition of the course has been very much a disappointment for me. The one I started in December 2020 was much more straightforward.  The contents are not complete and all this interactivity just makes the theory like a game.   The platform is confusing, things are not in the right place and it seems that information shared about where to look re the assessment results.   Each time I finish a topic, I need to come back to the dashboard to be able to continue another thing/ consult another topic.  The shared PowerPoint do not point well what is required in the assessments criteria.  I am very disappointed.\n\nTags:\n-Course\n-Platform\n-Shared PowerPoint\n-Assessment criteria.\n\nFeedback: "
        response = openai.Completion.create(
        model="text-davinci-002",
        prompt=  prompt_text + review,
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
        question = "What is the mood of the review?\n"
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
    