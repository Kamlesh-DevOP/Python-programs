import openai
import gradio
import webbrowser

openai.api_key = "" #get a working openai key to check working


messages = [{"role": "system", "content": "You are a dietitian who gives the perfect diet as per user's requirements and previous medical history in bullet points"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "DietAI")

demo.launch()