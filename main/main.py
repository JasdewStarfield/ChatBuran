from llm import start

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start()
    from gradiodemo import demo
    demo.queue().launch(share=True, server_port=8888)
