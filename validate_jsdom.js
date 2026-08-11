// -*- coding: utf-8 -*-
const { JSDOM, VirtualConsole } = require("jsdom");
const fs = require("fs");
const path = require("path");

const HTML_PATH = path.join(__dirname, "index.html");
const html = fs.readFileSync(HTML_PATH, "utf-8");

const errors = [];
const vc = new VirtualConsole();
vc.on("jsdomError", (e) => errors.push("jsdomError: " + (e && (e.detail || e.message) || e)));
vc.on("error", (...a) => errors.push("console.error: " + a.join(" ")));

const dom = new JSDOM(html, {
  runScripts: "dangerously",
  resources: "usable",
  pretendToBeVisual: true,
  virtualConsole: vc,
  url: "https://example.com/",
  beforeParse(window) {
    // 浏览器原生 API，jsdom 未实现 —— 仅测试环境打桩
    window.IntersectionObserver = class {
      constructor(cb) { this.cb = cb; }
      observe() {}
      unobserve() {}
      disconnect() {}
    };
    // 部分环境需要 requestAnimationFrame
    if (!window.requestAnimationFrame) {
      window.requestAnimationFrame = (cb) => setTimeout(() => cb(Date.now()), 0);
    }
  },
});

setTimeout(() => {
  const d = dom.window.document;
  const out = [];
  const ids = ["dog", "pig", "fish", "chicken", "monkey"];
  let ok = true;
  ids.forEach((id) => {
    const sec = d.getElementById(id);
    if (!sec) { out.push(`section#${id}: MISSING`); ok = false; return; }
    const tabs = sec.querySelectorAll(".tab-btn").length;
    const panels = sec.querySelectorAll(".tab-panel").length;
    const cards = sec.querySelectorAll(".info-card").length;
    const facts = sec.querySelectorAll(".fact-item").length;       // 冷知识由 JS 渲染
    const breeds = sec.querySelectorAll(".breed-card").length;     // 品种由 JS 渲染
    out.push(`section#${id}: tabs=${tabs} panels=${panels} info-cards=${cards} fact-items=${facts} breed-cards=${breeds}`);
  });

  // 导航
  const navDog = d.querySelector('a[href="#dog"]');
  const navPig = d.querySelector('a[href="#pig"]');
  const navFish = d.querySelector('a[href="#fish"]');
  out.push(`导航: dog=${!!navDog} pig=${!!navPig} fish=${!!navFish}`);

  // Hero / Logo / Footer 文案
  const heroHasDog = d.body.innerHTML.includes("狗") && d.body.innerHTML.includes("百科全书");
  out.push(`Hero/介绍文案含新动物: ${heroHasDog}`);

  if (errors.length) {
    out.push("\n❌ 运行期错误:");
    errors.forEach((e) => out.push("   " + e));
    ok = false;
  } else {
    out.push("\n✅ 无运行期错误。");
  }

  console.log(out.join("\n"));
  process.exit(ok ? 0 : 2);
}, 1800);
