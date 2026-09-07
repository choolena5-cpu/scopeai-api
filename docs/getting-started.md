# 接入指南

先阅读[服务开放状态](status.md)。以下新接口以正式开通为前提；当前仓库供接入准备，生产能力不可用时不要充值后反复尝试。

## 1. 获取账户和消费权限

在 [ScopeAI](https://camcat.net/login?mode=register) 创建账户，在[账户页](https://camcat.net/account/billing)联系官方客服确认服务与充值方式。余额到账后，在[开发者工作台](https://camcat.net/developers)创建 key，并授权对应产品。

新闻需明确允许新闻消费。GEO 的 `geo:write` 用于创建、修改和报价，`geo:run` 允许执行付费任务，`geo:schedule` 单独允许定时计划。账户与 key 的日预算共同生效。

## 2. 配置客户端

Python 示例仅使用标准库。把 `SCOPE_BASE_URL=https://camcat.net` 和你自己的 `SCOPE_API_KEY` 注入服务端环境；`.env.example` 只是字段说明，示例不会自动读取 `.env`。

```bash
python3 examples/python/quickstart.py
```

默认仅调用免费兼容余额接口 `/api/v1/geo/balance`。它不会创建任务或主动充值，结果只能证明账户查询是否成功，不代表新付费接口已开放。

已确认新闻服务开放时，先在自己的业务系统生成并持久保存一个操作编号，然后显式运行付费示例：

```bash
python3 examples/python/quickstart.py --news --request-key "$NEWS_REQUEST_KEY"
```

它读取最多 20 条摘要，最高允许消费 1 分。失败后重试时必须保留原操作编号。不要把该命令放进会每次生成新编号的自动重试循环。

TypeScript 项目可以引入 [scope-client.ts](../examples/typescript/scope-client.ts)，使用现有 TypeScript 构建工具编译；本仓库没有发布可直接 npm install 的 SDK 包。

```typescript
import { ScopeClient } from "./scope-client";

const client = new ScopeClient(process.env.SCOPE_BASE_URL!, process.env.SCOPE_API_KEY!);
// 这是你已保存的业务操作编号，重试不变。服务开通后本次最高 1 分。
const result = await client.news(savedOperationId, 20);
```

## 3. 购买 GEO 任务

创建项目时提交真实品牌信息，例如：

```json
{
  "name": "你的品牌",
  "site": "https://你的官方网站",
  "industry": "你的主营业务",
  "market": "目标市场"
}
```

以上为待替换字段示意，不是可直接请求的数据。调用 `POST /geo/projects`，或免费读取已有项目，保存返回的项目 ID 与 revision。

以实际项目 ID、revision 获取报价：

```python
from scope_client import ScopeClient

client = ScopeClient()
quote = client.quote(project_id, revision, ["企业团队知识库有哪些选择？"])
offer = quote["body"]["data"]
# 检查 offer["amount_cents"]，向你的业务用户展示费用。
# 保存操作编号并得到消费确认后，才执行以下付费步骤。
created = client.accept(saved_operation_id, offer["id"], offer["amount_cents"])
check_id = created["body"]["data"]["id"]
result = client.wait(check_id)
answers = client.request("GET", "/geo/checks/" + check_id + "/answers")
```

金额以分计。报价 15 分钟有效，创建任务先冻结费用，后台执行后仅结算成功单元。`wait` 超时只结束本地等待，不取消任务；继续查询原 ID 即可。

购买资料观察时，报价改为 `product=geo.research.standard`、`target_id=public-source-research`、空 questions、repeats=1、max_unit_cents=100。资料观察需要真实原文及完整分析才能交付。

计划需另外授权并调用 `POST /geo/schedules`，提交 request_key、quote_id、interval_days（1 或 7）、monthly_cents 和 accepted_price_version。不能把一次购买默认当作长期订阅授权。

## 4. 响应与费用

新接口成功响应一般为 `{data,meta}`，错误为 `{error:{code,message,request_id}}`；兼容 `/geo/balance`、`/geo/projects` GET 保留原格式。

新闻的 `meta.billing.charged_cents` 是原逻辑请求费用，`newly_charged_cents` 是本次新增金额，重试通常为 0。GEO 的费用在任务 `billing` 中区分 charged、remaining、released。交易编号用于核账。

401 表示密钥无效；402 表示余额不足；403 表示权限或产品未开放；409 表示参数、价格、预算或状态冲突；429 表示请求过快。不要对所有错误无限重试。

## 5. 同步、缓存与已有结果

新闻同步从 `/news/changes?cursor=0` 开始，按 sequence 应用 upsert / withdraw 并保存 `next_cursor`。每个新页使用新请求编号；同页网络重试复用编号。正文详情单独收费。

对同一查询使用 ETag / If-None-Match，可得到免费 304。新一轮条件轮询使用新编号，同一次网络重试保留原编号与原条件头。304 没有 JSON 响应体。

任务已有回答、来源、历史及账单查询免费，支持分页。导出只包含自己的已有结果，不会重新运行服务。

完整字段见 [OpenAPI](../openapi.json)，价格说明见[计费规则](pricing.md)。
