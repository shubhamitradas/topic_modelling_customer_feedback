import openai


    
class ml_backend:
        
    openai.api_key = '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'

    def get_review_category(self,review):
        """Returns a generated an email using GPT3 with a certain prompt and starting sentence"""
    
        response = openai.Completion.create(
        model="text-davinci-002",
        prompt="Can you find out the top 5 category of complaints from the following customer feedback?\n" + review + "\n",
        temperature=0.6,
        max_tokens=543,
        top_p=0.58,
        best_of=4,
        frequency_penalty=0.38,
        presence_penalty=0.33
       )
        return response.get("choices")