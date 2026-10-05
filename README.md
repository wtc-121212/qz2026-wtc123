# qz2026-wtc123

这是用于提交一次考核题目答案的仓库。

## 目录结构

```text
qz2026-wtc123/
├── README.md
├── .gitignore
├── written.md
├── q2/
│   ├── README.md
│   └── solution.py
├── q3/
│   ├── README.md
│   └── solution.py
└── project/
    ├── README.md
    ├── requirements.txt
    └── main.py
```

## 说明

- `written.md`：选择题 + 简答题答案
- `q2/`：编程题 2
- `q3/`：编程题 3
- `project/`：难题项目说明、依赖和运行方式

## 提交要求

1. 简单题与中等题直接提交到 `main` 分支
2. 建议每题或每小步保留一次过程性提交
3. 难题项目建议在功能分支中开发，完成后通过 Pull Request 合并回 `main`
4. 不要使用 `force push` 改写已推送历史
5. 不得提交 `__pycache__/`、`venv/`、`.idea/` 等无关产物

## 分支与目录的区别

- `written.md`、`q2/`、`q3/`、`project/` 是仓库中的文件和目录
- `main`、`feature/project` 等才是 Git 分支

因此，不需要用 `written`、`q2` 等名字创建分支，直接按目录结构来提交即可。
