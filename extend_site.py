# -*- coding: utf-8 -*-
"""把狗/猪/鱼三个动物的科普内容扩展进 index.html（自包含单文件版）。"""
import os

BASE = r"D:\ai练手\鸡与猴"
HTML = os.path.join(BASE, "index.html")

# ============ 科普内容数据 ============
def C(icon, title, text, hl=False):
    return {"icon": icon, "title": title, "text": text, "hl": hl}

def B(emoji, name, origin, desc):
    return {"emoji": emoji, "name": name, "origin": origin, "desc": desc}

animals = {
"dog": {
  "emoji": "🐶", "name": "狗", "en": "狗的百科全书",
  "desc": "从荒野灰狼到人类最忠诚的伙伴，揭秘犬类的演化、品种、智慧与情感",
  "tabs": {
    "origin": [
      C("🧬","灰狼的后裔","狗由<strong>灰狼</strong>（Canis lupus）驯化而来，是所有家犬的共同祖先。基因研究显示，狗与灰狼的相似度高达 99.9%。"),
      C("🌍","驯化时间","狗是人类<strong>最早驯化</strong>的动物，约在 1.5 万至 4 万年前。比农业的出现还早，堪称人类最古老的朋友。"),
      C("🏔️","驯化地点","主流研究认为狗可能在中东、东亚或欧洲多地独立驯化。中国南方出土的狗骨证明亚洲很早就有家犬。"),
      C("🤝","从猎伴到伙伴","最初狗帮助人类狩猎、警戒，后来逐渐成为看家护院、放牧和陪伴的伙伴，功能不断扩展。"),
      C("🧬","快速演化","与狼分家后，狗在短短万年间分化出<strong>数百个品种</strong>，是哺乳动物中形态差异最大的物种之一。"),
      C("🐺","仍保留狼性","狗虽然被驯化，但许多行为（如嚎叫、群体等级、领地意识）仍带着祖先灰狼的印记。"),
    ],
    "breeds": [
      B("🐕","拉布拉多寻回犬","加拿大纽芬兰","最 popular 的导盲和伴侣犬，性格温顺聪明，是检索水鸟的好手。"),
      B("🐶","德国牧羊犬","德国","警犬军犬首选，忠诚勇敢智商高，也常用于搜救和导盲。"),
      B("🦮","金毛寻回犬","苏格兰","友善耐心，是最受欢迎的家庭犬之一，常作为治疗犬和搜救犬。"),
      B("🐕","边境牧羊犬","英格兰苏格兰边界","智商最高的狗种，牧羊本能极强，学习指令极快。"),
      B("🐩","吉娃娃","墨西哥","体型最小的犬种，仅 1-3 公斤，性格勇敢警惕，适合公寓饲养。"),
      B("🐺","哈士奇","西伯利亚","雪橇犬，蓝眼厚毛耐力强，性格活泼但有点倔强搞笑。"),
      B("🐕","柯基","威尔士","短腿长身，原为牧牛犬，因英女王喜爱而全球闻名，活泼亲人。"),
      B("🐺","藏獒","青藏高原","体型巨大护主凶猛，历史上守护牛羊群，是著名的护卫犬。"),
    ],
    "biology": [
      C("👃","超凡嗅觉","狗的嗅觉受体约 <strong>3 亿个</strong>（人类仅 500 万），能分辨数万种气味，甚至嗅出癌症和低血糖。"),
      C("👂","敏锐听觉","狗能听到最高约 <strong>4.5 万赫兹</strong>的声音（人类约 2 万），能察觉远处脚步和超声波口哨。"),
      C("👁️","二色视觉","狗只有两种视锥细胞（二色视觉），看不到红绿色，但<strong>夜视能力</strong>远胜人类。"),
      C("👃","湿润的鼻子","狗鼻分泌黏液捕捉气味分子，<strong>鼻纹</strong>像指纹一样独一无二，可用于身份识别。"),
      C("🦴","牙齿与咬合","狗有 42 颗牙齿，咬合力因品种而异（藏獒可达数百公斤），适合撕咬和咀嚼。"),
      C("🐾","会出汗的脚垫","狗几乎没有汗腺，主要靠喘气和<strong>脚垫排汗</strong>散热，所以夏天脚垫会微微出汗。"),
    ],
    "behavior": [
      C("🐕","摇尾巴","摇尾巴不全是开心——右摇多表兴奋友好，左摇多表不安。尾巴是狗的「情绪显示器」。"),
      C("🗣️","吠叫沟通","狗用吠叫、呜咽、嚎叫表达不同情绪：警告、求关注、孤独或回应同类。"),
      C("🐺","群体等级","狗保留狼的等级观念，把主人视为「头领」，家庭内部也有微妙的地位排序。"),
      C("🧸","分离焦虑","狗是高度社会动物，独处过久会焦虑，表现为拆家、吠叫，需要从小适应独处。"),
      C("🎾","爱玩耍","游戏是狗学习和社交的方式，接飞盘、拔河能增进与主人的感情。"),
      C("🏠","领地意识","狗会标记并守护自己的领地，对陌生人警惕，这是祖先防御本能的遗留。"),
    ],
    "intelligence": [
      C("🧠","聪明的伙伴","狗的智力相当于 <strong>2-3 岁</strong>人类儿童，能理解约 100-300 个词语，边境牧羊犬更可学上千词。", True),
      C("🤚","读懂手势","狗擅长解读人类手势和眼神，甚至比黑猩猩更懂人的指向——这是万年共生的结果。"),
      C("🎓","工作犬","导盲犬、搜救犬、警犬、检疫犬……狗在各行各业协助人类，展现出极强的训练适应性。"),
      C("💞","情感共鸣","狗能感知主人情绪，主人悲伤时它会靠近安慰，双方压力激素水平也会随之变化。"),
      C("🧩","解决问题","实验显示狗能通过观察人类找到藏起的食物，甚至学会按按钮「说话」表达需求。"),
      C("🧠","左右偏好","研究发现狗也有「左撇子/右撇子」倾向，且偏好与性格和情绪相关。"),
    ],
    "culture": [
      C("🇨🇳","十二生肖","狗是中国十二生肖<strong>第十一位</strong>。属狗的人被认为忠诚、正直、可靠。"),
      C("🗿","忠犬八公","日本秋田犬八公每天到车站等已故主人，等待九年，成为忠诚的象征。"),
      C("🦮","导盲犬","上世纪起导盲犬帮助视障人士出行，是「无障碍」社会的重要伙伴。"),
      C("🐕","守护神兽","许多文化视狗为护家神，古埃及、古希腊都有狗形神祇。"),
      C("🎨","艺术常客","从拉斯科洞穴壁画到现代卡通（史努比、高飞），狗是艺术中的常青主题。"),
      C("🐺","狼的影子","神话中狗常与狼并提，既象征忠诚，也保留一丝野性的神秘。"),
    ],
  },
  "facts": [
    {"num":"01","text":"狗的<strong>鼻纹</strong>像人类指纹一样独一无二，可作为身份识别。"},
    {"num":"02","text":"狗能<strong>做梦</strong>——睡眠中会出现类似 REM 的阶段，可能梦到白天玩耍。"},
    {"num":"03","text":"一只狗的嗅觉细胞数量约为人类的 <strong>600 倍</strong>，能嗅出爆炸物与疾病。"},
    {"num":"04","text":"狗的听觉范围约 67-45000 赫兹，能听到人类听不到的高频声。"},
    {"num":"05","text":"「狗一岁等于人七岁」是粗略说法，实际<strong>小型犬衰老更慢</strong>。"},
    {"num":"06","text":"最古老的狗雕塑出土于中东，距今约 <strong>1.2 万年</strong>，证明早期人与狗亲密。"},
    {"num":"07","text":"狗能通过粪便、尿液气味判断其他狗的健康、性别和情绪。"},
    {"num":"08","text":"巴仙吉犬不会汪汪叫，只会发出类似约德尔唱法的「吠鸣」。"},
    {"num":"09","text":"狗的尾巴位置表达情绪：高举表自信，夹尾表恐惧或顺从。"},
    {"num":"10","text":"纽芬兰犬天生会游泳，脚有蹼，曾被称为「水上救援犬」。"},
    {"num":"11","text":"狗能学会按发声板拼出简单句子表达「玩耍」「外面」等需求。"},
    {"num":"12","text":"贵宾犬原是水猎犬，卷毛防水，如今是受欢迎的伴侣与表演犬。"},
  ],
  "daily": [
    {"date":"1月5日","emoji":"🐶","cat":"狗","title":"狗年说狗","body":"狗年每12年一轮，下一个狗年是2030年。属狗的人被认为忠诚可靠。"},
    {"date":"2月8日","emoji":"🐶","cat":"狗","title":"忠犬的嗅觉","body":"狗的嗅觉受体约3亿个，能嗅出癌症、低血糖甚至地震前的气味变化。"},
    {"date":"3月3日","emoji":"🐶","cat":"狗","title":"导盲犬","body":"导盲犬经严格训练后能帮助视障人士安全出行，是「无障碍社会」的重要伙伴。"},
    {"date":"4月4日","emoji":"🐶","cat":"狗","title":"狗的听觉","body":"狗能听到高达4.5万赫兹的声音，远超人类的2万赫兹，可听见超声波哨。"},
    {"date":"5月5日","emoji":"🐶","cat":"狗","title":"边境牧羊犬","body":"边境牧羊犬被广泛认为是最聪明的犬种，能学会上千个词汇与指令。"},
    {"date":"6月6日","emoji":"🐶","cat":"狗","title":"搜救犬","body":"搜救犬在地震、塌方中搜寻幸存者，是灾难救援中不可或缺的「四脚英雄」。"},
    {"date":"7月7日","emoji":"🐶","cat":"狗","title":"狗的鼻纹","body":"狗的鼻纹像指纹一样独一无二，已被用于宠物身份识别与寻找走失犬。"},
    {"date":"8月8日","emoji":"🐶","cat":"狗","title":"八公的等待","body":"日本忠犬八公在主人去世后仍每天到车站等候九年，成为忠诚的永恒象征。"},
    {"date":"9月9日","emoji":"🐶","cat":"狗","title":"狗的情绪","body":"研究发现狗能感知主人情绪，主人悲伤时它会靠近安慰，二者压力激素会同步变化。"},
    {"date":"10月10日","emoji":"🐶","cat":"狗","title":"工作犬","body":"从警犬、检疫犬到治疗犬，狗在人类社会的多个岗位发挥独特作用。"},
    {"date":"11月11日","emoji":"🐶","cat":"狗","title":"狗的梦","body":"狗睡眠中会出现类似 REM 的阶段，脑电图显示它们可能在做梦，常伴随轻颤与呜咽。"},
    {"date":"12月12日","emoji":"🐶","cat":"狗","title":"年度回顾","body":"从1.5万年前的灰狼驯化到今天数百个品种，狗是人类最古老也最忠诚的朋友。"},
  ],
  "quiz": [
    {"q":"狗的祖先是哪种动物？","options":["灰狼","狐狸","猫","熊"],"answer":0,"explain":"狗由灰狼（Canis lupus）驯化而来，基因相似度高达 99.9%。"},
    {"q":"狗能看到红绿灯的红色吗？","options":["能","不能，狗是二色视觉","能但很模糊","只有晚上能"],"answer":1,"explain":"狗只有两种视锥细胞（二色视觉），难以区分红绿色，但夜视更好。"},
    {"q":"狗的嗅觉受体约有多少？","options":["5百万","3千万","3亿","30亿"],"answer":2,"explain":"狗的嗅觉受体约 3 亿个，是人类的约 600 倍，能分辨数万种气味。"},
  ],
},
"pig": {
  "emoji": "🐷", "name": "猪", "en": "猪的百科全书",
  "desc": "从野猪到餐桌与萌宠，重新认识被低估的「聪明猪」：演化、品种、智慧与福气象征",
  "tabs": {
    "origin": [
      C("🧬","野猪驯化","家猪的祖先是<strong>野猪</strong>（Sus scrofa），约 9000 年前在多个地区被人类驯化。"),
      C("🌍","多地独立驯化","考古显示，近东（安纳托利亚）和中国约在 9000 年前各自独立驯化野猪。"),
      C("🐗","从野到家","驯化让猪的獠牙变小、性情变温顺、体脂增加，成为高效产肉的家畜。"),
      C("🇨🇳","中国的猪","中国是世界上最早养猪的国家之一，养猪史超过<strong>八千年</strong>，是农耕文明的重要部分。"),
      C("🌾","杂食天性","猪是杂食动物，能吃草根、果实、昆虫、厨余，这种食性让它们极易饲养。"),
      C("🔄","往返演化","有研究称部分家猪逃入野外会「野化」重回野猪状态，展现极强的适应力。"),
    ],
    "breeds": [
      B("🐷","大白猪（大约克夏）","英国","世界主流瘦肉型猪种，生长快、饲料转化率高，用于杂交育种。"),
      B("🐽","长白猪（兰德瑞斯）","丹麦","体型修长、瘦肉率高，著名的「流水线」瘦肉猪，全球广泛养殖。"),
      B("🐷","杜洛克","美国","红棕色、长势好、肉质佳，常作父本与瘦肉型母猪杂交。"),
      B("🐽","巴克夏","英国","黑猪白蹄，肉质细嫩风味好，是高端猪肉的代表品种。"),
      B("🐷","藏猪（藏香猪）","中国西藏","高原放养的小型黑猪，肉质紧实香味浓，被称为「高原之珍」。"),
      B("🐽","香猪（微型猪）","中国西南","体型小巧可作宠物，也用于医学实验，成年仅数十斤。"),
      B("🐷","约克夏","英国","白猪始祖之一，大白猪的前身，肉质与繁殖性能俱佳。"),
      B("🐽","梅山猪","中国江苏","著名高产母猪，一胎可产十几头，繁殖力惊人。"),
    ],
    "biology": [
      C("👃","惊人嗅觉","猪的嗅觉极其灵敏，能嗅出埋在地下的松露，嗅觉能力<strong>不输于狗</strong>。"),
      C("🧠","发达大脑","猪的大脑相对体型较大，神经结构复杂，认知能力与狗、黑猩猩相当。"),
      C("🐽","多功能的鼻","猪的鼻子（吻突）坚韧灵活，用来拱土觅食、探查环境，是主要工具器官。"),
      C("💦","无汗腺","猪几乎不出汗，靠<strong>泥浴和打滚</strong>散热，所以常看到猪在泥里打滚——那是在「降温洗澡」。"),
      C("🐷","多仔高产","母猪一胎通常产 <strong>8-14 头</strong>仔猪，是繁殖力最强的家养哺乳动物之一。"),
      C("👁️","色觉有限","猪的视觉一般，主要辨灰色调，但运动感知和空间记忆很好。"),
    ],
    "behavior": [
      C("🪱","拱土本能","猪用鼻子拱开泥土寻找根茎、蠕虫和块茎，这是刻在基因里的觅食方式。"),
      C("🛁","泥浴降温","猪喜欢在泥里打滚，泥层能隔绝阳光、驱虫并降温，是它们的「防晒泥膜」。"),
      C("👯","社群生活","猪有清晰的社会关系，群体中有地位排序，彼此用气味和叫声沟通。"),
      C("🐷","母性极强","母猪对仔猪呵护备至，会用哼唱声与幼崽交流，护崽时极具攻击性。"),
      C("🧸","爱干净","猪其实很爱干净，会在窝外固定地点排泄，只是圈养环境让人误解它脏。"),
      C("🎾","会玩耍","猪喜欢探索、玩玩具，甚至和同伴「赛跑」，聪明且富有好奇心。"),
    ],
    "intelligence": [
      C("🧠","被低估的天才","猪的智商常被低估，研究显示其认知水平可与<strong>狗甚至 3 岁孩童</strong>相当。", True),
      C("🪞","镜子自我识别","猪能通过镜子找到身后食物，表现出一定程度的自我意识，这在动物中并不多见。"),
      C("🎮","会玩电子游戏","实验里猪能用摇杆操控光标完成简单游戏任务，展现学习与记忆能力。"),
      C("🐷","情感丰富","猪会表达高兴、恐惧、沮丧，被剥夺社交时会抑郁，拥有复杂情绪。"),
      C("🧩","解决问题","猪能学会开门、按按钮取食，甚至会「欺骗」同伴独占食物。"),
      C("🧠","空间记忆","猪能记住迷宫路线和食物位置，空间记忆能力在农场动物中名列前茅。"),
    ],
    "culture": [
      C("🇨🇳","十二生肖","猪是十二生肖<strong>最后一位</strong>（第十二）。属猪的人被认为憨厚、福气、随和。"),
      C("🧧","福气象征","传统文化中猪代表富足，「肥猪拱门」寓意招财进宝，年画常见。"),
      C("🐗","野猪勇武","许多民族视野猪为勇猛象征，古代兵器、纹章上常见野猪形象。"),
      C("🐷","宠物猪潮流","微型香猪曾风靡都市，成为另类宠物，改变「猪只上餐桌」的成见。"),
      C("📜","农耕符号","在中国，猪是「六畜」之一，养猪多少曾是家庭富裕的标志。"),
      C("🎨","文艺常客","从《小猪佩奇》到《三只小猪》，猪是童话与动画里的快乐主角。"),
    ],
  },
  "facts": [
    {"num":"01","text":"猪其实非常爱干净，会在窝外固定地点排便，脏是因为<strong>圈养空间太小</strong>。"},
    {"num":"02","text":"猪的嗅觉能找到埋在地下 30 厘米深的松露，是顶级「松露猎手」。"},
    {"num":"03","text":"猪没有汗腺，靠泥浴和喘气散热，泥里打滚是它们的防晒降温方式。"},
    {"num":"04","text":"猪能通过镜子找到身后食物，具备一定的自我意识。"},
    {"num":"05","text":"猪的智商相当于 <strong>3 岁</strong>人类儿童，会玩电子游戏、按按钮取食。"},
    {"num":"06","text":"母猪一胎可产 10-14 头仔猪，是繁殖力最强的家养哺乳动物之一。"},
    {"num":"07","text":"野猪的獠牙终生生长，雄性越长越显威武，用于争斗与求偶。"},
    {"num":"08","text":"猪的叫声种类不少，仔猪的尖叫能召唤母猪赶来救援。"},
    {"num":"09","text":"越南大肚猪等微型猪可作为伴侣动物，成年体重可控制在数十斤。"},
    {"num":"10","text":"猪的嗅觉受体数量惊人，经训练可嗅探地雷与违禁品。"},
    {"num":"11","text":"猪的寿命可达 <strong>15-20 年</strong>，远比我们餐桌上的出栏时间短得多。"},
    {"num":"12","text":"猪的尾巴卷曲方向（左/右）曾被民间用来「预测」吉凶，纯属趣谈。"},
  ],
  "daily": [
    {"date":"1月6日","emoji":"🐷","cat":"猪","title":"生肖猪","body":"猪是十二生肖第十二位。属猪的人被认为憨厚福气，猪也象征富足。"},
    {"date":"2月9日","emoji":"🐷","cat":"猪","title":"松露猎手","body":"猪的嗅觉灵敏，能嗅出埋在地下的松露，欧洲曾用母猪寻找这种名贵食材。"},
    {"date":"3月8日","emoji":"🐷","cat":"猪","title":"母猪的繁殖力","body":"母猪一胎可产10-14头仔猪，是繁殖力最强的家养哺乳动物之一。"},
    {"date":"4月9日","emoji":"🐷","cat":"猪","title":"猪的智商","body":"研究显示猪的认知能力可与狗甚至3岁孩童相当，能玩简单电子游戏。"},
    {"date":"5月10日","emoji":"🐷","cat":"猪","title":"爱干净","body":"猪其实很讲卫生，会在窝外固定地点排便，脏主要是圈养空间太小所致。"},
    {"date":"6月11日","emoji":"🐷","cat":"猪","title":"泥浴降温","body":"猪几乎不出汗，靠在泥里打滚隔绝阳光、驱虫并降温，那是它们的「泥膜」。"},
    {"date":"7月12日","emoji":"🐷","cat":"猪","title":"镜子测试","body":"猪能通过镜子找到身后食物，表现出一定自我意识，在动物中并不多见。"},
    {"date":"8月13日","emoji":"🐷","cat":"猪","title":"中国养猪史","body":"中国养猪史超八千年，是世界上最早养猪的国家之一，猪是农耕文明的重要部分。"},
    {"date":"9月14日","emoji":"🐷","cat":"猪","title":"藏香猪","body":"青藏高原放养的藏香猪体型小、肉质紧实香味浓，被称为「高原之珍」。"},
    {"date":"10月15日","emoji":"🐷","cat":"猪","title":"宠物猪","body":"微型香猪、越南大肚猪可作伴侣动物，改变了「猪只上餐桌」的传统印象。"},
    {"date":"11月16日","emoji":"🐷","cat":"猪","title":"野猪归来","body":"多地野猪种群恢复甚至「进城」，引发人猪冲突，也提示生态链的复苏。"},
    {"date":"12月17日","emoji":"🐷","cat":"猪","title":"年度回顾","body":"从8000年前驯化到今天，猪既是最主要的肉源，也是聪明的「被低估天才」。"},
  ],
  "quiz": [
    {"q":"家猪的祖先是？","options":["野猪","河马","鹿","羊"],"answer":0,"explain":"家猪由野猪（Sus scrofa）驯化而来，约9000年前在多地独立驯化。"},
    {"q":"猪主要靠什么方式降温？","options":["出汗","泥浴和喘气","喝水","脱毛"],"answer":1,"explain":"猪几乎没有汗腺，靠在泥里打滚（泥膜）和张嘴喘气散热。"},
    {"q":"关于猪的智力，下列说法正确的是？","options":["很笨","相当于3岁孩童，会玩电子游戏","只会吃睡","没有记忆"],"answer":1,"explain":"猪认知能力强，能玩简单电子游戏、通过镜子测试，相当于3岁孩童水平。"},
  ],
},
"fish": {
  "emoji": "🐟", "name": "鱼", "en": "鱼的百科全书",
  "desc": "从 5 亿年前的脊椎动物始祖到 3.4 万种现生鱼类，探秘水中居民的身体、行为与智慧",
  "tabs": {
    "origin": [
      C("🧬","脊椎动物始祖","鱼类是最早的<strong>脊椎动物</strong>，约 5 亿年前的寒武纪后期出现，是所有四足动物的远古祖先。"),
      C("🌊","从水到陆","约 3.7 亿年前，肉鳍鱼登上陆地演化成两栖动物，最终诞生了包括人类在内的四足动物。"),
      C("🐟","物种之最","现生鱼类超过 <strong>3.4 万种</strong>，占已知脊椎动物的一半以上，是最成功的脊椎动物类群。"),
      C("🧬","持续演化","从软骨鱼（鲨鱼）到硬骨鱼（鲤鱼），鱼类在数亿年间分化出惊人多样的形态与习性。"),
      C("🌍","无处不在","从深海热泉到高山溪流，从咸水到淡水，鱼几乎占领了所有水域生态系统。"),
      C("⏳","古老而年轻","腔棘鱼曾被认为已灭绝，却在 1938 年被重新发现，被称为「活化石」。"),
    ],
    "breeds": [
      B("🐠","金鱼","中国","由鲫鱼选育而来，品种逾百，是最受欢迎的观赏鱼之一。"),
      B("🎏","锦鲤","日本/中国","色彩斑斓的观赏鲤，象征好运，可活数十年甚至上百年。"),
      B("🐟","孔雀鱼","中南美洲","小型热带鱼，繁殖力强、色彩绚丽，新手养鱼首选。"),
      B("🐠","小丑鱼","印度洋太平洋","与海葵共生，因电影《海底总动员》家喻户晓。"),
      B("🦈","鲨鱼","全球海洋","软骨鱼代表，已存在超 4 亿年，是海洋顶级掠食者。"),
      B("🐟","鲤鱼","亚洲广布","适应力强，锦鲤与食用鲤皆出其类，会跃出水面。"),
      B("🐟","三文鱼（鲑）","北大西洋太平洋","降海洄游，逆流回乡产卵，肉质富含油脂。"),
      B("🐉","斗鱼","东南亚","雄性好斗、鳍如纱丽，色彩艳丽，是著名观赏鱼。"),
    ],
    "biology": [
      C("🫁","鳃呼吸","鱼用<strong>鳃</strong>提取水中氧气，水流过鳃丝完成气体交换，离水后因鳃丝粘连窒息。"),
      C("📏","侧线系统","鱼体侧有「侧线」感受水流与震动，像水下雷达，能感知同伴与天敌。"),
      C("🎈","鱼鳔浮力","多数硬骨鱼有<strong>鱼鳔</strong>调节气体控制沉浮，像自带「潜水艇气囊」。"),
      C("🐟","鳞片护甲","鳞片重叠排列保护身体并减少阻力，不同鱼类的鳞形各异。"),
      C("👁️","视觉差异","多数鱼能看到紫外线或偏振光，部分鱼四色视觉，但深海鱼视觉退化。"),
      C("👂","听觉与平衡","鱼无外耳，靠内耳与鱼鳔感知声音振动，保持身体平衡。"),
    ],
    "behavior": [
      C("🏊","洄游奇迹","<strong>三文鱼</strong>逆流千里回到出生河流产卵，靠记忆与嗅觉定位，堪称生命壮举。"),
      C("🐟","群游协作","沙丁鱼等形成庞大鱼群迷惑捕食者，集体转向如同一个巨大生物体。"),
      C("🐠","清洁共生","清洁鱼为大型鱼清理寄生虫，双方互利，形成「水下清洁站」。"),
      C("🎭","伪装大师","比目鱼随底质变色、叶海龙形似海藻，拟态躲避天敌堪称一绝。"),
      C("🐡","膨胀自卫","河鲀受惊会吞水膨胀成刺球，用体型吓退敌人，是著名的防御绝技。"),
      C("🪺","育儿有方","不少鱼由雄鱼口含卵孵化（如丽鱼），或用泡巢护卵，父爱十足。"),
    ],
    "intelligence": [
      C("🧠","会数数的鱼","研究发现部分鱼能分辨数量多少，甚至「数」到 4，<strong>空间记忆</strong>超乎想象。", True),
      C("🪞","自我认知","清洁鱼能通过镜子测试，会攻击镜中「入侵者」后明白那是自己，展现自我意识。"),
      C("🧩","长期记忆","鱼类的记忆远不止「7 秒」，某些鱼能记住食物位置<strong>数月甚至数年</strong>。"),
      C("🎯","工具使用","射水鱼能喷水击落水面昆虫，精准计算折射，是罕见的「鱼枪手」。"),
      C("🤝","社会学习","部分鱼会观察同伴学会新技能，群体中存在「文化」传递。"),
      C("🧠","个性鲜明","研究表明鱼也有「性格」——有的大胆探索，有的胆小谨慎，个体差异明显。"),
    ],
    "culture": [
      C("🇨🇳","年年有余","汉语「鱼」谐音「余」，年夜饭必有鱼，寓意<strong>年年有余</strong>、富贵盈门。"),
      C("🎏","鲤鱼跳龙门","传说鲤鱼跃过龙门便化身为龙，象征逆流而上、金榜题名。"),
      C("🍀","锦鲤文化","锦鲤象征好运与坚韧，转发「锦鲤」成为当代祈愿学业事业顺利的网络习俗。"),
      C("🐟","宗教符号","早期基督教用鱼（ΙΧΘΥΣ）作秘密标记，鱼也是多神信仰中的水神使者。"),
      C("🍜","艺术意象","从宋画《藻鱼图》到浮世绘锦鲤，鱼是东西方艺术中灵动的主题。"),
      C("🐠","现代萌宠","观赏鱼与水族造景风靡全球，养鱼成为减压与审美兼具的都市爱好。"),
    ],
  },
  "facts": [
    {"num":"01","text":"鱼的记忆远不止7秒，某些鱼能记住食物位置长达<strong>数月</strong>。"},
    {"num":"02","text":"三文鱼能逆流千里洄游回出生地繁衍，靠嗅觉与地磁导航。"},
    {"num":"03","text":"射水鱼能喷水精准击落水面上方昆虫，会计算光线折射。"},
    {"num":"04","text":"鲨鱼已存在超过 <strong>4 亿年</strong>，比恐龙还古老，且一生不断换牙。"},
    {"num":"05","text":"鱼有「侧线」器官感受水流震动，像水下雷达探测周围。"},
    {"num":"06","text":"清洁鱼会为大型鱼「洗澡」除寄生虫，双方形成互利关系。"},
    {"num":"07","text":"河鲀受惊会吞水膨胀成带刺圆球，是著名的自卫绝技。"},
    {"num":"08","text":"某些鱼能通过镜子测试，表现出一定的自我意识。"},
    {"num":"09","text":"腔棘鱼曾被认定灭绝，1938年却被人捕到，是著名「活化石」。"},
    {"num":"10","text":"金鱼的祖先是鲫鱼，经千年选育才有今天的百变外形。"},
    {"num":"11","text":"深海鱼很多靠<strong>发光器官</strong>（生物荧光）在黑暗中交流与诱捕。"},
    {"num":"12","text":"鱼也会「睡觉」，只是多数睁着眼、减缓活动，保持警觉。"},
  ],
  "daily": [
    {"date":"1月7日","emoji":"🐟","cat":"鱼","title":"年年有余","body":"汉语「鱼」谐音「余」，年夜饭必有鱼，寓意年年有余、富贵盈门。"},
    {"date":"2月10日","emoji":"🐟","cat":"鱼","title":"鲤鱼跳龙门","body":"传说鲤鱼跃过龙门便化身为龙，象征逆流而上、金榜题名，激励无数学子。"},
    {"date":"3月11日","emoji":"🐟","cat":"鱼","title":"鱼的记忆","body":"鱼的记忆远不止7秒，某些鱼能记住食物位置长达数月，空间记忆惊人。"},
    {"date":"4月12日","emoji":"🐟","cat":"鱼","title":"射水鱼","body":"射水鱼能喷水精准击落水面昆虫，会计算光线折射，是罕见的「鱼枪手」。"},
    {"date":"5月13日","emoji":"🐟","cat":"鱼","title":"三文鱼洄游","body":"三文鱼逆流千里回到出生河流产卵，靠嗅觉与地磁导航，堪称生命壮举。"},
    {"date":"6月14日","emoji":"🐟","cat":"鱼","title":"清洁鱼","body":"清洁鱼为大型鱼清理寄生虫，形成互利「水下清洁站」，是共生典范。"},
    {"date":"7月15日","emoji":"🐟","cat":"鱼","title":"鲨鱼之年","body":"鲨鱼已存在超4亿年，比恐龙古老，一生不断换牙，是海洋顶级掠食者。"},
    {"date":"8月16日","emoji":"🐟","cat":"鱼","title":"锦鲤好运","body":"锦鲤象征好运与坚韧，转发「锦鲤」成为祈愿学业事业顺利的网络习俗。"},
    {"date":"9月17日","emoji":"🐟","cat":"鱼","title":"活化石腔棘鱼","body":"腔棘鱼曾被认为已灭绝，1938年却被重新捕获，被称为「活化石」。"},
    {"date":"10月18日","emoji":"🐟","cat":"鱼","title":"金鱼起源","body":"金鱼的祖先是普通鲫鱼，经中国人千年选育才有今天百变的外形与色彩。"},
    {"date":"11月19日","emoji":"🐟","cat":"鱼","title":"深海发光","body":"许多深海鱼靠生物荧光在黑暗中交流、诱捕猎物，是深海的「活灯笼」。"},
    {"date":"12月20日","emoji":"🐟","cat":"鱼","title":"年度回顾","body":"从5亿年前最早的脊椎动物到今天3.4万种，鱼是地球水域真正的「原住民」。"},
  ],
  "quiz": [
    {"q":"鱼用什么器官呼吸？","options":["肺","鳃","皮肤","鳍"],"answer":1,"explain":"鱼用鳃提取水中氧气，水流过鳃丝完成气体交换，离水会窒息。"},
    {"q":"关于鱼的记忆，正确的是？","options":["只有7秒","能记住数月","完全没有","只有1天"],"answer":1,"explain":"鱼类记忆远不止7秒，某些鱼能记住食物位置长达数月。"},
    {"q":"三文鱼繁殖时会？","options":["原地产卵","逆流洄游回出生地","飞到树上","冬眠"],"answer":1,"explain":"三文鱼会逆流千里洄游回出生河流产卵，靠嗅觉与地磁导航。"},
  ],
},
}

TAB_META = [
    ("origin","起源驯化"),
    ("biology","生理特征"),
    ("behavior","行为习性"),
    ("intelligence","智力与情感"),
    ("culture","%s与文化"),
    ("breeds","品种大全"),
    ("facts","冷知识"),
]

# ============ 生成 HTML 片段 ============
def gen_section(key):
    a = animals[key]
    L = []
    L.append('<section class="encyclopedia %s-section" id="%s">' % (key, key))
    L.append('  <div class="container">')
    L.append('    <div class="section-header">')
    L.append('      <div class="section-icon">%s</div>' % a["emoji"])
    L.append('      <h2 class="section-title">%s</h2>' % a["en"])
    L.append('      <p class="section-desc">%s</p>' % a["desc"])
    L.append('    </div>')
    # tab-bar
    L.append('    <div class="tab-bar" id="%sTabs">' % key)
    for i,(tk,label) in enumerate(TAB_META):
        lab = label % a["name"] if "%s" in label else label
        active = ' active' if i==0 else ''
        L.append('      <button class="tab-btn%s" data-tab="%s-%s">%s</button>' % (active, key, tk, lab))
    L.append('    </div>')
    # panels
    for i,(tk,label) in enumerate(TAB_META):
        active = ' active' if i==0 else ''
        L.append('    <div class="tab-panel%s" id="%s-%s">' % (active, key, tk))
        if tk == "breeds":
            L.append('      <div class="breed-grid">')
            for b in a["tabs"]["breeds"]:
                L.append('        <div class="breed-card %s">' % key)
                L.append('          <div class="breed-emoji">%s</div>' % b["emoji"])
                L.append('          <h4>%s</h4>' % b["name"])
                L.append('          <p class="breed-origin">📍 %s</p>' % b["origin"])
                L.append('          <p>%s</p>' % b["desc"])
                L.append('        </div>')
            L.append('      </div>')
        elif tk == "facts":
            L.append('      <div class="facts-list" id="%sFactsList">' % key)
            L.append('        <!-- 由 JS 动态填充 -->')
            L.append('      </div>')
        else:
            L.append('      <div class="content-grid">')
            for c in a["tabs"][tk]:
                hl = ' highlight' if c.get("hl") else ''
                L.append('        <div class="info-card%s">' % hl)
                L.append('          <div class="card-icon">%s</div>' % c["icon"])
                L.append('          <h3>%s</h3>' % c["title"])
                L.append('          <p>%s</p>' % c["text"])
                L.append('        </div>')
            L.append('      </div>')
        L.append('    </div>')
    L.append('  </div>')
    L.append('</section>')
    return "\n".join(L)

sections_html = "\n\n".join(gen_section(k) for k in ["dog","pig","fish"])

# ============ 生成 data 片段（facts + daily） ============
def arr(items, fmt):
    return ",\n".join(fmt(it) for it in items)

facts_js = {k: ("[\n" + arr(animals[k]["facts"], lambda f: '  { num: "%s", text: "%s" }' % (f["num"], f["text"])) + "\n]") for k in animals}
daily_js = {k: ("[\n" + arr(animals[k]["daily"], lambda d: '  { date: "%s", emoji: "%s", cat: "%s", title: "%s", body: "%s" }' % (d["date"], d["emoji"], d["cat"], d["title"], d["body"])) + "\n]") for k in animals}

data_block = ""
for k in ["dog","pig","fish"]:
    data_block += "const %sFacts = %s;\n" % (k, facts_js[k])
for k in ["dog","pig","fish"]:
    data_block += "const %sDailyFacts = %s;\n" % (k, daily_js[k])
data_block += "\n"

# ============ 生成 quiz 追加 ============
def quiz_obj(q):
    opts = "[" + ", ".join('"%s"' % o for o in q["options"]) + "]"
    return '  {\n    q: "%s",\n    options: %s,\n    answer: %d,\n    explain: "%s"\n  }' % (q["q"], opts, q["answer"], q["explain"])

quiz_append = ",\n".join(quiz_obj(q) for k in ["dog","pig","fish"] for q in animals[k]["quiz"])

# ============ 读取并修改 index.html ============
with open(HTML, "r", encoding="utf-8") as f:
    html = f.read()

def must_replace(s, old, new, label):
    if s.count(old) != 1:
        raise SystemExit("锚点不唯一或缺失 [%s]，出现 %d 次" % (label, s.count(old)))
    return s.replace(old, new, 1)

# 1) CSS 插入（</style> 前）
css_block = """
/* ===== 狗/猪/鱼 新增配色与板块样式 ===== */
:root {
  --dog-primary: #A0522D;
  --dog-light: #F0E0D6;
  --dog-dark: #5C3317;
  --pig-primary: #EC9A9A;
  --pig-light: #FCE4E2;
  --pig-dark: #B5655E;
  --fish-primary: #2E86AB;
  --fish-light: #D6EAF8;
  --fish-dark: #1B4965;
}
.dog-section { background: linear-gradient(180deg, var(--bg-main), #FBF3EE); }
.pig-section { background: linear-gradient(180deg, #FDF5F4, #F7EAE8); }
.fish-section { background: linear-gradient(180deg, #F0F7FB, #E6F2F8); }
.dog-section .section-title { background: linear-gradient(135deg, var(--dog-primary), var(--dog-dark)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
.pig-section .section-title { background: linear-gradient(135deg, var(--pig-primary), var(--pig-dark)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
.fish-section .section-title { background: linear-gradient(135deg, var(--fish-primary), var(--fish-dark)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
.dog-section .tab-btn:hover, .dog-section .tab-btn.active { background: var(--dog-primary); color: #fff; box-shadow: 0 4px 15px rgba(160,82,45,0.3); }
.pig-section .tab-btn:hover, .pig-section .tab-btn.active { background: var(--pig-primary); color: #fff; box-shadow: 0 4px 15px rgba(236,154,154,0.3); }
.fish-section .tab-btn:hover, .fish-section .tab-btn.active { background: var(--fish-primary); color: #fff; box-shadow: 0 4px 15px rgba(46,134,171,0.3); }
.dog-section .info-card::before { background: var(--dog-primary); }
.pig-section .info-card::before { background: var(--pig-primary); }
.fish-section .info-card::before { background: var(--fish-primary); }
.dog-section .info-card.highlight { background: linear-gradient(135deg, #FBF0E9, #F0E0D6); border-color: var(--dog-light); }
.pig-section .info-card.highlight { background: linear-gradient(135deg, #FCEDED, #FCE4E2); border-color: var(--pig-light); }
.fish-section .info-card.highlight { background: linear-gradient(135deg, #EDF5FB, #D6EAF8); border-color: var(--fish-light); }
.dog-section .fact-item { border-left-color: var(--dog-primary); }
.pig-section .fact-item { border-left-color: var(--pig-primary); }
.fish-section .fact-item { border-left-color: var(--fish-primary); }
.dog-section .fact-number { color: var(--dog-primary); }
.pig-section .fact-number { color: var(--pig-primary); }
.fish-section .fact-number { color: var(--fish-primary); }
.dog-section .fact-text strong { color: var(--dog-primary); }
.pig-section .fact-text strong { color: var(--pig-primary); }
.fish-section .fact-text strong { color: var(--fish-primary); }
.breed-card.dog:hover { border-color: var(--dog-light); }
.breed-card.pig:hover { border-color: var(--pig-light); }
.breed-card.fish:hover { border-color: var(--fish-light); }
.news-card-tag.cat-dog { background: var(--dog-light); color: var(--dog-dark); }
.news-card-tag.cat-pig { background: var(--pig-light); color: var(--pig-dark); }
.news-card-tag.cat-fish { background: var(--fish-light); color: var(--fish-dark); }
.title-dog { background: linear-gradient(135deg, #A0522D, #C77B4E); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
.title-pig { background: linear-gradient(135deg, #EC9A9A, #E06B6B); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
.title-fish { background: linear-gradient(135deg, #2E86AB, #1B4965); -webkit-background-clip: text; -webkit-text-fill-color: transparent; background-clip: text; }
"""
html = must_replace(html, "</style>", css_block + "</style>", "css-insert")

# 2) 三动物 section（鸡猴大比拼前）
html = must_replace(html,
  '<!-- ===== 鸡猴大比拼 ===== -->',
  sections_html + "\n\n<!-- ===== 鸡猴大比拼 ===== -->",
  "section-insert")

# 3) data facts+daily（const quizQuestions 前）
html = must_replace(html, "const quizQuestions = [", data_block + "const quizQuestions = [", "data-insert")

# 4) quiz 追加
quiz_anchor = '    explain: "鸡蛋在37.5°C下孵化21天。第3天心脏开始跳动，第21天小鸡破壳而出。"\n  },\n];'
html = must_replace(html, quiz_anchor,
  '    explain: "鸡蛋在37.5°C下孵化21天。第3天心脏开始跳动，第21天小鸡破壳而出。"\n  },\n' + quiz_append + '\n];',
  "quiz-insert")

# 5) IIFE initTabs
html = must_replace(html,
  "  initTabs('monkeyTabs');\n",
  "  initTabs('monkeyTabs');\n  initTabs('dogTabs');\n  initTabs('pigTabs');\n  initTabs('fishTabs');\n",
  "initTabs")

# 6) IIFE renderFacts
html = must_replace(html,
  "  renderFacts('monkeyFactsList', monkeyFacts);\n",
  "  renderFacts('monkeyFactsList', monkeyFacts);\n  renderFacts('dogFactsList', dogFacts);\n  renderFacts('pigFactsList', pigFacts);\n  renderFacts('fishFactsList', fishFacts);\n",
  "renderFacts")

# 7) IIFE dailyFacts 合并（var today 前插入 allDailyFacts，并把该节内 dailyFacts 替换为 allDailyFacts）
daily_sec_anchor = "  var today = new Date();"
html = must_replace(html, daily_sec_anchor,
  "  var allDailyFacts = dailyFacts.concat(typeof dogDailyFacts!=='undefined'?dogDailyFacts:[], typeof pigDailyFacts!=='undefined'?pigDailyFacts:[], typeof fishDailyFacts!=='undefined'?fishDailyFacts:[]);\n" + daily_sec_anchor,
  "allDailyFacts-def")
# 仅替换从 dailySec 到 renderDailyList 之间的 dailyFacts
idx_start = html.index("  var today = new Date();")
idx_end = html.index("  renderDailyList();") + len("  renderDailyList();")
seg = html[idx_start:idx_end]
seg = seg.replace("dailyFacts", "allDailyFacts")
html = html[:idx_start] + seg + html[idx_end:]

# 8) paintNews catClass
html = must_replace(html,
  "var catClass = item.category === '猴' ? 'cat-monkey' : 'cat-chicken';",
  "var catClass = item.category === '猴' ? 'cat-monkey' : (item.category === '狗' ? 'cat-dog' : (item.category === '猪' ? 'cat-pig' : (item.category === '鱼' ? 'cat-fish' : 'cat-chicken')));",
  "catClass")

# 9) 导航加狗猪鱼
html = must_replace(html,
  '      <a href="#monkey" class="nav-link">🐒 猴子百科</a>\n',
  '      <a href="#monkey" class="nav-link">🐒 猴子百科</a>\n      <a href="#dog" class="nav-link">🐶 狗的百科</a>\n      <a href="#pig" class="nav-link">🐷 猪的百科</a>\n      <a href="#fish" class="nav-link">🐟 鱼的百科</a>\n',
  "nav")

# 10) Hero 标题（鸡 与 猴 → 五动物）
html = must_replace(html,
  '      <span class="title-chicken">鸡</span>\n      <span class="title-vs">与</span>\n      <span class="title-monkey">猴</span>',
  '      <span class="title-chicken">鸡</span><span class="title-vs">·</span><span class="title-monkey">猴</span><span class="title-vs">·</span><span class="title-dog">狗</span><span class="title-vs">·</span><span class="title-pig">猪</span><span class="title-vs">·</span><span class="title-fish">鱼</span>',
  "hero-title")

# 11) Hero 副标题
html = must_replace(html,
  '    <p class="hero-subtitle">从农场到丛林 · 从羽毛到毛发 · 每天认识多一点</p>',
  '    <p class="hero-subtitle">从农场到丛林 · 从羽毛到鳍鳞 · 五种生灵，每天认识多一点</p>',
  "hero-sub")

# 12) logo 文案
html = must_replace(html,
  '      <span class="logo-text">鸡与猴<sup>百科</sup></span>',
  '      <span class="logo-text">动物趣味<sup>百科</sup></span>',
  "logo")
html = must_replace(html,
  '      <span class="logo-icon">🐔</span>\n      <span class="logo-text">动物趣味<sup>百科</sup></span>\n      <span class="logo-icon">🐒</span>',
  '      <span class="logo-icon">🐔</span>\n      <span class="logo-text">动物趣味<sup>百科</sup></span>\n      <span class="logo-icon">🐶</span>\n      <span class="logo-icon">🐷</span>\n      <span class="logo-icon">🐟</span>',
  "logo-icons")

# 13) 页脚 h4 与简介
html = must_replace(html,
  '      <h4>🐔🐒 鸡与猴百科</h4>',
  '      <h4>🐔🐒🐶🐷🐟 动物趣味百科</h4>',
  "footer-h4")
html = must_replace(html,
  '      <p>专注于鸡和猴子的趣味科普平台，每天更新，带你从不同角度认识这两种神奇的动物。</p>',
  '      <p>涵盖鸡、猴、狗、猪、鱼五大类动物的趣味科普平台，每天更新，带你从不同角度认识这些神奇的动物。</p>',
  "footer-desc")

with open(HTML, "w", encoding="utf-8") as f:
    f.write(html)

print("OK: index.html 扩展完成")
print("新增 section 字符数:", len(sections_html))
print("data_block 字符数:", len(data_block))
