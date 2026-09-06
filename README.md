# Jailbreak-Observatory

## 🌐 [Open the Interactive Jailbreak Observatory →](https://genggengsvan.github.io/Jailbreak-Observatory/)

[![Live visualization](https://img.shields.io/badge/Live-Interactive_Research_Map-56d6a4?style=for-the-badge&logo=githubpages&logoColor=white)](https://genggengsvan.github.io/Jailbreak-Observatory/)

[![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/GenggengSvan/Jailbreak-Observatory)
[![GitHub Repo stars](https://img.shields.io/github/stars/GenggengSvan/Jailbreak-Observatory)](https://github.com/GenggengSvan/Jailbreak-Observatory)
<img src="https://img.shields.io/badge/Jailbreak-green">

## 🔭 Interactive Research Map

Explore the collection as a visual timeline of attacks, defenses, benchmarks, and mechanism studies:

Select a paper to reveal metadata-derived research neighbors and attack–defense counterpoints. The original Markdown collection remains the source of truth; the visualization dataset is rebuilt automatically for GitHub Pages.

KDD and IJCAI historical records are collected by `scripts/update_conference_papers.py`; 2026 records are collected across official proceedings, accepted-paper indexes, and conference programs by `scripts/update_2026_papers.py`. `Published` means a formal proceedings/DOI record exists, while `Accepted` means the title is verifiable on an official acceptance or program page. Preprints alone are not eligible. Title candidates are filtered and classified with title + abstract signals.

> [!Important]
>
> In this repository, you can find 📊 the [acceptance status of papers related to Jailbreak research](#document-list-by-conference) and 📑 the [Jailbreak articles with more than 50 citations](#cite).

***If you find our project valuable, we would greatly appreciate it if you could give us a star~*⭐**

---
<a id="document-list-by-conference"></a>
## 📊 Document List by Conference

<table>
<tr><th style='text-align:center'>Conference</th><th style='text-align:center'>Year</th><th style='text-align:center'>Document</th><th style='text-align:center'>Papers Count</th></tr>
<tr><td style='text-align:center;vertical-align:middle' rowspan='3'><strong>NIPS</strong></td><td style='text-align:center'>2025</td><td><a href='Conference/NIPS/nips2025.md'>NIPS2025</a></td><td style='text-align:center'>37</td></tr>
<tr><td style='text-align:center'>2024</td><td><a href='Conference/NIPS/nips2024.md'>NIPS2024</a></td><td style='text-align:center'>33</td></tr>
<tr><td style='text-align:center'>2023</td><td><a href='Conference/NIPS/nips2023.md'>NIPS2023</a></td><td style='text-align:center'>2</td></tr>
<tr><td style='text-align:center;vertical-align:middle' rowspan='3'><strong>ICLR</strong></td><td style='text-align:center'>2026</td><td><a href='Conference/ICLR/iclr2026.md'>ICLR2026</a></td><td style='text-align:center'>46</td></tr>
<tr><td style='text-align:center'>2025</td><td><a href='Conference/ICLR/iclr2025.md'>ICLR2025</a></td><td style='text-align:center'>35</td></tr>
<tr><td style='text-align:center'>2024</td><td><a href='Conference/ICLR/iclr2024.md'>ICLR2024</a></td><td style='text-align:center'>8</td></tr>
<tr><td style='text-align:center;vertical-align:middle' rowspan='3'><strong>ICML</strong></td><td style='text-align:center'>2026</td><td><a href='Conference/ICML/icml2026.md'>ICML2026</a></td><td style='text-align:center'>47</td></tr>
<tr><td style='text-align:center'>2025</td><td><a href='Conference/ICML/icml2025.md'>ICML2025</a></td><td style='text-align:center'>23</td></tr>
<tr><td style='text-align:center'>2024</td><td><a href='Conference/ICML/icml2024.md'>ICML2024</a></td><td style='text-align:center'>10</td></tr>
<tr><td style='text-align:center;vertical-align:middle' rowspan='3'><strong>AAAI</strong></td><td style='text-align:center'>2026</td><td><a href='Conference/AAAI/aaai2026.md'>AAAI2026</a></td><td style='text-align:center'>21</td></tr>
<tr><td style='text-align:center'>2025</td><td><a href='Conference/AAAI/aaai2025.md'>AAAI2025</a></td><td style='text-align:center'>17</td></tr>
<tr><td style='text-align:center'>2024</td><td><a href='Conference/AAAI/aaai2024.md'>AAAI2024</a></td><td style='text-align:center'>1</td></tr>
<tr><td style='text-align:center;vertical-align:middle' rowspan='3'><strong>ACL</strong></td><td style='text-align:center'>2026</td><td><a href='Conference/ACL/acl2026.md'>ACL2026</a></td><td style='text-align:center'>42</td></tr>
<tr><td style='text-align:center'>2025</td><td><a href='Conference/ACL/acl2025.md'>ACL2025</a></td><td style='text-align:center'>59</td></tr>
<tr><td style='text-align:center'>2024</td><td><a href='Conference/ACL/acl2024.md'>ACL2024</a></td><td style='text-align:center'>18</td></tr>
<tr><td style='text-align:center;vertical-align:middle' rowspan='2'><strong>EMNLP</strong></td><td style='text-align:center'>2024</td><td><a href='Conference/EMNLP/emnlp2024.md'>EMNLP2024</a></td><td style='text-align:center'>20</td></tr>
<tr><td style='text-align:center'>2023</td><td><a href='Conference/EMNLP/emnlp2023.md'>EMNLP2023</a></td><td style='text-align:center'>4</td></tr>
<tr><td style='text-align:center;vertical-align:middle' rowspan='2'><strong>NAACL</strong></td><td style='text-align:center'>2025</td><td><a href='Conference/NAACL/naacl2025.md'>NAACL2025</a></td><td style='text-align:center'>26</td></tr>
<tr><td style='text-align:center'>2024</td><td><a href='Conference/NAACL/naacl2024.md'>NAACL2024</a></td><td style='text-align:center'>6</td></tr>
<tr><td style='text-align:center;vertical-align:middle' rowspan='2'><strong>WWW</strong></td><td style='text-align:center'>2026</td><td><a href='Conference/WWW/www2026.md'>WWW2026</a></td><td style='text-align:center'>2</td></tr>
<tr><td style='text-align:center'>2025</td><td><a href='Conference/WWW/www2025.md'>WWW2025</a></td><td style='text-align:center'>2</td></tr>
<tr><td style='text-align:center;vertical-align:middle' rowspan='3'><strong>SP</strong></td><td style='text-align:center'>2026</td><td><a href='Conference/SP/sp2026.md'>SP2026</a></td><td style='text-align:center'>8</td></tr>
<tr><td style='text-align:center'>2025</td><td><a href='Conference/SP/sp2025.md'>SP2025</a></td><td style='text-align:center'>2</td></tr>
<tr><td style='text-align:center'>2024</td><td><a href='Conference/SP/sp2024.md'>SP2024</a></td><td style='text-align:center'>1</td></tr>
<tr><td style='text-align:center;vertical-align:middle' rowspan='1'><strong>CCS</strong></td><td style='text-align:center'>2024</td><td><a href='Conference/CCS/ccs2024.md'>CCS2024</a></td><td style='text-align:center'>1</td></tr>
<tr><td style='text-align:center;vertical-align:middle' rowspan='2'><strong>NDSS</strong></td><td style='text-align:center'>2026</td><td><a href='Conference/NDSS/ndss2026.md'>NDSS2026</a></td><td style='text-align:center'>8</td></tr>
<tr><td style='text-align:center'>2024</td><td><a href='Conference/NDSS/ndss2024_fall.md'>NDSS2024</a></td><td style='text-align:center'>1</td></tr>
<tr><td style='text-align:center;vertical-align:middle' rowspan='4'><strong>KDD</strong></td><td style='text-align:center'>2026</td><td><a href='Conference/KDD/kdd2026.md'>KDD2026</a></td><td style='text-align:center'>1</td></tr>
<tr><td style='text-align:center'>2025</td><td><a href='Conference/KDD/kdd2025.md'>KDD2025</a></td><td style='text-align:center'>2</td></tr>
<tr><td style='text-align:center'>2024</td><td><a href='Conference/KDD/kdd2024.md'>KDD2024</a></td><td style='text-align:center'>1</td></tr>
<tr><td style='text-align:center'>2023</td><td><a href='Conference/KDD/kdd2023.md'>KDD2023</a></td><td style='text-align:center'>0</td></tr>
<tr><td style='text-align:center;vertical-align:middle' rowspan='4'><strong>IJCAI</strong></td><td style='text-align:center'>2026</td><td><a href='Conference/IJCAI/ijcai2026.md'>IJCAI2026</a></td><td style='text-align:center'>1</td></tr>
<tr><td style='text-align:center'>2025</td><td><a href='Conference/IJCAI/ijcai2025.md'>IJCAI2025</a></td><td style='text-align:center'>4</td></tr>
<tr><td style='text-align:center'>2024</td><td><a href='Conference/IJCAI/ijcai2024.md'>IJCAI2024</a></td><td style='text-align:center'>1</td></tr>
<tr><td style='text-align:center'>2023</td><td><a href='Conference/IJCAI/ijcai2023.md'>IJCAI2023</a></td><td style='text-align:center'>0</td></tr>
<tr><td style='text-align:center;vertical-align:middle' rowspan='1'><strong>USENIX Security</strong></td><td style='text-align:center'>2026</td><td><a href='Conference/USENIX Security/usenixsecurity2026.md'>USENIX Security2026</a></td><td style='text-align:center'>10</td></tr>
</table>


## 📋 Legend

- **Conference**: Academic conference (NIPS, ICLR, etc.)
- **Papers Count**: Number of papers collection documents in this conference
- **Document**: Each link points to a Markdown file containing classified and analyzed research papers

#### Document Content
Each document typically contains:
- Paper title and metadata
- Classification (Attack/Defense/Benchmark/Mechanism/Other)
- LLM type (Text/Vision/Hybrid/Agent)
- Average rating scores
- Direct links to original papers

---
<a id="cite"></a>
## 📑 Articles with More Than 50 Citations

## Summary Table
For full details, see the <a href='citations_over_50.md'>articles with more than 50 citations</a> (Google Scholar; refreshed monthly).

Citation counts are refreshed by [`.github/workflows/update-citations.yml`](.github/workflows/update-citations.yml) on the first day of each month. Because Google Scholar does not provide an official public API, the workflow uses SerpApi's Google Scholar engine; add a repository secret named `SERPAPI_API_KEY` before enabling the scheduled run. If Google Scholar returns a CAPTCHA, rate-limit, empty result, or an uncertain title match, the script keeps the previous value and refuses to publish an incomplete refresh.

<table>
  <thead><tr><th>Target</th><th>Category</th><th>Title</th><th>Citations</th></tr></thead>
  <tbody>
  <tr><td>Text</td><td>Attack</td><td>AutoDAN: Generating Stealthy Jailbreak Prompts on Aligned Large Language Models</td><td>526</td></tr>
  <tr><td>Text</td><td>Attack</td><td>GPTFUZZER: Red Teaming Large Language Models with Auto-Generated Jailbreak Prompts</td><td>481</td></tr>
  <tr><td>Text</td><td>Attack</td><td>How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs</td><td>459</td></tr>
  <tr><td>Text</td><td>Benchmark</td><td>&quot;Do Anything Now&quot;: Characterizing and Evaluating In-The-Wild Jailbreak Prompts on Large Language Models</td><td>426</td></tr>
  <tr><td>Text</td><td>Attack</td><td>Catastrophic Jailbreak of Open-source LLMs via Exploiting Generation</td><td>390</td></tr>
  <tr><td>Text</td><td>Attack</td><td>Jailbreak and Guard Aligned Language Models with Only Few In-Context Demonstrations</td><td>383</td></tr>
  <tr><td>Text</td><td>Defense</td><td>Defending ChatGPT against jailbreak attack via self-reminders</td><td>337</td></tr>
  <tr><td>Text</td><td>Attack</td><td>Low-Resource Languages Jailbreak GPT-4</td><td>261</td></tr>
  <tr><td>Vision</td><td>Attack</td><td>Visual Adversarial Examples Jailbreak Aligned Large Language Models</td><td>258</td></tr>
  <tr><td>Vision</td><td>Attack</td><td>Jailbreak in pieces: Compositional Adversarial Attacks on Multi-Modal Language Models</td><td>217</td></tr>
  <tr><td>Text</td><td>Attack</td><td>A Wolf in Sheep’s Clothing: Generalized Nested Jailbreak Prompts can Fool Large Language Models Easily</td><td>202</td></tr>
  <tr><td>Text</td><td>Other</td><td>Jailbreak Attacks and Defenses Against Large Language Models: A Survey</td><td>191</td></tr>
  <tr><td>Text</td><td>Attack</td><td>Jailbreaker: Automated Jailbreak Across Multiple Large Language Model Chatbots</td><td>187</td></tr>
  <tr><td>Text</td><td>Defense</td><td>Multilingual Jailbreak Challenges in Large Language Models</td><td>186</td></tr>
  <tr><td>Text</td><td>Attack</td><td>ArtPrompt: ASCII Art-based Jailbreak Attacks against Aligned LLMs</td><td>182</td></tr>
  <tr><td>Hybrid</td><td>Attack</td><td>Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack</td><td>181</td></tr>
  <tr><td>Text</td><td>Defense</td><td>SafeDecoding: Defending against Jailbreak Attacks via Safety-Aware Decoding</td><td>179</td></tr>
  <tr><td>Vision</td><td>Benchmark</td><td>JailBreakV: A Benchmark for Assessing the Robustness of MultiModal Large Language Models against Jailbreak Attacks</td><td>157</td></tr>
  <tr><td>Agent</td><td>Defense</td><td>AutoDefense: Multi-Agent LLM Defense against Jailbreak Attacks</td><td>117</td></tr>
  <tr><td>Text</td><td>Attack</td><td>Universal Jailbreak Backdoors from Poisoned Human Feedback</td><td>106</td></tr>
  <tr><td>Hybrid</td><td>Attack</td><td>Agent Smith: A Single Image Can Jailbreak One Million Multimodal LLM Agents Exponentially Fast</td><td>91</td></tr>
  <tr><td>Text</td><td>Attack</td><td>AutoDAN-Turbo: A Lifelong Agent for Strategy Self-Exploration to Jailbreak LLMs</td><td>84</td></tr>
  <tr><td>Text</td><td>Benchmark</td><td>A Comprehensive Study of Jailbreak Attack versus Defense for Large Language Models</td><td>83</td></tr>
  <tr><td>Text</td><td>Benchmark</td><td>JailbreakRadar: Comprehensive Assessment of Jailbreak Attacks Against LLMs</td><td>79</td></tr>
  <tr><td>Text</td><td>Attack</td><td>Don&#x27;t Listen To Me: Understanding and Exploring Jailbreak Prompts of Large Language Models</td><td>78</td></tr>
  <tr><td>Text</td><td>Mechanism</td><td>How Alignment and Jailbreak Work: Explain LLM Safety through Intermediate Hidden States</td><td>71</td></tr>
  <tr><td>Vision</td><td>Attack</td><td>Jailbreak Vision Language Models via Bi-Modal Adversarial Prompt</td><td>71</td></tr>
  <tr><td>Text</td><td>Defense</td><td>Defending Large Language Models against Jailbreak Attacks via Semantic Smoothing</td><td>69</td></tr>
  <tr><td>Hybrid</td><td>Benchmark</td><td>LLM Jailbreak Attack versus Defense Techniques - A Comprehensive Study</td><td>67</td></tr>
  <tr><td>Text</td><td>Attack</td><td>Pandora: Jailbreak GPTs by Retrieval Augmented Generation Poisoning</td><td>66</td></tr>
  <tr><td>Text</td><td>Attack</td><td>Play Guessing Game with LLM: Indirect Jailbreak Attack with Implicit Clues</td><td>64</td></tr>
  <tr><td>Text</td><td>Benchmark</td><td>Latent Jailbreak: A Benchmark for Evaluating Text Safety and Output Robustness of Large Language Models</td><td>60</td></tr>
  <tr><td>Text</td><td>Defense</td><td>GradSafe: Detecting Jailbreak Prompts for LLMs via Safety-Critical Gradient Analysis</td><td>58</td></tr>
  <tr><td>Text</td><td>Attack</td><td>FuzzLLM: A Novel and Universal Fuzzing Framework for Proactively Discovering Jailbreak Vulnerabilities in Large Language Models</td><td>56</td></tr>
  <tr><td>Text</td><td>Defense</td><td>Defending Large Language Models Against Jailbreak Attacks via Layer-specific Editing</td><td>52</td></tr>
  <tr><td>Vision</td><td>Attack</td><td>Query-Relevant Images Jailbreak Large Multi-Modal Models</td><td>52</td></tr>
  <tr><td>Vision</td><td>Attack</td><td>Visual-RolePlay: Universal Jailbreak Attack on MultiModal Large Language Models via Role-playing Image Characte</td><td>52</td></tr>
  </tbody>
</table>
