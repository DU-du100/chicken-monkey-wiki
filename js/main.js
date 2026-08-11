/* ============================================================
   鸡与猴百科 · 主交互逻辑
   功能：导航栏、标签切换、每日趣闻、数字动画、
        冷知识渲染、趣味问答、滚动动画、返回顶部
   ============================================================ */

(function () {
  'use strict';

  /* ===== 1. 导航栏 ===== */
  const navbar = document.getElementById('navbar');
  const navToggle = document.getElementById('navToggle');
  const navMenu = document.getElementById('navMenu');
  const navLinks = document.querySelectorAll('.nav-link');

  // 滚动时改变导航栏样式
  window.addEventListener('scroll', function () {
    if (window.scrollY > 50) {
      navbar.classList.add('scrolled');
    } else {
      navbar.classList.remove('scrolled');
    }
    updateActiveNav();
    toggleBackToTop();
  });

  // 移动端菜单
  navToggle.addEventListener('click', function () {
    navToggle.classList.toggle('open');
    navMenu.classList.toggle('open');
  });

  // 点击导航链接关闭移动端菜单
  navLinks.forEach(function (link) {
    link.addEventListener('click', function () {
      navToggle.classList.remove('open');
      navMenu.classList.remove('open');
    });
  });

  // 根据滚动位置高亮当前导航项
  function updateActiveNav() {
    var sections = document.querySelectorAll('section[id]');
    var scrollPos = window.scrollY + 100;

    sections.forEach(function (section) {
      var top = section.offsetTop;
      var height = section.offsetHeight;
      var id = section.getAttribute('id');

      if (scrollPos >= top && scrollPos < top + height) {
        navLinks.forEach(function (link) {
          link.classList.remove('active');
          if (link.getAttribute('href') === '#' + id) {
            link.classList.add('active');
          }
        });
      }
    });
  }

  /* ===== 2. 标签切换 ===== */
  function initTabs(tabBarId) {
    var tabBar = document.getElementById(tabBarId);
    if (!tabBar) return;

    var tabBtns = tabBar.querySelectorAll('.tab-btn');

    tabBtns.forEach(function (btn) {
      btn.addEventListener('click', function () {
        var targetTab = btn.getAttribute('data-tab');

        // 取消所有 active
        tabBtns.forEach(function (b) { b.classList.remove('active'); });
        // 找到同 section 内所有 panel
        var section = btn.closest('.encyclopedia');
        var panels = section.querySelectorAll('.tab-panel');
        panels.forEach(function (p) { p.classList.remove('active'); });

        // 激活当前
        btn.classList.add('active');
        var targetPanel = document.getElementById(targetTab);
        if (targetPanel) targetPanel.classList.add('active');
      });
    });
  }

  initTabs('chickenTabs');
  initTabs('monkeyTabs');

  /* ===== 3. 数字滚动动画 ===== */
  function animateNumber(el, target, duration) {
    var start = 0;
    var startTime = null;

    function step(timestamp) {
      if (!startTime) startTime = timestamp;
      var progress = Math.min((timestamp - startTime) / duration, 1);
      var current = Math.floor(progress * target);
      el.textContent = current.toLocaleString();
      if (progress < 1) {
        requestAnimationFrame(step);
      }
    }

    requestAnimationFrame(step);
  }

  // 当 Hero 区域可见时启动数字动画
  var heroStats = document.querySelector('.hero-stats');
  if (heroStats) {
    var statNums = document.querySelectorAll('.stat-num');
    var observer = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          statNums.forEach(function (el) {
            var target = parseInt(el.getAttribute('data-target'), 10);
            animateNumber(el, target, 2000);
          });
          observer.disconnect();
        }
      });
    }, { threshold: 0.3 });
    observer.observe(heroStats);
  }

  /* ===== 4. 滚动渐入动画 ===== */
  var revealObserver = new IntersectionObserver(function (entries) {
    entries.forEach(function (entry) {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.1 });

  // 给卡片添加 reveal 类
  document.querySelectorAll('.info-card, .breed-card, .fact-item, .vs-side, .compare-conclusion, .daily-feature-card, .daily-list-item').forEach(function (el) {
    el.classList.add('reveal');
    revealObserver.observe(el);
  });

  /* ===== 5. 日期工具 ===== */
  function getDayOfYear(date) {
    var start = new Date(date.getFullYear(), 0, 0);
    var diff = date - start;
    return Math.floor(diff / (1000 * 60 * 60 * 24));
  }

  function formatDate(date) {
    var months = ['1月', '2月', '3月', '4月', '5月', '6月', '7月', '8月', '9月', '10月', '11月', '12月'];
    var weeks = ['周日', '周一', '周二', '周三', '周四', '周五', '周六'];
    return months[date.getMonth()] + date.getDate() + '日 · ' + weeks[date.getDay()];
  }

  /* ===== 6. 每日趣闻 ===== */
  var today = new Date();
  var dayOfYear = getDayOfYear(today);
  var dailyIndex = dayOfYear % dailyFacts.length;

  // 获取今日数据
  function getDailyFact(index) {
    return dailyFacts[index % dailyFacts.length];
  }

  // 渲染顶部每日横幅
  function renderDailyBanner() {
    var fact = getDailyFact(dailyIndex);
    var dateEl = document.getElementById('todayDate');
    var emojiEl = document.getElementById('dailyEmoji');
    var titleEl = document.getElementById('dailyTitle');
    var bodyEl = document.getElementById('dailyBody');
    var tagEl = document.getElementById('dailyTag');

    if (dateEl) dateEl.textContent = formatDate(today);
    if (emojiEl) emojiEl.textContent = fact.emoji;
    if (titleEl) titleEl.textContent = fact.title;
    if (bodyEl) bodyEl.textContent = fact.body;
    if (tagEl) {
      tagEl.textContent = fact.cat;
      tagEl.classList.toggle('monkey-tag', fact.cat === '猴');
    }
  }

  // 渲染每日趣闻区域 - 今日大卡片
  function renderDailyFeature() {
    var fact = getDailyFact(dailyIndex);
    var dateEl = document.getElementById('featureDate');
    var catEl = document.getElementById('featureCat');
    var emojiEl = document.getElementById('featureEmoji');
    var titleEl = document.getElementById('featureTitle');
    var bodyEl = document.getElementById('featureBody');

    if (dateEl) dateEl.textContent = fact.date;
    if (catEl) {
      catEl.textContent = fact.cat;
      catEl.classList.toggle('monkey-cat', fact.cat === '猴');
    }
    if (emojiEl) emojiEl.textContent = fact.emoji;
    if (titleEl) titleEl.textContent = fact.title;
    if (bodyEl) bodyEl.textContent = fact.body;
  }

  // 渲染近期趣闻列表（显示前7天和后7天的内容）
  function renderDailyList() {
    var listEl = document.getElementById('dailyList');
    if (!listEl) return;

    var html = '';
    for (var i = 1; i <= 7; i++) {
      var idx = (dailyIndex - i + dailyFacts.length) % dailyFacts.length;
      var fact = dailyFacts[idx];
      html += '<div class="daily-list-item" data-index="' + idx + '">' +
        '<div class="daily-list-emoji">' + fact.emoji + '</div>' +
        '<div class="daily-list-text">' +
        '<div class="daily-list-title">' + fact.title + '</div>' +
        '<div class="daily-list-date">' + fact.date + ' · ' + fact.cat + '</div>' +
        '</div></div>';
    }
    listEl.innerHTML = html;

    // 点击列表项可以查看该条趣闻
    listEl.querySelectorAll('.daily-list-item').forEach(function (item) {
      item.addEventListener('click', function () {
        var idx = parseInt(this.getAttribute('data-index'), 10);
        var fact = dailyFacts[idx];
        var dateEl = document.getElementById('featureDate');
        var catEl = document.getElementById('featureCat');
        var emojiEl = document.getElementById('featureEmoji');
        var titleEl = document.getElementById('featureTitle');
        var bodyEl = document.getElementById('featureBody');

        if (dateEl) dateEl.textContent = fact.date;
        if (catEl) {
          catEl.textContent = fact.cat;
          catEl.classList.toggle('monkey-cat', fact.cat === '猴');
        }
        if (emojiEl) emojiEl.textContent = fact.emoji;
        if (titleEl) titleEl.textContent = fact.title;
        if (bodyEl) bodyEl.textContent = fact.body;

        // 平滑滚动到大卡片
        var featureCard = document.getElementById('dailyFeatureCard');
        if (featureCard) {
          featureCard.scrollIntoView({ behavior: 'smooth', block: 'center' });
          featureCard.style.animation = 'none';
          setTimeout(function () {
            featureCard.style.animation = 'fadeInUp 0.5s ease';
          }, 10);
        }
      });
    });
  }

  // 随机刷新（换一条）
  var refreshBtn = document.getElementById('dailyRefresh');
  if (refreshBtn) {
    var randomIndex = dailyIndex;
    refreshBtn.addEventListener('click', function () {
      var newIndex;
      do {
        newIndex = Math.floor(Math.random() * dailyFacts.length);
      } while (newIndex === randomIndex && dailyFacts.length > 1);
      randomIndex = newIndex;
      var fact = dailyFacts[newIndex];

      var emojiEl = document.getElementById('dailyEmoji');
      var titleEl = document.getElementById('dailyTitle');
      var bodyEl = document.getElementById('dailyBody');
      var tagEl = document.getElementById('dailyTag');

      if (emojiEl) emojiEl.textContent = fact.emoji;
      if (titleEl) titleEl.textContent = fact.title;
      if (bodyEl) bodyEl.textContent = fact.body;
      if (tagEl) {
        tagEl.textContent = fact.cat;
        tagEl.classList.toggle('monkey-tag', fact.cat === '猴');
      }

      // 动画
      var card = document.getElementById('dailyCard');
      if (card) {
        card.style.animation = 'none';
        setTimeout(function () {
          card.style.animation = 'fadeInUp 0.4s ease';
        }, 10);
      }
    });
  }

  renderDailyBanner();
  renderDailyFeature();
  renderDailyList();

  /* ===== 7. 冷知识渲染 ===== */
  function renderFacts(listId, facts) {
    var container = document.getElementById(listId);
    if (!container) return;

    var html = '';
    facts.forEach(function (fact) {
      html += '<div class="fact-item">' +
        '<div class="fact-number">' + fact.num + '</div>' +
        '<div class="fact-text">' + fact.text + '</div>' +
        '</div>';
    });
    container.innerHTML = html;

    // 重新观察新添加的元素
    container.querySelectorAll('.fact-item').forEach(function (el) {
      el.classList.add('reveal');
      revealObserver.observe(el);
    });
  }

  renderFacts('chickenFactsList', chickenFacts);
  renderFacts('monkeyFactsList', monkeyFacts);

  /* ===== 7.5 最新资讯 =====
   * 部署到线上（如 GitHub Pages）后，优先运行时拉取 ./daily.json，
   * 该文件由「每日自动更新」任务定时重写并推送到仓库，实现上线后每天自动更新。
   * 本地以 file:// 打开或离线时 fetch 会失败，则回退到内联的 window.DAILY_NEWS。
   */
  function paintNews(news) {
    var grid = document.getElementById('newsGrid');
    var empty = document.getElementById('newsEmpty');
    if (!grid) return;

    if (!news || news.length === 0) {
      if (empty) empty.style.display = 'block';
      return;
    }
    if (empty) empty.style.display = 'none';

    var html = '';
    news.forEach(function (item) {
      var catClass = item.category === '猴' ? 'cat-monkey' : 'cat-chicken';
      html += '<div class="news-card">' +
        '<div class="news-card-header">' +
        '<div class="news-card-emoji">' + item.emoji + '</div>' +
        '<div class="news-card-meta">' +
        '<span class="news-card-date">' + item.date + '</span>' +
        '<span class="news-card-tag ' + catClass + '">' + item.category + '</span>' +
        '</div>' +
        '</div>' +
        '<div class="news-card-body">' +
        '<h4>' + item.title + '</h4>' +
        '<p>' + item.body + '</p>' +
        '</div>' +
        '</div>';
    });
    grid.innerHTML = html;

    grid.querySelectorAll('.news-card').forEach(function (el) {
      el.classList.add('reveal');
      revealObserver.observe(el);
    });
  }

  function renderNews() {
    var grid = document.getElementById('newsGrid');
    if (!grid) return;

    // 兜底数据（内联，离线/本地可用）
    function fallback() {
      paintNews((typeof window.DAILY_NEWS !== 'undefined') ? window.DAILY_NEWS : []);
    }

    // 优先运行时拉取线上数据
    if (typeof fetch === 'function') {
      fetch('./daily.json', { cache: 'no-store' })
        .then(function (res) { return res.ok ? res.json() : Promise.reject(); })
        .then(function (data) { paintNews(Array.isArray(data) ? data : []); })
        .catch(function () { fallback(); });
    } else {
      fallback();
    }
  }

  renderNews();

/* ===== 8. 趣味问答 ===== */
  var quizState = {
    currentQ: 0,
    score: 0,
    answered: false
  };

  var quizQuestionEl = document.getElementById('quizQuestion');
  var quizOptionsEl = document.getElementById('quizOptions');
  var quizFeedbackEl = document.getElementById('quizFeedback');
  var quizNextBtn = document.getElementById('quizNext');
  var quizResultEl = document.getElementById('quizResult');
  var quizProgressEl = document.getElementById('quizProgress');
  var progressFillEl = document.getElementById('progressFill');
  var quizRestartBtn = document.getElementById('quizRestart');

  function renderQuiz() {
    if (quizState.currentQ >= quizQuestions.length) {
      showQuizResult();
      return;
    }

    var q = quizQuestions[quizState.currentQ];
    quizState.answered = false;

    // 进度
    quizProgressEl.textContent = '第 ' + (quizState.currentQ + 1) + ' / ' + quizQuestions.length + ' 题';
    progressFillEl.style.width = ((quizState.currentQ + 1) / quizQuestions.length * 100) + '%';

    // 问题
    quizQuestionEl.textContent = q.q;

    // 选项
    var labels = ['A', 'B', 'C', 'D'];
    var html = '';
    q.options.forEach(function (opt, i) {
      html += '<button class="quiz-option" data-index="' + i + '">' +
        '<span class="opt-label">' + labels[i] + '</span>' +
        '<span>' + opt + '</span>' +
        '</button>';
    });
    quizOptionsEl.innerHTML = html;

    // 隐藏反馈和下一题按钮
    quizFeedbackEl.classList.remove('show', 'correct-fb', 'wrong-fb');
    quizNextBtn.style.display = 'none';

    // 绑定选项点击
    quizOptionsEl.querySelectorAll('.quiz-option').forEach(function (btn) {
      btn.addEventListener('click', function () {
        if (quizState.answered) return;
        handleQuizAnswer(parseInt(this.getAttribute('data-index'), 10));
      });
    });
  }

  function handleQuizAnswer(selectedIndex) {
    quizState.answered = true;
    var q = quizQuestions[quizState.currentQ];
    var options = quizOptionsEl.querySelectorAll('.quiz-option');
    var isCorrect = selectedIndex === q.answer;

    if (isCorrect) {
      quizState.score++;
      options[selectedIndex].classList.add('correct');
    } else {
      options[selectedIndex].classList.add('wrong');
      options[q.answer].classList.add('correct');
    }

    // 禁用所有选项
    options.forEach(function (opt) {
      opt.classList.add('disabled');
    });

    // 显示反馈
    quizFeedbackEl.classList.add('show');
    if (isCorrect) {
      quizFeedbackEl.classList.add('correct-fb');
      quizFeedbackEl.innerHTML = '✅ 答对了！' + q.explain;
    } else {
      quizFeedbackEl.classList.add('wrong-fb');
      quizFeedbackEl.innerHTML = '❌ 答错了。' + q.explain;
    }

    // 显示下一题按钮
    if (quizState.currentQ < quizQuestions.length - 1) {
      quizNextBtn.textContent = '下一题 →';
    } else {
      quizNextBtn.textContent = '查看结果 🏆';
    }
    quizNextBtn.style.display = 'inline-flex';
  }

  function showQuizResult() {
    // 隐藏问题和选项
    quizQuestionEl.style.display = 'none';
    quizOptionsEl.style.display = 'none';
    quizFeedbackEl.classList.remove('show');
    quizNextBtn.style.display = 'none';
    document.querySelector('.quiz-progress').style.display = 'none';

    quizResultEl.style.display = 'block';

    var titleEl = document.getElementById('resultTitle');
    var textEl = document.getElementById('resultText');
    var total = quizQuestions.length;
    var score = quizState.score;
    var percent = (score / total * 100).toFixed(0);

    var title, text;

    if (percent === '100') {
      title = '🏆 满分通关！';
      text = '太厉害了！你答对了全部 ' + total + ' 题。你对鸡和猴子的了解已经达到专家级别！';
    } else if (percent >= '75') {
      title = '🎉 优秀！';
      text = '你答对了 ' + score + ' / ' + total + ' 题（' + percent + '%）。你对鸡和猴子的知识掌握得很好！';
    } else if (percent >= '50') {
      title = '👍 还不错！';
      text = '你答对了 ' + score + ' / ' + total + ' 题（' + percent + '%）。继续探索本站了解更多有趣知识吧！';
    } else {
      title = '🌱 继续加油！';
      text = '你答对了 ' + score + ' / ' + total + ' 题（' + percent + '%）。多看看本站的百科内容，下次一定能做得更好！';
    }

    titleEl.textContent = title;
    textEl.textContent = text;
  }

  if (quizNextBtn) {
    quizNextBtn.addEventListener('click', function () {
      quizState.currentQ++;
      renderQuiz();
    });
  }

  if (quizRestartBtn) {
    quizRestartBtn.addEventListener('click', function () {
      quizState.currentQ = 0;
      quizState.score = 0;
      quizState.answered = false;
      quizQuestionEl.style.display = '';
      quizOptionsEl.style.display = '';
      document.querySelector('.quiz-progress').style.display = '';
      quizResultEl.style.display = 'none';
      renderQuiz();
    });
  }

  // 初始化问答
  renderQuiz();

  /* ===== 9. 返回顶部 ===== */
  var backToTopBtn = document.getElementById('backToTop');

  function toggleBackToTop() {
    if (window.scrollY > 500) {
      backToTopBtn.classList.add('show');
    } else {
      backToTopBtn.classList.remove('show');
    }
  }

  if (backToTopBtn) {
    backToTopBtn.addEventListener('click', function () {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  /* ===== 10. Hero 背景视差效果 ===== */
  var heroBg = document.querySelector('.hero-bg');
  if (heroBg) {
    window.addEventListener('scroll', function () {
      var scrollY = window.scrollY;
      if (scrollY < window.innerHeight) {
        heroBg.style.transform = 'translateY(' + scrollY * 0.3 + 'px)';
      }
    });
  }

})();
