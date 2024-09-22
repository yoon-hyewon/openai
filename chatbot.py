import openai
import os

# OpenAI API 키 설정
openai.api_key = "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"

# 논문 요약 기능
def summarize_paper(text):
    messages = [
        {"role": "system", "content": "You are a helpful assistant that summarizes papers."},
        {"role": "user", "content": f"Summarize the following paper:\n\n{text}"}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4",  # 또는 gpt-3.5-turbo
        messages=messages,
        max_tokens=200
    )
    return response['choices'][0]['message']['content']


# 한국어-영어 번역 기능
def translate_korean_to_english(text):
    messages = [
        {"role": "system", "content": "You are a helpful assistant that translates Korean to English."},
        {"role": "user", "content": f"Translate the following Korean text to English:\n\n{text}"}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        max_tokens=200
    )
    return response['choices'][0]['message']['content']


# Chain-of-Thought 기능
def chain_of_thought_chatbot(question):
    messages = [
        {"role": "system", "content": "You are an assistant that answers questions with step-by-step reasoning."},
        {"role": "user", "content": question}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        max_tokens=200
    )
    return response['choices'][0]['message']['content']


# 메인 챗봇 함수
def chatbot():
    print("안녕하세요! 이 챗봇은 논문 요약, 번역, 그리고 Chain-of-Thought를 지원합니다.")
    while True:
        user_input = input("\n명령어를 입력하세요 (요약, 번역, 생각의흐름, 종료): ").strip().lower()

        if user_input == "종료":
            print("챗봇을 종료합니다.")
            break
        elif user_input == "요약":
            text = input("요약할 논문 텍스트를 입력하세요: ")
            summary = summarize_paper(text)
            print("\n요약 결과:\n", summary)
        elif user_input == "번역":
            text = input("번역할 한국어 텍스트를 입력하세요: ")
            translation = translate_korean_to_english(text)
            print("\n번역 결과:\n", translation)
        elif user_input == "생각의흐름":
            question = input("질문을 입력하세요: ")
            response = chain_of_thought_chatbot(question)
            print("\n답변:\n", response)
        else:
            print("유효한 명령어가 아닙니다. '요약', '번역', '생각의흐름' 중 하나를 선택해 주세요.")


# 챗봇 실행
if __name__ == "__main__":
    chatbot()
