#!/usr/bin/env python3
"""Gugen corporate site: Cybozu header, kubell (Cvel) hero, Sansan UX, SoftBank company pages."""
from pathlib import Path
from content import NEWS, FAQ, WORKS, ARTICLES

ROOT = Path(__file__).resolve().parent

AX_URL = "https://www.gugen-kobo.com/ja"
HCI_URL = "https://human-centered-intelligence-lab.vercel.app/"
LAB_URL = "https://www.gugenlab.com/"

DECO = """
<svg class="deco" viewBox="0 0 420 70" aria-hidden="true">
  <path d="M0 22 C80 6,160 34,240 18 S360 8,420 24" fill="none" stroke="#00c4cc" stroke-width="2.2"/>
  <path d="M0 38 C90 18,170 48,260 32 S370 22,420 40" fill="none" stroke="#12abb1" stroke-width="1.8" opacity=".7"/>
  <path d="M0 52 C100 36,190 58,280 46 S380 40,420 54" fill="none" stroke="#00c4cc" stroke-width="1.4" opacity=".45"/>
</svg>
"""

# (label, href, external)
NAV = [
    ("事業内容", "/service/", [
        ("具現AX", AX_URL, True),
        ("任せた", "/service/makaseta/", False),
        ("人間知能意識研究所", HCI_URL, True),
        ("人材育成事業", "/service/education/", False),
        ("プロジェクト・実績", "/works/", False),
    ]),
    ("会社概要", "/philosophy/", [
        ("理念", "/philosophy/mission/", False),
        ("ビジョン", "/philosophy/vision/", False),
        ("代表挨拶", "/philosophy/message/", False),
        ("カルチャー", "/philosophy/culture/", False),
        ("会社情報", "/company/", False),
        ("Leaders", "/company/management/", False),
        ("アクセス", "/company/access/", False),
    ]),
    ("ニュース", "/news/", []),
    ("採用情報", "/recruit/", [
        ("採用情報", "/recruit/", False),
        ("なぜGugenか", "/recruit/#why", False),
        ("募集職種", "/recruit/#roles", False),
        ("インターン応募", "/recruit/apply.html", False),
        ("カジュアル面談", "/casual-meeting/", False),
    ]),
]


def _link(t, h, ext=False):
    extra = ' target="_blank" rel="noopener"' if ext else ""
    mark = '<span class="ext" aria-hidden="true"></span>' if ext else ""
    return f'<a href="{h}"{extra}>{t}{mark}</a>'


def header(title="Gugen | 人は、まだ進化できる。", desc=None):
    if not desc:
        desc = "Gugen株式会社は「人は、まだ進化できる。」を経営理念に、具現AX、任せた、人間知能意識研究所、人材育成事業を展開するテクノロジーカンパニーです。"
    items = []
    sp = []
    for label, href, subs in NAV:
        mega = ""
        if subs:
            mega = (
                '<div class="mega">'
                f'<a class="mega-top" href="{href}">{label} トップ</a>'
                + "".join(_link(t, h, ext) for t, h, ext in subs)
                + "</div>"
            )
        items.append(f'<li class="gnav-item"><a href="{href}">{label}</a>{mega}</li>')
        if subs:
            sub = "".join(_link(t, h, ext) for t, h, ext in subs)
            sp.append(
                f'<div class="sp-acc"><button type="button">{label}</button>'
                f'<div class="sub"><a href="{href}">{label} トップ</a>{sub}</div></div>'
            )
        else:
            sp.append(f'<div class="sp-acc"><a href="{href}">{label}</a></div>')
    return f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="/favicon.ico">
<link rel="apple-touch-icon" href="/images/icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Heebo:wght@500;700&family=Lato:wght@400;700&family=Noto+Sans+JP:wght@400;500;700;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/style.css?v=gugenhp1">
</head>
<body>
<a class="skip" href="#main">このページの本文へ移動</a>
<header class="header" id="header">
  <div class="header-top">
    <div class="header-widgets">
      <button class="js-search-open" type="button">サイト内検索</button>
      <a href="/sitemap/">サイトマップ</a>
    </div>
    <div class="header-contact">
      <a href="/recruit/">採用情報</a>
      <a href="/contact/">お問い合わせ</a>
      <div class="tel">導入相談　<a href="mailto:info@gugenlab.com"><strong>info@gugenlab.com</strong></a></div>
    </div>
  </div>
  <div class="header-brand">
    <a href="/" rel="home"><img src="/images/logo-gugen.png" alt="Gugen"></a>
  </div>
  <button class="hamburger" type="button" aria-label="メニュー"><i></i><i></i><i></i></button>
  <nav class="gnav" aria-label="グローバルナビゲーション">
    <ul class="gnav-list">{"".join(items)}</ul>
  </nav>
  <div class="sp-menu">
    {"".join(sp)}
    <div class="sp-acc"><a href="/recruit/">採用情報</a></div>
    <div class="sp-acc"><a href="/contact/">お問い合わせ</a></div>
  </div>
  <div class="search-panel" id="search-overlay">
    <form action="/search/" method="get">
      <input type="search" name="q" placeholder="キーワードで検索する" aria-label="サイト内検索">
      <button type="submit">検索</button>
    </form>
  </div>
</header>
"""


def recruit_cta():
    return """
<section class="recruit">
  <div class="recruit-inner">
    <div>
      <h2>私たちは一緒に働く<br>メンバーを探しています。</h2>
      <p>2026年7月設立、4人の会社です。いま募集しているのはインターンだけ。時間も場所も指定せず、お客さまに出すものを任せます。</p>
      <p>ミッション・バリューへの共感を何よりも大切に考え、一緒に働くメンバーを探しています。</p>
      <div class="btns">
        <a class="btn" href="/recruit/">採用情報</a>
        <a class="btn btn-ghost" href="/casual-meeting/">カジュアル面談</a>
      </div>
    </div>
    <div class="mosaic">
      <img src="/images/sustain/society.jpg" alt="">
      <img src="/images/team/yukito-go.jpg" alt="">
      <img src="/images/team/taiki-mishima.png" alt="">
      <img src="/images/philosophy/message.jpg" alt="">
    </div>
  </div>
</section>
"""


def footer():
    cols = []
    for label, href, subs in NAV:
        if subs:
            kids = "".join(_link(t, h, ext) for t, h, ext in subs)
        else:
            kids = _link(label, href)
        cols.append(f'<div><h3><a href="{href}">{label}</a></h3>{kids}</div>')
    return f"""
<footer class="footer">
  <div class="footer-inner">
    <a class="logo" href="/"><span class="logo-mark"></span><img src="/images/logo-gugen-white.png" alt="Gugen"></a>
    <div class="footer-nav">{"".join(cols)}</div>
    <div class="footer-sub">
      <a href="/privacy/">個人情報保護への対応</a>
      <a href="/security/">情報セキュリティ方針</a>
      <a href="/legal/transactions.html">特定商取引法に基づく表記</a>
      <a href="/legal/">決算公告</a>
      <a href="/contact/">お問い合わせ</a>
      <a href="/sitemap/">サイトマップ</a>
    </div>
    <p class="footer-copy">&copy; Gugen Inc.</p>
  </div>
</footer>
<script src="/js/main.js"></script>
</body></html>
"""


def related(items):
    cards = []
    for href, img, label in items:
        extra = ' target="_blank" rel="noopener"' if href.startswith("http") else ""
        cards.append(
            f'<a class="link-card" href="{href}"{extra}><img src="{img}" alt=""><div class="txt">{label}</div></a>'
        )
    return f'<div class="related"><h2>関連ページ</h2><div class="link-cards">{"".join(cards)}</div></div>'


def page(title, en, h1, body, rel=None, extra=""):
    rel_html = related(rel) if rel else ""
    return (
        header(f"{title} | Gugen株式会社")
        + f"""<main id="main">
<div class="page-hero">
  <p class="en">{en}</p>
  <h1>{h1}</h1>
  {DECO}
</div>
<div class="page-body">{body}</div>
{rel_html}
{extra}
{recruit_cta()}
</main>
"""
        + footer()
    )


def write(rel, html):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(html, encoding="utf-8")
    print("wrote", rel)


ABOUT_REL = [
    ("/about/", "/images/philosophy/hero.jpg", "私たちについて"),
    ("/service/", "/images/segments/os.jpg", "サービス"),
    ("/company/", "/images/philosophy/about-hero.jpg", "会社情報"),
]
COMP_REL = [
    ("/company/", "/images/philosophy/about-hero.jpg", "会社情報"),
    ("/company/management/", "/images/team/yukito-go.jpg", "Leaders"),
    ("/company/access/", "/images/philosophy/about-hero.jpg", "アクセス"),
]
SVC_REL = [
    (AX_URL, "/images/segments/ax.jpg", "具現AX"),
    ("/service/makaseta/", "/images/segments/os.jpg", "任せた"),
    (HCI_URL, "/images/segments/research.jpg", "人間知能意識研究所"),
    ("/service/education/", "/images/segments/lab.jpg", "人材育成事業"),
    ("/works/", "/images/kv/kv02.jpg", "プロジェクト・実績"),
]
PHI_REL = [
    ("/philosophy/mission/", "/images/philosophy/hero.jpg", "理念"),
    ("/philosophy/vision/", "/images/philosophy/vision.jpg", "ビジョン"),
    ("/philosophy/message/", "/images/philosophy/message.jpg", "代表挨拶"),
    ("/philosophy/culture/", "/images/philosophy/strategy.jpg", "カルチャー"),
]


def home():
    news_items = []
    for n in NEWS[:5]:
        news_items.append(
            f'<a class="news-item" href="/news/"><span class="date">{n["date"]}</span>'
            f'<span class="cat">{n["cat"]}</span><h3>{n["title"]}</h3></a>'
        )
    return header() + f"""
<main id="main">
  <section class="fv" aria-label="キービジュアル">
    <video autoplay muted loop playsinline poster="/images/kv/kv01.jpg">
      <source src="/video/hero.mp4" type="video/mp4">
    </video>
    <div class="fv-inner">
      <p class="fv-brand">Gugen</p>
      <h1>見えないものを、<br>形にする。</h1>
      <p class="lead">企業のAI活用を、要件定義から実装・社内定着まで伴走します。<br>自社の業務も、自分たちでつくったシステムで回しています。</p>
    </div>
    <a class="scroll" href="#mission">SCROLL</a>
  </section>

  <section class="mission" id="mission">
    <div>
      <p class="kicker">MISSION</p>
      <h2>人は、<br>まだ進化できる。</h2>
      {DECO}
      <a class="btn" href="/philosophy/mission/">理念を見る</a>
    </div>
    <div class="copy">
      <p>社名のGugenは「具現」——見えないものに形を与えること。人も組織も社会も、いまの姿が完成形ではありません。構想を磨き、実装し、学び直す。その反復によって、まだ見えていない可能性へ進めると私たちは信じています。</p>
      <p>AIは、この数年で「使えるかどうか」から「どう使うか」の議論へ移りました。道具は十分に揃っています。それでも、多くの現場ではアイデアが形にならないまま止まっています。技術がないから。時間がないから。判断できる人がいないから。私たちはその停滞を、時代の必然ではなく、設計で解ける課題だと考えています。</p>
    </div>
  </section>

  <section class="section" id="business">
    <div class="section-inner">
      <p class="en">Business</p>
      <h2>事業内容</h2>
      <p class="lead">変える「具現AX」とつくる「任せた」を両輪で回し、実装と変革の現場で人を育てる。そこで得た知見と収益を「人間知能意識研究所」の研究に投じ、研究から生まれたものは会社に帰属して再び事業になる。</p>
      <div class="biz-grid">
        <a class="biz-card" href="{AX_URL}" target="_blank" rel="noopener">
          <img src="/images/segments/ax.jpg" alt="">
          <div class="body">
            <p class="k">変える / 組織変革　LPへ</p>
            <h3>具現AX</h3>
            <p>御社専属のAIコンシェルジュ。業務を棚卸ししてどこをAIに任せるかを設計し、AI顧問・コンサル・研修として社内で回せる状態まで並走します。</p>
          </div>
        </a>
        <a class="biz-card" href="/service/makaseta/">
          <img src="/images/segments/os.jpg" alt="">
          <div class="body">
            <p class="k">つくる / AI実装</p>
            <h3>任せた</h3>
            <p>チャットボット・AIエージェント・業務自動化からハードウェアまで。要件定義からPoC・実装・運用までをプロトコル化し、仕事を任せられる状態をつくります。</p>
          </div>
        </a>
        <a class="biz-card" href="{HCI_URL}" target="_blank" rel="noopener">
          <img src="/images/segments/research.jpg" alt="">
          <div class="body">
            <p class="k">研究する / HCI　研究所サイトへ</p>
            <h3>人間知能意識研究所</h3>
            <p>人とAIの関係を問い直す研究開発機関。受託と顧問で積み上げた技術と収益を研究に還流させ、複数のプロジェクトを並行して進めます。</p>
          </div>
        </a>
        <a class="biz-card" href="/service/education/">
          <img src="/images/segments/lab.jpg" alt="">
          <div class="body">
            <p class="k">育てる / 学生支援</p>
            <h3>人材育成事業</h3>
            <p>AIXと連携し、学生のAI実践とキャリア形成を支援します。Gugen Labのコミュニティを起点に、学ぶ場と働く機会をつなぎます。</p>
          </div>
        </a>
      </div>
      <a class="btn" href="/service/">事業内容を見る</a>
    </div>
  </section>

  <section class="section section-soft">
    <div class="section-inner">
      <p class="en">Company</p>
      <h2>会社概要</h2>
      <p class="lead">理念からカルチャーまで。Gugenが何を大切にし、どこへ向かうかをまとめています。</p>
      <div class="phi-grid">
        <a class="phi-card" href="/philosophy/mission/"><img src="/images/philosophy/hero.jpg" alt=""><span>理念</span></a>
        <a class="phi-card" href="/philosophy/vision/"><img src="/images/philosophy/vision.jpg" alt=""><span>ビジョン</span></a>
        <a class="phi-card" href="/philosophy/message/"><img src="/images/philosophy/message.jpg" alt=""><span>代表挨拶</span></a>
        <a class="phi-card" href="/philosophy/culture/"><img src="/images/philosophy/strategy.jpg" alt=""><span>カルチャー</span></a>
      </div>
      <a class="btn btn-ghost" href="/philosophy/">会社概要トップ</a>
    </div>
  </section>

  <section class="section">
    <div class="section-inner">
      <p class="en">News</p>
      <h2>ニュース</h2>
      <div class="news-list">{"".join(news_items)}</div>
      <a class="btn btn-ghost" href="/news/">ニュース一覧</a>
    </div>
  </section>

  <div class="twin">
    <a href="/company/"><img src="/images/philosophy/about-hero.jpg" alt=""><span class="label">会社情報</span></a>
    <a href="/recruit/"><img src="/images/sustain/society.jpg" alt=""><span class="label">採用情報</span></a>
  </div>

  {recruit_cta()}
</main>
""" + footer()


def about_page():
    body = """
<div class="prose" id="katachi">
<p>経営理念、Vision、Values、Cultureと会社情報をまとめています。</p>
<p>AIは、この数年で「使えるかどうか」から「どう使うか」の議論へ移りました。道具は十分に揃っています。それでも、多くの現場ではアイデアが形にならないまま止まっています。技術がないから。時間がないから。判断できる人がいないから。私たちはその停滞を、時代の必然ではなく、設計で解ける課題だと考えています。</p>
</div>
<div class="section" style="padding-left:0;padding-right:0">
  <p class="en" style="color:var(--teal-3)">MISSION</p>
  <h2 style="font-size:clamp(2.8rem,4vw,4.4rem);font-weight:700;margin:8px 0 16px">人は、まだ進化できる。</h2>
  <div class="prose">
    <p>社名のGugenは「具現」——見えないものに形を与えること。人も組織も社会も、いまの姿が完成形ではありません。構想を磨き、実装し、学び直す。その反復によって、まだ見えていない可能性へ進めると私たちは信じています。</p>
    <h2>導入して終わりにしない。</h2>
    <p>私たちは、思いつきを語るだけの会社でも、技術を納めて終わる会社でもありません。物事の奥を深く見て、未来から逆算し、小さく試す。そこで勝ち筋が見えた構想を、現場で使われる状態まで持っていくところまでを仕事にします。</p>
    <h2>3つのサービスと、1つの研究機関</h2>
    <p>「Gugen Lab」でAIに関心のある学生・若手の接点をつくり、「Gugen OS」でAI受託開発とハードウェアをプロトコル化し、「Gugen AX」でAI顧問・コンサル・研修として中小企業の業務をAIネイティブへ移す。この3つで得た知見と収益を、社内研究組織である「人間知能・意識研究所」に投じます。研究所はAIと接した人間の側に何が起きたかを測ります。研究から生まれたものは会社に帰属し、再び事業として展開します。現時点で、効果を示すデータはありません。</p>
    <h2>小さく出して、動かしながら更新する</h2>
    <p>完成してから世に出すのではなく、最小の形で出し、現場で動かしながら磨いていく。個別の実装で得たパターンは、再利用可能な資産として積み上げていく。属人性に頼らず、再現性のある形でAIを実装すること。それが、私たちが選んだやり方です。</p>
    <p>設立は、ゴールではなく出発点です。誰もが未来の創り手として生きる時代へ。学び続け、己を磨き、これからも手を動かし続けます。</p>
    <p>Gugen株式会社 代表取締役<br>郷 由稀斗</p>
  </div>
</div>
<div id="values">
  <p class="en" style="color:var(--teal-3)">VALUES</p>
  <h2 style="font-size:clamp(2.4rem,3vw,3.6rem);font-weight:700;margin:8px 0 16px">Vision</h2>
  <div class="prose">
    <p>どんな世界をつくるか</p>
    <p style="font-size:2.2rem;font-weight:700">誰もが未来の創り手として生きる時代へ。</p>
    <p>私たちのビジョンは「創りたいを創れる社会を創る」です。アイデアはあるのに、技術がない。やりたいのに、時間がない。そうした「創りたい」と「創れる」の間にある壁を、AIと職人のクラフトで取り除いていきます。</p>
  </div>
  <div class="values">
    <div class="value"><p class="n">01</p><h3>深観</h3><p>物事の奥を深く見る。</p></div>
    <div class="value"><p class="n">02</p><h3>造形</h3><p>見えないものに形を与える。</p></div>
    <div class="value"><p class="n">03</p><h3>逆算</h3><p>未来から今を選ぶ。</p></div>
    <div class="value"><p class="n">04</p><h3>試斬</h3><p>小さく試し、勝ち筋を見極める。</p></div>
    <div class="value"><p class="n">05</p><h3>美勝</h3><p>美しく勝つ。</p></div>
  </div>
  <div class="prose">
    <h2>Culture</h2>
    <p>鍛錬</p>
    <p>学び続け、己を磨き、未来をつくる。</p>
  </div>
</div>
<div id="logo" class="prose" style="margin-top:48px">
  <p><img src="/images/logo-gugen.png" alt="Gugenのロゴ" style="width:240px"></p>
  <h2>Our Symbol　ロゴに込めた想い</h2>
  <p>シンボルは、まだ輪郭のないアイデアを受け止める「器」と、そこから立ち上がる形を表しています。閉じた枠ではなく、外へひらかれた線にすることで、可能性を決めつけない姿勢を込めました。</p>
  <p>見えないものを受け取り、手を動かし、現実にする。それがGugenの仕事です。</p>
</div>
"""
    return page("私たちについて", "About", "私たちについて", body, ABOUT_REL)


def service_index():
    body = f"""
<div class="prose">
<p>変える「具現AX」とつくる「任せた」を両輪で回し、実装と変革の現場で人を育てる。そこで得た知見と収益を「人間知能意識研究所」の研究に投じ、研究から生まれたものは会社に帰属して再び事業になる。</p>
</div>
<div class="biz-grid" style="margin:40px 0">
  <a class="biz-card" href="{AX_URL}" target="_blank" rel="noopener"><img src="/images/segments/ax.jpg" alt=""><div class="body"><p class="k">変える / 組織変革</p><h3>具現AX</h3><p>御社専属のAIコンシェルジュとして、内製化まで並走します。</p></div></a>
  <a class="biz-card" href="/service/makaseta/"><img src="/images/segments/os.jpg" alt=""><div class="body"><p class="k">つくる / AI実装</p><h3>任せた</h3><p>要件定義から実装・運用までをプロトコル化し、仕事を任せられる状態をつくります。</p></div></a>
  <a class="biz-card" href="{HCI_URL}" target="_blank" rel="noopener"><img src="/images/segments/research.jpg" alt=""><div class="body"><p class="k">研究する / HCI</p><h3>人間知能意識研究所</h3><p>人とAIの関係を問い直す研究開発機関です。</p></div></a>
  <a class="biz-card" href="/service/education/"><img src="/images/segments/lab.jpg" alt=""><div class="body"><p class="k">育てる / 学生支援</p><h3>人材育成事業</h3><p>AIXと連携し、学生のAI実践とキャリア形成を支援します。</p></div></a>
</div>
<div class="prose">
<h2>具現AX　すべての企業に、AIを。</h2>
<p>御社専属のAIコンシェルジュ。業務を棚卸ししてどこをAIに任せるかを設計し、AI顧問・コンサル・研修として社内で回せる状態まで並走します。専用のランディングページで、サービス内容・料金・実績をご覧いただけます。</p>
<p><a class="btn" href="{AX_URL}" target="_blank" rel="noopener">具現AXのサイトへ</a></p>
<h2>任せた　仕事を、任せた。</h2>
<p>チャットボット・AIエージェント・業務自動化からハードウェアまで。要件定義からPoC・実装・運用までをプロトコル化し、磨いたパターンを再利用可能な資産にします。LP公開までのあいだ、概要はこのサイトでご覧いただけます。</p>
<p><a class="btn btn-ghost" href="/service/makaseta/">任せたの概要を見る</a></p>
<h2>人間知能意識研究所</h2>
<p>人とAIの関係を問い直す研究開発機関。受託と顧問で積み上げた技術と収益を研究に還流させます。研究所サイトで、研究領域とプロジェクトをご覧いただけます。</p>
<p><a class="btn" href="{HCI_URL}" target="_blank" rel="noopener">研究所サイトへ</a></p>
<h2>人材育成事業　学生と、次の実装者を育てる。</h2>
<p>AIXと連携し、学生支援を軸にした人材育成を進めていきます。Gugen Labのコミュニティを起点に、学ぶ場と働く機会をつなぎます。</p>
<p><a class="btn btn-ghost" href="/service/education/">人材育成事業の概要を見る</a></p>
</div>
"""
    return page("事業内容", "Business", "事業内容", body, SVC_REL)


def service_makaseta():
    body = """
<div class="prose">
<p>つくる / AI実装　稼働中　旧称 Gugen OS</p>
<h2>仕事を、任せた。</h2>
<p>繰り返せる仕事はAIへ。人は、判断と意志に時間を使う。それが「任せた」の出発点です。</p>
<p>チャットボット・AIエージェント・業務自動化からハードウェアまで。要件定義からPoC・実装・運用までをプロトコル化し、磨いたパターンを再利用可能な資産にします。LP・HP、チャットボット、AIエージェント、業務自動化、そしてハードウェア開発までを一気通貫で扱い、初期費用ゼロ・月額制・最短翌日納品で、属人化に頼らず再現性のあるAI実装を最短で動かします。</p>
<p>専用LPは準備中です。いまは概要と進め方を、このページでご確認ください。動くデモは <a href="https://app.gugen-kobo.com/" target="_blank" rel="noopener">デモカタログ</a> でもご覧いただけます。</p>
<p><a href="/works/">実装実績を見る</a></p>
<h2>何を任せられるか</h2>
<ul>
<li>社内ナレッジを根拠に一次対応するチャットボット</li>
<li>問い合わせ・予約・事務作業の自動化エージェント</li>
<li>コーポレートサイト・LPの企画から実装</li>
<li>PoCから本開発への段階的なスケール</li>
<li>ハードウェア試作を含む実装</li>
</ul>
<h2>プロトコルで段階的にスケールする4ステップ</h2>
<ol class="steps">
<li><h3>PoC・要件定義</h3><p>最短1営業日で着手。検証スコープを切り出し、動くものから議論を始めます。</p></li>
<li><h3>LP/HP・チャットボット</h3><p>標準化した手順で短納期に納品。Webサイト・社内チャットボット・資料請求の自動化まで一気通貫で。</p></li>
<li><h3>AIエージェント・本開発</h3><p>業務自動化・カスタム実装・SaaS開発まで。月額制で小さく始めて伸ばせます。</p></li>
<li><h3>保守運用・ハードウェア</h3><p>Slack伴走と月次MTGで運用を続けます。ドキュメントを残し、属人化を防ぎます。</p></li>
</ol>
<h2>こんなときに</h2>
<p>つくるものが決まっている。動くものを早く見たい。自社で回せる状態まで持っていきたい。入口は「任せた」です。何をAIに任せるかから一緒に考えたい場合は、具現AXが先になります。</p>
</div>
"""
    return page("任せた", "Makaseta", "任せた", body, SVC_REL)


def service_ax():
    body = f"""
<div class="prose">
<p>変える / 組織変革　稼働中</p>
<h2>すべての企業に、AIを。</h2>
<p>御社専属のAIコンシェルジュ。業務を棚卸ししてどこをAIに任せるかを設計し、AI顧問・コンサル・研修として社内で回せる状態まで並走します。</p>
<p>サービス詳細・料金・導入の流れは、具現AXのランディングページをご覧ください。</p>
<p><a class="btn" href="{AX_URL}" target="_blank" rel="noopener">具現AXのサイトへ</a></p>
<h2>現場に入り、内製化まで並走する4ステップ</h2>
<ol class="steps">
<li><h3>業務の棚卸し</h3><p>現場に入って業務を洗い出し、AIに任せられる範囲と残すべき人の判断を切り分けます。</p></li>
<li><h3>AI顧問</h3><p>御社専属のAIコンシェルジュとして、ツール選定から運用ルールまで継続的に相談を受けます。</p></li>
<li><h3>AIコンサルティング</h3><p>導入計画・費用対効果・体制設計まで、経営の意思決定に必要な材料を揃えます。</p></li>
<li><h3>AI研修監修・内製化</h3><p>社員向け研修を設計・監修し、社内で回せる状態になるまで並走します。</p></li>
</ol>
</div>
"""
    return page("具現AX", "Gugen AX", "具現AX", body, SVC_REL)


def service_education():
    body = f"""
<div class="prose">
<p>育てる / 学生支援事業　展開予定</p>
<h2>学生と、次の実装者を育てる。</h2>
<p>Gugenは、実装の現場で人を育てる会社です。いまはAIXと連携し、学生がAIを「触る」段階から「現場で使える」段階までを支援する事業を進めていきます。専用LPは準備中のため、現時点の考え方と活動をここにまとめています。</p>
<h2>なぜ、学生支援か</h2>
<p>AIを触れる人は増えました。足りないのは、顧客の業務を聞いて、どこに入れるかを決めて、使われる状態まで持っていける人です。その力は、座学だけでは身につきません。実際の案件とコミュニティの往復のなかで育ちます。</p>
<p>AIXとの連携は、学ぶ場と実践の場を一本の道にするためのものです。学生が現場の課題に触れ、手を動かし、次のキャリアへ進める状態をつくります。</p>
<h2>いま動いていること — Gugen Lab</h2>
<p>人材育成の土台として、学生・若手向けAIコミュニティ「Gugen Lab」を運営しています。</p>
<p><a href="{LAB_URL}" target="_blank" rel="noopener">Gugen Lab を見る</a></p>
<ol class="steps">
<li><h3>朝AIニュース（LINE OC）</h3><p>毎日9時にLINEオープンチャットへAI最新情報を配信。2026年4月28日から継続稼働中。</p></li>
<li><h3>ハッカソン（月1開催）</h3><p>学生チームが1日でAIプロダクトをつくる。第1回は約100名が参加しました。</p></li>
<li><h3>モクモク会</h3><p>夜のオンライン作業会。継続的に手を動かすコアメンバーを育てる場です。</p></li>
<li><h3>企業・事業への接続</h3><p>課題を持つ企業を具現AX・任せたへつなぎ、参加者はインターン・業務委託の候補にもなります。</p></li>
</ol>
<h2>これから</h2>
<p>AIXと連携した学生支援のプログラム、企業課題の持ち込み、採用接続を順次開いていきます。企業として関わりたい方、学生として参加したい方は、お問い合わせください。</p>
<p><a class="btn" href="/contact/">相談する</a>　<a class="btn btn-ghost" href="/recruit/">採用情報を見る</a></p>
</div>
"""
    return page("人材育成事業", "Education", "人材育成事業", body, SVC_REL)


def service_lab():
    return service_education()


def service_os():
    return service_makaseta()


def service_research():
    body = f"""
<div class="prose">
<p>Human-Centered Intelligence Lab　研究中</p>
<h2>AIと接した人間の側に何が起きたかを測る。</h2>
<p>人とAIの関係を問い直す研究開発機関。受託と顧問で積み上げた技術と収益を研究に還流させます。研究機関登録（e-Rad）は2026年8月に完了しました。現時点で、効果を示すデータはありません。研究から生まれたものはGugen株式会社に帰属し、事業として展開します。</p>
<p>詳細は研究所サイトをご覧ください。</p>
<p><a class="btn" href="{HCI_URL}" target="_blank" rel="noopener">研究所サイトへ</a></p>
<p><a href="https://www.gugen-egg.com/" target="_blank" rel="noopener">The EGG</a> — 15分遮断＋AI音声対話の没入空間</p>
</div>
"""
    return page("人間知能意識研究所", "HCI", "人間知能意識研究所", body, SVC_REL)


def philosophy_hub():
    body = """
<div class="prose">
<p>理念・ビジョン・代表挨拶・カルチャーを分けて公開しています。Gugenが何を大切にし、どこへ向かうかの起点です。</p>
</div>
<div class="phi-grid" style="margin:40px 0 64px">
  <a class="phi-card" href="/philosophy/mission/"><img src="/images/philosophy/hero.jpg" alt=""><span>理念</span></a>
  <a class="phi-card" href="/philosophy/vision/"><img src="/images/philosophy/vision.jpg" alt=""><span>ビジョン</span></a>
  <a class="phi-card" href="/philosophy/message/"><img src="/images/philosophy/message.jpg" alt=""><span>代表挨拶</span></a>
  <a class="phi-card" href="/philosophy/culture/"><img src="/images/philosophy/strategy.jpg" alt=""><span>カルチャー</span></a>
</div>
<div class="prose">
<p>会社名・所在地・役員などの数値情報は <a href="/company/">会社情報</a> をご覧ください。</p>
</div>
"""
    return page("会社概要", "Company", "会社概要", body, PHI_REL)


def philosophy_mission():
    body = """
<div class="prose">
<p>経営理念</p>
<p class="mission-line">人は、まだ進化できる。</p>
<p>社名のGugenは「具現」——見えないものに形を与えること。人も組織も社会も、いまの姿が完成形ではありません。構想を磨き、実装し、学び直す。その反復によって、まだ見えていない可能性へ進めると私たちは信じています。</p>
<h2>導入して終わりにしない。</h2>
<p>私たちは、思いつきを語るだけの会社でも、技術を納めて終わる会社でもありません。物事の奥を深く見て、未来から逆算し、小さく試す。そこで勝ち筋が見えた構想を、現場で使われる状態まで持っていくところまでを仕事にします。</p>
<h2>4つの事業で、理念を実装する</h2>
<p>「具現AX」で組織の使い方を変え、「任せた」で実装を動かし、「人材育成事業」で次の実装者を育てる。この現場で得た知見と収益を「人間知能意識研究所」に投じます。研究から生まれたものは会社に帰属し、再び事業になります。</p>
</div>
"""
    return page("理念", "Philosophy", "理念", body, PHI_REL)


def philosophy_vision():
    body = """
<div class="prose">
<p>どんな世界をつくるか</p>
<p class="mission-line">誰もが未来の創り手として生きる時代へ。</p>
<p>私たちのビジョンは「創りたいを創れる社会を創る」です。アイデアはあるのに、技術がない。やりたいのに、時間がない。そうした「創りたい」と「創れる」の間にある壁を、AIと職人のクラフトで取り除いていきます。</p>
<h2>小さく出して、動かしながら更新する</h2>
<p>完成してから世に出すのではなく、最小の形で出し、現場で動かしながら磨いていく。個別の実装で得たパターンは、再利用可能な資産として積み上げていく。属人性に頼らず、再現性のある形でAIを実装すること。それが、私たちが選んだやり方です。</p>
</div>
"""
    return page("ビジョン", "Vision", "ビジョン", body, PHI_REL)


def philosophy_message():
    body = """
<div class="prose">
<p>設立は、ゴールではなく出発点です。誰もが未来の創り手として生きる時代へ。学び続け、己を磨き、これからも手を動かし続けます。</p>
<p>Gugen株式会社 代表取締役<br>郷 由稀斗</p>
</div>
<div class="officer">
  <img src="/images/team/yukito-go.jpg" alt="郷 由稀斗">
  <div>
    <p class="role">代表取締役 / Co-founder / CTO</p>
    <h3>郷 由稀斗</h3>
    <p>ごうゆきと</p>
    <p>筑波大学情報メディア創成学類（落合陽一研究室所属）。福岡修猷館高卒。10歳よりシステム開発を開始し、現在は個人事業主としてAI受託開発・研修・コンサルを展開。Queue株式会社PMをはじめ、複数社でのエンジニア/CTO経験を経て、金融機関等の大規模案件や地方自治体向けイベントPFの立ち上げを統括。「誰もが創りたいものを創れる社会」を掲げ、技術とビジネスの両軸からAIの民主化を推進中。</p>
    <p>肩書き</p>
    <ul><li>EQパートナーズ株式会社 CAIO — Chief AI Officerとして参画。全社AI戦略の策定、AI実装テーマの選定・PoC推進、社内AIリテラシー向上を支援。</li></ul>
    <blockquote>誰もが創りたいものを創れる社会を創る</blockquote>
  </div>
</div>
<div class="officer">
  <img src="/images/team/taiki-mishima.png" alt="三島 大毅">
  <div>
    <p class="role">Co-founder / CEO</p>
    <h3>三島 大毅</h3>
    <p>みしまたいき</p>
    <p>立教大学経済学部二年(休学中)。日米両方の高校を卒業。高校時代はアニメ業界におけるDAO技術の促進について研究。「学生団体連合UNION」創設→株式会社Cometreeへ事業譲渡/売却を経験。その他自衛隊とのコラボなど多数のプロジェクトの統括を経験。今までの経験や課題感からThe EGGを構想し、プロダクト・パートナーシップを統括。J-StarX Stanfordにて現地に1ヶ月滞在し、Stanford d schoolにてデザイン思考のプログラムを修了。</p>
    <p>肩書き</p>
    <ul><li>株式会社トップクリエイターズ 外部AI顧問 — ベクトルグループ子会社の株式会社トップクリエイターズに外部AI顧問として参画。AI活用の戦略策定・現場実装の伴走を担当。</li></ul>
    <blockquote>未知をテクノロジーで体現し、日々を世界観でUpdate</blockquote>
  </div>
</div>
"""
    return page("代表挨拶", "Message", "代表挨拶", body, PHI_REL)


def philosophy_culture():
    body = """
<div class="prose">
<h2>Culture</h2>
<p class="mission-line">鍛錬</p>
<p>学び続け、己を磨き、未来をつくる。</p>
<p>組織文化は「鍛錬」です。完成形を待たず、手を動かし、学び直す。その反復が、人をまだ進化できる存在として扱うことだと考えています。</p>
<h2>Values</h2>
</div>
<div class="values">
  <div class="value"><p class="n">01</p><h3>深観</h3><p>物事の奥を深く見る。</p></div>
  <div class="value"><p class="n">02</p><h3>造形</h3><p>見えないものに形を与える。</p></div>
  <div class="value"><p class="n">03</p><h3>逆算</h3><p>未来から今を選ぶ。</p></div>
  <div class="value"><p class="n">04</p><h3>試斬</h3><p>小さく試し、勝ち筋を見極める。</p></div>
  <div class="value"><p class="n">05</p><h3>美勝</h3><p>美しく勝つ。</p></div>
</div>
<div class="prose" style="margin-top:48px">
<h2>ロゴに込めた想い</h2>
<p><img src="/images/logo-gugen.png" alt="Gugenのロゴ" style="width:240px"></p>
<p>シンボルは、まだ輪郭のないアイデアを受け止める「器」と、そこから立ち上がる形を表しています。閉じた枠ではなく、外へひらかれた線にすることで、可能性を決めつけない姿勢を込めました。</p>
<p>見えないものを受け取り、手を動かし、現実にする。それがGugenの仕事です。</p>
</div>
"""
    return page("カルチャー", "Culture", "カルチャー", body, PHI_REL)



def news_page():
    cards = []
    for n in NEWS:
        img = f'<img class="thumb" src="{n["img"]}" alt="">' if n["img"] else '<div class="ph"></div>'
        cards.append(
            f'<a class="news-card" href="/news/" data-cat="{n["id"]}">{img}'
            f'<p class="meta">{n["date"]}　{n["cat"]}</p><h3>{n["title"]}</h3></a>'
        )
    faq = []
    for group, qs in FAQ:
        items = "".join(
            f'<details><summary>{q}</summary><div class="a">{a}</div></details>' for q, a in qs
        )
        faq.append(f"<h3>{group}</h3><div class='faq'>{items}</div>")
    body = f"""
<div class="prose"><p>Gugenからの最新のお知らせ・リリース・イベント情報と、よくあるご質問をまとめています。</p></div>
<div class="filter-bar" data-filter-group=".news-card">
  <button type="button" class="is-on" data-filter="">すべて</button>
  <button type="button" data-filter="info">お知らせ</button>
  <button type="button" data-filter="release">リリース</button>
  <button type="button" data-filter="event">イベント</button>
  <button type="button" data-filter="recruit">採用</button>
</div>
<div class="news-grid">{"".join(cards)}</div>
<div class="prose" id="faq" style="margin-top:64px">
<h2>よくあるご質問</h2>
<p>お問い合わせの多い質問をまとめました。ここに無いご質問はお気軽にお問い合わせください。</p>
</div>
{"".join(faq)}
"""
    return page("ニュース", "News", "ニュース", body)


def company_page():
    body = """
<div class="prose"><h2>会社概要</h2></div>
<div class="spec">
  <div class="row"><div class="k">会社名</div><div class="v">Gugen株式会社</div></div>
  <div class="row"><div class="k">設立</div><div class="v">2026年7月14日</div></div>
  <div class="row"><div class="k">代表取締役</div><div class="v">郷 由稀斗</div></div>
  <div class="row"><div class="k">CEO</div><div class="v">三島 大毅</div></div>
  <div class="row"><div class="k">資本金</div><div class="v">500,000円</div></div>
  <div class="row"><div class="k">法人番号</div><div class="v">3010001267312</div></div>
  <div class="row"><div class="k">所在地</div><div class="v">〒102-0083 東京都千代田区麹町6丁目2-1 麹町サイトビル6階 crosshub内</div></div>
  <div class="row"><div class="k">決算月</div><div class="v">3月</div></div>
  <div class="row"><div class="k">事業内容</div><div class="v">具現AX（AI顧問・コンサル・研修） / 任せた（AI受託開発・ハードウェア） / 人間知能意識研究所（研究開発） / 人材育成事業（学生支援・Gugen Lab）</div></div>
  <div class="row"><div class="k">メール</div><div class="v"><a href="mailto:info@gugenlab.com">info@gugenlab.com</a></div></div>
</div>
<div class="prose" style="margin-top:48px">
<h2>Partners　提携先・顧問</h2>
<p>Gugenの事業を支えていただいている、国内外のアクセラレーター・育成プログラム・顧問・海外展示のパートナーをご紹介します。</p>
<ul>
<li>J-StarX Stanford / d.school US　Founder Program/完了 — J-StarXプログラムでStanfordに滞在し、d.schoolのデザイン思考プログラムを修了。</li>
<li>DMZ Basecamp Canada　Accelerator/進行中 — カナダのアクセラレーター「DMZ Basecamp」に参加し、ピッチ／メンタリング／事業検証を推進。</li>
<li>anobaka u25 AI Accelerator Japan　Accelerator / Advisory/完了 — anobakaでのメンタリング（複数回）や勉強会・合宿に参加し、プロダクト／事業戦略のブラッシュアップを実施。</li>
<li>Project KATAYABURI Japan　Program/進行中 — プログラム「KATAYABURI」に参加し、アイデア検証・事業仮説の具体化を推進。</li>
<li>AI TAIWAN 2026 Taiwan　海外展示会/完了 — 海外展示会「AI TAIWAN 2026」の情報収集・説明会参加を通じて、海外展開の足がかりを調査。</li>
</ul>
<h2>取引・支援実績</h2>
<div class="clients-row">
  <img src="/images/clients/logo-hunter.jpg" alt="株式会社HUNTER">
  <img src="/images/clients/logo-relie.png" alt="株式会社Relie">
  <img src="/images/clients/logo-zeronity.jpg" alt="Zeronity株式会社">
  <img src="/images/clients/logo-changebase.png" alt="change&amp;base合同会社">
  <img src="/images/clients/logo-bestiee.png" alt="株式会社bestiee">
</div>
<ul>
<li>株式会社HUNTER</li>
<li>株式会社Relie</li>
<li>Zeronity株式会社</li>
<li>change&amp;base合同会社</li>
<li>株式会社bestiee</li>
</ul>
</div>
"""
    return page("会社情報", "Company", "会社情報", body, COMP_REL)


def leaders_page():
    body = """
<div class="officer">
  <img src="/images/team/yukito-go.jpg" alt="郷 由稀斗">
  <div>
    <p class="role">代表取締役 / Co-founder / CTO</p>
    <h3>郷 由稀斗</h3>
    <p>ごうゆきと</p>
    <p>筑波大学情報メディア創成学類（落合陽一研究室所属）。福岡修猷館高卒。10歳よりシステム開発を開始し、現在は個人事業主としてAI受託開発・研修・コンサルを展開。Queue株式会社PMをはじめ、複数社でのエンジニア/CTO経験を経て、金融機関等の大規模案件や地方自治体向けイベントPFの立ち上げを統括。「誰もが創りたいものを創れる社会」を掲げ、技術とビジネスの両軸からAIの民主化を推進中。</p>
    <p>肩書き</p>
    <ul><li>EQパートナーズ株式会社 CAIO — Chief AI Officerとして参画。全社AI戦略の策定、AI実装テーマの選定・PoC推進、社内AIリテラシー向上を支援。</li></ul>
    <blockquote>誰もが創りたいものを創れる社会を創る</blockquote>
  </div>
</div>
<div class="officer">
  <img src="/images/team/taiki-mishima.png" alt="三島 大毅">
  <div>
    <p class="role">Co-founder / CEO</p>
    <h3>三島 大毅</h3>
    <p>みしまたいき</p>
    <p>立教大学経済学部二年(休学中)。日米両方の高校を卒業。高校時代はアニメ業界におけるDAO技術の促進について研究。「学生団体連合UNION」創設→株式会社Cometreeへ事業譲渡/売却を経験。その他自衛隊とのコラボなど多数のプロジェクトの統括を経験。今までの経験や課題感からThe EGGを構想し、プロダクト・パートナーシップを統括。J-StarX Stanfordにて現地に1ヶ月滞在し、Stanford d schoolにてデザイン思考のプログラムを修了。</p>
    <p>肩書き</p>
    <ul><li>株式会社トップクリエイターズ 外部AI顧問 — ベクトルグループ子会社の株式会社トップクリエイターズに外部AI顧問として参画。AI活用の戦略策定・現場実装の伴走を担当。</li></ul>
    <blockquote>未知をテクノロジーで体現し、日々を世界観でUpdate</blockquote>
  </div>
</div>
"""
    return page("Leaders", "Management", "Leaders", body, COMP_REL)


def access_page():
    body = """
<div class="prose">
<h2>アクセス</h2>
<p>〒102-0083 東京都千代田区麹町6丁目2-1 麹町サイトビル6階 crosshub内</p>
<p>メール　<a href="mailto:info@gugenlab.com">info@gugenlab.com</a></p>
<p>リモートが基本です。登記上の所在地は千代田区麹町で、2026年10月から東京（後楽園）に作業拠点ができます。</p>
<iframe class="map" title="地図" src="https://maps.google.com/maps?q=%E6%9D%B1%E4%BA%AC%E9%83%BD%E5%8D%83%E4%BB%A3%E7%94%B0%E5%8C%BA%E9%BA%B9%E7%94%BA6%E4%B8%81%E7%9B%AE2-1&output=embed" loading="lazy"></iframe>
<p><a href="https://maps.google.com/?q=東京都千代田区麹町6丁目2-1" target="_blank" rel="noopener">Google マップで見る</a></p>
</div>
"""
    return page("アクセス", "Access", "アクセス", body, COMP_REL)


def works_page():
    cards = []
    for title, cat, role, desc, impact, tags, url, filt in WORKS:
        link = f'<p><a href="{url}" target="_blank" rel="noopener">プロジェクトを見る →</a></p>' if url else ""
        cards.append(
            f'<article class="work-card" data-cat="{filt}"><p class="k">{cat}　{role}</p>'
            f'<h3>{title}</h3><p>{desc}</p><p class="impact">IMPACT　{impact}</p>'
            f'<p class="tags">{tags}</p>{link}</article>'
        )
    body = f"""
<div class="prose">
<p>AI受託開発「Gugen OS」による導入事例から、自社プロダクトまで。これまで手掛けてきたプロジェクトをすべて掲載しています。</p>
<p><a href="https://app.gugen-kobo.com/" target="_blank" rel="noopener">Gugen OS デモを見る</a></p>
<p>31 / 31 件</p>
</div>
<div class="filter-bar" data-filter-group=".work-card">
  <button type="button" class="is-on" data-filter="">すべて</button>
  <button type="button" data-filter="受託開発">受託開発</button>
  <button type="button" data-filter="Deep Tech">Deep Tech</button>
  <button type="button" data-filter="AI">AI</button>
  <button type="button" data-filter="Hardware">Hardware</button>
  <button type="button" data-filter="Web Development">Web Development</button>
  <button type="button" data-filter="B2B SaaS">B2B SaaS</button>
  <button type="button" data-filter="Community">Community</button>
  <button type="button" data-filter="Media">Media</button>
  <button type="button" data-filter="Web Platform">Web Platform</button>
  <button type="button" data-filter="自社プロダクト">自社プロダクト</button>
</div>
<div class="works-grid">{"".join(cards)}</div>
"""
    return page("プロジェクト・実績", "Works", "プロジェクト・実績", body, SVC_REL)


def articles_index():
    rows = []
    for a in ARTICLES:
        img = f'<img src="{a["img"]}" alt="">' if a["img"] else '<div class="ph"></div>'
        rows.append(
            f'<a class="row" href="/articles/{a["slug"]}.html" data-cat="{a["cat"]}">{img}<div>'
            f'<p class="meta">{a["date"]}　{a["cat"]}　{a["min"]}</p><h3>{a["title"]}</h3>'
            f'<p>{a["lead"]}</p><p>by {a["author"]}</p></div></a>'
        )
    body = f"""
<div class="prose"><p>Gugen のビジョン、エンジニアリング、現場の知見をお届けします。</p></div>
<div class="filter-bar" data-filter-group=".card-list .row">
  <button type="button" class="is-on" data-filter="">すべて</button>
  <button type="button" data-filter="VISION">Vision</button>
  <button type="button" data-filter="ENGINEERING">Engineering</button>
  <button type="button" data-filter="CASE STUDY">Case Study</button>
  <button type="button" data-filter="FOUNDER NOTE">Founder Note</button>
  <button type="button" data-filter="COMMUNITY">Community</button>
</div>
<div class="card-list">{"".join(rows)}</div>
"""
    return page("記事", "Articles", "記事", body)


def article_page(a):
    img = f'<p><img src="{a["img"]}" alt="{a["title"]}" style="border-radius:16px"></p>' if a["img"] else ""
    related_html = "".join(
        f'<li><a href="/articles/{b["slug"]}.html">{b["date"]}　{b["title"]}</a></li>'
        for b in ARTICLES if b["slug"] != a["slug"]
    )[:3]
    others = []
    for b in ARTICLES:
        if b["slug"] == a["slug"]:
            continue
        others.append(f'<li><a href="/articles/{b["slug"]}.html">{b["date"]}　{b["title"]}</a></li>')
        if len(others) == 3:
            break
    body = f"""
<div class="prose">
<p><a href="/articles/">←記事一覧へ</a></p>
<p>{a["date"]}　{a["cat"]}　{a["min"]}<br>by {a["author"]}</p>
{img}
<p>{a["lead"]}</p>
{a["body"]}
<h2>他の記事を読む</h2>
<ul>{"".join(others)}</ul>
<p><a href="/articles/">すべての記事を見る</a></p>
</div>
"""
    return page(a["title"], a["cat"], a["title"], body)


def recruit_page():
    body = """
<nav class="career-nav" aria-label="採用情報の目次">
  <a href="#why">なぜGugenか</a>
  <a href="#work">働き方</a>
  <a href="#roles">募集職種</a>
  <a href="#terms">条件</a>
  <a href="#apply">応募</a>
</nav>
<div class="prose">
<p>2026年7月設立、4人の会社です。いま募集しているのはインターンだけ。時間も場所も指定せず、お客さまに出すものを任せます。</p>
<h2 id="why">なぜAIを、なぜ今か</h2>
<h3>01 — Why AI　AIは、人の余白を増やした</h3>
<p>判断の要らない作業をAIに渡すと、時間が空きます。私たちはその余白を、次に何をつくるかを考えることに使っています。会社の業務システム（20画面）は自分たちで作って、自分たちの本番で毎日使っています。お客さまに売る前に、まず自社で回しています。</p>
<h3>02 — Why now　使える人より、入れられる人が足りない</h3>
<p>AIを触れる人は増えました。足りないのは、顧客の業務を聞いて、どこに入れるかを決めて、使われる状態まで持っていける人です。中小企業の現場は、いまも表計算と電話で回っています。ここを変える仕事は、これからの数年に集中します。</p>
<h3>03 — Why here　まだ形が決まっていない側に、入れる</h3>
<p>メンバー4名。事業部長の席は3つとも空いています。聞く相手が2人しかいないので、確認は半日で返ってきます。入って1か月で、お客さまに出るものを担当します。</p>
<p>そのぶん、決まっていないことを自分で決める場面が多くなります。整った環境で学びたい人には向きません。</p>
<h2 id="work">4人でどう働くか</h2>
<p>会議は週に2本、合計1時間だけです。残りの時間は、手を動かすために空けています。確認が要ることは Slack で聞けば半日で返ってきます。承認を何段も待つ場面はありません。</p>
<h3>エンジニアの一日</h3>
<ol class="steps">
<li>10:00 Gugen Hub を開いて、今日やること3件を確認する</li>
<li>10:15 担当案件を実装する。要件が曖昧なところは Slack で聞く（半日で返ってきます）</li>
<li>12:00 中断。授業へ</li>
<li>16:00 戻って、書いたコードを自分で動かして確かめる</li>
<li>17:00 プルリクエストを出す。レビューを待つ</li>
</ol>
<h3>営業の一日</h3>
<ol class="steps">
<li>10:00 Gugen Hub を開いて、今日の商談と返信待ちの案件を確認する</li>
<li>11:00 経営者とオンラインで商談。何に何時間かかっているかを実額で聞いてくる</li>
<li>12:00 中断。授業へ</li>
<li>16:00 戻って、聞いた内容を提案書に落とす。詰まったら Slack で聞く</li>
<li>17:00 提案書を提出。レビューを待つ</li>
</ol>
<h3>広報・マーケの一日</h3>
<ol class="steps">
<li>10:00 前日の数字を見る。アクセスが落ちたページを1つ選ぶ</li>
<li>10:30 業界別LPの原稿を書く。AIで初稿を出し、出す前に自分の目で通す</li>
<li>12:00 中断。授業へ</li>
<li>16:00 戻って、検索広告の文面を差し替えて配信する</li>
<li>17:00 明日見る数字を決めて、Gugen Hub に書いておく</li>
</ol>
<h3>バックオフィスの一日</h3>
<ol class="steps">
<li>10:00 入金を消し込み、期日が近い書類を確認する</li>
<li>10:30 請求書を発行する。未回収の契約書は Slack で催促する</li>
<li>12:00 中断。授業へ</li>
<li>16:00 戻って、経費の仕訳を1円単位で合わせる</li>
<li>17:00 今週の期日を一覧にして共有する</li>
</ol>
<p>※ 時間は例です。始業も終業も決まっていません。授業のある時間帯は、どの職種でも空けられます。</p>
<h3>一週間のリズム</h3>
<p>ここは職種によらず全員同じです。</p>
<ul>
<li>月曜 朝　会社全体で30分。現預金と、今週の詰まりを1つ潰す。聞いているだけでもかまいません</li>
<li>週の途中　案件を進める。同席が必要な商談があれば入る</li>
<li>週1回 30分　担当領域の定例。案件の進捗と数字</li>
<li>週の終わり　メンターと1on1。詰まっているところを話す</li>
<li>月初　全員で60分。前月の数字と、今月の重点を1つ</li>
</ul>
<h3>ひとりで抱えさせません</h3>
<p>任せる範囲は段階で上げます。最初はレビュー前の下書きから。3件目までは、出すものを全件レビューします。お客さまの場に出る最初の1回は、必ず三島か郷が同席します。</p>
<p>週の終わりにメンターと30分。詰まっているところを話す時間です。入って1か月の時点で、続けるかどうかを双方で確認します。合わなければそこで終われます。</p>
<h3>学業との両立について</h3>
<p>時間も場所も指定しません。委託するのは成果物で、勤怠も取りません。だから、授業や研究と並べて進められます。試験の週に手を止めても、責める人はいません。</p>
<p>ただし、消化するだけの作業は渡しません。段階を踏んで、最後はお客さまの前に出るものを担当してもらいます。</p>
<h2 id="roles">インターンを募集しています</h2>
<p>入口は1つです。応募のときに、下の4つから興味のあるものを選んでください。全員が全業務に触れるフェーズなので、途中で変わってもかまいません。</p>
<h3>ソフトウェアエンジニア</h3>
<p>受託開発と自社プロダクト（Gugen Hub）の実装。要件が固まっていないところから、動くものにするまで。</p>
<ul>
<li>AIを使って、要件が曖昧な状態から動くものを作りきれる</li>
<li>出力を動かして確かめてから出す</li>
<li>他の人が読めるコードを書く</li>
<li>納期を守る。守れないと分かった時点で言える</li>
</ul>
<p>任せる範囲：合意した要件と予算の範囲で、技術選定・設計・実装手順・リリース判断を担います。納期、予算、セキュリティに影響する変更はチームで承認します。</p>
<p>TypeScript / Next.js / Supabase / Python / LLM</p>
<h3>営業 / AIコンサルタント・AI顧問</h3>
<p>中小企業の経営者に会って、何にどれだけ困っているかを実額で聞いてきます。そのまま、AIをどこに入れるかの設計と定着支援まで担います。営業経験の年数は問いません。</p>
<ul>
<li>初対面の経営者と1時間話せる</li>
<li>「困っていますか」と聞かず、何時間かかっているか・いくら払っているかを聞ける</li>
<li>金額の話を避けない</li>
<li>使われなかった原因を、人のせいにせず設計に戻せる</li>
</ul>
<p>任せる範囲：合意した価格帯と提案方針の範囲で、開拓先の選定から商談設計、提案内容までを自ら決められます。値引き・契約条件の変更は共同創業者と決定します。</p>
<p>BtoB / SMB商談 / 業務設計 / AI導入</p>
<h3>広報・マーケティング</h3>
<p>Gugenを見つけてもらう状態をつくります。業界別LPの制作と検索広告の検証、導入事例の記事化、採用広報まで。</p>
<ul>
<li>読者が誰かを決めてから書ける</li>
<li>数字を見て直せる（アクセス・問い合わせ率・アポ率）</li>
<li>AIで量を出しつつ、出す前に人の目で通せる</li>
</ul>
<p>任せる範囲：合意した目的と予算の範囲で、発信テーマ、媒体、制作方法、検証サイクルを決められます。会社の公式見解や未公開情報の発信は事前承認が必要です。</p>
<p>BtoB / LP / 検索広告 / コンテンツ</p>
<h3>バックオフィス・経理</h3>
<p>お金と書類が滞らない状態をつくります。請求と入金、経費、契約管理、月次の締め、税務・社会保険の期日管理まで。</p>
<ul>
<li>数字を1円単位で合わせられる</li>
<li>期日を落とさない仕組みを自分で作れる</li>
<li>分からない税務・法務を、調べて専門家に正しく質問できる</li>
</ul>
<p>任せる範囲：既定のルールと予算内で、業務フロー、管理方法、利用ツール、締め日程を改善できます。契約・給与・税務上の最終判断は共同創業者や専門家と行います。</p>
<p>請求 / 経理 / 契約管理 / 労務</p>
<h2 id="terms">条件</h2>
</div>
<div class="spec">
  <div class="row"><div class="k">契約</div><div class="v">業務委託です。雇用ではありません。</div></div>
  <div class="row"><div class="k">報酬</div><div class="v">作業単価 1,500円から。レベルが上がると 2,500円まで上がります。</div></div>
  <div class="row"><div class="k">決め方</div><div class="v">成果物 × 作業単価 × 見積工数を、着手する前に合意します。実際にかかった時間では増減しません。早く終わっても減りません。</div></div>
  <div class="row"><div class="k">稼働</div><div class="v">週7〜8時間から相談。時間と場所は指定しません。勤怠も取りません。</div></div>
  <div class="row"><div class="k">場所</div><div class="v">リモートが基本です。登記上の所在地は千代田区麹町で、2026年10月から東京（後楽園）に作業拠点ができます。</div></div>
  <div class="row"><div class="k">上がり方</div><div class="v">案件を1本まるごと持てたら。人の成果物をレビューして直せたら。新しく入った人を受け入れて案件に立たせられたら。この3段で上がります。在籍期間では上げません。</div></div>
  <div class="row"><div class="k">先に伝えること</div><div class="v">勤怠を取らないかわりに、締切と品質は自分で守ってもらいます。報酬は給与ではないので、金額によっては確定申告が必要です。扶養の範囲についても、契約前に説明します。</div></div>
</div>
<div class="prose">
<h3>この先どうなるか</h3>
<ul>
<li>レベルが上がると作業単価が上がります（1,500円 → 2,500円）。上がる条件は上の表のとおりで、在籍期間では上げません。</li>
<li>担当した仕事は、お客さまを特定できる情報を除いたうえで、こちらの承諾を得て実績として使えます。持ち帰れるものが残ります。</li>
<li>正社員の募集は、事業の再現性（粗利が3か月続くこと・受注が積み上がること）を確かめてから開きます。いまはインターンだけです。その段階になったら、まず中にいる人に声をかけます。</li>
<li>合わなかった場合も、提携先の受け入れ先を紹介します。</li>
</ul>
<h2>求める人物像</h2>
<div class="values">
  <div class="value"><p class="n">01</p><h3>「創りたい」を自分の手で形にした経験がある</h3></div>
  <div class="value"><p class="n">02</p><h3>AIに何をやらせて、何を自分でやるかを判断できる</h3></div>
  <div class="value"><p class="n">03</p><h3>出力をそのまま出さず、動かして確かめてから出せる</h3></div>
</div>
<h2>働く環境</h2>
<h3>柔軟な働き方</h3>
<p>リモートを基本に、稼働時間と参加方法は役割・契約形態に応じて相談できます。</p>
<h3>AI・開発環境</h3>
<p>業務に必要なAIツール、クラウド、開発環境の費用を会社が負担します。</p>
<h3>学習・研究支援</h3>
<p>業務に関連する書籍、勉強会、カンファレンス、研究費を内容に応じて支援します。</p>
<h3>副業・社外活動</h3>
<p>守秘義務と利益相反のルールを守ることを前提に、副業や研究・創作活動を尊重します。</p>
<h2>メンバー</h2>
<p>詳細は <a href="/company/management/">Leaders</a> および <a href="/about/">私たちについて</a> をご覧ください。</p>
<h2 id="apply">応募から面談まで</h2>
<ol class="steps">
<li><h3>書類</h3><p>応募フォームから、作ったもののURLを送ってください。履歴書も学歴も見ません。動くものが1つあれば十分です。</p></li>
<li><h3>カジュアル面接</h3><p>取締役CEO 三島と30分。作ったものの話を聞きます。AIに何をやらせて、何を自分でやるかの判断を見ています。</p></li>
<li><h3>最終面接</h3><p>代表取締役CTO 郷と30分。技術の見立てと、お客さまの前に出せるかを確認します。落ちた場合も、足りなかったことを1つお伝えします。</p></li>
</ol>
<p style="margin-top:24px"><a class="btn" href="/recruit/apply.html">応募する</a>　<a class="btn btn-ghost" href="/casual-meeting/">カジュアル面談を申し込む</a></p>
</div>
"""
    return page("採用情報", "Careers", "学生と、会社をつくる", body)


def form_contact():
    body = """
<div class="prose"><p>お気軽にお問い合わせください。</p></div>
<form class="form js-form">
  <label>お名前 <span class="req">*</span></label><input name="name" required>
  <label>会社名</label><input name="company">
  <label>メールアドレス <span class="req">*</span></label><input type="email" name="email" required>
  <label>ご関心のある領域</label>
  <select name="area">
    <option value="">選択してください</option>
    <option>人材育成事業 / Gugen Lab</option>
    <option>任せた（AI受託開発・ハードウェア）</option>
    <option>具現AX（AI顧問・コンサル・研修）</option>
    <option>PoC・小規模実装からの相談</option>
    <option>The EGG</option>
    <option>採用について</option>
    <option>協業・パートナーシップ</option>
    <option>その他</option>
  </select>
  <label>お問い合わせ内容 <span class="req">*</span></label><textarea name="body" required></textarea>
  <p class="note">* は必須項目です。送信内容は<a href="/privacy/">プライバシーポリシー</a>に基づき取り扱います。</p>
  <button type="submit">送信する</button>
</form>
<div class="form-ok">お問い合わせを受け付けました。担当よりご連絡いたします。</div>
<div class="prose" style="margin-top:40px">
<h2>直接お問い合わせ</h2>
<p>Email　<a href="mailto:info@gugenlab.com">info@gugenlab.com</a></p>
<p>Office　〒102-0083 東京都千代田区麹町6丁目2-1 麹町サイトビル6階 crosshub内</p>
</div>
"""
    return page("お問い合わせ", "Contact", "お問い合わせ", body)


def form_apply():
    body = """
<div class="prose"><p>応募書類を提出してください。内容を確認し、社内承認後に面談予約リンクをメールでお送りします。</p></div>
<form class="form js-form">
  <label>お名前 <span class="req">*</span></label><input name="name" required>
  <label>メールアドレス <span class="req">*</span></label><input type="email" name="email" required>
  <label>希望職種 <span class="req">*</span></label>
  <select name="role" required>
    <option value="">選択してください</option>
    <option>ソフトウェアエンジニア</option>
    <option>営業 / AIコンサルタント・AI顧問</option>
    <option>広報・マーケティング</option>
    <option>バックオフィス・経理</option>
    <option>まだ決められない / 相談したい</option>
  </select>
  <label>所属（大学・会社）</label><input name="org">
  <label>稼働できる時間（週あたり）</label><input name="hours">
  <label>応募書類URL <span class="req">*</span></label><input type="url" name="docs" required>
  <p class="note">履歴書・職務経歴書などを、閲覧できるGoogle Drive、Notion、PDF等のURLで提出してください。</p>
  <label>制作物・ポートフォリオURL</label><input type="url" name="portfolio">
  <label>志望理由・自己PR <span class="req">*</span></label><textarea name="pr" required></textarea>
  <p class="note">* は必須項目です。ご入力いただいた内容は<a href="/privacy/">プライバシーポリシー</a>に基づき、採用選考の目的にのみ利用します。</p>
  <button type="submit">応募する</button>
</form>
<div class="form-ok">送信内容を受け付けました。内容を確認し、承認後に面談予約リンクをメールでお送りします。</div>
"""
    return page("応募する", "Apply", "応募する", body)


def form_casual():
    body = """
<div class="prose"><p>「まずは話を聞いてみたい」という段階で大歓迎です。事業のこと、AI導入の相談、採用のこと。テーマが決まっていなくても構いません。オンラインで30分ほどお話ししましょう。</p></div>
<form class="form js-form">
  <label>お名前 <span class="req">*</span></label><input name="name" required>
  <label>会社名・所属</label><input name="org">
  <label>メールアドレス <span class="req">*</span></label><input type="email" name="email" required>
  <label>話したいテーマ</label>
  <select name="theme">
    <option value="">選択してください</option>
    <option>事業・サービスについて聞きたい</option>
    <option>AI導入・開発の相談</option>
    <option>採用・キャリアについて</option>
    <option>協業・パートナーシップ</option>
    <option>その他</option>
  </select>
  <label>ご希望の日程</label><input name="date">
  <label>ご要望・補足</label><textarea name="note"></textarea>
  <p class="note">* は必須項目です。送信内容は<a href="/privacy/">プライバシーポリシー</a>に基づき取り扱います。</p>
  <button type="submit">カジュアル面談を申し込む</button>
</form>
<div class="form-ok">お申し込みを受け付けました。1〜2営業日以内に、担当より日程調整のご連絡をいたします。</div>
<div class="prose" style="margin-top:32px">
<h2>当日までの流れ</h2>
<ol class="steps">
<li>このページのフォームからお申し込みいただきます。</li>
<li>1〜2営業日以内に、担当より日程調整のご連絡をいたします。</li>
<li>確定した日時にオンラインでお話しします。</li>
</ol>
</div>
"""
    return page("カジュアル面談", "Casual Meeting", "カジュアル面談", body)


def legal_pages():
    privacy = page("プライバシーポリシー", "Privacy", "プライバシーポリシー", """
<div class="prose">
<p>Gugen株式会社は、お客様の個人情報の保護を重要な責務と認識し、以下のとおりプライバシーポリシーを定め、適切な管理・保護に努めます。</p>
<h2>1. 個人情報の取得について</h2>
<p>当社は、適法かつ公正な手段により、業務上必要な範囲で個人情報を取得いたします。</p>
<h2>2. 利用目的</h2>
<p>取得した個人情報は、以下の目的で利用いたします。</p>
<p>・お問い合わせへの対応<br>・サービスの提供・改善<br>・採用活動における選考・連絡<br>・法令に基づく対応</p>
<h2>3. 第三者提供</h2>
<p>当社は、法令に定める場合を除き、あらかじめご本人の同意を得ることなく、個人情報を第三者に提供いたしません。</p>
<h2>4. 安全管理措置</h2>
<p>当社は、個人情報の漏えい、滅失又は毀損の防止その他の安全管理のために、必要かつ適切な措置を講じます。</p>
<h2>5. 開示・訂正・削除のご請求</h2>
<p>ご本人から個人情報の開示・訂正・削除等のご請求があった場合は、本人確認の上、合理的な期間内に対応いたします。</p>
<h2>6. お問い合わせ窓口</h2>
<p>個人情報の取扱いに関するお問い合わせは、当社ウェブサイトのお問い合わせフォームよりご連絡ください。</p>
<p>制定日: 2026年2月12日<br>Gugen株式会社</p>
</div>
""")
    security = page("セキュリティ", "Security", "セキュリティ", """
<div class="prose">
<p>Gugen のセキュリティに対する考え方と実施している対策をまとめています。B2B 契約時には別途詳細資料をご提供します。</p>
<h2>方針</h2>
<p>Gugen は、お客様の情報とプロダクトの信頼性を守るため、セキュリティ・バイ・デザインを原則として開発・運用を行っています。法令・ガイドラインを遵守し、継続的な改善を行います。</p>
<h2>データ暗号化</h2>
<p>すべての通信は TLS 1.2 以上で暗号化し、保存データは AES-256 で暗号化しています。鍵管理はクラウドベンダーのマネージド KMS を使用します。</p>
<h2>アクセス制御</h2>
<p>本番環境へのアクセスは最小権限の原則に基づき、多要素認証 (MFA) を必須としています。アクセスログは監査可能な形で保管されます。</p>
<h2>AI 学習ポリシー</h2>
<p>任せた・具現AX・Gugen Lab その他お客様から預かったデータを、Gugen 社内の汎用モデル学習に利用することはありません。利用用途はご依頼内容の遂行に限定されます。</p>
<h2>インシデント対応</h2>
<p>セキュリティインシデントを検知した場合、定められた手順に基づき影響範囲を特定し、関係者への速やかな通知を行います。</p>
<h2>データ保持・削除</h2>
<p>契約終了後、お客様データは所定の期間内に安全に削除します。保管期間は契約書に明示されます。</p>
<h2>委託先管理</h2>
<p>クラウド・分析・決済・認証等の委託先を使用する場合、事前に評価を行い、必要な契約 (DPA 等) を締結します。主要委託先の一覧は、お問い合わせいただければご提供します。</p>
<h2>認証・準拠</h2>
<p>現在、ISO/IEC 27001 の取得準備を進めています。必要に応じて SOC 2 Type II、Pマーク等の取得も検討します。</p>
<h2>脆弱性報告</h2>
<p>セキュリティ上の問題を発見された方は info@gugenlab.com までご連絡ください。善意でご報告いただいた方には速やかに対応し、お礼をお伝えします。</p>
</div>
""")
    legal = page("決算公告", "Legal", "決算公告", """
<div class="prose">
<p>会社法第440条に基づく決算公告を掲載しています。</p>
<p>第1期（2026年7月14日〜2027年3月31日）の決算公告は、確定次第このページに掲載します。</p>
<p><a href="/legal/transactions.html">特定商取引法に基づく表記</a></p>
</div>
""")
    trans = page("特定商取引法に基づく表記", "Legal", "特定商取引法に基づく表記", """
<div class="prose">
<p>特定商取引法第 11 条に基づき、以下の事項を表記します。商品・サービスごとの条件は個別契約書に定めます。</p>
<div class="spec">
  <div class="row"><div class="k">販売事業者</div><div class="v">Gugen株式会社</div></div>
  <div class="row"><div class="k">運営責任者</div><div class="v">郷 由稀斗 ・ 三島 大毅</div></div>
  <div class="row"><div class="k">所在地</div><div class="v">〒102-0083 東京都千代田区麹町6丁目2-1 麹町サイトビル6階 crosshub内</div></div>
  <div class="row"><div class="k">お問い合わせ</div><div class="v">info@gugenlab.com</div></div>
  <div class="row"><div class="k">販売価格</div><div class="v">各サービスページに記載 (税込)。個別見積もりの場合は別途お見積書を発行します。</div></div>
  <div class="row"><div class="k">商品以外の必要料金</div><div class="v">銀行振込の振込手数料、通信料等はお客様のご負担となります。</div></div>
  <div class="row"><div class="k">支払方法</div><div class="v">銀行振込 / クレジットカード (Stripe 等)</div></div>
  <div class="row"><div class="k">支払時期</div><div class="v">請求書発行日より 30 日以内 (契約により異なる)</div></div>
  <div class="row"><div class="k">役務提供時期</div><div class="v">契約締結後、個別契約書に記載された期日内に開始します。</div></div>
  <div class="row"><div class="k">返品・キャンセル</div><div class="v">役務の性質上、原則として契約後のキャンセル・返金はお受けできません。ハードウェア (The EGG 等) は別途リース契約の定めによります。</div></div>
  <div class="row"><div class="k">動作環境</div><div class="v">Web サービス（任せた・具現AX・Gugen Lab 等）: モダンブラウザ (Chrome / Safari / Edge 最新版) を推奨。</div></div>
</div>
</div>
""")
    return privacy, security, legal, trans


def main():
    write("index.html", home())
    write("about/index.html", about_page())
    write("service/index.html", service_index())
    write("service/makaseta/index.html", service_makaseta())
    write("service/os/index.html", service_makaseta())
    write("service/ax/index.html", service_ax())
    write("service/education/index.html", service_education())
    write("service/lab/index.html", service_education())
    write("service/research/index.html", service_research())
    write("works/index.html", works_page())
    write("news/index.html", news_page())
    write("company/index.html", company_page())
    write("company/info/index.html", company_page())
    write("company/management/index.html", leaders_page())
    write("company/leaders/index.html", leaders_page())
    write("company/access/index.html", access_page())
    write("articles/index.html", articles_index())
    for a in ARTICLES:
        write(f"articles/{a['slug']}.html", article_page(a))
    write("recruit/index.html", recruit_page())
    write("recruit/apply.html", form_apply())
    write("careers/index.html", recruit_page())
    write("careers/apply.html", form_apply())
    write("contact/index.html", form_contact())
    write("casual-meeting/index.html", form_casual())
    privacy, security, legal, trans = legal_pages()
    write("privacy/index.html", privacy)
    write("security/index.html", security)
    write("legal/index.html", legal)
    write("legal/transactions.html", trans)
    write("sitemap/index.html", page("サイトマップ", "Sitemap", "サイトマップ",
        "<ul>" + "".join(
            f'<li><a href="{h}">{t}</a></li>' for t, h in [
                ("トップ", "/"),
                ("事業内容", "/service/"),
                ("任せた", "/service/makaseta/"),
                ("人材育成事業", "/service/education/"),
                ("会社概要", "/philosophy/"),
                ("理念", "/philosophy/mission/"),
                ("ビジョン", "/philosophy/vision/"),
                ("代表挨拶", "/philosophy/message/"),
                ("カルチャー", "/philosophy/culture/"),
                ("会社情報", "/company/"),
                ("ニュース", "/news/"),
                ("採用情報", "/recruit/"),
                ("お問い合わせ", "/contact/"),
            ]
        ) + "</ul>"))
    write("search/index.html", page("検索", "Search", "検索", """
<form class="form" action="/search/" method="get">
  <input type="search" name="q" placeholder="検索する">
  <button type="submit">検索</button>
</form>
"""))
    write("company/philosophy/index.html", philosophy_hub())
    write("company/message/index.html", philosophy_message())
    write("services/index.html", service_index())
    write("services/os.html", service_makaseta())
    write("services/ax.html", service_ax())
    write("services/lab.html", service_education())
    write("services/research.html", service_research())
    write("philosophy/index.html", philosophy_hub())
    write("philosophy/mission/index.html", philosophy_mission())
    write("philosophy/corporate_philosophy.html", philosophy_mission())
    write("philosophy/identity.html", philosophy_culture())
    write("philosophy/message/index.html", philosophy_message())
    write("philosophy/message.html", philosophy_message())
    write("philosophy/value.html", philosophy_culture())
    write("philosophy/culture/index.html", philosophy_culture())
    write("philosophy/vision/index.html", philosophy_vision())
    write("philosophy/vision.html", philosophy_vision())
    write("about/profile.html", company_page())
    write("about/officer.html", leaders_page())
    write("technology/index.html", page(
        "テクノロジー", "Technology", "テクノロジー",
        """<div class="prose">
<p>任せた（AI実装）と具現AX（組織変革）を両輪に、要件定義からPoC・実装・運用までをプロトコル化しています。</p>
<p><a href="/service/">事業内容を見る</a></p>
</div>""",
        SVC_REL,
    ))
    print("done")


if __name__ == "__main__":
    main()
