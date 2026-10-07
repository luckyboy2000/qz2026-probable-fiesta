import json
import os


def analyze_log(filepath: str) -> dict:

    # 初始化结果结构
    result = {
        "total": 0,
        "by_level": {},
        "by_user": {},
        "last_error": None
    }

    # 检查文件是否存在，不存在直接返回空结果
    if not os.path.exists(filepath):
        return result

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                # 解析JSON
                try:
                    log_entry = json.loads(line)
                except json.JSONDecodeError:
                    continue

                # 更新统计
                result["total"] += 1

                level = log_entry.get("level")
                user = log_entry.get("user")
                message = log_entry.get("message")

                # level
                if level:
                    if level in result["by_level"]:
                        result["by_level"][level] += 1
                    else:
                        result["by_level"][level] = 1

                # user
                if user:
                    if user in result["by_user"]:
                        result["by_user"][user] += 1
                    else:
                        result["by_user"][user] = 1

                # 最后一条ERROR
                if level == "ERROR":
                    result["last_error"] = message

    except Exception:
        pass

    return result
