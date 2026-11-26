# 生成流程图

画流程图时，按以下顺序把 skill 的流程和规则做成流程图 `skill-workflow.html`：先推出流程，再填写流程数据，最后校验。用户确认后的流程图是写 SKILL.md 的唯一依据，流程图上的每一句都必须是 SKILL.md 的原文。

## 1. 怎么画

- 先以需求方案中的实例为线索，从输入一路推到交付结果，画出主线；再挑一两个会走不同路线的情况推一遍，例如输入缺失、中途失败、用户否决，补上分支。
- 修订时，如果原 skill 没有 `skill-workflow.html`，先把它的 SKILL.md 如实还原成流程，标出原文含糊或自相矛盾的地方，再修改受影响的部分，并在交给用户时说明改动。
- 画完后，用实例沿流程走一遍，确认能到达期望的结果。

## 2. 填写流程数据

流程图由固定的模板生成：把模板复制到目标 skill 的目录下，命名为 `skill-workflow.html`，只替换 `FLOW_DATA_START` 与 `FLOW_DATA_END` 两行标记之间的内容，写成一个 `const FLOW = {……}` 对象。布局、样式、校验和文字版导出都由模板完成，不得修改模板的其他部分；`RES_CONTENT_START` 与 `RES_CONTENT_END` 之间存放引用文件的内容，不得手动填写。

FLOW 的字段：

| 字段 | 内容 |
| --- | --- |
| `name`、`description` | 名称和触发描述 |
| `summary` | 一段话说明这个 skill 做什么、交付什么 |
| `globalRules` | 全局约束，每条一句话；没有就写空数组 |
| `resources` | 正文引用的 references、scripts、assets 文件，每项写 `path`、`title`、`purpose`；脚本另写 `input`、`output` 和 `steps`（核心处理步骤的数组），供审阅者了解脚本做什么 |
| `steps` | 步骤数组，见下文 |

步骤分两种：父步骤写成 `{ id, title, children: [子步骤……] }`；直接包含指令的步骤写成 `{ id, title, body: [指令……], next, rules }`，其中 `next` 是指令执行完后的去向，`rules` 是这一步的约束，都可以省略。

指令和流程指令都是带 `type` 的对象：

| type | 字段 | 含义 |
| --- | --- | --- |
| `do` | `text` | 执行指令 |
| `decide` | `text`、`branches` | 判断指令 |
| `ask` | `text`、`branches` | 提问指令；写在分支里、问完按回复继续的提问，可以不写 `branches` |
| `check` | `text`、`items` | 带清单的指令，`items` 是清单项 |
| `goto` | `to`、`text` | 进入或回到步骤 `to`；`text` 写到那里做什么，可以省略。页面按步骤的先后，自动写成“进入”或“回到” |
| `retry` | `text` | 在本步骤内重做，导出为“然后……” |
| `end` | `text` | 结束，写明交付什么或要告诉用户什么，并包含“结束本次任务” |

分支写成 `{ when, then: [……] }`：`when` 是完整的条件；`then` 是命中后依次执行的指令，可以包含流程指令。

填写要求：

- `text` 写 SKILL.md 中的完整原句，但不带句末标点，标点由导出时补上；不另写简短名称、摘要或简化版。
- 引用文件时，用反引号写出路径，例如 `` `references/foo.md` ``，并在 `resources` 中登记。

示例：

```js
{ id: '1.2', title: '读懂要修订的 skill', body: [
  { type: 'decide', text: '读取要修订的 skill，写清它现在的表现和期望的表现', branches: [
    { when: '找不到这个 skill', then: [
      { type: 'ask', text: '询问用户是否改为新建，并给出建议', branches: [
        { when: '用户同意', then: [{ type: 'goto', to: '1.3' }] },
        { when: '用户不同意', then: [{ type: 'end', text: '结束本次任务' }] },
      ] },
    ] },
  ] },
], next: { type: 'goto', to: '1.4' } }
```

## 3. 校验

在浏览器中打开 `skill-workflow.html`：顶部显示“结构校验通过”才算完成；未通过时，按页面列出的问题逐条修改。
