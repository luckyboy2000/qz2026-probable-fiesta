import main


result = main.analyze_log("app.jsonl")

print(result["total"])
print(result["by_level"])
print(result["by_user"])
print(result["last_error"])