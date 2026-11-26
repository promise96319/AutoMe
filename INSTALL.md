# 安装 AutoMe

把这份文件交给正在使用的 AI，告诉它「按 INSTALL.md 安装 AutoMe」即可。默认安装 Git 提交规范和 Diff 展示规范，供当前 AI 在你的各个项目中使用。也可以点名要装的内容，例如「只给 Codex 安装 Diff 展示规范」。

## 1 选择安装项

| 安装项 | 用途 | 仓库源文件 | 安装方式 |
| --- | --- | --- | --- |
| Git 提交规范 | 约定提交范围、提交说明和推送时机 | [rules/git-commit.md](rules/git-commit.md) | 默认 |
| Diff 展示规范 | 查看改动时按文件逐行对照修改前后的内容 | [rules/show-diff.md](rules/show-diff.md) | 默认 |
| `create-skill` | 指导 AI 创建或修订 skill | [skills/create-skill/](skills/create-skill/) | 按需 |

用户点名时只安装所选项。未指定 AI 时，使用当前 AI 的用户级配置。用户指定多个 AI 时，分别接入。

## 2 取得源文件

表中的路径都相对于 AutoMe 仓库根目录。手上有本地 AutoMe 时直接从中读取。只有这份说明时，从 [promise96319/AutoMe](https://github.com/promise96319/AutoMe) 取得仓库，再按清单取用文件。如果所用版本缺少某项，说明缺少的路径，并请用户提供包含它的版本或本地目录。

## 3 安装与核对

| 目标 AI | 用户级指令入口 | 个人 skill 目录 |
| --- | --- | --- |
| Codex | `~/.codex/AGENTS.md` | `~/.agents/skills/` |
| Claude Code | `~/.claude/CLAUDE.md` | `~/.claude/skills/` |

表中是默认路径。Codex 的指令入口位于 `CODEX_HOME`（默认 `~/.codex/`），该目录中非空的 `AGENTS.override.md` 优先。Claude Code 设置了 `CLAUDE_CONFIG_DIR` 时，使用该配置目录。详见 [Codex 指令](https://developers.openai.com/codex/guides/agents-md/)、[Codex skills](https://developers.openai.com/codex/skills/)、[Claude Code 指令](https://code.claude.com/docs/en/memory)和 [Claude Code skills](https://code.claude.com/docs/en/skills)。

**规范文件。** 将每条选中的规范按原文件名复制到 `~/.config/autome/rules/`，创建缺少的目录。多个 AI 共用同一份规范。在每个选中 AI 的用户级指令文件末尾，分别加入所选规范对应的一行。

| 规范 | 写入的指令 |
| --- | --- |
| Git 提交规范 | 创建 Git 提交或推送前，读取并遵循 `~/.config/autome/rules/git-commit.md`。当前仓库有明确约定时，以仓库约定为准。 |
| Diff 展示规范 | 用户要求查看 diff 或对比修改前后时，读取并遵循 `~/.config/autome/rules/show-diff.md`，按文件展示逐行差异。 |

已有相同引用时跳过追加，保留文件中的其他指令。核对每条选中的规范与源文件内容一致，且每个选中的指令入口都包含对应引用。

**create-skill。** 将整个 `skills/create-skill/` 目录复制到所选 AI 的个人 skill 目录下，使其入口为 `<个人 skill 目录>/create-skill/SKILL.md`。核对目录中的文件与源目录一致，包括 `references/`、`assets/`、`scripts/` 和 `skill-workflow.html`。

再次安装时，内容一致的项跳过，已有的 AutoMe 副本就地更新。遇到来源不明的同名文件或需要保留的本地改动时，先向用户指出差异。完成后列出本次新增、更新或已是最新的项及其本地路径。
