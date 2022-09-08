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
from ml_backend import ml_backend


os.environ["TOKENIZERS_PARALLELISM"] = "false"
logging.basicConfig(
    format="%(asctime)s : %(levelname)s : %(message)s", level=logging.INFO
)






def print_memory_usage():
    logging.info(f"RAM memory % used: {psutil.virtual_memory()[2]}")


@st.cache(allow_output_mutation=True, suppress_st_warning=True, max_entries=1)


def main():

    st.title("Analysis of Customer feedbacks")

    backend = ml_backend()

    # st.info("Max char limit of 350 (memory management)")
    text = st.text_area(
        "Enter the Customer Feedback",
        "I fell short with time management to complete all units on weekly basis due to holidays and also multiple issues with the courses access to start with and to add one more thing that till now I didn't receive my membership number",
        height=400,
        max_chars=850,
    )

    if st.button("Get Categories of feedback"):
        #print_memory_usage()

        st.text("Output")
        with st.spinner("Analysing the feedback (This may take some time)"):
              output = backend.get_review_category()
        st.markdown("#Topics extracted from the review:")
        st.subheader(output)

if __name__ == "__main__":
    main()
