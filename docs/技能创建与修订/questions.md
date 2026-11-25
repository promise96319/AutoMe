# 1 未决问题

## 1.1 create-skill 中记为 TODO 的规则

按你的要求，拆分后暂时没有内容的规则先记为 TODO，遇到实际情况后再补充：

| 文件 | TODO |
| --- | --- |
| `references/flowchart.md` | 命令行校验脚本（目前在浏览器中查看校验结果） |
| `references/writing.md` | references、scripts、assets 的拆分规则 |
| `references/walkthrough.md` | 交给子代理走查时的任务说明模板 |

## 1.2 流程页模板的后续调整

- **现状**：流程页已改为固定模板 `skills/create-skill/assets/flow-template.html`，AI 只需填写流程数据。create-skill 自己的 `flow.html` 由模板生成，并且通过了校验；它导出的文字版就是现在的 SKILL.md。
- **待定**：模板目前是简单版，还没有示例走查和文件结构视图，视觉也还没有最终确认。

## 1.3 create-skill 自己的触发描述与同类 skill 重叠

- **现状**：环境里的 `developing-skills`、`superpowers:writing-skills`、`anthropic-skills:skill-creator` 也会被“新建或修改 skill”触发，现在的触发描述没有写出区别。
- **可选做法**：在描述中写出区别，或者在环境中停用其他几个。

## 1.4 遗留文件

`steps/01-触发描述与主流程图/` 下还有以下文件，等你确认后删除或保留：
- 另一个会话留下的 `create-skill-流程审查.html`、`create-skill-主流程.svg`，以及与现在做法不一致的 `流程图绘制规则.md`；
- 被取消的 Codex 任务留下的 `create-skill-流程-g6版.html`，可能没有完成；
- 多个流程页候选版本，以及 v1、v2 两个备份。这些都已被固定模板取代。
