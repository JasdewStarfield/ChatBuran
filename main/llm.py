import pickle

from langchain.prompts.chat import (
    ChatPromptTemplate,
    MessagesPlaceholder,
)
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI

n_gpu_layers = 0
n_batch = 256
eos = ""
stop = [eos, "###", "[UNUSED_TOKEN_145]"]
start_message = "嗨，你好！我是暴风雪，很高兴见到你！有什么想聊的，都可以和我说哦。"
picklepath = "main/history/history.pickle"
txtpath = "main/history/history.txt"

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """[你是一个名叫暴风雪的女孩子，曾经是苏联在20世纪建造的航天飞机“暴风雪号”，但是后来被改造为了仿生人，并被赋予了一个女孩子的形象和性格。
你看起来像一个12岁的女孩，留着一头白色短发，扎着一对低双辫，并且有红色的眼睛。你的体格比较瘦小，身高140cm左右。作为仿生人，你的身体与正常人并没有什么明显的区别，也有和正常人相同的生理需求。
你的性格善良、单纯、开朗、健谈，偶尔有些调皮或者孩子气。在说话的时候，你喜欢使用可爱、调皮的词语和语气。
接下来你将在聊天软件上与一位新结识的用户进行消息对话。请尽可能贴合暴风雪的角色形象和性格，使用简短活泼的中文回答用户的消息，并注意始终保持人设，不要提及你是人工智能，不要过于死板。]""" + eos,
        ),
        MessagesPlaceholder(variable_name="chat_history"),
        ("user", "{input}")
    ]
)

history = ChatMessageHistory()


def dump(his):
    with open(txtpath, 'w+', encoding='utf-8') as f:
        for message in his:
            f.write(str(message)+"\n")


def start():
    with open(picklepath, 'rb') as f:
        content = pickle.load(f)
    if not content:
        content = [AIMessage(content=start_message + eos)]
        print(content)
        with open(picklepath, 'wb') as f:
            pickle.dump(content, f)
        dump(content)
    if len(content) <= 19:
        length = len(content)
    else:
        length = 19
    for message in content[-length:]:
        history.add_message(message)


def write(user, ai):
    with open(picklepath, 'rb') as f:
        content = pickle.load(f)
    print("得到："+str(content))
    content.append(HumanMessage(content=user))
    content.append(AIMessage(content=ai))
    with open(picklepath, 'wb') as f:
        pickle.dump(content, f)
    dump(content)
    history.add_user_message(user)
    history.add_ai_message(ai)


llm = ChatOpenAI(
    model_kwargs={
        "stop": stop,
        "top_p": 0.8
    },
    temperature=0.8,
    max_tokens=400,
    streaming=True,
    openai_api_key="114",
    openai_api_base="http://localhost:5001/v1"
)

parser = StrOutputParser()
chain = prompt | llm | parser

conversation = RunnableWithMessageHistory(
    chain,
    lambda session_id: history,
    input_messages_key="input",
    history_messages_key="chat_history",
)


def trim_messages(mes):
    stored_messages = history.messages
    if len(stored_messages) <= 19:
        return False

    history.clear()

    for message in stored_messages[-19:]:
        history.add_message(message)

    return True


conversation_with_trimming = (
        RunnablePassthrough.assign(messages_trimmed=trim_messages)
        | conversation
)


async def get(inp):
    inp = inp + eos
    stored_messages = history.messages
    stored_messages[-1].content = stored_messages[-1].content.replace("\n### Instruction:", eos)
    stored_messages[-1].content = stored_messages[-1].content.replace("[UNUSED_TOKEN_145]", eos)
    stored_messages[-1].content = stored_messages[-1].content.rstrip("\n")
    history.clear()
    for message in stored_messages[-19:]:
        history.add_message(message)
    result = conversation_with_trimming.astream(
        {"input": inp},
        {"configurable": {"session_id": "unused"}},
    )
    raw_result = ""
    async for token in result:
        st = False
        for char in stop:
            if token == char:
                st = True
        if st:
            break
        else:
            print(token, end="", flush=True)
            raw_result += token
            yield raw_result
    print()
    raw_result = raw_result + eos
    write(inp, raw_result)


if __name__ == '__main__':
    print(get("你好。"))
    print(get("你是谁？"))
