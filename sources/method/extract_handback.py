import sys, json
path, out = sys.argv[1], sys.argv[2]
msg = None
for line in open(path):
    try: d = json.loads(line)
    except Exception: continue
    m = d.get("message")
    if isinstance(m, dict) and isinstance(m.get("content"), list):
        for b in m["content"]:
            if b.get("type") == "tool_use" and b.get("name") == "SubagentHandback":
                msg = b["input"]["message"]
if msg is None: sys.exit(f"no handback in {path}")
open(out, "w").write(msg.rstrip() + "\n")
