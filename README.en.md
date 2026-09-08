![ScopeAI API — AI news and GEO detection](assets/cover.png)

# AI news and GEO detection for your products

[中文](README.md) · [Request API access](https://camcat.net/developers) · [Explore ScopeAI](https://camcat.net)

**Integration preview.** The paid API is awaiting production activation. Confirm product availability before funding an account. See [service status](docs/status.md).

## AI news

Build a news section, an internal AI digest or an industry assistant with public articles, summaries, categories and source links. Synchronize updates and withdrawals.

![ScopeAI news interface, historical screenshot dated September 5, 2026](assets/news.png)

This is a historical product screenshot, not evidence that the paid API is already live.

## GEO detection

Observe whether model answers mention or explicitly recommend a brand. Use source evidence, model-answer sampling and historical results to build brand reports and monitoring tools.

![Lutule brand visibility case, visualization of verified September 7, 2026 results](assets/lutule-geo.png)

**Lutule case:** 2 mentions and 2 explicit recommendations across 11 natural questions; score 18.2/100. This visualization uses verified historical results; it is not a UI screenshot. It is a single small-sample observation, not a stable industry ranking or a measure of product quality or market share, and does not imply brand endorsement.

The historical website case used DeepSeek with web search enabled. The first paid API sampling target uses the **DeepSeek model API with search disabled**, not its consumer website or app. It does not promise to reproduce these scores. Public-source research is a separate service, not measured multi-platform visibility. See [visual provenance and scope](docs/showcase.md).

## Hosted and prepaid

| Service | Initial price preview |
| --- | --- |
| News | CNY 0.01 / nonempty successful request, up to 50 summaries; article detail billed separately |
| Public-source research | CNY 1.00 / fully delivered run |
| Model-answer sampling | CNY 1.00 / successful question × repetition unit |
| Scheduled monitoring | Actual services delivered, with separate authorization and a monthly budget |

Create an [account](https://camcat.net/login?mode=register), confirm availability with [support](https://camcat.net/account/billing), fund your balance, authorize an API key and set spending limits. Funding currently uses support-assisted confirmation. Final prices and availability come from the service.

GEO reserves the maximum quote, charges successful deliveries and releases failed portions. Valid retries using the same request key do not create duplicate charges. A valid answer that does not mention your brand is still billable. Read [billing rules](docs/pricing.md).

This repository publishes integration documentation, visuals and client examples. **The backend, data collection, news database, GEO analysis engine and billing implementation remain private.** Downloading the repository does not grant data access or model credits; paid operations require an enabled product, prepaid balance and an API key authorized to spend.

[Quick start](docs/getting-started.md) · [OpenAPI](openapi.json) · [Python](examples/python/quickstart.py) · [TypeScript](examples/typescript/scope-client.ts) · [Request access](https://camcat.net/developers)
