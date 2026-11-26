#!/usr/bin/env python3
"""把流程图中登记的引用文件内容写入 skill-workflow.html。

用法：python3 embed-resources.py <skill-workflow.html 的路径>

读取 FLOW_DATA_START 与 FLOW_DATA_END 之间登记的 resources 路径，
按相对于 skill-workflow.html 所在目录的位置读取文件，
把内容写入 RES_CONTENT_START 与 RES_CONTENT_END 之间。
有文件找不到时，列出这些文件并以状态 1 退出。
"""
import json
import re
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) != 2:
        print("用法：python3 embed-resources.py <skill-workflow.html 的路径>")
        return 2

    page = Path(sys.argv[1])
    text = page.read_text(encoding="utf-8")

    data = re.search(r"/\* FLOW_DATA_START.*?/\* FLOW_DATA_END \*/", text, re.S)
    block = re.search(r"(/\* RES_CONTENT_START[^\n]*\n)(.*?)(\n/\* RES_CONTENT_END \*/)", text, re.S)
    if not data or not block:
        print("没有找到 FLOW_DATA 或 RES_CONTENT 标记，请确认页面由模板生成。")
        return 2

    paths = re.findall(r"""path:\s*['"]([^'"]+)['"]""", data.group(0))
    content, missing = {}, []
    for rel in paths:
        file = page.parent / rel
        if file.is_file():
            content[rel] = file.read_text(encoding="utf-8")
        else:
            missing.append(rel)

    # 把 < 转义，避免文件中的 </script>、<!-- 等片段打断页面脚本
    blob = json.dumps(content, ensure_ascii=False).replace("<", "\\u003c")
    text = text[: block.start(2)] + "const RES_CONTENT = " + blob + ";" + text[block.end(2):]
    page.write_text(text, encoding="utf-8")

    print(f"已写入 {len(content)} 个文件的内容。")
    for rel in missing:
        print(f"未找到：{rel}")
    return 1 if missing else 0


if __name__ == "__main__":
    sys.exit(main())
