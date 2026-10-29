# Finovo — Telegram Finance Tracker

> `[PERSONAL PROJECT]` · Live Telegram bot · Public source code

**Try it:** [@finovo_tracker_bot](https://t.me/finovo_tracker_bot) · **Source:** [GitHub repository](https://github.com/saltsnuff2204/finovo-telegram-finance-tracker)

## Product

Finovo is a personal-finance tracker that lets a user record income and expenses directly in Telegram instead of filling out a separate spreadsheet or form.

## What it does

- Records an expense or income from a short chat message, for example `coffee 1200` or `+ salary 450000`.
- Supports entries in KZT and USD.
- Confirms the recorded transaction in chat and keeps a readable description/category context.
- Shows summaries for today and the current month through `/today` and `/month`.
- Supports personal finance tracking for goals, debts, and credits through the bot and its companion app flow.

## Product thinking

The core idea is to reduce the friction of expense tracking: a user can capture a purchase in the same chat app they already use, then return later for a daily or monthly overview.

## Technical evidence

The public repository documents the implementation with Next.js, React, TypeScript, Cloudflare D1, Drizzle ORM and a Telegram Mini App flow. It includes automated checks for statement import, PDF parsing and Telegram webhook deduplication, plus a GitHub Actions quality workflow.

## Public demo boundary

The public demo includes the Telegram bot and source repository. Neither contains user transactions, financial records, database exports, source tokens, private logs, or production deployment identifiers. The repository image uses a synthetic `Демо` account with zero balances.

## Scope

Finovo is presented as a personal project and live product demo. No claim is made here about payment processing, bank integration, financial advice, or handling other users' private financial data.
