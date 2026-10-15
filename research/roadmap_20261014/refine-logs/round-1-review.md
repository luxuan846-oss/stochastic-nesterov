# 外部复核未完成

research-refine 指定 gpt-5.5 / xhigh / Codex MCP。调用返回 403，模型不存在或未启用。没有产生有效评审、评分或 READY 判定。未换用未经指定的服务。

<details><summary>完整原始返回</summary>

```json
{
  "content": [
    {
      "type": "text",
      "text": "unexpected status 403 Forbidden: 模型不存在或未启用: gpt-5.5，请查看模型库：https://yxai.chat/model-library, url: https://yxai.chat/v1/responses"
    }
  ],
  "structuredContent": {
    "threadId": "01a13a91-e490-7672-98b9-88b5d5d3bc78",
    "content": "unexpected status 403 Forbidden: 模型不存在或未启用: gpt-5.5，请查看模型库：https://yxai.chat/model-library, url: https://yxai.chat/v1/responses"
  },
  "isError": true
}
```

</details>
