# 1. 라이브러리 임포트
import streamlit as st
import openai
# 2. 기능 구현 함수
def askGPT(prompt):
    message_prompt = [{"role": "user", "content":prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message_prompt)
    gptResponse = response["choices"][0]["message"]["content"]
    return gptResponse

# 3. 메인 함수
def main():
    st.set_page_config(page_title='요약 프로그램',
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
    # 사이드바
    with st.sidebar:
        open_apikey = st.text_input(label='🔑OPENAI API 키☑️',
            placeholder='input OpenAI API Key',
            value='', type='password')
        if open_apikey:
            openai.api_key = open_apikey
        st.markdown('---')
    # 메인공간
    st.header("📝 요약 프로그램")
    st.markdown('---')
    
    text = st.text_area('글을 요약합니다')
    if st.button('요약'):
        prompt = f'''
        **Instructions** :
    - You are an expert assistant that summarizes text into **Korean language**.
    - Your task is to summarize the **text** sentences in **Korean language**.
    - Your summaries should include the following :
        - Omit duplicate content, but increase the summary weight of duplicate content.
        - Summarize by emphasizing concepts and arguments rather than case evidence.
        - Summarize in 3 lines.
        - Use the format of a bullet point.
    -text : {text}
    '''
        st.info(askGPT(prompt))

if __name__=='__main__':
    main()