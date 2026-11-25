# AutoMe

AutoMe 收集我在开发中反复用到的 AI skills 和工作规范。目前可以让 Codex 或 Claude Code 帮你创建和修订 skill、按约定提交代码，以及逐行审阅改动。安装到个人配置后，换一个项目也能继续用。

## 1 能力一览

| 能力 | 可以这样对 AI 说 | AI 会怎么做 | 安装方式 |
| --- | --- | --- | --- |
| [Git 提交规范](rules/git-commit.md) | “把这次解析器修复提交一下。” | 核对暂存差异，只提交这次修复，按仓库约定写提交说明。Codex 参与时附共同作者署名。说“提交并推送”时，再核对远程分支并推送。 | 默认 |
| [Diff 展示规范](rules/show-diff.md) | “只看解析器的改动，给我 diff。” | 按文件展示修改前后的行号和上下文。优先使用红删绿增的原生差异视图，在聊天里用标准 `diff` 代码块对照。 | 默认 |
| [create-skill](skills/create-skill/SKILL.md) | “把我写发布说明的做法整理成一个 skill。” | 明确触发场景和交付结果，画出流程图供你确认，再编写 `SKILL.md` 并用实例走查。也可以用它修改已有 skill 的触发条件、步骤或规则。 | 按需 |

## 2 快速安装

把下面这句话发给正在使用的 Codex 或 Claude Code，即可安装两条默认规范。

```text
请按 https://github.com/promise96319/AutoMe/blob/main/INSTALL.md 安装 AutoMe。
```

如果三项都需要，可以说“按这份说明安装默认规范和 create-skill”。也可以只点名一项，例如“只安装 Diff 展示规范”。安装位置、更新方式和核对步骤见[安装说明](INSTALL.md)。

## 3 了解项目

在本仓库参与开发时，可以查阅[协作约定](AGENTS.md)。想了解 `create-skill` 的设计过程和当前进度，可以从[工作索引](docs/README.md)进入。
