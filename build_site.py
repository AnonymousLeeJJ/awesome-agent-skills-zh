#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the static Awesome Agent Skills Chinese directory."""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DOCS = ROOT / "docs"
DATA = json.loads((ROOT / "skills.json").read_text(encoding="utf-8"))

payload = json.dumps(DATA, ensure_ascii=False).replace("</", "<\\/")
updated = html.escape(DATA["meta"]["updated"])

page = f"""<!doctype html>
<html lang="zh-CN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Awesome Agent Skills 中文导航</title>
<meta name="description" content="精选真实可用的 Agent Skills、技能合集与规范资源，中文解读、按场景分类、附安装方式">
<style>
:root {{
  color-scheme: dark;
  --bg: #090b12;
  --panel: rgba(255,255,255,.06);
  --panel-strong: rgba(255,255,255,.1);
  --text: #f6f7fb;
  --muted: #a7adbf;
  --line: rgba(255,255,255,.12);
  --violet: #8b5cf6;
  --cyan: #22d3ee;
  --green: #34d399;
  --amber: #fbbf24;
  --red: #fb7185;
  --blue: #60a5fa;
}}
* {{ box-sizing: border-box; }}
body {{
  margin: 0;
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Microsoft YaHei", sans-serif;
  background:
    radial-gradient(circle at 10% -10%, rgba(139,92,246,.34), transparent 32rem),
    radial-gradient(circle at 88% 0%, rgba(34,211,238,.22), transparent 30rem),
    linear-gradient(180deg, #0b1020 0%, var(--bg) 42%);
  color: var(--text);
}}
a {{ color: inherit; }}
button, input {{ font: inherit; }}
.shell {{ width: min(1180px, calc(100% - 36px)); margin: 0 auto; }}
.hero {{ padding: 76px 0 34px; text-align: center; }}
.eyebrow {{
  display: inline-flex; align-items: center; gap: 8px;
  padding: 7px 13px; border: 1px solid var(--line); border-radius: 999px;
  background: rgba(255,255,255,.06); color: #dbeafe; font-size: 13px;
}}
.hero h1 {{ margin: 22px 0 14px; font-size: clamp(38px, 7vw, 76px); line-height: 1.02; letter-spacing: -0.055em; }}
.hero h1 span {{ background: linear-gradient(90deg, #c4b5fd, #67e8f9); -webkit-background-clip: text; color: transparent; }}
.sub {{ max-width: 760px; margin: 0 auto; color: var(--muted); font-size: 18px; line-height: 1.8; }}
.actions {{ display: flex; justify-content: center; flex-wrap: wrap; gap: 12px; margin-top: 28px; }}
.btn {{
  border: 1px solid var(--line); border-radius: 14px; padding: 12px 18px;
  text-decoration: none; background: rgba(255,255,255,.07); font-weight: 800;
}}
.btn.primary {{ border: 0; background: linear-gradient(135deg, var(--violet), var(--cyan)); color: white; }}
.stats {{ display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin: 34px 0 24px; }}
.stat {{ padding: 18px; border: 1px solid var(--line); border-radius: 20px; background: rgba(255,255,255,.055); }}
.stat b {{ display: block; font-size: 30px; letter-spacing: -0.04em; }}
.stat span {{ color: var(--muted); font-size: 13px; }}
.toolbar {{
  position: sticky; top: 0; z-index: 20;
  padding: 14px 0; margin-bottom: 22px;
  background: rgba(9,11,18,.82); backdrop-filter: blur(18px);
  border-bottom: 1px solid rgba(255,255,255,.08);
}}
.searchrow {{ display: grid; grid-template-columns: 1fr auto; gap: 10px; margin-bottom: 12px; }}
.search {{
  width: 100%; border: 1px solid var(--line); outline: none; border-radius: 16px;
  padding: 14px 16px; background: rgba(255,255,255,.075); color: var(--text);
}}
.search:focus {{ border-color: rgba(34,211,238,.65); box-shadow: 0 0 0 4px rgba(34,211,238,.11); }}
.filters, .sourcefilters {{ display: flex; gap: 8px; flex-wrap: wrap; }}
.chip {{
  border: 1px solid var(--line); background: rgba(255,255,255,.055); color: var(--muted);
  border-radius: 999px; padding: 8px 12px; cursor: pointer;
}}
.chip.active {{ color: white; border-color: rgba(34,211,238,.7); background: rgba(34,211,238,.14); }}
.chip.source.active {{ border-color: rgba(139,92,246,.75); background: rgba(139,92,246,.18); }}
.notice {{
  display: flex; gap: 12px; align-items: flex-start;
  border: 1px solid rgba(251,191,36,.28); background: rgba(251,191,36,.08);
  color: #fde68a; padding: 14px 16px; border-radius: 18px; line-height: 1.65; margin-bottom: 18px;
}}
.grid {{ display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 16px; padding-bottom: 42px; }}
.card {{
  position: relative; overflow: hidden;
  border: 1px solid var(--line); border-radius: 24px;
  background: linear-gradient(180deg, rgba(255,255,255,.085), rgba(255,255,255,.045));
  padding: 20px;
}}
.card::before {{
  content: ""; position: absolute; inset: 0 0 auto 0; height: 3px;
  background: linear-gradient(90deg, var(--violet), var(--cyan)); opacity: .75;
}}
.card.featured {{ border-color: rgba(34,211,238,.34); }}
.top {{ display: flex; align-items: flex-start; justify-content: space-between; gap: 14px; }}
.name {{ margin: 0; font-size: 22px; letter-spacing: -0.025em; }}
.name a {{ text-decoration: none; }}
.name a:hover {{ color: #93c5fd; }}
.star {{ color: var(--amber); font-size: 20px; }}
.desc {{ color: #c8cedd; line-height: 1.72; min-height: 58px; margin: 12px 0 14px; }}
.badges {{ display: flex; flex-wrap: wrap; gap: 7px; margin-bottom: 14px; }}
.badge {{ border-radius: 999px; padding: 5px 9px; font-size: 12px; font-weight: 800; }}
.badge.category {{ background: rgba(96,165,250,.13); color: #93c5fd; }}
.badge.official {{ background: rgba(52,211,153,.13); color: #86efac; }}
.badge.community {{ background: rgba(139,92,246,.15); color: #c4b5fd; }}
.badge.index {{ background: rgba(251,191,36,.13); color: #fde68a; }}
.badge.original {{ background: rgba(251,113,133,.14); color: #fda4af; }}
.badge.type {{ background: rgba(255,255,255,.1); color: #d7dbe7; }}
.badge.license {{ background: rgba(34,211,238,.1); color: #67e8f9; }}
.install {{
  display: grid; grid-template-columns: 1fr auto; gap: 8px; align-items: center;
  border: 1px solid rgba(255,255,255,.1); border-radius: 14px; background: rgba(0,0,0,.23);
  padding: 9px 9px 9px 12px;
}}
.install code {{ color: #dbeafe; font-size: 13px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }}
.copy {{
  border: 0; border-radius: 10px; padding: 7px 10px; cursor: pointer;
  color: white; background: rgba(255,255,255,.12);
}}
.copy:hover {{ background: rgba(34,211,238,.25); }}
.meta {{ margin-top: 12px; color: var(--muted); font-size: 12px; line-height: 1.6; }}
.empty {{ display: none; padding: 60px 0; text-align: center; color: var(--muted); }}
footer {{ border-top: 1px solid var(--line); color: var(--muted); padding: 26px 0 42px; line-height: 1.8; }}
footer a {{ color: #93c5fd; }}
@media (max-width: 760px) {{
  .stats, .grid {{ grid-template-columns: 1fr; }}
  .searchrow {{ grid-template-columns: 1fr; }}
  .hero {{ padding-top: 52px; }}
  .sub {{ font-size: 16px; }}
}}
</style>
</head>
<body>
<header class="hero shell">
  <div class="eyebrow">🧩 Agent Skills · 中文精选 · 更新于 {updated}</div>
  <h1>让 AI Agent<br><span>装上真正的专业能力</span></h1>
  <p class="sub">精选真实存在的 Agent Skills、技能合集与规范资源。中文解读、按场景分类、标注来源与安装方式，帮你少踩“凭空清单”的坑。</p>
  <div class="actions">
    <a class="btn primary" href="https://github.com/AnonymousLeeJJ/awesome-agent-skills-zh">⭐ GitHub Star</a>
    <a class="btn" href="https://github.com/AnonymousLeeJJ/awesome-agent-skills-zh/issues/new?template=submit-skill.yml">提交 Skill</a>
    <a class="btn" href="https://github.com/AnonymousLeeJJ/shuling-skill">用书灵生成 Skill</a>
  </div>
</header>
<main class="shell">
  <section class="stats">
    <div class="stat"><b id="statTotal">0</b><span>收录条目</span></div>
    <div class="stat"><b id="statOfficial">0</b><span>官方技能</span></div>
    <div class="stat"><b id="statCollection">0</b><span>合集索引</span></div>
    <div class="stat"><b id="statOriginal">0</b><span>原创技能</span></div>
  </section>
  <div class="toolbar">
    <div class="searchrow">
      <input id="search" class="search" type="search" placeholder="搜索：PDF、前端、部署、规划、书灵……">
    </div>
    <div id="categories" class="filters"></div>
    <div id="sources" class="sourcefilters" style="margin-top:9px"></div>
  </div>
  <div class="notice">⚠️ <div><strong>安全提示：</strong>Skills 可以包含会在本机执行的脚本。安装前请阅读 SKILL.md 与脚本内容；本站“链接已核验”不代表安全审计或官方推荐。</div></div>
  <section id="grid" class="grid"></section>
  <div id="empty" class="empty">没有找到匹配的 Skill，换个关键词试试。</div>
</main>
<footer class="shell">
  <p>Made with ❤️ by <a href="https://github.com/AnonymousLeeJJ">AnonymousLeeJJ</a> · 内容和数据采用 CC BY 4.0，构建脚本采用 MIT。</p>
  <p>相关项目：<a href="https://github.com/AnonymousLeeJJ/shuling-skill">书灵.skill</a> · <a href="https://anonymousleejj.github.io/ai-tools-nav/">AI Tools 导航</a> · <a href="https://anonymousleejj.github.io/cheatsheets-zh/">开发者速查表</a></p>
</footer>
<script id="skills-data" type="application/json">{payload}</script>
<script>
const DATA = JSON.parse(document.getElementById('skills-data').textContent);
const skills = DATA.skills;
const state = {{ q: '', category: 'all', source: 'all' }};
const SOURCE = {{ official: '官方', community: '社区', index: '索引', original: '原创' }};
const TYPE = {{ skill: '单项 Skill', collection: '技能合集', framework: '框架', guide: '指南', index: '资源索引' }};
const grid = document.getElementById('grid');
const empty = document.getElementById('empty');
function esc(s) {{ return String(s).replace(/[&<>"']/g, c => ({{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}}[c])); }}
function categoryName(id) {{ return (DATA.categories.find(c => c.id === id) || {{ icon: '📌', name: id }}); }}
function renderFilters() {{
  const cats = [{{ id: 'all', name: '全部', icon: '✨' }}, ...DATA.categories];
  document.getElementById('categories').innerHTML = cats.map(c => `<button class="chip ${{state.category === c.id ? 'active' : ''}}" data-category="${{c.id}}">${{c.icon}} ${{c.name}}</button>`).join('');
  const sources = [{{ id: 'all', name: '全部来源' }}, {{ id: 'official', name: '官方' }}, {{ id: 'community', name: '社区' }}, {{ id: 'index', name: '索引' }}, {{ id: 'original', name: '原创' }}];
  document.getElementById('sources').innerHTML = sources.map(s => `<button class="chip source ${{state.source === s.id ? 'active' : ''}}" data-source="${{s.id}}">${{s.name}}</button>`).join('');
}}
function filtered() {{
  return skills.filter(s => {{
    if (state.category !== 'all' && s.category !== state.category) return false;
    if (state.source !== 'all' && s.source !== state.source) return false;
    const hay = `${{s.name}} ${{s.description}} ${{s.install}} ${{s.compatibility}} ${{s.license}}`.toLowerCase();
    return hay.includes(state.q.toLowerCase());
  }});
}}
function card(s) {{
  const cat = categoryName(s.category);
  return `<article class="card ${{s.featured ? 'featured' : ''}}">
    <div class="top"><h2 class="name"><a href="${{s.url}}" target="_blank" rel="noopener">${{esc(s.name)}}</a></h2>${{s.featured ? '<span class="star">★</span>' : ''}}</div>
    <p class="desc">${{esc(s.description)}}</p>
    <div class="badges">
      <span class="badge category">${{cat.icon}} ${{cat.name}}</span>
      <span class="badge ${{s.source}}">${{SOURCE[s.source] || s.source}}</span>
      <span class="badge type">${{TYPE[s.type] || s.type}}</span>
      <span class="badge license">${{esc(s.license)}}</span>
    </div>
    <div class="install"><code title="${{esc(s.install)}}">${{esc(s.install)}}</code><button class="copy" data-copy="${{esc(s.install)}}">复制</button></div>
    <div class="meta">兼容：${{esc(s.compatibility)}} · 链接已核验</div>
  </article>`;
}}
function render() {{
  const list = filtered();
  grid.innerHTML = list.map(card).join('');
  empty.style.display = list.length ? 'none' : 'block';
}}
function updateStats() {{
  document.getElementById('statTotal').textContent = skills.length;
  document.getElementById('statOfficial').textContent = skills.filter(s => s.source === 'official').length;
  document.getElementById('statCollection').textContent = skills.filter(s => ['collection', 'index'].includes(s.type)).length;
  document.getElementById('statOriginal').textContent = skills.filter(s => s.source === 'original').length;
}}
document.getElementById('search').addEventListener('input', e => {{ state.q = e.target.value; render(); }});
document.getElementById('categories').addEventListener('click', e => {{ const b = e.target.closest('[data-category]'); if (!b) return; state.category = b.dataset.category; renderFilters(); render(); }});
document.getElementById('sources').addEventListener('click', e => {{ const b = e.target.closest('[data-source]'); if (!b) return; state.source = b.dataset.source; renderFilters(); render(); }});
document.addEventListener('click', async e => {{
  const b = e.target.closest('[data-copy]');
  if (!b) return;
  await navigator.clipboard.writeText(b.dataset.copy);
  b.textContent = '已复制';
  setTimeout(() => b.textContent = '复制', 1200);
}});
updateStats(); renderFilters(); render();
</script>
</body>
</html>
"""

DOCS.mkdir(exist_ok=True)
(DOCS / "index.html").write_text(page, encoding="utf-8")
print(f"OK -> {DOCS / 'index.html'} ({len(DATA['skills'])} skills)")
