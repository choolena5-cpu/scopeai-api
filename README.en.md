<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/brand-light.png">
  <img src="assets/brand-dark.png" alt="ScopeAI" width="140" height="36">
</picture>

# ScopeAI GEO observation API

Track how AI answers mention and recommend your brand through public-source research and model-answer sampling.

[Request access](https://camcat.net/developers) · [Explore ScopeAI](https://camcat.net/geo) · [Integration guide](docs/getting-started.md) · [中文](README.md)

> **Integration preview:** paid API production activation is pending. Confirm availability before funding an account. [Service status](docs/status.md)

## GEO observation

Create a private brand project, manage questions and competitors, purchase public-source research or specified model-answer sampling, and query original answers, source evidence and historical results. Scheduled monitoring requires separate authorization and a monthly budget.

![Lutule GEO interface design preview](assets/lutule-geo.png)

<sub>The interface is a design preview; numbers come from verified September 7, 2026 records. Lutule received 2 mentions and 2 explicit recommendations across 11 natural questions. This single observation is not a stable industry ranking or brand endorsement. [Case details](docs/showcase.md)</sub>

The historical case used DeepSeek with web search enabled. The first API sampling target uses the **DeepSeek model API with search disabled**, not its consumer website or app, and does not promise to reproduce these scores. Public-source research is billed separately and is not measured multi-platform visibility.

## Pricing and access

Paid operations require an enabled product, prepaid account balance and an API key authorized to spend. Initial prices below are previews; final availability and quotes come from the service.

| Service | CNY | Unit |
| --- | ---: | --- |
| Public-source research | **1.00** | Fully delivered run |
| Model-answer sampling | **1.00** | Successful question × repetition unit |

Tasks reserve the maximum quote, charge successful deliveries and release failed portions. A valid answer without a brand mention is still billable. Valid retries with the same request key do not create duplicate charges. Scheduled monitoring requires separate authorization and a monthly budget. [Billing rules](docs/pricing.md)

1. [Create an account](https://camcat.net/login?mode=register) and visit the [developer portal](https://camcat.net/developers).
2. Confirm availability with [support](https://camcat.net/account/billing), then fund your balance through the current support-assisted process.
3. Create an API key, authorize GEO spending, set budgets and call from your server.
4. Check results, balance and transactions. Reading previously purchased results has no additional charge.

## Developer resources

[Integration guide](docs/getting-started.md) · [OpenAPI 3.1](openapi.json) · [Python](examples/python/quickstart.py) · [TypeScript](examples/typescript/scope-client.ts)

[Use cases](docs/use-cases.md) · [FAQ](docs/faq.md) · [Releases](https://github.com/choolena5-cpu/scopeai-api/releases)

---

This repository publishes GEO observation documentation, design previews, API contracts and client examples. The analysis engine, billing implementation, customer data and backend source remain private. Downloading the repository does not grant model credits or access to customer data.
