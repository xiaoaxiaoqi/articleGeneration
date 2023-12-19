import requests

title = "手机网站建设有必要吗"
data = {
    "messages": [
        {"role": "user",
         "content": f"以{title}为中心，按照下面的要求写一篇800左右汉字的文章！1、介绍文章{title}，引出读者兴趣，并给读者提供背景信息。2、请从随机6-10个方面对{title}做详细的阐述，每个方面都要有3个以上的自然段，并且这4个方面的小标题，字数能够控制在10汉字左右;几个小标题使用<h2></h2>进行包裹;主要内容，分为多个段落或章节。详细解释主题、陈述观点、提供支持和证据，并引用其他人的研究和观点。3、总结文章的主要观点和结论，重申引言中的目的和重要性，并可能提出建议或未来的研究方向。此外，新写的文章需要具备以下特点:1、适当的结构:文章结构清晰明了，段落之间的过渡自然流畅，读者可以轻松理解文章的思路。2、丰富的内容:文章包含充足的信息和证据，能够支撑作者的观点和论据，同时具有独特的见解和观点。3、准确的语言:文章使用准确、简练、明确的语言，语法正确，拼写无误，让读者可以轻松理解作者的意图。4、合适的风格:文章风格合适，包括用词、语气、句式和结构，适应读者的背景和阅读目的。文章格式演示例子:<p>摘要内容</p><h2>—、小标题1</h2><p>1、文字阐述内容1</p><p>2、文字阐述内容2</p><p>3、文字阐述内容3</p><h2>二、小标题2</h2><p>1、文字阐述内容1</p><p>2、文字阐述内容2</p><p>3、文字阐述内容3/p><h2>三、小标题3</h2><p>1、文字阐述内容1</p><p>2、文字阐述内容2</p><p>3、文字阐述内容3</p><h2>四、小标题4</h2><p>1、文字阐述内容1</p><p>2、文字阐述内容2</p><p>3、文字阐述内容3</p><p>文章总结内容第一自然段</p><p>文章总结内容第二自然段</p>"},
    ],
    "model": "gpt-3.5-turbo",
    "temperature": 0.5,
    "max_tokens": 2000,
}
# 设置请求头，包括认证信息
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer sk-laAJIQZ6r8G4YN003ehpD7JgsqollgHO6uzAL2IaQcW2HVmU"
}
timeout = 180
# 发送POST请求
response = requests.post("https://api.openai-proxy.org/v1/chat/completions", json=data, headers=headers,
                         timeout=timeout)
print(response.json())
content = response.json()
content = content['choices'][0]['message']['content']
print(content)
