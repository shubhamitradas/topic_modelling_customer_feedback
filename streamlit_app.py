import streamlit as st
from streamlit import components
from streamlit.caching import clear_cache
from ml_backend import ml_backend




#@st.cache(allow_output_mutation=True, suppress_st_warning=True, max_entries=1)


def main():

    st.title("Analysis of Customer feedbacks")

    backend = ml_backend()

    # st.info("Max char limit of 350 (memory management)")
    text = st.text_area(
        "Customer feedback",
        height=300,
        max_chars=950,
    )
    
    option = st.selectbox(
     'What do you want to know?',
     ('Options',
      'Get me the Key topics.', 
      'Mood of the review.',
      'Get the postive and negative aspects.',
      'Is the customer polite?',
      'Write a response for this review.',
      'Potential steps to improve user experience.'))

    if option == "Get me the Key topics.":
        #print_memory_usage()

        with st.spinner("Analysing the text (This may take some time)"):
            output = backend.get_review_category(text)  
        
        themes = output.split("Key topics:")  
        print(themes)
        items = themes[1]
        values = items.split(";")
        for item_values in values:
           st.write(item_values)
           
    elif option == "Potential steps to improve user experience.":
        #print_memory_usage()

        with st.spinner("Analysing the text (This may take some time)"):
            output = backend.get_improvement_steps(text)  
        st.write(output)  
        
    elif option == "Mood of the review.":
        #print_memory_usage()

        with st.spinner("Analysing the text (This may take some time)"):
            output = backend.get_review_mood(text)  
        st.write(output)  
        
    elif option == "Is the customer polite?":
        #print_memory_usage()

        with st.spinner("Analysing the text (This may take some time)"):
            output = backend.is_customer_polite(text)  
        st.write(output)   
        
    elif option == "Write a response for this review.":
        #print_memory_usage()

        with st.spinner("Analysing the text (This may take some time)"):
            output = backend.compose_response(text)  
        st.write(output)      
        
    elif option == "Get the postive and negative aspects.":
        #print_memory_usage()

        with st.spinner("Analysing the text (This may take some time)"):
            output = backend.get_positve_negative_aspects(text)  
        st.write(output)               
 
       

if __name__ == "__main__":
    main()
