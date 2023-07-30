import streamlit as st

# サイドバー
st.sidebar.title('Streamlit 入門')
number = st.sidebar.slider('数値入力', 0, 100, 50)
st.sidebar.write(f'あなたの好きな数字を教えてください: {number}')

# 指定した数字分だけカラムを作成
left_col, right_col = st.columns(2)

left_col.subheader('ここは左カラムです')
right_col.subheader('ここは右カラムです')
if left_col.button('右カラムに文字を表示'):
    right_col.write('左カラムからボタンが押されました')

# コンテナ
c = left_col.container()
c.write('ここはコンテナです')

#
expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

# 空のコンテナを作成。後から中身を書き換えることができる
e = st.empty()
e.text('空っぽのコンテナ')
