import streamlit as st
import pickle
import pandas as pd
from fuzzywuzzy import fuzz

model = pickle.load(
open(
'model.pkl',
'rb'
)
)

st.title(
"Quora Duplicate Question Detector"
)

q1 = st.text_input(
"Question 1"
)

q2 = st.text_input(
"Question 2"
)

if st.button(
"Predict"
):

    q1_len=len(q1)

    q2_len=len(q2)

    q1_words=len(
    q1.split()
    )

    q2_words=len(
    q2.split()
    )

    fuzz_ratio=fuzz.ratio(
    q1,
    q2
    )

    token_sort=fuzz.token_sort_ratio(
    q1,
    q2
    )

    token_set=fuzz.token_set_ratio(
    q1,
    q2
    )

    sample=pd.DataFrame({

    'q1_len':[q1_len],

    'q2_len':[q2_len],

    'q1_words':[q1_words],

    'q2_words':[q2_words],

    'fuzz_ratio':[fuzz_ratio],

    'token_sort':[token_sort],

    'token_set':[token_set]

    })

    prob=model.predict_proba(
    sample
    )

    score=prob[0][1]

    st.write(
    f"Duplicate Probability: {score:.2f}"
    )

    if score>0.4:

        st.success(
        "Duplicate Question"
        )

    else:

        st.error(
        "Not Duplicate"
        )