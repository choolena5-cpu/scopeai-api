<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/brand-light.png">
  <img src="assets/brand-dark.png" alt="ScopeAI" width="140" height="36">
</picture>

# ScopeAI · AI 资讯、模型对比与 GEO 观察

看 AI 行业发生了什么，按任务比较模型，追踪 Codex 额度重置公告，并观察品牌在 AI 回答中的表现。

[访问网站](https://scopeai.cc/) · [AI 实测室](https://scopeai.cc/lab) · [Codex 重置](https://scopeai.cc/codex-resets) · [GEO 观察](https://scopeai.cc/geo-services) · [English](README.en.md)

## 网站能做什么

| 功能 | 适合解决的问题 | 入口 |
| --- | --- | --- |
| AI 新闻时间线与精选热点 | 浏览模型发布、产品更新、开源项目和融资消息，沿原始来源核对信息 | [时间线](https://scopeai.cc/) · [精选热点](https://scopeai.cc/hot) |
| 今日分析与深度解读 | 了解重要 AI 事件的背景与影响 | [今日分析](https://scopeai.cc/observations) · [深度解读](https://scopeai.cc/insights) |
| AI 模型排行 | 查看模型比较结果，辅助选择候选模型 | [模型排行](https://scopeai.cc/ranking) |
| AI 实测室 | 按 PPT 设计、编程、写作、数学与科学、知识问答、深度研究、智能体任务查看第三方公开评测 | [实测室](https://scopeai.cc/lab) |
| Codex 重置观察 | 查看公开额度重置公告、历史记录与相关动态，区分额度重置和重置卡 | [Codex 重置](https://scopeai.cc/codex-resets) |
| GEO 品牌观察 | 了解品牌提及、推荐与引用证据，查看服务范围并进入品牌工作区 | [服务介绍](https://scopeai.cc/geo-services) · [工作区](https://scopeai.cc/geo) |
| RSS 与 Agent 接入说明 | 用阅读器订阅资讯，或了解 AI Agent / MCP 的接入方式与服务边界 | [RSS](https://scopeai.cc/rss.xml) · [Agent 文档](https://scopeai.cc/agents) |

实测室整理第三方评测，不同基准与测试配置的分数应分别理解。Codex 重置页是独立的信息观察页，非 OpenAI 官方服务；个人账户剩余额度和重置时间请以账户用量页面为准。

### 页面预览

[![ScopeAI 精选热点页面](assets/scopeai-hot.png)](https://scopeai.cc/hot)

<details>
<summary>查看 AI 实测室截图</summary>

[![ScopeAI AI 实测室：按任务比较第三方评测结果](assets/scopeai-lab.png)](https://scopeai.cc/lab)

</details>

<sub>2026-10-19 网站实际页面截图；新闻、模型和评测结果会随网站更新。</sub>

## GEO API 与开发者接入

本仓库提供产品介绍、GEO API 文档、接口契约与客户端示例。网站浏览功能与付费 API 的开放状态分别说明。

[申请 API 接入](https://scopeai.cc/developers) · [接入文档](docs/getting-started.md)

> **接入预览**：付费 API 待生产开放。请先确认所需服务可用，再充值。[查看状态](docs/status.md)

## GEO 观察

为品牌建立独立项目，管理问题与竞品，购买公开资料观察或指定模型回答采样，并查询原始回答、来源证据和历史结果。周期监测需要单独授权和月预算。

![路途乐 GEO 界面设计预览](assets/lutule-geo.png)

<sub>路途乐案例：界面为设计预览，数值来自 2026-09-07 已核验的单轮记录。11 道自然问题中，品牌被提及 2 次、明确推荐 2 次。单轮观察不代表稳定行业排名或品牌背书。[案例说明](docs/showcase.md)</sub>

案例使用 DeepSeek 联网采样；首版 API 实际回答采样使用 **DeepSeek 模型 API，搜索关闭**，不等同于其网页或 App，也不承诺复现案例分数。公开资料观察单独报价，不代表多平台实测。

## 价格与接入

托管服务采用**账户充值、API key 授权、按量扣余额**。以下为首版预览价格，实际开放范围与金额以服务端价目和报价为准。

| 服务 | 价格 | 计费单位 |
| --- | ---: | --- |
| 公开资料观察 | **¥1.00** | 完整交付一轮 |
| 模型回答采样 | **¥1.00** | 一道问题的一次成功采样 |

任务先冻结最高费用，按成功交付结算，失败部分释放。成功回答未提到品牌仍正常计费；相同请求编号的合规重试不重复扣费。定时监测单独授权，按每轮服务结算并受月预算限制。[完整计费规则](docs/pricing.md)

1. [创建账户](https://scopeai.cc/login?mode=register)，进入[开发者工作台](https://scopeai.cc/developers)。
2. [联系客服](https://scopeai.cc/account/billing)确认开放状态并充值；当前由管理员核实收款后入账。
3. 创建 API key，授予 GEO 消费权限、设置预算，在自己的服务器调用。
4. 查看结果、余额和消费流水；读取已购买结果不额外收费。

## 开发者资料

[接入指南](docs/getting-started.md) · [OpenAPI 3.1](openapi.json) · [Python 示例](examples/python/quickstart.py) · [TypeScript 客户端](examples/typescript/scope-client.ts)

[业务案例](docs/use-cases.md) · [常见问题](docs/faq.md) · [开放公告](https://github.com/choolena5-cpu/scopeai-api/releases)

---

本仓库公开 GEO 观察说明、效果图、接口契约与客户端示例。分析引擎、计费后台、客户数据和服务端源码保持私有。付费业务必须连接 ScopeAI 托管 API，通过账户、服务权限、预算和余额校验；下载仓库不会获得模型额度或客户数据。
