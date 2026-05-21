import re

with open('index.html', 'r') as f:
    content = f.read()

new_article = """<article class="blog-post">
                    <div class="blog-post-content">
                        <span class="blog-date">April 15, 2025</span>
                        <h3>Extracting Huawei FreeBuds Pro 5 Firmware</h3>
                        <p>Have you ever wondered what makes your wireless earbuds tick? I set out to analyze the firmware of the FreeBuds Pro 5. By decompiling the Huawei Audio Connect app, bypassing a custom certificate pinning mechanism with mitmproxy, and patching the smali code, I managed to intercept the OTA update to grab the raw binary.</p>
                        <a href="blog/blog-huawei-firmware.html" class="read-more">Read More <i class="fas fa-arrow-right"></i></a>
                    </div>
                </article>
                """

target = '<h3 style="margin-top: 3rem; margin-bottom: 1.5rem; color: var(--accent);">Reverse Engineering</h3>\n            <div class="blog-grid">'
content = content.replace(target, target + '\n                ' + new_article)

with open('index.html', 'w') as f:
    f.write(content)
