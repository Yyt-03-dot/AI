import streamlit as st
import base64
import streamlit.components.v1 as components

_FW_FULLSCREEN = """
<script>
(function () {
  const pdoc = window.parent.document;
  const pwin = window.parent;

  // 1) 清掉上一次残留（rerun 时不会叠一堆 canvas）
  const old = pdoc.getElementById('fw-canvas');
  if (old) old.remove();

  // 2) 建一个覆盖全屏的 canvas
  const cv = pdoc.createElement('canvas');
  cv.id = 'fw-canvas';
  Object.assign(cv.style, {
    position: 'fixed', inset: '0',
    width: '100vw', height: '100vh',
    pointerEvents: 'none', zIndex: '9999'
  });
  pdoc.body.appendChild(cv);

  const ctx  = cv.getContext('2d');
  const dpr  = pwin.devicePixelRatio || 1;
  const colors = ['#ff6b9d','#ffd93d','#6bcbff','#a78bfa','#7bff9e','#ff9ecb'];
  let parts = [];

  function resize() {
    cv.width  = pwin.innerWidth  * dpr;
    cv.height = pwin.innerHeight * dpr;
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }
  resize();
  pwin.addEventListener('resize', resize);

  function boom(x, y) {
    for (let i = 0; i < 60; i++) {
      const a = Math.random() * Math.PI * 2;
      const s = Math.random() * 6 + 2;
      parts.push({
        x, y,
        vx: Math.cos(a) * s, vy: Math.sin(a) * s,
        life: 1,
        color: colors[(Math.random() * colors.length) | 0]
      });
    }
  }

  for (let i = 0; i < 5; i++) {
    setTimeout(() => boom(Math.random() * pwin.innerWidth,
                         Math.random() * pwin.innerHeight * 0.6 + 50), i * 300);
  }

  const start = Date.now();
  (function tick() {
    ctx.clearRect(0, 0, pwin.innerWidth, pwin.innerHeight);
    for (const p of parts) {
      p.x += p.vx; p.y += p.vy;
      p.vy += 0.05; p.vx *= 0.985; p.life -= 0.012;
      ctx.globalAlpha = Math.max(p.life, 0);
      ctx.fillStyle = p.color;
      ctx.beginPath();
      ctx.arc(p.x, p.y, 3 * Math.max(p.life, 0.2), 0, Math.PI * 2);
      ctx.fill();
    }
    parts = parts.filter(p => p.life > 0);
    if (Date.now() - start < 4000 || parts.length) {
      pwin.requestAnimationFrame(tick);
    } else {
      cv.remove();
    }
  })();

  // 3) iframe 被 Streamlit 销毁时，把 canvas 一并带走
  window.addEventListener('pagehide', () => cv.remove());
})();
</script>
"""


# ===== 原来的页面逻辑 =====
st.title("你最喜欢的角色是哪个？")

name = st.text_input("输入TA的名字：").strip()

answers = {
    "莉奈娅": "D:/新建文件夹/素材/“无解的眼神心像海底针～” [BV19xGg6EE3o].mp3",
}

if name:
    if name in answers:
        st.success(f"答对了！你也喜欢{name}呀 🎉")
        fireworks()
        st.audio(answers[name], autoplay=True)
    else:
        st.warning("不对哦，再猜猜～")