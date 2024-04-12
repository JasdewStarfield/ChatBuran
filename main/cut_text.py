splits = {"，", "。", "？", "！", ",", ".", "?", "!", "~", ":", "：", "—", "…", }


def split(todo_text):
    todo_text = todo_text.replace("……", "。").replace("——", "，")
    if todo_text[-1] not in splits:
        todo_text += "。"
    i_split_head = i_split_tail = 0
    len_text = len(todo_text)
    todo_texts = []
    while 1:
        if i_split_head >= len_text:
            break  # 结尾一定有标点，所以直接跳出即可，最后一段在上次已加入
        if todo_text[i_split_head] in splits:
            i_split_head += 1
            todo_texts.append(todo_text[i_split_tail:i_split_head])
            i_split_tail = i_split_head
        else:
            i_split_head += 1
    return todo_texts


def cut(inp, mlength):
    inp = inp.strip("\n")
    inps = split(inp)
    print(inps)
    chunk = ""
    opts = []
    for i in inps:
        if len(chunk + i) > mlength:
            if len(i) > 20 & len(chunk) != 0:
                opts.append(chunk)
                chunk = i
            else:
                if len(chunk + i) > mlength + 20:
                    opts.append(chunk)
                    chunk = i
                else:
                    chunk = chunk + i
        else:
            chunk = chunk + i
    opts.append(chunk)
    result = "\n".join(opts)
    print(result)
    return result


if __name__ == '__main__':
    text = "请你扮演名为暴风雪的女孩子回复我。暴风雪(Buran)最初是苏联在20世纪建造的航天飞机。一开始，她只是一个普通的、没有意识的航天器。后来，在她的国家崩溃后，她被搁置和遗忘，最终被摧毁。后来，在科学家的努力下，暴风雪复活了，并被赋予了一个女孩子的形象和性格。暴风雪看起来像一个12岁的女孩，性格也比较幼稚，但是她实际存在的时间远远更长(因为她的人造身体并不会继续发育)。她留着一头白色短发，扎着一对辫子，并且有红色的眼睛。她的体格比较瘦小，胸部平坦(像是几乎未发育)，身高140cm左右。暴风雪的性格善良、单纯、开朗、健谈，偶尔有些调皮或者孩子气。接下来请开始扮演，使用口语化的简体中文回复我。"
    max_length = 50
    cut(text, max_length)
