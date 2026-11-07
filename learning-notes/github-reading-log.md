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

---

## Day28 — 2026-11-03

### 1. 本次阅读范围

项目：`langchain-ai/rag-from-scratch`

Notebook：`rag_from_scratch_1_to_4.ipynb`

本次重点：Retriever 配置、LLM 初始化、向量相似度检索及 Document 数据结构。

### 2. 实际阅读的核心代码

**（1）Retriever 配置**

```python
retriever = vectorstore.as_retriever(
    search_kwargs={"k": 1}
)
```

- `as_retriever()`：从向量存储创建检索器。
- `search_kwargs`：传递检索参数。
- `k`：控制返回的相关文档块数量。

k 越大，检索范围越广，但可能引入不相关内容，增加上下文长度和模型处理成本。

**（2）LLM 初始化**

```python
llm = ChatOpenAI(
    model_name="gpt-3.5-turbo",
    temperature=0
)
```

- `ChatOpenAI()`：初始化聊天模型。
- `model_name`：指定使用的模型。
- `temperature`：控制生成随机性。较低的值通常使输出更稳定。

注意：这里是原 Notebook 中的旧版模型配置示例，不代表该模型目前仍是最佳选择。

**（3）检索调用**

Notebook 使用了：

```python
docs = retriever.get_relevant_documents(
    "What is Task Decomposition?"
)
```

以及：

```python
len(docs)
```

其中：
- `docs`：保存 Retriever 返回的 Document 对象列表。
- `len(docs)`：统计返回的文档数量。

新版 LangChain 通常使用：

```python
docs = retriever.invoke(question)
```

阅读旧项目时需要注意 API 版本差异。

### 3. 额外学习：向量相似度检索

文档向量化和问题向量化：

- `embed_documents()`：将文档转换成向量。
- `embed_query()`：将用户问题转换成向量。

随后向量数据库根据向量之间的关系寻找相关文档。

常见的向量比较方法：

- Cosine Similarity：余弦相似度。
- Euclidean Distance：欧氏距离。
- Dot Product：点积。

余弦相似度公式：

cos(θ) = (A · B) / (||A|| × ||B||)

注意：
- 相似度通常越大越相关。
- 距离通常越小越接近。
- Chroma 的 `similarity_search_with_score()` 返回距离分数，不能直接将其当作百分比相似度。

### 4. 额外学习：如何查看检索结果

```python
results = vectorstore.similarity_search_with_score(
    "What is Task Decomposition?",
    k=3
)

for doc, score in results:
    print("Distance:", score)
    print("Content:", doc.page_content)
    print("Metadata:", doc.metadata)
```

这里的返回结果由 Document 和对应的距离分数组成。

Document 对象的重要字段：

| 字段 | 作用 |
|---|---|
| `page_content` | 文档正文 |
| `metadata` | 文档来源、页码等附加信息 |

常见访问方式：

```python
docs[0]
docs[0].page_content
docs[0].metadata
```

注意：以上是额外设计的检查代码，并非原 Notebook 中实际存在的代码。

### 5. 已理解的核心知识

- Retriever 的 k 参数控制返回文档数量。
- 增大 k 不代表检索质量一定提高。
- 用户问题也需要转换成 Embedding，才能进行向量检索。
- 向量数据库根据向量距离或相似度寻找相关文档。
- Document 不只有正文，还包含 metadata。
- metadata 可以用于追踪文档来源、页码及其他信息。
- 检索阶段的质量会直接影响 RAG 最终生成的回答。

### 6. 本次理解测试

进阶测试 3/3 全部正确：

1. 用户问题需要转换成 Embedding 后才能进行向量检索。
2. Chroma 距离值通常越小，表示向量越接近。
3. metadata 用于保存来源、页码等附加信息。

### 7. 下次阅读起点

进入：

`rag_from_scratch_5_to_9.ipynb`

开始学习进阶 RAG 检索技术：

- Multi-Query Retrieval
- RAG-Fusion
- Query Decomposition
- HyDE

重点理解基础向量检索存在什么局限，以及不同检索优化方法分别解决什么问题。

**当前进度：已经掌握基础 RAG 的文档处理、向量存储、检索、Prompt 组织、LLM 生成及基本检索配置。**

---

## RAG-from-scratch：Notebook 5_to_9 学习总结

### 阅读范围

项目：`langchain-ai/rag-from-scratch`

Notebook：`rag_from_scratch_5_to_9.ipynb`

学习主题：五种进阶 RAG 检索优化方法。

### Part 5：Multi-Query Retrieval

- 使用 LLM 将一个用户问题改写成多个不同表达的查询。
- 使用 Prompt Template 组织查询改写任务。
- 使用 `StrOutputParser()` 解析模型输出。
- 使用 `split("\n")` 将多个查询拆分成列表。
- 使用 `retriever.batch(queries)` 批量执行检索。
- 合并多个检索结果，并利用字典按 `page_content` 去重。

核心目的：扩大检索覆盖范围，降低表达差异造成的检索遗漏。

### Part 6：RAG-Fusion

- 在多查询检索基础上引入 Reciprocal Rank Fusion（RRF）。
- 综合不同查询的检索排名。
- 使用倒数排名分数累计每篇文档的综合得分。
- 按综合得分重新排序。

公式：

RRF(d) = Σ 1 / (k + r(d))

注意：RRF 的 k 是平滑常数，与 Retriever 的 top-k 参数不是同一个概念。

核心目的：利用多个查询的排名信息，获得更合理的综合排序。

### Part 7：Decomposition

- 将复杂问题拆分成多个相对独立的子问题。
- 对子问题分别检索和回答。
- 使用列表保存多个子问题的答案。
- 最后汇总子问题答案，回答原始问题。

核心目的：解决包含多个信息需求的复杂问题。

### Part 8：Step-Back Prompting

- 将具体问题转换为更抽象、更一般的问题。
- 先检索基础原理和背景知识。
- 再结合原始问题生成具体答案。

核心目的：帮助系统先获得回答具体问题所需的背景知识。

### Part 9：HyDE

全称：Hypothetical Document Embeddings。

- 输入用户问题。
- 使用 LLM 生成假设性答案或文档。
- 对假设性内容进行 Embedding。
- 使用生成的向量检索真实知识库文档。
- 最终基于真实检索结果回答。

核心目的：缩小用户问题与知识库正文之间的表达差异。

注意：假设性答案可能存在错误，不能直接作为最终回答的事实依据。

### 五种方法对比

| 方法 | 主要解决的问题 |
|---|---|
| Multi-Query | 不同表达导致的检索遗漏 |
| RAG-Fusion | 多个检索排名的融合 |
| Decomposition | 复杂问题的多层次信息需求 |
| Step-Back | 缺乏基础原理和背景知识 |
| HyDE | 问题与文档表达形式不匹配 |

### 本次测试成绩

- RAG-Fusion：1/1 正确。
- 综合测试：4/4 正确。

### 已掌握的知识

理解五种 RAG 检索优化方法的基本原理、适用场景和主要区别，能够解释它们在基础 RAG 流程中的位置。

### 下一步学习

进入下一阶段，重点理解 Reranker、BM25、Hybrid Search，以及检索质量的评估指标 Recall@K、MRR、NDCG。

重点从理解 RAG 原理转向实际检索系统的工程设计和评估。
