<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/brand-light.png">
  <img src="assets/brand-dark.png" alt="ScopeAI" width="140" height="36">
</picture>

# AI 新闻与 GEO 检测 API

给网站、App 和行业助手接入 AI 资讯，为品牌观察提供模型回答与原文证据。

[申请接入](https://camcat.net/developers) · [体验产品](https://camcat.net) · [接入文档](docs/getting-started.md) · [English](README.en.md)

> **接入预览**：付费 API 待生产开放。请先确认所需服务可用，再充值。[查看状态](docs/status.md)

## AI 新闻

读取本站公开新闻，支持列表、搜索、热门、专题、正文与来源，以及内容修改和撤回同步。适合资讯栏目、企业日报和主题追踪。

![AI 新闻界面设计预览](assets/news.png)

<sub>界面设计预览，新闻内容依据历史记录简化展示；非线上截图。</sub>

## GEO 检测

查看指定模型的回答是否提到、推荐你的品牌。结合公开资料、原文证据和历史结果，为品牌诊断、客户报告与周期观察提供依据。

![路途乐 GEO 界面设计预览](assets/lutule-geo.png)

<sub>路途乐案例：界面为设计预览，数值来自 2026-09-07 已核验的单轮记录。11 道自然问题中，品牌被提及 2 次、明确推荐 2 次。单轮观察不代表稳定行业排名或品牌背书。[案例说明](docs/showcase.md)</sub>

案例使用 DeepSeek 联网采样；首版 API 实际回答采样使用 **DeepSeek 模型 API，搜索关闭**，不等同于其网页 / App，不承诺复现案例分数。公开资料观察单独报价，不代表多平台实测。

## 价格与接入

托管服务采用**账户充值、API key 授权、按量扣余额**。以下为首版预览价格，实际开放范围与金额以服务端价目和报价为准。

| 服务 | 价格 | 计费单位 |
| --- | ---: | --- |
| 新闻数据 | **¥0.01** | 非空成功请求；一页最多 50 条，正文详情另算一次 |
| 公开资料观察 | **¥1.00** | 完整交付一轮 |
| 模型回答采样 | **¥1.00** | 一道问题的一次成功采样 |

GEO 先冻结最高费用，按成功交付结算，失败部分释放。成功回答未提到品牌仍正常计费；相同请求编号的合规重试不重复扣费。定时监测单独授权，按每轮服务结算并受月预算限制。[完整计费规则](docs/pricing.md)

1. [创建账户](https://camcat.net/login?mode=register)，进入[开发者工作台](https://camcat.net/developers)。
2. [联系客服](https://camcat.net/account/billing)确认开放状态并充值；当前由管理员核实收款后入账。
3. 创建 API key，授予消费权限、设置预算，在自己的服务器调用。
4. 查看结果、余额和消费流水；读取已购买结果不额外收费。

## 开发者资料

[接入指南](docs/getting-started.md) · [OpenAPI 3.1](openapi.json) · [Python 示例](examples/python/quickstart.py) · [TypeScript 客户端](examples/typescript/scope-client.ts)

[业务案例](docs/use-cases.md) · [常见问题](docs/faq.md) · [开放公告](https://github.com/choolena5-cpu/scopeai-api/releases)

---

本仓库公开说明、效果图、接口契约与客户端示例。**新闻数据库、采集系统、GEO 分析引擎、计费后台和服务端源码保持私有。** 付费业务必须连接 ScopeAI 托管 API，通过账户、服务权限、预算和余额校验；下载仓库不会获得免费数据或模型额度。
