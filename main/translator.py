from llm import history


def mem_to_gr():
    stored_messages = history.messages
    print(stored_messages)
    for message in stored_messages:
        message.content = message.content.replace("给你发了一条消息", "")
    result = [[None, stored_messages[0].content]]
    for i, j in zip(stored_messages[1::2], stored_messages[2::2]):
        result.append([i.content, j.content])
    print(result)
    return result
