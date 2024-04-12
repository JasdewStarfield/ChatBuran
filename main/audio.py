import requests
import pyaudio
from cut_text import cut

def_character = 'Buran3'
#def_text = '这是一段测试文本，旨在通过多种语言风格和复杂性的内容来全面检验文本到语音系统的性能。接下来，我们会探索各种主题和语言结构，包括文学引用、技术性描述、日常会话以及诗歌等。首先，让我们从一段简单的描述性文本开始：“在一个阳光明媚的下午，一位年轻的旅者站在山顶上，眺望着下方那宽广而繁忙的城市。他的心中充满了对未来的憧憬和对旅途的期待。”这段文本测试了系统对自然景观描写的处理能力和情感表达的细腻程度。'
#def_text = '嗨，茉露！我呀，想和你聊聊我们的星球，你知道的，我来自一个叫“暴风雪号”的航天飞机。那里有许多有趣的故事呢。'
#def_text = '你的肛门比较松弛，但是呢你的痔疮呢又弥补了这一部分。如果做痔疮手术把痔疮切除的话，可能会显得你的肛门就比较大，可能会有一些漏液漏气的情况。现在最好的办法就是，在做痔疮手术的同时，给你做一个肛门紧缩术。'
def_text = '你的升力系数比较松弛，但是呢你的推重比又弥补了这一点。如果降低推力的话，可能就会显得你的重量比较大，可能会有一些失控失速的情况。现在最好的办法就是，在降低推力的同时，给你改装一个升力体布局。'
def_emo = 'default'
def_max_length = 30


def gen_audio(character, text, emo, max_length):
    spliced_text = cut(text, max_length)

    # 初始化pyaudio
    p = pyaudio.PyAudio()

    # 打开音频流
    stream = p.open(format=p.get_format_from_width(2),
                    channels=1,
                    rate=32000,
                    output_device_index=6,
                    output=True)
    stream2 = p.open(format=p.get_format_from_width(2),
                     channels=1,
                     rate=32000,
                     output_device_index=5,
                     output=True)

    stream_url = (f'http://127.0.0.1:5000/tts?character={character}&text={spliced_text}'
                  f'&emotion={emo}&cut_method=cut0&stream=true')
    response = requests.get(stream_url, stream=True)

    # 读取数据块并播放
    for data in response.iter_content(chunk_size=1024):
        stream.write(data)
        stream2.write(data)

    # 停止和关闭流
    stream.stop_stream()
    stream.close()
    stream2.stop_stream()
    stream2.close()

    # 终止pyaudio
    p.terminate()


if __name__ == '__main__':
    gen_audio(def_character, def_text, def_emo, def_max_length)
