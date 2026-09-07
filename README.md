<div align="center">

# ScopeAI API

### 给你的产品接入 AI 新闻与品牌观察

**AI 新闻数据 · 集优观察 / GEO · 模型回答采样 · 定时监测**

[申请接入](https://camcat.net/developers) · [创建账户](https://camcat.net/login?mode=register) · [充值与账单](https://camcat.net/account/billing) · [English](README.en.md)

</div>

---

把本站公开 AI 新闻接入你的网站、App 或企业日报；围绕自己的品牌获取公开证据，查看指定模型在回答行业问题时是否提到你。

**当前阶段：接入预览 / 申请开通。** 新闻与 GEO 付费能力已完成开发和本地验收，生产开放仍在准备中。请先确认所需服务已开放，再充值。[查看开放状态](docs/status.md)

## 你能做什么

| 你的业务 | ScopeAI 提供什么 |
| --- | --- |
| 给网站或 App 增加 AI 新闻栏目 | 公开新闻标题、摘要、分类、配图、正文与来源 |
| 做企业 AI 日报、行业信息助手 | 按分类、日期和关键词读取新闻，支持修改与撤回同步 |
| 给品牌做公开资料诊断 | 问题、原文来源、品牌证据、竞品资料与内容建议 |
| 做品牌在 AI 回答中的观察报告 | 指定模型的实际回答、品牌提及判断、采样时间与历史 |
| 为客户提供周期监测服务 | 单独授权的日 / 周监测、消费预算和结果查询 |

[查看具体业务案例](docs/use-cases.md)

## 接入工具公开，托管服务付费

本仓库提供文档、接口契约和客户端示例。实际新闻数据、观察任务、执行与计费由 **ScopeAI 托管 API** 提供。

使用付费业务需要：**ScopeAI 账户、已开通的服务、预付余额，以及对应消费授权的 API key。** 下载本仓库不会获得新闻数据库、模型额度或服务端运行环境。

金额由服务端结算。客户端不能通过修改示例代码跳过鉴权、消费权限、余额检查或费用上限。免费账户查询不等于免费获取付费数据。

## 首版价格

以下是首版预览价目；正式开放时以服务端价目表及接受的报价为准。

| 服务 | 计费单位 | 首版价格 |
| --- | --- | --- |
| 新闻数据 | 每个非空成功请求，一页最多 50 条；详情另算一次 | **¥0.01** |
| 公开资料观察 | 完整交付一轮 | **¥1.00** |
| DeepSeek 模型 API 回答采样 | 一道问题的一次成功采样 | **¥1.00** |
| 定时监测 | 按每轮实际服务结算 | 同上，受月预算限制 |

GEO 先冻结最高费用，再按成功部分扣款，失败部分释放。相同请求编号的重试不重复扣费。余额、报价、已购买结果与账单查询不额外收费。[完整计费规则](docs/pricing.md)

## 从注册到调用

1. [创建账户](https://camcat.net/login?mode=register)，打开[开发者工作台](https://camcat.net/developers)。
2. 在[充值与账单](https://camcat.net/account/billing)页联系官方客服，说明需要的业务并确认开放状态。
3. 按确认的方式充值。当前采用客服协助充值，管理员核实收款后入账。
4. 获取 API key，开启所需消费权限，设置账户和密钥预算。
5. 在你的服务器调用 ScopeAI，查看结果与实际消费。

## 一次新闻读取

**仅在对应服务已经开通、账户有余额时运行。以下请求可能消费 ¥0.01。**

```bash
export SCOPE_BASE_URL="https://camcat.net"
# 将密钥通过你的环境变量或密钥管理工具注入 SCOPE_API_KEY。
# 为本次业务操作生成并保存 NEWS_REQUEST_KEY；网络重试复用它。

curl "$SCOPE_BASE_URL/api/v1/news/articles?limit=50" \
  -H "Authorization: Bearer $SCOPE_API_KEY" \
  -H "Idempotency-Key: $NEWS_REQUEST_KEY" \
  -H "X-Max-Charge-Cents: 1"
```

[完整接入指南](docs/getting-started.md) · [OpenAPI 3.1](openapi.json) · [Python 示例](examples/python/quickstart.py) · [TypeScript 客户端](examples/typescript/scope-client.ts)

## 数据与观察范围

- 新闻仅包含本站当前公开内容。待审稿、编辑后台及其他用户的私有资料不开放。
- 资料观察基于实际读取的公开证据，不代表多家 AI 产品的真实回答。
- 首版实际回答采样目标是 **DeepSeek 模型 API，搜索关闭**；不等同于其网页 / App。
- 历史查询只访问自己的项目和购买结果。比较报告时应保持模型、问题版本及口径一致。

[常见问题](docs/faq.md) · [服务开放状态](docs/status.md)

## 联系与反馈

接入、额度和充值问题，请到[账户页联系官方客服](https://camcat.net/account/billing)。接口文档和示例问题可以提交 GitHub Issue。涉及账户、充值凭证或 API key 的内容请通过客服处理。

如果这套服务适合你的项目，可以 Star 收藏本仓库，并关注后续开放公告。
