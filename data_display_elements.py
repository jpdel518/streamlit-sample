import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})
# highlight_maxは最大値をハイライトする
# axis=0は列方向に最大値を探す, axis=1は行方向に最大値を探す
st.dataframe(df.style.highlight_max(axis=0))

st.json({
    'name': 'abc',
    'age': 123,
    'stuff': [
        'stuff 1',
        'stuff 2',
        'stuff 3',
        'stuff 5',
    ],
})
