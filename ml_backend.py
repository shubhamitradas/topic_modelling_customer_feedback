import openai

    
class ml_backend:
        
    openai.api_key = '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'

    def get_review_category(self, userPrompt ="Write me a professionally sounding email", start="Dear"):
        """Returns a generated an email using GPT3 with a certain prompt and starting sentence"""
    
        response = openai.Completion.create(
        model="text-davinci-002",
        prompt="The below paragraph is a customer feedback on a e-learning course..\nGive the key complaints in bullets.\n\"\nMore lesson and interacting with the class.  As this is the first module and everyone has come into being extremely nervous the amount of support provided has been limited. The first lesson was spent with 140 people waiting for the tutor to talk 1 person through tech issues! She then ran through the assignment in less the ten mins. I assumed from speaking with the sales rep we would have done a bit of learning rather then all by ourselves. Being in a whatsapp group with 100 other students everyone is feeling the same and disappointed. I would highly recommend watching the online lesson back.\"\n",
        temperature=0.6,
        max_tokens=543,
        top_p=0.58,
        best_of=4,
        frequency_penalty=0.38,
        presence_penalty=0.33
       )
        return response.get("choices")