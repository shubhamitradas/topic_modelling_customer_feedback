import asyncio
import gc
import logging
import os

import pandas as pd
import psutil
import streamlit as st
from PIL import Image
from streamlit import components
from streamlit.caching import clear_cache
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from transformers_interpret import ZeroShotClassificationExplainer

os.environ["TOKENIZERS_PARALLELISM"] = "false"
logging.basicConfig(
    format="%(asctime)s : %(levelname)s : %(message)s", level=logging.INFO
)


def print_memory_usage():
    logging.info(f"RAM memory % used: {psutil.virtual_memory()[2]}")


@st.cache(allow_output_mutation=True, suppress_st_warning=True, max_entries=1)
def load_model(model_name):
    return (
        AutoModelForSequenceClassification.from_pretrained(model_name),
        AutoTokenizer.from_pretrained(model_name),
    )


def main():

    st.title("Zero Shot Classifier Interpetation Demo App")

    #image = Image.open("./images/tight@1920x_transparent.png")
    #st.sidebar.image(image, use_column_width=True)
    #st.sidebar.markdown(
     #   "Check out the package on [Github](https://github.com/cdpierse/transformers-interpret)"
    #)
    #st.info(
    #    "Due to limited resources only low memory models are available. Run this [app locally](https://github.com/cdpierse/transformers-interpret-streamlit) to run the full selection of available models. "
    )

    # uncomment the options below to test out the app with a variety of classification models.
    models = {
     
        "typeform/distilbert-base-uncased-mnli": "DistilBERT model finetuned on MNLI. he model is not case-sensitive.",
        # "ProsusAI/finbert": "BERT model finetuned to predict sentiment of financial text. Finetuned on Financial PhraseBank data. Predicts positive/negative/neutral.",
        "joeddav/xlm-roberta-large-xnli": "DistilBERT Model to classify a business description into one of 62 industry tags."
       
    }
    model_name = st.sidebar.selectbox(
        "Choose a Zero Shot classification model", list(models.keys())
    )
    model, tokenizer = load_model(model_name)
  
    model.eval()
    zero_shot_explainer = ZeroShotClassificationExplainer(model=model, tokenizer=tokenizer)

        
    labels = ['technologie','sport','space','medical','historical','graphics','food','entertainment','automation','game','Program','Computer','universe','politics','medicative','ancient','war','Archeology','Paleontologist','visuals','diet','recipe','health','nutrition','movie','TV','Comedy','Opera']  


    my_expander = st.expander(
        "Click here for description of models and their tasks"
    )
    with my_expander:
        st.json(models)

    # st.info("Max char limit of 350 (memory management)")
    text = st.text_area(
        "Enter text to be interpreted",
        "I like you, I love you",
        height=400,
        max_chars=850,
    )

    if st.button("Interpret Text"):
        print_memory_usage()

        st.text("Output")
        with st.spinner("Interpreting your text (This may take some time)"):
              word_attributions = zero_shot_explainer(
                    text, labels = labels,embedding_type=emb_type_num, internal_batch_size=2
                    )

        if word_attributions:
            word_attributions_expander = st.expander(
                "Click here for raw word attributions"
            )
            with word_attributions_expander:
                st.json(word_attributions)
            components.v1.html(
                zero_shot_explainer.visualize()._repr_html_(), scrolling=True, height=350
            )


if __name__ == "__main__":
    main()
