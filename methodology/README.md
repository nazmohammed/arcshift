# Arcshift Methodology

A structured, Copilot-driven approach to application modernisation delivered in five phases.

## Phases

```
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  01 Discover │───▶│  02 Design  │───▶│  03 Migrate │───▶│ 04 Validate │───▶│  05 Deploy  │
│   & Assess   │    │ Architecture│    │    Code      │    │   & Test    │    │  to Azure   │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
     @assess          @architect         @migrate          @validate          @deploy
```

## Phase Overview

| Phase | Agent | Input | Output | Duration Guide |
|-------|-------|-------|--------|---------------|
| [01 Discover & Assess](01-discover/README.md) | `@assess` | Legacy codebase | Assessment report (JSON) | 1-2 days |
| [02 Design Architecture](02-design/README.md) | `@architect` | Assessment report | ADRs + service map | 2-3 days |
| [03 Migrate Code](03-migrate/README.md) | `@migrate` | ADRs + source code | Modernised codebase | 1-4 weeks |
| [04 Validate & Test](04-validate/README.md) | `@validate` | Modernised code | Parity report + test suite | 3-5 days |
| [05 Deploy to Azure](05-deploy/README.md) | `@deploy` | Validated code | IaC + CI/CD + deployed app | 2-3 days |

## How It Works

Each phase is powered by a dedicated Copilot agent with specialised skills:

1. **Invoke the agent** — Use `@assess`, `@architect`, `@migrate`, `@validate`, or `@deploy` in Copilot Chat
2. **Agent loads skills** — The agent automatically loads relevant SKILL.md files for domain knowledge
3. **Instructions apply** — File-scoped `.instructions.md` files guide code generation patterns
4. **Prompts accelerate** — Pre-built `.prompt.md` templates handle common tasks with parameters

## Engagement Model

### For SI/Partners

1. Fork this repository
2. Copy the legacy application into `samples/{client-name}/before/`
3. Walk through each phase sequentially with the client
4. Customise agents and skills for client-specific technology stacks
5. Deliver the modernised application in `samples/{client-name}/after/`

### For Direct Use

1. Clone this repository alongside your legacy codebase
2. Start with `@assess` to generate the assessment report
3. Follow the methodology phase by phase
4. Each phase produces artefacts that feed into the next

## Principles

- **Copilot-first**: Every phase is designed for AI-assisted execution
- **Evidence-based**: Decisions are backed by assessment data and ADRs
- **Incremental**: Modernise service by service, not big-bang
- **Reversible**: Strangler fig pattern ensures rollback capability
- **Cloud-native**: Target architecture is Azure-optimised from day one
