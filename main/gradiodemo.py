import gradio as gr
from llm import get, start_message
from translator import mem_to_gr


async def prompt(history, name):
    print(history[-1][0])
    inp = history[-1][0].replace(name + "：", "")
    history[-1][1] = "暴风雪思考中……"
    yield history
    final_prompt = name + "给你发了一条消息：" + inp
    result = get(final_prompt)
    history[-1][1] = ""
    async for i in result:
        history[-1][1] = i
        yield history


def user(user_message, name):
    return "", mem_to_gr() + [[name + "：" + user_message, None]]


with gr.Blocks() as demo:
    gr.Markdown("""
    # Chat With Buran!\n
    \n
    暴风雪是一个仿生人，曾经是苏联建造的航天飞机“暴风雪号”，现在是一个12岁的小女孩的样子。\n
    来和暴风雪聊天吧！（按回车键发送消息）\n
    """)

    username = gr.Textbox("茉露", label="用户名")
    chatbot = gr.Chatbot(label="暴风雪", value=[], show_copy_button=True,
                         avatar_images=(None, "main/Buran.png"), bubble_full_width=False)
    message = gr.Textbox(placeholder="要和暴风雪说什么呢？", label="将要发送的消息")

    with gr.Row():
        clear = gr.ClearButton([message], value="清除输入")
        refresh = gr.Button(value="刷新消息")

    message.submit(user, [message, username], [message, chatbot], queue=False).then(prompt, [chatbot, username],
                                                                                    [chatbot])
    refresh.click(mem_to_gr, None, chatbot, queue=False)
