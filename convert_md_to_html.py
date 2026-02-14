#!/usr/bin/env python3
import markdown
import os

# 读取Markdown文件
def read_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

# 转换Markdown为HTML
def convert_to_html(markdown_text):
    return markdown.markdown(markdown_text, extensions=['fenced_code', 'codehilite', 'tables'])

# 生成完整的HTML页面
def generate_full_html(title, content, language='zh'):
    # 基础HTML模板，基于项目现有页面结构
    template = f'''
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  
  <title>{title} | Hello,programe</title>
  <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">
  <meta name="description" content="{title}">
  
    <link rel="alternative" href="/atom.xml" title="Hello,programe" type="application/atom+xml">
  
  
    <link rel="icon" href="/favicon.png">
  
  <link href="//fonts.googleapis.com/css?family=Source+Code+Pro" rel="stylesheet" type="text/css">
  <link rel="stylesheet" href="/css/style.css">
  

</head>
<body>
  <div id="container">
    <div id="wrap">
      <header id="header">
  <div id="banner"></div>
  <div id="header-outer" class="outer">
    <div id="header-title" class="inner">
      <h1 id="logo-wrap">
        <a href="/" id="logo">Hello,programe</a>
      </h1>
      
    </div>
    <div id="header-inner" class="inner">
      <nav id="main-nav">
        <a id="main-nav-toggle" class="nav-icon"></a>
        
          <a class="main-nav-link" href="/">Home</a>
        
          <a class="main-nav-link" href="/apps">应用</a>
        
          <a class="main-nav-link" href="/privacy">隐私政策</a>
        
          <a class="main-nav-link" href="/support">技术支持</a>
        
          <a class="main-nav-link" href="/about">关于</a>
        
      </nav>
      <nav id="sub-nav">
        
          <a id="nav-rss-link" class="nav-icon" href="/atom.xml" title="RSS Feed"></a>
        
        <a id="nav-search-btn" class="nav-icon" title="Search"></a>
      </nav>
      <div id="search-form-wrap">
        <form action="//google.com/search" method="get" accept-charset="UTF-8" class="search-form"><input type="search" name="q" results="0" class="search-form-input" placeholder="Search"><button type="submit" class="search-form-submit">&#xF002;</button><input type="hidden" name="sitesearch" value="http://yoursite.com"></form>
      </div>
    </div>
  </div>
</header>
      <div class="outer">
        <section id="main"><article class="article article-type-post" itemscope itemprop="blogPost">
  <div class="article-meta">
    <a href="#" class="article-date">
  <time datetime="2026-02-14T00:00:00.000Z" itemprop="datePublished">2026-02-14</time>
</a>
    
  </div>
  <div class="article-inner">
    
    
      <header class="article-header">
        
  
    <h1 class="article-title" itemprop="name">
      {title}
    </h1>
  

      </header>
    
    <div class="article-entry" itemprop="articleBody">
      
{content}
      
    </div>
    <footer class="article-footer">
      <a data-url="#" data-id="" class="article-share-link">Share</a>
      
      
      
    </footer>
  </div>
  
  
  
    
</article>

</section>
        
      </div>
      <footer id="footer">
  
  <div class="outer">
    <div id="footer-info" class="inner">
      &copy; 2026 yylover<br>
      Powered by <a href="http://hexo.io/" target="_blank">Hexo</a>
    </div>
  </div>
</footer>
    </div>
    <nav id="mobile-nav">
  
    <a href="/" class="mobile-nav-link">Home</a>
  
    <a href="/apps" class="mobile-nav-link">应用</a>
  
    <a href="/privacy" class="mobile-nav-link">隐私政策</a>
  
    <a href="/support" class="mobile-nav-link">技术支持</a>
  
    <a href="/about" class="mobile-nav-link">关于</a>
  
</nav>
    

<script src="//ajax.googleapis.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>


  <link rel="stylesheet" href="/fancybox/jquery.fancybox.css">
  <script src="/fancybox/jquery.fancybox.pack.js"></script>


<script src="/js/script.js"></script>

  </div>
</body>
</html>
'''
    return template

# 处理单个Markdown文件
def process_file(input_file, output_file, title):
    markdown_text = read_markdown(input_file)
    html_content = convert_to_html(markdown_text)
    full_html = generate_full_html(title, html_content)
    
    # 确保输出目录存在
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(full_html)
    
    print(f"Converted {input_file} to {output_file}")

# 自动处理所有应用的隐私政策
def process_all_privacy_policies():
    privacy_dir = 'privacy'
    
    # 遍历privacy目录下的所有应用文件夹
    for app_name in os.listdir(privacy_dir):
        app_dir = os.path.join(privacy_dir, app_name)
        
        # 确保是目录
        if not os.path.isdir(app_dir):
            continue
        
        # 处理中文隐私政策
        zh_file = os.path.join(app_dir, 'privacy.md')
        if os.path.exists(zh_file):
            output_file = os.path.join(app_dir, 'index.html')
            title = f'{app_name}隐私政策'
            process_file(zh_file, output_file, title)
        
        # 处理英文隐私政策
        en_file = os.path.join(app_dir, 'privacy-eng.md')
        if os.path.exists(en_file):
            output_file = os.path.join(app_dir, 'index-eng.html')
            title = f'{app_name} Privacy Policy'
            process_file(en_file, output_file, title)

# 主函数
def main():
    process_all_privacy_policies()

if __name__ == '__main__':
    main()
