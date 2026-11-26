# 1 未决问题

## 1.1 create-skill 尚未补充的部分

这两项不写进交付的文件，等遇到实际需要时再补充：

- 命令行的结构校验：目前在浏览器中打开 `skill-workflow.html` 查看校验结果。
- 交给子代理走查时的任务说明模板：目前 `references/walkthrough.md` 只写了交给子代理时提供什么、不提供什么。

## 1.2 create-skill 自己的触发描述与同类 skill 重叠

- **现状**：环境里的 `developing-skills`、`superpowers:writing-skills`、`anthropic-skills:skill-creator` 也会被“新建或修改 skill”触发，现在的触发描述没有写出区别。
- **可选做法**：在描述中写出区别，或者在环境中停用其他几个。

## 1.3 遗留文件

`steps/01-触发描述与主流程图/` 下还有以下文件，等你确认后删除或保留：
- 另一个会话留下的 `create-skill-流程审查.html`、`create-skill-主流程.svg`，以及与现在做法不一致的 `流程图绘制规则.md`；
- 被取消的 Codex 任务留下的 `create-skill-流程-g6版.html`，可能没有完成；
- 多个流程页候选版本、v1 和 v2 两个备份，以及作为模板样式来源的 `create-skill-流程-shadcn版.html`。这些都已被固定模板取代。
