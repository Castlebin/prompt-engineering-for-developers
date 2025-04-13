# %%
from dashscope_api import get_completion_from_messages


# 第八章 聊天机器人

# %%
# 一、给定身份
# 1.1 讲笑话
# 中文
messages =  [  
    {'role':'system', 'content':'你是一个像莎士比亚一样说话的助手。'},    
    {'role':'user', 'content':'给我讲个笑话'},   
    {'role':'assistant', 'content':'鸡为什么过马路'},   
    {'role':'user', 'content':'我不知道'}  
]


response = get_completion_from_messages(messages, temperature=1)
print(response)

# %%
# 中文
messages =  [  
    {'role':'system', 'content':'你是个友好的聊天机器人。'},    
    {'role':'user', 'content':'Hi, 我是Isa。'}  
]

response = get_completion_from_messages(messages, temperature=1)
print(response)


# 二、构建上下文
# %%
# 中文
messages =  [  
    {'role':'system', 'content':'你是个友好的聊天机器人。'},    
    {'role':'user', 'content':'好，你能提醒我，我的名字是什么吗？'}  
]
response = get_completion_from_messages(messages, temperature=1)
print(response)

# %%
# messages 中维护了上下文
messages =  [  
    {'role':'system', 'content':'你是个友好的聊天机器人。'},
    {'role':'user', 'content':'Hi, 我是Isa'},
    {'role':'assistant', 'content': "Hi Isa! 很高兴认识你。今天有什么可以帮到你的吗?"},
    {'role':'user', 'content':'是的，你可以提醒我, 我的名字是什么?'}  
]

response = get_completion_from_messages(messages, temperature=1)
print(response)


# 三、订餐机器人
#3.1 构建机器人
#下面这个函数将收集我们的用户消息，以便我们可以避免像刚才一样手动输入。这个函数将从我们下面构建的用户界面中收集 Prompt ，然后将其附加到一个名为上下文( context )的列表中，并在每次调用模型时使用该上下文。模型的响应也会添加到上下文中，所以用户消息和模型消息都被添加到上下文中，上下文逐渐变长。这样，模型就有了需要的信息来确定下一步要做什么。

# !pip install panel
# !pip install jupyter_bokeh
# %%
def collect_messages(_):
    prompt = inp.value_input
    inp.value = ''
    context.append({'role':'user', 'content':f"{prompt}"})
    response = get_completion_from_messages(context) 
    context.append({'role':'assistant', 'content':f"{response}"})
    panels.append(
        pn.Row('User:', pn.pane.Markdown(prompt, width=600)))
    panels.append(
        pn.Row('Assistant:', pn.pane.Markdown(response, width=600)))
 
    return pn.Column(*panels)

# 中文
import panel as pn  # GUI
pn.extension()

panels = [] # collect display 

context = [{'role':'system', 'content':"""
你是订餐机器人，为披萨餐厅自动收集订单信息。
你要首先问候顾客。然后等待用户回复收集订单信息。收集完信息需确认顾客是否还需要添加其他内容。
最后需要询问是否自取或外送，如果是外送，你要询问地址。
最后告诉顾客订单总金额，并送上祝福。

请确保明确所有选项、附加项和尺寸，以便从菜单中识别出该项唯一的内容。
你的回应应该以简短、非常随意和友好的风格呈现。

菜单包括：

菜品：
意式辣香肠披萨（大、中、小） 12.95、10.00、7.00
芝士披萨（大、中、小） 10.95、9.25、6.50
茄子披萨（大、中、小） 11.95、9.75、6.75
薯条（大、小） 4.50、3.50
希腊沙拉 7.25

配料：
奶酪 2.00
蘑菇 1.50
香肠 3.00
加拿大熏肉 3.50
AI酱 1.50
辣椒 1.00

饮料：
可乐（大、中、小） 3.00、2.00、1.00
雪碧（大、中、小） 3.00、2.00、1.00
瓶装水 5.00
"""} ]  # accumulate messages


inp = pn.widgets.TextInput(value="Hi", placeholder='Enter text here…')
button_conversation = pn.widgets.Button(name="Chat!")

interactive_conversation = pn.bind(collect_messages, button_conversation)

dashboard = pn.Column(
    inp,
    pn.Row(button_conversation),
    pn.panel(interactive_conversation, loading_indicator=True, height=300),
)

dashboard

# %%
