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
