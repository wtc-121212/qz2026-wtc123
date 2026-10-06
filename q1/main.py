import json


def analyze_log(filepath: str) -> dict:
    result = {
        "total": 0,
        "by_level": {},
        "by_user": {},
        "last_error": None
    }

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()

                if not line:
                    continue

                try:
                    data = json.loads(line)
                except json.JSONDecodeError:
                    continue

                if not all(key in data for key in ["timestamp", "level", "message", "user"]):
                    continue

                result["total"] += 1

                level = data["level"]
                user = data["user"]

                if level in result["by_level"]:
                    result["by_level"][level] += 1
                else:
                    result["by_level"][level] = 1

                if user in result["by_user"]:
                    result["by_user"][user] += 1
                else:
                    result["by_user"][user] = 1

                if level == "ERROR":
                    result["last_error"] = data["message"]

    except FileNotFoundError:
        return result

    return result