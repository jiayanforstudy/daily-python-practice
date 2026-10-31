# GitHub 阅读学习日志

## 阅读项目：RAG from Scratch

- **项目地址：** https://github.com/langchain-ai/rag-from-scratch
- **Notebook：** `rag_from_scratch_1_to_4.ipynb`
- **学习方式：** 逐段阅读真实代码，追踪变量、函数调用和数据流

---

## Day24 — 2026-10-29

### 1. 本次阅读范围

从网页加载器开始，追踪 RAG 的文档处理和生成流程。

### 2. 已阅读的代码

```python
loader = WebBaseLoader(
    web_paths=("https://lilianweng.github.io/posts/2023-06-23-agent/",),
    ...
)
blog_docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
splits = text_splitter.split_documents(blog_docs)

vectorstore = Chroma.from_documents(
    documents=splits,
    embedding=OpenAIEmbeddings()
)

retriever = vectorstore.as_retriever()

rag_chain = (
    {"context": retriever,
     "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

rag_chain.invoke("What is Task Decomposition?")
```

### 3. 已理解的知识

- `WebBaseLoader`：加载指定网页内容。
- `loader.load()`：执行加载并返回文档。
- `RecursiveCharacterTextSplitter`：将文档切分为多个文本块。
- `split_documents(docs)`：切分文档并返回结果。
- `Chroma.from_documents()`：根据文档和指定的 Embedding 模型创建向量存储。
- `vectorstore.as_retriever()`：创建检索器接口。
- `RunnablePassthrough()`：原样传递输入。
- `rag_chain.invoke(question)`：执行整条 RAG 链，触发检索、Prompt 处理和 LLM 生成。

### 4. 已经理解的数据流

`loader → blog_docs → splits → vectorstore → retriever → rag_chain`

已理解：`retriever` 被放入 RAG 链的 `context` 分支中，因此调用整条链就会触发检索，不必单独写 `retriever.invoke()`。

### 5. 需要继续学习的内容

- `retriever` 实际返回什么数据结构？
- 返回的 `Document` 对象包含哪些字段？
- `context` 中的检索结果如何被 Prompt 使用？
- 当前链的检索结果是否包含相似度分数？如何查看？
- 如果检索器返回多个文档，后续代码如何处理？

### 6. 下次阅读起点

继续在同一个 Notebook 中追踪 `retriever` 的返回值及其在 RAG 链中的传递过程。

**下次不要重新学习整个 RAG 流程，直接从检索结果的数据结构开始。**

---

## Day25 — 2026-10-31

### 1. 本次阅读范围

继续阅读 `rag_from_scratch_1_to_4.ipynb`，重点理解 Retriever 返回的文档如何经过格式化和 Prompt 处理，最终进入 LLM。

### 2. 核心代码

```python
def format_docs(docs):
    return "\n\n".join(
        doc.page_content for doc in docs
    )

template = """Answer the question based only on the following context:

{context}

Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
```

### 3. 已掌握的知识

- `Document`：LangChain 文档对象。
- `page_content`：提取文档正文。
- `metadata`：保存文档来源、页码等附加信息。
- `format_docs()`：提取多个 Document 的正文并拼接。
- `"\n\n".join()`：使用两个换行符连接多个字符串。
- `retriever | format_docs`：先检索文档，再格式化检索结果。
- `RunnablePassthrough()`：原样传递用户问题。
- `ChatPromptTemplate.from_template()`：将字符串模板转换为 Prompt 模板对象。
- `{context}`：检索到的上下文。
- `{question}`：用户提出的问题。
- `StrOutputParser()`：将模型输出解析为字符串。

### 4. 已理解的数据流

Question → Retriever → Document List → format_docs → Context

原始问题通过 `RunnablePassthrough()` 保留。

两路数据进入 Prompt 后，依次经过 LLM 和输出解析器，最终生成回答。

### 5. 工程理解

Prompt 可以要求模型仅根据检索上下文回答，但不能绝对避免幻觉。实际项目还需要考虑检索相关性判断、相似度阈值和拒答机制。

### 6. 下次阅读起点

继续阅读同一个 Notebook 中的 LLM 初始化和 Retriever 配置。

重点关注：

- `ChatOpenAI()` 的初始化参数
- 模型名称与 temperature 参数
- Retriever 的检索数量和搜索策略
- 检索结果是否包含相似度分数

**当前进度：已经理解 RAG 从文档加载、切分、向量化、检索到 Prompt 和 LLM 生成的基本流程。**
