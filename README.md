

# Chat Buran

基于LangChain的纯本地AI聊天Agent类项目

练手作

<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<br />

<p align="center">
  <a href="https://github.com/JasdewStarfield/ChatBuran/tree/master/main/Buran.png">
    <img src="main/Buran.png" alt="Logo" width="160" height="160">
  </a>

  <h3 align="center">Chat Buran</h3>
  <p align="center">
    基于LangChain的纯本地AI聊天Agent类项目！
    <br />
    <a href="https://github.com/JasdewStarfield/ChatBuran"><strong>探索本项目的文档（还没写） »</strong></a>
    <br />
    <br />
    <a href="https://github.com/JasdewStarfield/ChatBuran">查看Demo（还没部署）</a>
    ·
    <a href="https://github.com/JasdewStarfield/ChatBuran/issues">报告Bug</a>
    ·
    <a href="https://github.com/JasdewStarfield/ChatBuran/issues">提出新特性</a>
  </p>

</p>


 
## 目录

- [上手指南](#上手指南)
  - [开发前的配置要求](#开发前的配置要求)
  - [安装步骤](#安装步骤)
- [文件目录说明](#文件目录说明)
- [开发的架构](#开发的架构)
- [部署](#部署)
- [使用到的框架](#使用到的框架)
- [贡献者](#贡献者)
  - [如何参与开源项目](#如何参与开源项目)
- [版本控制](#版本控制)
- [作者](#作者)
- [鸣谢](#鸣谢)

### 上手指南

没写



###### 开发前的配置要求

本项目自身并不需要很高级的配置，但是如果需要在本地运行LLM模型的话，则需要一定的CPU/GPU配置。本地模型可以用任何支持OpenAI的api的模型（本人使用的是KoboldCpp加载InternLM2的gguf量化模型）。

如果配置不足（而且有经费），可以使用OpenAI的api。本项目对接模型的接口和OpenAI是完全兼容的，只需要修改llm.py中的openai_api_base为官方源即可。

###### **安装步骤**

1. 克隆仓库
2. （可选）创建虚拟环境
3. pip install -r requirements.txt
4. 启动launch.bat，同时保证本地模型的api运行在[http://localhost:5001/v1](http://localhost:5001/v1)上
5. 打开生成的gradio链接

### 文件目录说明

```
filetree 
├── LICENSE.txt
├── README.md
├── launch.bat
├── （慎点）清理历史记录（重启有效）.bat
├── main
│  ├── history
│  ├── clear_history.py
│  ├── gradiodemo.py
│  ├── llm.py
│  ├── main.py
│  └── translator.py
└── （待补充）

```





### 开发的架构 

占位符.jpg

### 部署

暂无

### 使用到的框架

等我有时间写

### 贡献者

请阅读**CONTRIBUTING.md** 查阅为该项目做出贡献的开发者。（还没写，反正目前就我一个人）

#### 如何参与开源项目

贡献使开源社区成为一个学习、激励和创造的绝佳场所。你所作的任何贡献都是**非常感谢**的。


1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



### 版本控制

该项目使用Git进行版本管理。您可以在repository参看当前可用版本。

### 作者

茉露星圃 | Jasdew Starfield

qq:952988294    

 *您也可以在贡献者名单中参看所有参与该项目的开发者。*

### 版权说明

该项目签署了MIT 授权许可，详情请参阅 [LICENSE.txt](https://github.com/JasdewStarfield/ChatBuran/blob/master/LICENSE.txt)

### 鸣谢


- [LangChain](https://www.langchain.com/)
- [🌩最好的中文README模板⚡️Best README template](https://github.com/shaojintian/Best_README_template)
- [Choose an Open Source License](https://choosealicense.com)

<!-- links -->
[your-project-path]:https://github.com/JasdewStarfield/ChatBuran
[contributors-shield]: https://img.shields.io/github/contributors/JasdewStarfield/ChatBuran.svg?style=flat-square
[contributors-url]: https://github.com/JasdewStarfield/ChatBuran/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/JasdewStarfield/ChatBuran?style=flat-square
[forks-url]: https://github.com/JasdewStarfield/ChatBuran/network/members
[stars-shield]: https://img.shields.io/github/stars/JasdewStarfield/ChatBuran.svg?style=flat-square
[stars-url]: https://github.com/JasdewStarfield/ChatBuran/stargazers
[issues-shield]: https://img.shields.io/github/issues/JasdewStarfield/ChatBuran.svg?style=flat-square
[issues-url]: https://github.com/JasdewStarfield/ChatBuran/issues
[license-shield]: https://img.shields.io/github/license/JasdewStarfield/ChatBuran.svg?style=flat-square
[license-url]: https://github.com/JasdewStarfield/ChatBuran/master/LICENSE.txt




