import datetime
import streamlit as st

# ボタン
if st.button('Hit me'):
    st.write('Nice!!')

# チェックボックス
if st.checkbox('check me out'):
    st.write('checked!!')

# ラジオボタン
radio = st.radio('choose one', ['A', 'B', 'C'])
if radio == 'A':
    st.write('A is selected')
elif radio == 'B':
    st.write('B is selected')
else:
    st.write('C is selected')

# セレクトボックス
option = st.selectbox('choose one', ['A', 'B', 'C'])
if option == 'A':
    st.write('A is selected')
elif option == 'B':
    st.write('B is selected')
else:
    st.write('C is selected')

# マルチセレクトボックス
options = st.multiselect('What are your favorite colors', ['Green', 'Yellow', 'Red', 'Blue'], ['Yellow', 'Red'])
if len(options) == 0:
    st.write('You didn\'t select anything.')
else:
    st.write(f'You selected:, {options}')

# スライダー
age = st.slider('How old are you?', 0, 130, 25)
st.write(f'I\'m {age} years old.')

# 期間スライダー
values = st.slider('Select a range of values', 0.0, 100.0, (25.0, 75.0))
st.write(f'Values: {values}')

# セレクトスライダー
color = st.select_slider('Select a color of the rainbow', options=['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet'])
st.write(f'My favorite color is {color}.')

# タイムインプット
st.time_input('Set an alarm for', datetime.time(8, 45))

# DatePicker
d = st.date_input(
    "When's your birthday",
    datetime.date(2019, 7, 6)
)
st.write('Your birthday is:', d)

# 画像表示
st.image('https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png', width=200)

# 動画表示
st.video('https://www.youtube.com/watch?v=9Q6sLbz37gk')

# ファイルアップローダー
uploaded = st.file_uploader('File uploader')

# カメラ
image = st.camera_input('Camera input')
if image is not None:
    st.image(image, caption='Camera input', use_column_width=True)
