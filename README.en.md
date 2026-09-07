# ScopeAI API

AI news data and brand observation for your applications.

[中文介绍](README.md) · [Developer portal](https://camcat.net/developers) · [Create an account](https://camcat.net/login?mode=register)

**Integration preview.** Paid news and GEO features have completed development and local validation. Production activation is pending. Confirm availability with ScopeAI before funding an account. See [service status](docs/status.md).

## What you can build

- AI news feeds for websites and apps, with public articles, images and source links.
- Internal industry digests and content synchronization with update and withdrawal events.
- Public-source brand research with verified source text and content suggestions.
- Brand mention reports based on actual answers from the DeepSeek model API.
- Separately authorized daily or weekly monitoring with spending limits.

## Hosted, prepaid service

This repository contains client examples and API documentation. Data delivery, research execution and billing run on the ScopeAI hosted service. Paid operations require an account, an enabled product, prepaid balance and an API key authorized to spend.

Initial price preview: CNY 0.01 per nonempty successful news request (up to 50 summaries); CNY 1.00 per completed research run; CNY 1.00 per successful model-answer unit. Final availability and quotes come from the service. Failed GEO units release their reserved amount; identical request retries do not create another charge.

Registration, developer access and billing are available at [camcat.net](https://camcat.net). Funding currently uses support-assisted confirmation, not automated card or wallet checkout.

[Quick start](docs/getting-started.md) · [OpenAPI](openapi.json) · [Python](examples/python/quickstart.py) · [TypeScript](examples/typescript/scope-client.ts)

Public-source research is not measured visibility across AI platforms. DeepSeek model API sampling does not represent its consumer website or app. This repository does not include the hosted backend, source datasets or provider credentials.
