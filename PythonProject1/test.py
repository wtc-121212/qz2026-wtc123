from main import analyze_log


# 正常文件
result = analyze_log("app.jsonl")
print(result)

assert result["total"] == 5
assert result["by_level"]["INFO"] == 3
assert result["by_level"]["ERROR"] == 2
assert result["by_user"]["张三"] == 2
assert result["by_user"]["李四"] == 2
assert result["by_user"]["王五"] == 1
assert result["last_error"] == "超时"

print("正常文件测试通过")


# 文件不存在
result = analyze_log("not_exist.jsonl")

assert result["total"] == 0
assert result["by_level"] == {}
assert result["by_user"] == {}
assert result["last_error"] is None

print("文件不存在测试通过")


# 空文件
result = analyze_log("empty.jsonl")

assert result["total"] == 0
assert result["by_level"] == {}
assert result["by_user"] == {}
assert result["last_error"] is None

print("空文件测试通过")


# 有错误 JSON 的文件
result = analyze_log("bad.jsonl")

assert result["total"] == 2
assert result["by_level"]["ERROR"] == 1
assert result["by_level"]["INFO"] == 1
assert result["last_error"] == "失败"

print("错误 JSON 测试通过")


print("全部测试通过")