# %%
from dashscope_api import get_completion


# 第六章 文本转换

# 一、文本翻译

# %%
# 1.1 翻译为西班牙语
prompt = f"""
将以下中文翻译成西班牙语: \
```您好，我想订购一个搅拌机。```
"""
response = get_completion(prompt)
print(response)


# %%
# 翻译为英语
prompt = f"""
将以下中文翻译成英语: \
```您好，我想订购一个搅拌机。```
"""
response = get_completion(prompt)
print(response)

# %%
# 1.2 识别语种
prompt = f"""
请告诉我以下文本是什么语种: 
```Combien coûte le lampadaire?```
"""
response = get_completion(prompt)
print(response)

# %%
# 1.3 多语种翻译
prompt = f"""
请将以下文本分别翻译成中文、英文、法语和西班牙语: 
```I want to order a basketball.```
"""
response = get_completion(prompt)
print(response)

# %%
# 1.4 同时进行语气转换
prompt = f"""
请将以下文本翻译成中文，分别展示成正式与非正式两种语气: 
```Would you like to order a pillow?```
"""
response = get_completion(prompt)
print(response)

# %%
# 1.5 通用翻译器
# 在当今全球化的环境下，不同国家的用户需要频繁进行跨语言交流。但是语言的差异常使交流变得困难。为了打通语言壁垒，实现更便捷的国际商务合作和交流，我们需要一个智能的通用翻译工具。该翻译工具需要能够自动识别不同语言文本的语种，无需人工指定。然后它可以将这些不同语言的文本翻译成目标用户的母语。在这种方式下，全球各地的用户都可以轻松获得用自己母语书写的内容。
# 开发一个识别语种并进行多语种翻译的工具，将大大降低语言障碍带来的交流成本。它将有助于构建一个语言无关的全球化世界，让世界更为紧密地连结在一起。
user_messages = [
  "La performance du système est plus lente que d'habitude.",  # System performance is slower than normal         
  "Mi monitor tiene píxeles que no se iluminan.",              # My monitor has pixels that are not lighting
  "Il mio mouse non funziona",                                 # My mouse is not working
  "Mój klawisz Ctrl jest zepsuty",                             # My keyboard has a broken control key
  "我的屏幕在闪烁"                                             # My screen is flashing
]

# %%
import time
for issue in user_messages:
    # time.sleep(1) 
    prompt = f"告诉我以下文本是什么语种，直接输出语种，如法语，无需输出标点符号: ```{issue}```"
    lang = get_completion(prompt)
    print(f"原始消息 ({lang}): {issue}\n")

    prompt = f"""
    将以下消息分别翻译成英文和中文，并写成
    中文翻译：xxx
    英文翻译：yyy
    的格式：
    ```{issue}```
    """
    response = get_completion(prompt)
    print(response, "\n=========================================")


# 二、语气与写作风格调整
# 在写作中，语言语气的选择与受众对象息息相关。比如工作邮件需要使用正式、礼貌的语气和书面词汇；而与朋友的聊天可以使用更轻松、口语化的语气。
# 选择恰当的语言风格，让内容更容易被特定受众群体所接受和理解，是技巧娴熟的写作者必备的能力。随着受众群体的变化调整语气也是大语言模型在不同场景中展现智能的一个重要方面。

# %%
prompt = f"""
将以下文本翻译成商务信函的格式: 
```小老弟，我小羊，上回你说咱部门要采购的显示器是多少寸来着？```
"""
response = get_completion(prompt)
print(response)


# 三、文件格式转换
# 大语言模型如 ChatGPT 在不同数据格式之间转换方面表现出色。它可以轻松实现 JSON 到 HTML、XML、Markdown 等格式的相互转化。下面是一个示例,展示如何使用大语言模型将 JSON 数据转换为 HTML 格式:

# 假设我们有一个 JSON 数据,包含餐厅员工的姓名和邮箱信息。现在我们需要将这个 JSON 转换为 HTML 表格格式，以便在网页中展示。在这个案例中,我们就可以使用大语言模型,直接输入JSON 数据,并给出需要转换为 HTML 表格的要求。语言模型会自动解析 JSON 结构,并以 HTML 表格形式输出,完成格式转换的任务。

# 利用大语言模型强大的格式转换能力,我们可以快速实现各种结构化数据之间的相互转化,大大简化开发流程。掌握这一转换技巧将有助于读者更高效地处理结构化数据。

# %%
data_json = { "resturant employees" :[ 
    {"name":"Shyam", "email":"shyamjaiswal@gmail.com"},
    {"name":"Bob", "email":"bob32@gmail.com"},
    {"name":"Jai", "email":"jai87@gmail.com"}
]}

# %%
prompt = f"""
将以下Python字典从JSON转换为HTML表格，保留表格标题和列名：{data_json}

直接输出 HTML 代码，不要有任何其他输出
"""
response = get_completion(prompt)
print(response)

# %%
# 将上述 HTML 代码展示出来如下：
from IPython.display import display, Markdown, Latex, HTML, JSON
display(HTML(response))


# 四、拼写及语法纠正
# %%
# 在使用非母语撰写时，拼写和语法错误比较常见，进行校对尤为重要。例如在论坛发帖或撰写英语论文时，校对文本可以大大提高内容质量。

# 利用大语言模型进行自动校对可以极大地降低人工校对的工作量。
# 假设我们有一系列英语句子，其中部分句子存在错误。我们可以遍历每个句子，要求语言模型进行检查，如果句子正确就输出“未发现错误”，如果有错误就输出修改后的正确版本。

# 通过这种方式，大语言模型可以快速自动校对大量文本内容，定位拼写和语法问题。这极大地减轻了人工校对的负担，同时也确保了文本质量。利用语言模型的校对功能来提高写作效率，是每一位非母语写作者都可以采用的有效方法。
text = [ 
  "The girl with the black and white puppies have a ball.",  # The girl has a ball.
  "Yolanda has her notebook.", # ok
  "Its going to be a long day. Does the car need it’s oil changed?",  # Homonyms
  "Their goes my freedom. There going to bring they’re suitcases.",  # Homonyms
  "Your going to need you’re notebook.",  # Homonyms
  "That medicine effects my ability to sleep. Have you heard of the butterfly affect?", # Homonyms
  "This phrase is to cherck chatGPT for spelling abilitty"  # spelling
]


# %%
for i in range(len(text)):
    #time.sleep(20)
    prompt = f"""请校对并更正以下文本，注意纠正文本保持原始语种，无需输出原始文本。
    如果您没有发现任何错误，请说“未发现错误”。
    
    例如：
    输入：I happy.
    输出：I am happy.
    ```{text[i]}```"""
    response = get_completion(prompt)
    print(i, response)

# %%
# 下面是一个使用大语言模型进行语法纠错的简单示例，类似于Grammarly（一个语法纠正和校对的工具）的功能。

# 输入一段关于熊猫玩偶的评价文字，语言模型会自动校对文本中的语法错误，输出修改后的正确版本。这里使用的Prompt比较简单直接，只要求进行语法纠正。我们也可以通过扩展Prompt，同时请求语言模型调整文本的语气、行文风格等。
text = f"""
Got this for my daughter for her birthday cuz she keeps taking \
mine from my room.  Yes, adults also like pandas too.  She takes \
it everywhere with her, and it's super soft and cute.  One of the \
ears is a bit lower than the other, and I don't think that was \
designed to be asymmetrical. It's a bit small for what I paid for it \
though. I think there might be other options that are bigger for \
the same price.  It arrived a day earlier than expected, so I got \
to play with it myself before I gave it to my daughter.
"""
prompt = f"校对并更正以下商品评论：```{text}```"
response = get_completion(prompt)
print(response)

# %%
prompt = f"校对并更正以下商品评论 只需要输出校正后的内容：```{text}```"
response = get_completion(prompt)
print(response)

# %%
# 引入 Redlines 包，详细显示并对比纠错过程：
# 如未安装redlines，需先安装
# !pip install redlines
from redlines import Redlines
from IPython.display import display, Markdown

diff = Redlines(text,response)
display(Markdown(diff.output_markdown))


# %%
# 五、综合样例
# 语言模型具有强大的组合转换能力，可以通过一个Prompt同时实现多种转换，大幅简化工作流程。

# 下面是一个示例，展示了如何使用一个Prompt，同时对一段文本进行翻译、拼写纠正、语气调整和格式转换等操作。
prompt = f"""
针对以下三个反引号之间的英文评论文本，
首先进行拼写及语法纠错，
然后将其转化成中文，
再将其转化成优质淘宝评论的风格，从各种角度出发，分别说明产品的优点与缺点，并进行总结。
润色一下描述，使评论更具有吸引力。
输出结果格式为：
【优点】xxx
【缺点】xxx
【总结】xxx
注意，只需填写xxx部分，并分段输出。
将结果输出成Markdown格式。
```{text}```
"""

response = get_completion(prompt)
display(Markdown(response))
# 通过这个例子，我们可以看到大语言模型可以流畅地处理多个转换要求，实现中文翻译、拼写纠正、语气升级和格式转换等功能。
# 利用大语言模型强大的组合转换能力，我们可以避免多次调用模型来进行不同转换，极大地简化了工作流程。这种一次性实现多种转换的方法，可以广泛应用于文本处理与转换的场景中。

# %%
