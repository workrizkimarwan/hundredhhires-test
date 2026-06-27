# hundredhhires-test

**Tools Installed**

-⁠  ⁠Cursor (code editor)

-⁠  ⁠Claude Code extension

-⁠  ⁠Codex extension

**Steps Completed**

-  ⁠Installed Cursor as the main code editor

-  ⁠Added the Claude Code extension

-  ⁠Added the Codex extension

-  Cloned the repository to my local machine 
``` bash 
`git clone`
```

-⁠  ⁠Initialized a local Git repository 
``` bash 
`git init`
```

-⁠  ⁠Connected the local repository to a remote GitHub repository 
```bash 
`git remote add origin`
```

-⁠  ⁠Staged and committed changes 
``` bash 
`git add`, `git commit`
```

-⁠  ⁠Pushed the repository to GitHub 
``` bash 
⁠`git push origin main`
```

**Issues Encountered & Solutions**
- **Issue:** Git push to GitHub failed due to missing `user.name` and `user.email` configuration.

- **Solution:** Configured Git identity using:
```bash
  git config --global user.name "work Rizki"
  git config --global user.email "work.rizkimarwan@gamil.com"
```

  After setting this up, commits and pushes worked as expected.

---

**Research Project: LinkedIn Organic Content Strategy for B2B SaaS**

I chose "LinkedIn organic content strategy for B2B SaaS" as my research topic. The goal is to study how genuine practitioners (not just commentators) approach organic LinkedIn content, and to collect enough real source material to support a real playbook later.

**What I collected and why**

I identified 10 experts who actively practice what they teach — people running real content motions, podcasts, or campaigns, not just writing generic advice. The full list with profile links, dates, and selection notes is in `research/sources.md`.

I deliberately avoided two traps when selecting these experts:

-⁠  ⁠Agency listicles over practitioners. Many "Top LinkedIn Influencer" articles are dominated by agencies selling services rather than individuals actually running their own content motion.

-⁠  ⁠Generic SEO roundups over signal. Several search results just recycled the same five names. I cross-checked each candidate against evidence of hands-on practice (a podcast they host, a documented campaign, or founder-led content tied directly to their name) before including them.

The final list intentionally mixes channel types — LinkedIn-native creators, podcast hosts, and YouTube — since most B2B SaaS practitioners repurpose the same strategic thinking across multiple formats.

**What I collected**

-⁠  ⁠10 LinkedIn posts, one per expert, summarized in my own words with links to the original post (`research/linkedin-posts/`)

-⁠  ⁠2 YouTube transcripts collected using a Python script with the `youtube-transcript-api` library (`research/youtube-transcripts/`)

**Repository structure**

**Progress**

-⁠  ⁠Selected 10 experts and documented selection reasoning

-⁠  ⁠Collected LinkedIn posts for all 10 experts

-⁠  ⁠Collected 2 YouTube transcripts using a custom Python script

-⁠  ⁠Commits and pushes were made incrementally as work progressed, not in a single batch at the end