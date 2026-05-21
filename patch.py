import re

with open("index.html", "r") as f:
    content = f.read()

new_blog_section = """<section id="blog" class="section bg-alt blog-section">
            <h2 class="section-title">Technical Blog</h2>
            <p class="blog-intro">Deep dives into my past projects, algorithms, and technical challenges.</p>
            
            <h3 style="margin-top: 3rem; margin-bottom: 1.5rem; color: var(--accent);">AI & Machine Learning</h3>
            <div class="blog-grid">
                <article class="blog-post">
                    <div class="blog-post-content">
                        <span class="blog-date">August 12, 2023</span>
                        <h3>Fine-Tuning Flan-T5: Cutting Training Time in Half</h3>
                        <p>For my Bachelor's thesis, I tackled automatic ad description generation. Scraping over 9,000 listings yielded a rich dataset of 44 features. The challenge wasn't just accuracy—it was efficiency. By leveraging correlation feature selection, I managed to reduce training epochs from 10 to 5 for Flan-T5. This 50% drop in compute costs maintained a solid 0.16 ROUGE accuracy, proving that smarter data engineering can easily rival throwing more compute at the problem.</p>
                        <a href="blog-flan-t5.html" class="read-more">Read More <i class="fas fa-arrow-right"></i></a>
                    </div>
                </article>

                <article class="blog-post">
                    <div class="blog-post-content">
                        <span class="blog-date">November 22, 2022</span>
                        <h3>Winning Strategies: Statistical Encoding for Categorical Data</h3>
                        <p>In a recent university group competition to predict income tiers, traditional one-hot or label encoding wasn't cutting it due to high cardinality and implicit bias. Our team engineered a novel statistical encoding approach based on demographic distributions. This reduced feature dimensionality while preserving nuanced relationships, ultimately leading to the highest prediction score in the entire class.</p>
                        <a href="blog-statistical-encoding.html" class="read-more">Read More <i class="fas fa-arrow-right"></i></a>
                    </div>
                </article>
            </div>

            <h3 style="margin-top: 3rem; margin-bottom: 1.5rem; color: var(--accent);">Reverse Engineering</h3>
            <div class="blog-grid">
                <article class="blog-post">
                    <div class="blog-post-content">
                        <span class="blog-date">March 05, 2025</span>
                        <h3>Android Reverse Engineering: Bypassing App Certificates</h3>
                        <p>Extracting raw firmware from proprietary hardware often starts with its companion app. Using tools like `jadx` and `APKtool`, I disassembled a commercial Android application to understand its API endpoints. The tricky part? Certificate pinning. By configuring a custom authentication workflow via `mitmproxy`, I successfully intercepted the traffic and downloaded the raw firmware package, opening up new paths for security analysis.</p>
                        <a href="blog-reverse-engineering.html" class="read-more">Read More <i class="fas fa-arrow-right"></i></a>
                    </div>
                </article>
            </div>
        </section>"""

content = re.sub(r'<section id="blog" class="section bg-alt blog-section">.*?</section>', new_blog_section, content, flags=re.DOTALL)

with open("index.html", "w") as f:
    f.write(content)
