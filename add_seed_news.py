# -*- coding: utf-8 -*-
"""向 daily.json 与 js/daily.js 注入狗/猪/鱼的种子资讯（新到旧排在最前）。"""
import json, os, re

BASE = r"D:\ai练手\鸡与猴"

seed = [
    {"date": "2026-08-11", "emoji": "🐶", "category": "狗",
     "title": "研究揭示家犬能区分人类语调与真实情绪",
     "body": "多项认知实验显示，狗不仅能听懂指令词汇，还能结合人类语调与面部表情判断情绪真假，并做出差异化回应。这种跨模态情绪辨识能力，是万年共生中逐步演化出的「读人」专长。"},
    {"date": "2026-08-10", "emoji": "🐶", "category": "狗",
     "title": "城市文明养犬新规倡导牵绳与粪便清理",
     "body": "多地升级养犬管理条例，明确携犬出户须束犬链、即时清理排泄物，并推广犬只电子标识。规范养犬既保障公共安全，也减少人与犬的冲突，营造更友好的城市共处环境。"},
    {"date": "2026-08-09", "emoji": "🐶", "category": "狗",
     "title": "工作犬在搜救与医疗辅助中持续立功",
     "body": "从地震坍塌现场的生命探测，到癫痫预警犬对发作前的异常嗅探，工作犬凭借敏锐感官与稳定性格，在灾害救援、医疗陪伴等场景中发挥着不可替代的作用。"},

    {"date": "2026-08-11", "emoji": "🐷", "category": "猪",
     "title": "异种器官移植研究以猪为模型取得进展",
     "body": "因猪的器官大小与人类相近，科学家通过基因编辑降低免疫排斥，推动猪—人异种移植走向临床。此举有望缓解供体器官短缺，为终末期患者带来新的希望。"},
    {"date": "2026-08-10", "emoji": "🐷", "category": "猪",
     "title": "地方黑猪种质资源保护初见成效",
     "body": "针对本土黑猪生长慢、数量少的状况，多地建立保种场与基因库，结合生态放养恢复风味与种群。保护和开发并举，让优质地方猪种免于基因单一化风险。"},
    {"date": "2026-08-09", "emoji": "🐷", "category": "猪",
     "title": "仔猪腹泻新型疫苗获批推广",
     "body": "针对危害仔猪成活率的病毒性腹泻，新获批疫苗可经母猪免疫传递母源抗体，显著提升哺乳仔猪保护率，有望降低养殖损耗、稳定猪肉供给。"},

    {"date": "2026-08-11", "emoji": "🐟", "category": "鱼",
     "title": "长江十年禁渔鱼类资源恢复迹象明显",
     "body": "禁渔实施数年来，长江干流及重点湖泊的鱼类物种数、个体规格均呈回升态势，江豚频现。退捕渔民转产安置与生态补偿并行，印证「共抓大保护」的路径可行。"},
    {"date": "2026-08-10", "emoji": "🐟", "category": "鱼",
     "title": "深海新鱼种在科考中现身",
     "body": "载人深潜与遥控潜器在数千米深渊采集到形态奇特的新鱼种，其适应高压、低温与黑暗的生理机制，为生命极限研究提供了珍贵样本。"},
    {"date": "2026-08-09", "emoji": "🐟", "category": "鱼",
     "title": "智慧渔场实现投喂与水质监测自动化",
     "body": "基于传感器与算法的陆基循环水养殖系统，可实时调节溶氧、水温与投饵量，在节水节地同时提升成活率和品质，推动水产养殖向精细化转型。"},
]

def insert_json():
    p = os.path.join(BASE, "daily.json")
    with open(p, "r", encoding="utf-8") as f:
        data = json.load(f)
    # 去重（按 title）后前插
    existing = {d.get("title") for d in data}
    fresh = [s for s in seed if s["title"] not in existing]
    merged = fresh + data
    with open(p, "w", encoding="utf-8") as f:
        json.dump(merged, f, ensure_ascii=False, indent=2)
    print("daily.json: +%d 条 -> 共 %d 条" % (len(fresh), len(merged)))

def insert_js():
    p = os.path.join(BASE, "js", "daily.js")
    with open(p, "r", encoding="utf-8") as f:
        txt = f.read()
    # 在 window.DAILY_NEWS = [ 之后插入
    anchor = "window.DAILY_NEWS = ["
    assert txt.count(anchor) == 1, "anchor 不唯一"
    # 构造 JS 对象文本
    def js_obj(s):
        return (
            "  {\n"
            '    date: "%s",\n'
            '    emoji: "%s",\n'
            '    category: "%s",\n'
            '    title: "%s",\n'
            '    body: "%s"\n'
            "  },\n" % (s["date"], s["emoji"], s["category"], s["title"], s["body"])
        )
    block = "\n" + "".join(js_obj(s) for s in seed)
    txt = txt.replace(anchor, anchor + block, 1)
    with open(p, "w", encoding="utf-8") as f:
        f.write(txt)
    print("js/daily.js: 前插 %d 条种子资讯" % len(seed))

insert_json()
insert_js()
print("OK")
