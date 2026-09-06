# Papers with More Than 50 Citations

> Citation counts are queried from Google Scholar and refreshed monthly. Only papers with **more than 50 citations** are included.
> Last successful refresh: 2026-09-06

## AutoDAN: Generating Stealthy Jailbreak Prompts on Aligned Large Language Models
📑 Citations: 1602
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2023  📍 Venue: International Conference on Learning Representations

Abstract:
The aligned Large Language Models (LLMs) are powerful language understanding and decision-making tools that are created through extensive alignment with human feedback. However, these large models remain susceptible to jailbreak attacks, where adversaries manipulate prompts to elicit malicious outputs that should not be given by aligned LLMs. Investigating jailbreak prompts can lead us to delve into the limitations of LLMs and further guide us to secure them. Unfortunately, existing jailbreak techniques suffer from either (1) scalability issues, where attacks heavily rely on manual crafting of prompts, or (2) stealthiness problems, as attacks depend on token-based algorithms to generate prompts that are often semantically meaningless, making them susceptible to detection through basic perplexity testing. In light of these challenges, we intend to answer this question: Can we develop an approach that can automatically generate stealthy jailbreak prompts? In this paper, we introduce AutoDAN, a novel jailbreak attack against aligned LLMs. AutoDAN can automatically generate stealthy jailbreak prompts by the carefully designed hierarchical genetic algorithm. Extensive evaluations demonstrate that AutoDAN not only automates the process while preserving semantic meaningfulness, but also demonstrates superior attack strength in cross-model transferability, and cross-sample universality compared with the baseline. Moreover, we also compare AutoDAN with perplexity-based defense methods and show that AutoDAN can bypass them effectively.

## "Do Anything Now": Characterizing and Evaluating In-The-Wild Jailbreak Prompts on Large Language Models
📑 Citations: 1581
🎯 Target: Text  🗂️ Category: Benchmark
📅 Year: 2023  📍 Venue: Conference on Computer and Communications Security

Abstract:
The misuse of large language models (LLMs) has drawn significant attention from the general public and LLM vendors. One particular type of adversarial prompt, known as jailbreak prompt, has emerged as the main attack vector to bypass the safeguards and elicit harmful content from LLMs. In this paper, employing our new framework JailbreakHub, we conduct a comprehensive analysis of 1,405 jailbreak prompts spanning from December 2022 to December 2023. We identify 131 jailbreak communities and discover unique characteristics of jailbreak prompts and their major attack strategies, such as prompt injection and privilege escalation. We also observe that jailbreak prompts increasingly shift from online Web communities to prompt-aggregation websites and 28 user accounts have consistently optimized jailbreak prompts over 100 days. To assess the potential harm caused by jailbreak prompts, we create a question set comprising 107,250 samples across 13 forbidden scenarios. Leveraging this dataset, our experiments on six popular LLMs show that their safeguards cannot adequately defend jailbreak prompts in all scenarios. Particularly, we identify five highly effective jailbreak prompts that achieve 0.95 attack success rates on ChatGPT (GPT-3.5) and GPT-4, and the earliest one has persisted online for over 240 days. We hope that our study can facilitate the research community and LLM vendors in promoting safer and regulated LLMs.

## Automatic Prompt Optimization with "Gradient Descent" and Beam Search
📑 Citations: 979
🎯 Target: Text  🗂️ Category: Defense
📅 Year: 2023  📍 Venue: EMNLP

Abstract:


## DecodingTrust: A Comprehensive Assessment of Trustworthiness in GPT Models
📑 Citations: 905
🎯 Target: Text  🗂️ Category: Benchmark
📅 Year: 2023  📍 Venue: NIPS

Abstract:


## How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs
📑 Citations: 844
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2024  📍 Venue: Annual Meeting of the Association for Computational Linguistics

Abstract:
Most traditional AI safety research has approached AI models as machines and centered on algorithm-focused attacks developed by security experts. As large language models (LLMs) become increasingly common and competent, non-expert users can also impose risks during daily interactions. This paper introduces a new perspective to jailbreak LLMs as human-like communicators, to explore this overlooked intersection between everyday language interaction and AI safety. Specifically, we study how to persuade LLMs to jailbreak them. First, we propose a persuasion taxonomy derived from decades of social science research. Then, we apply the taxonomy to automatically generate interpretable persuasive adversarial prompts (PAP) to jailbreak LLMs. Results show that persuasion significantly increases the jailbreak performance across all risk categories: PAP consistently achieves an attack success rate of over $92\%$ on Llama 2-7b Chat, GPT-3.5, and GPT-4 in $10$ trials, surpassing recent algorithm-focused attacks. On the defense side, we explore various mechanisms against PAP and, found a significant gap in existing defenses, and advocate for more fundamental mitigation for highly interactive LLMs

## GPTFUZZER: Red Teaming Large Language Models with Auto-Generated Jailbreak Prompts
📑 Citations: 726
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2023  📍 Venue: arXiv.org

Abstract:
Large language models (LLMs) have recently experienced tremendous popularity and are widely used from casual conversations to AI-driven programming. However, despite their considerable success, LLMs are not entirely reliable and can give detailed guidance on how to conduct harmful or illegal activities. While safety measures can reduce the risk of such outputs, adversarial jailbreak attacks can still exploit LLMs to produce harmful content. These jailbreak templates are typically manually crafted, making large-scale testing challenging. In this paper, we introduce GPTFuzz, a novel black-box jailbreak fuzzing framework inspired by the AFL fuzzing framework. Instead of manual engineering, GPTFuzz automates the generation of jailbreak templates for red-teaming LLMs. At its core, GPTFuzz starts with human-written templates as initial seeds, then mutates them to produce new templates. We detail three key components of GPTFuzz: a seed selection strategy for balancing efficiency and variability, mutate operators for creating semantically equivalent or similar sentences, and a judgment model to assess the success of a jailbreak attack. We evaluate GPTFuzz against various commercial and open-source LLMs, including ChatGPT, LLaMa-2, and Vicuna, under diverse attack scenarios. Our results indicate that GPTFuzz consistently produces jailbreak templates with a high success rate, surpassing human-crafted templates. Remarkably, GPTFuzz achieves over 90% attack success rates against ChatGPT and Llama-2 models, even with suboptimal initial seed templates. We anticipate that GPTFuzz will be instrumental for researchers and practitioners in examining LLM robustness and will encourage further exploration into enhancing LLM safety.

## Visual Adversarial Examples Jailbreak Aligned Large Language Models
📑 Citations: 625
🎯 Target: Vision  🗂️ Category: Attack
📅 Year: 2023  📍 Venue: AAAI Conference on Artificial Intelligence

Abstract:
Warning: this paper contains data, prompts, and model outputs that are offensive in nature. Recently, there has been a surge of interest in integrating vision into Large Language Models (LLMs), exemplified by Visual Language Models (VLMs) such as Flamingo and GPT-4. This paper sheds light on the security and safety implications of this trend. First, we underscore that the continuous and high-dimensional nature of the visual input makes it a weak link against adversarial attacks, representing an expanded attack surface of vision-integrated LLMs. Second, we highlight that the versatility of LLMs also presents visual attackers with a wider array of achievable adversarial objectives, extending the implications of security failures beyond mere misclassification. As an illustration, we present a case study in which we exploit visual adversarial examples to circumvent the safety guardrail of aligned LLMs with integrated vision. Intriguingly, we discover that a single visual adversarial example can universally jailbreak an aligned LLM, compelling it to heed a wide range of harmful instructions (that it otherwise would not) and generate harmful content that transcends the narrow scope of a `few-shot' derogatory corpus initially employed to optimize the adversarial example. Our study underscores the escalating adversarial risks associated with the pursuit of multimodality. Our findings also connect the long-studied adversarial vulnerabilities of neural networks to the nascent field of AI alignment. The presented attack suggests a fundamental adversarial challenge for AI alignment, especially in light of the emerging trend toward multimodality in frontier foundation models.

## Multilingual Jailbreak Challenges in Large Language Models
📑 Citations: 622
🎯 Target: Text  🗂️ Category: Defense
📅 Year: 2023  📍 Venue: International Conference on Learning Representations

Abstract:
While large language models (LLMs) exhibit remarkable capabilities across a wide range of tasks, they pose potential safety concerns, such as the ``jailbreak'' problem, wherein malicious instructions can manipulate LLMs to exhibit undesirable behavior. Although several preventive measures have been developed to mitigate the potential risks associated with LLMs, they have primarily focused on English. In this study, we reveal the presence of multilingual jailbreak challenges within LLMs and consider two potential risky scenarios: unintentional and intentional. The unintentional scenario involves users querying LLMs using non-English prompts and inadvertently bypassing the safety mechanisms, while the intentional scenario concerns malicious users combining malicious instructions with multilingual prompts to deliberately attack LLMs. The experimental results reveal that in the unintentional scenario, the rate of unsafe content increases as the availability of languages decreases. Specifically, low-resource languages exhibit about three times the likelihood of encountering harmful content compared to high-resource languages, with both ChatGPT and GPT-4. In the intentional scenario, multilingual prompts can exacerbate the negative impact of malicious instructions, with astonishingly high rates of unsafe output: 80.92\% for ChatGPT and 40.71\% for GPT-4. To handle such a challenge in the multilingual context, we propose a novel \textsc{Self-Defense} framework that automatically generates multilingual training data for safety fine-tuning. Experimental results show that ChatGPT fine-tuned with such data can achieve a substantial reduction in unsafe content generation. Data is available at \url{https://github.com/DAMO-NLP-SG/multilingual-safety-for-LLMs}.

## A StrongREJECT for Empty Jailbreaks
📑 Citations: 619
🎯 Target: Text  🗂️ Category: Benchmark
📅 Year: 2024  📍 Venue: NIPS

Abstract:


## Catastrophic Jailbreak of Open-source LLMs via Exploiting Generation
📑 Citations: 614
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2023  📍 Venue: International Conference on Learning Representations

Abstract:
The rapid progress in open-source large language models (LLMs) is significantly advancing AI development. Extensive efforts have been made before model release to align their behavior with human values, with the primary goal of ensuring their helpfulness and harmlessness. However, even carefully aligned models can be manipulated maliciously, leading to unintended behaviors, known as"jailbreaks". These jailbreaks are typically triggered by specific text inputs, often referred to as adversarial prompts. In this work, we propose the generation exploitation attack, an extremely simple approach that disrupts model alignment by only manipulating variations of decoding methods. By exploiting different generation strategies, including varying decoding hyper-parameters and sampling methods, we increase the misalignment rate from 0% to more than 95% across 11 language models including LLaMA2, Vicuna, Falcon, and MPT families, outperforming state-of-the-art attacks with $30\times$ lower computational cost. Finally, we propose an effective alignment method that explores diverse generation strategies, which can reasonably reduce the misalignment rate under our attack. Altogether, our study underscores a major failure in current safety evaluation and alignment procedures for open-source LLMs, strongly advocating for more comprehensive red teaming and better alignment before releasing such models. Our code is available at https://github.com/Princeton-SysML/Jailbreak_LLM.

## Jailbreak and Guard Aligned Language Models with Only Few In-Context Demonstrations
📑 Citations: 607
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2023  📍 Venue: arXiv.org

Abstract:
Large Language Models (LLMs) have shown remarkable success in various tasks, yet their safety and the risk of generating harmful content remain pressing concerns. In this paper, we delve into the potential of In-Context Learning (ICL) to modulate the alignment of LLMs. Specifically, we propose the In-Context Attack (ICA) which employs harmful demonstrations to subvert LLMs, and the In-Context Defense (ICD) which bolsters model resilience through examples that demonstrate refusal to produce harmful responses. We offer theoretical insights to elucidate how a limited set of in-context demonstrations can pivotally influence the safety alignment of LLMs. Through extensive experiments, we demonstrate the efficacy of ICA and ICD in respectively elevating and mitigating the success rates of jailbreaking prompts. Our findings illuminate the profound influence of ICL on LLM behavior, opening new avenues for improving the safety of LLMs.

## Defending ChatGPT against jailbreak attack via self-reminders
📑 Citations: 550
🎯 Target: Text  🗂️ Category: Defense
📅 Year: 2023  📍 Venue: Nature Machine Intelligence

Abstract:
No abstract provided.

## Low-Resource Languages Jailbreak GPT-4
📑 Citations: 533
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2023  📍 Venue: arXiv.org

Abstract:
AI safety training and red-teaming of large language models (LLMs) are measures to mitigate the generation of unsafe content. Our work exposes the inherent cross-lingual vulnerability of these safety mechanisms, resulting from the linguistic inequality of safety training data, by successfully circumventing GPT-4's safeguard through translating unsafe English inputs into low-resource languages. On the AdvBenchmark, GPT-4 engages with the unsafe translated inputs and provides actionable items that can get the users towards their harmful goals 79% of the time, which is on par with or even surpassing state-of-the-art jailbreaking attacks. Other high-/mid-resource languages have significantly lower attack success rate, which suggests that the cross-lingual vulnerability mainly applies to low-resource languages. Previously, limited training on low-resource languages primarily affects speakers of those languages, causing technological disparities. However, our work highlights a crucial shift: this deficiency now poses a risk to all LLMs users. Publicly available translation APIs enable anyone to exploit LLMs' safety vulnerabilities. Therefore, our work calls for a more holistic red-teaming efforts to develop robust multilingual safeguards with wide language coverage.

## Benchmarking and Defending against Indirect Prompt Injection Attacks on Large Language Models
📑 Citations: 504
🎯 Target: Agent  🗂️ Category: Benchmark
📅 Year: 2025  📍 Venue: KDD

Abstract:


## Jailbreak Attacks and Defenses Against Large Language Models: A Survey
📑 Citations: 493
🎯 Target: Text  🗂️ Category: Other
📅 Year: 2024  📍 Venue: arXiv.org

Abstract:
Large Language Models (LLMs) have performed exceptionally in various text-generative tasks, including question answering, translation, code completion, etc. However, the over-assistance of LLMs has raised the challenge of"jailbreaking", which induces the model to generate malicious responses against the usage policy and society by designing adversarial prompts. With the emergence of jailbreak attack methods exploiting different vulnerabilities in LLMs, the corresponding safety alignment measures are also evolving. In this paper, we propose a comprehensive and detailed taxonomy of jailbreak attack and defense methods. For instance, the attack methods are divided into black-box and white-box attacks based on the transparency of the target model. Meanwhile, we classify defense methods into prompt-level and model-level defenses. Additionally, we further subdivide these attack and defense methods into distinct sub-classes and present a coherent diagram illustrating their relationships. We also conduct an investigation into the current evaluation methods and compare them from different perspectives. Our findings aim to inspire future research and practical implementations in safeguarding LLMs against adversarial attacks. Above all, although jailbreak remains a significant concern within the community, we believe that our work enhances the understanding of this domain and provides a foundation for developing more secure LLMs.

## Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack
📑 Citations: 484
🎯 Target: Hybrid  🗂️ Category: Attack
📅 Year: 2024  📍 Venue: USENIX Security Symposium

Abstract:
Large Language Models (LLMs) have risen significantly in popularity and are increasingly being adopted across multiple applications. These LLMs are heavily aligned to resist engaging in illegal or unethical topics as a means to avoid contributing to responsible AI harms. However, a recent line of attacks, known as jailbreaks, seek to overcome this alignment. Intuitively, jailbreak attacks aim to narrow the gap between what the model can do and what it is willing to do. In this paper, we introduce a novel jailbreak attack called Crescendo. Unlike existing jailbreak methods, Crescendo is a simple multi-turn jailbreak that interacts with the model in a seemingly benign manner. It begins with a general prompt or question about the task at hand and then gradually escalates the dialogue by referencing the model's replies progressively leading to a successful jailbreak. We evaluate Crescendo on various public systems, including ChatGPT, Gemini Pro, Gemini-Ultra, LlaMA-2 70b and LlaMA-3 70b Chat, and Anthropic Chat. Our results demonstrate the strong efficacy of Crescendo, with it achieving high attack success rates across all evaluated models and tasks. Furthermore, we present Crescendomation, a tool that automates the Crescendo attack and demonstrate its efficacy against state-of-the-art models through our evaluations. Crescendomation surpasses other state-of-the-art jailbreaking techniques on the AdvBench subset dataset, achieving 29-61% higher performance on GPT-4 and 49-71% on Gemini-Pro. Finally, we also demonstrate Crescendo's ability to jailbreak multimodal models.

## AgentHarm: A Benchmark for Measuring Harmfulness of LLM Agents
📑 Citations: 478
🎯 Target: Agent  🗂️ Category: Benchmark
📅 Year: 2025  📍 Venue: ICLR

Abstract:


## Jailbreak in pieces: Compositional Adversarial Attacks on Multi-Modal Language Models
📑 Citations: 401
🎯 Target: Vision  🗂️ Category: Attack
📅 Year: 2023  📍 Venue: International Conference on Learning Representations

Abstract:
We introduce new jailbreak attacks on vision language models (VLMs), which use aligned LLMs and are resilient to text-only jailbreak attacks. Specifically, we develop cross-modality attacks on alignment where we pair adversarial images going through the vision encoder with textual prompts to break the alignment of the language model. Our attacks employ a novel compositional strategy that combines an image, adversarially targeted towards toxic embeddings, with generic prompts to accomplish the jailbreak. Thus, the LLM draws the context to answer the generic prompt from the adversarial image. The generation of benign-appearing adversarial images leverages a novel embedding-space-based methodology, operating with no access to the LLM model. Instead, the attacks require access only to the vision encoder and utilize one of our four embedding space targeting strategies. By not requiring access to the LLM, the attacks lower the entry barrier for attackers, particularly when vision encoders such as CLIP are embedded in closed-source LLMs. The attacks achieve a high success rate across different VLMs, highlighting the risk of cross-modality alignment vulnerabilities, and the need for new alignment approaches for multi-modal models.

## A Wolf in Sheep’s Clothing: Generalized Nested Jailbreak Prompts can Fool Large Language Models Easily
📑 Citations: 384
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2023  📍 Venue: North American Chapter of the Association for Computational Linguistics

Abstract:
Large Language Models (LLMs), such as ChatGPT and GPT-4, are designed to provide useful and safe responses. However, adversarial prompts known as ‘jailbreaks’ can circumvent safeguards, leading LLMs to generate potentially harmful content. Exploring jailbreak prompts can help to better reveal the weaknesses of LLMs and further steer us to secure them. Unfortunately, existing jailbreak methods either suffer from intricate manual design or require optimization on other white-box models, which compromises either generalization or efficiency. In this paper, we generalize jailbreak prompt attacks into two aspects: (1) Prompt Rewriting and (2) Scenario Nesting. Based on this, we propose ReNeLLM, an automatic framework that leverages LLMs themselves to generate effective jailbreak prompts. Extensive experiments demonstrate that ReNeLLM significantly improves the attack success rate while greatly reducing the time cost compared to existing baselines. Our study also reveals the inadequacy of current defense methods in safeguarding LLMs. Finally, we analyze the failure of LLMs defense from the perspective of prompt execution priority, and propose corresponding defense strategies. We hope that our research can catalyze both the academic community and LLMs developers towards the provision of safer and more regulated LLMs. The code is available at https://github.com/NJUNLP/ReNeLLM.

## SafeDecoding: Defending against Jailbreak Attacks via Safety-Aware Decoding
📑 Citations: 357
🎯 Target: Text  🗂️ Category: Defense
📅 Year: 2024  📍 Venue: Annual Meeting of the Association for Computational Linguistics

Abstract:
As large language models (LLMs) become increasingly integrated into real-world applications such as code generation and chatbot assistance, extensive efforts have been made to align LLM behavior with human values, including safety. Jailbreak attacks, aiming to provoke unintended and unsafe behaviors from LLMs, remain a significant/leading LLM safety threat. In this paper, we aim to defend LLMs against jailbreak attacks by introducing SafeDecoding, a safety-aware decoding strategy for LLMs to generate helpful and harmless responses to user queries. Our insight in developing SafeDecoding is based on the observation that, even though probabilities of tokens representing harmful contents outweigh those representing harmless responses, safety disclaimers still appear among the top tokens after sorting tokens by probability in descending order. This allows us to mitigate jailbreak attacks by identifying safety disclaimers and amplifying their token probabilities, while simultaneously attenuating the probabilities of token sequences that are aligned with the objectives of jailbreak attacks. We perform extensive experiments on five LLMs using six state-of-the-art jailbreak attacks and four benchmark datasets. Our results show that SafeDecoding significantly reduces the attack success rate and harmfulness of jailbreak attacks without compromising the helpfulness of responses to benign user queries. SafeDecoding outperforms six defense methods.

## ArtPrompt: ASCII Art-based Jailbreak Attacks against Aligned LLMs
📑 Citations: 348
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2024  📍 Venue: Annual Meeting of the Association for Computational Linguistics

Abstract:
Safety is critical to the usage of large language models (LLMs). Multiple techniques such as data filtering and supervised fine-tuning have been developed to strengthen LLM safety. However, currently known techniques presume that corpora used for safety alignment of LLMs are solely interpreted by semantics. This assumption, however, does not hold in real-world applications, which leads to severe vulnerabilities in LLMs. For example, users of forums often use ASCII art, a form of text-based art, to convey image information. In this paper, we propose a novel ASCII art-based jailbreak attack and introduce a comprehensive benchmark Vision-in-Text Challenge (ViTC) to evaluate the capabilities of LLMs in recognizing prompts that cannot be solely interpreted by semantics. We show that five SOTA LLMs (GPT-3.5, GPT-4, Gemini, Claude, and Llama2) struggle to recognize prompts provided in the form of ASCII art. Based on this observation, we develop the jailbreak attack ArtPrompt, which leverages the poor performance of LLMs in recognizing ASCII art to bypass safety measures and elicit undesired behaviors from LLMs. ArtPrompt only requires black-box access to the victim LLMs, making it a practical attack. We evaluate ArtPrompt on five SOTA LLMs, and show that ArtPrompt can effectively and efficiently induce undesired behaviors from all five LLMs. Our code is available at https://github.com/uw-nsl/ArtPrompt.

## JailBreakV: A Benchmark for Assessing the Robustness of MultiModal Large Language Models against Jailbreak Attacks
📑 Citations: 305
🎯 Target: Vision  🗂️ Category: Benchmark
📅 Year: 2024  📍 Venue: Unknown

Abstract:
With the rapid advancements in Multimodal Large Language Models (MLLMs), securing these models against malicious inputs while aligning them with human values has emerged as a critical challenge. In this paper, we investigate an important and unexplored question of whether techniques that successfully jailbreak Large Language Models (LLMs) can be equally effective in jailbreaking MLLMs. To explore this issue, we introduce JailBreakV-28K, a pioneering benchmark designed to assess the transferability of LLM jailbreak techniques to MLLMs, thereby evaluating the robustness of MLLMs against diverse jailbreak attacks. Utilizing a dataset of 2, 000 malicious queries that is also proposed in this paper, we generate 20, 000 text-based jailbreak prompts using advanced jailbreak attacks on LLMs, alongside 8, 000 image-based jailbreak inputs from recent MLLMs jailbreak attacks, our comprehensive dataset includes 28, 000 test cases across a spectrum of adversarial scenarios. Our evaluation of 10 open-source MLLMs reveals a notably high Attack Success Rate (ASR) for attacks transferred from LLMs, highlighting a critical vulnerability in MLLMs that stems from their text-processing capabilities. Our findings underscore the urgent need for future research to address alignment vulnerabilities in MLLMs from both textual and visual inputs.

## Assessing the Brittleness of Safety Alignment via Pruning and Low-Rank Modifications
📑 Citations: 295
🎯 Target: Text  🗂️ Category: Mechanism
📅 Year: 2024  📍 Venue: ICML

Abstract:


## Defending Against Alignment-Breaking Attacks via Robustly Aligned LLM
📑 Citations: 294
🎯 Target: Text  🗂️ Category: Defense
📅 Year: 2024  📍 Venue: ACL

Abstract:


## Jailbreaker: Automated Jailbreak Across Multiple Large Language Model Chatbots
📑 Citations: 267
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2023  📍 Venue: arXiv.org

Abstract:
No abstract provided.

## COLD-Attack: Jailbreaking LLMs with Stealthiness and Controllability
📑 Citations: 262
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2024  📍 Venue: ICML

Abstract:


## Defending Large Language Models Against Jailbreaking Attacks Through Goal Prioritization
📑 Citations: 255
🎯 Target: Text  🗂️ Category: Defense
📅 Year: 2024  📍 Venue: ACL

Abstract:


## AdvPrompter: Fast Adaptive Adversarial Prompting for LLMs
📑 Citations: 254
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2025  📍 Venue: ICML

Abstract:


## AutoDAN-Turbo: A Lifelong Agent for Strategy Self-Exploration to Jailbreak LLMs
📑 Citations: 253
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2024  📍 Venue: International Conference on Learning Representations

Abstract:
In this paper, we propose AutoDAN-Turbo, a black-box jailbreak method that can automatically discover as many jailbreak strategies as possible from scratch, without any human intervention or predefined scopes (e.g., specified candidate strategies), and use them for red-teaming. As a result, AutoDAN-Turbo can significantly outperform baseline methods, achieving a 74.3% higher average attack success rate on public benchmarks. Notably, AutoDAN-Turbo achieves an 88.5 attack success rate on GPT-4-1106-turbo. In addition, AutoDAN-Turbo is a unified framework that can incorporate existing human-designed jailbreak strategies in a plug-and-play manner. By integrating human-designed strategies, AutoDAN-Turbo can even achieve a higher attack success rate of 93.4 on GPT-4-1106-turbo.

## Don't Listen To Me: Understanding and Exploring Jailbreak Prompts of Large Language Models
📑 Citations: 246
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2024  📍 Venue: USENIX Security Symposium

Abstract:
Recent advancements in generative AI have enabled ubiquitous access to large language models (LLMs). Empowered by their exceptional capabilities to understand and generate human-like text, these models are being increasingly integrated into our society. At the same time, there are also concerns on the potential misuse of this powerful technology, prompting defensive measures from service providers. To overcome such protection, jailbreaking prompts have recently emerged as one of the most effective mechanisms to circumvent security restrictions and elicit harmful content originally designed to be prohibited. Due to the rapid development of LLMs and their ease of access via natural languages, the frontline of jailbreak prompts is largely seen in online forums and among hobbyists. To gain a better understanding of the threat landscape of semantically meaningful jailbreak prompts, we systemized existing prompts and measured their jailbreak effectiveness empirically. Further, we conducted a user study involving 92 participants with diverse backgrounds to unveil the process of manually creating jailbreak prompts. We observed that users often succeeded in jailbreak prompts generation regardless of their expertise in LLMs. Building on the insights from the user study, we also developed a system using AI as the assistant to automate the process of jailbreak prompt generation.

## A Comprehensive Study of Jailbreak Attack versus Defense for Large Language Models
📑 Citations: 243
🎯 Target: Text  🗂️ Category: Benchmark
📅 Year: 2024  📍 Venue: Annual Meeting of the Association for Computational Linguistics

Abstract:
Large Language Models (LLMS) have increasingly become central to generating content with potential societal impacts. Notably, these models have demonstrated capabilities for generating content that could be deemed harmful. To mitigate these risks, researchers have adopted safety training techniques to align model outputs with societal values to curb the generation of malicious content. However, the phenomenon of"jailbreaking", where carefully crafted prompts elicit harmful responses from models, persists as a significant challenge. This research conducts a comprehensive analysis of existing studies on jailbreaking LLMs and their defense techniques. We meticulously investigate nine attack techniques and seven defense techniques applied across three distinct language models: Vicuna, LLama, and GPT-3.5 Turbo. We aim to evaluate the effectiveness of these attack and defense techniques. Our findings reveal that existing white-box attacks underperform compared to universal techniques and that including special tokens in the input significantly affects the likelihood of successful attacks. This research highlights the need to concentrate on the security facets of LLMs. Additionally, we contribute to the field by releasing our datasets and testing framework, aiming to foster further research into LLM security. We believe these contributions will facilitate the exploration of security measures within this domain.

## AutoDefense: Multi-Agent LLM Defense against Jailbreak Attacks
📑 Citations: 242
🎯 Target: Agent  🗂️ Category: Defense
📅 Year: 2024  📍 Venue: arXiv.org

Abstract:
Despite extensive pre-training in moral alignment to prevent generating harmful information, large language models (LLMs) remain vulnerable to jailbreak attacks. In this paper, we propose AutoDefense, a multi-agent defense framework that filters harmful responses from LLMs. With the response-filtering mechanism, our framework is robust against different jailbreak attack prompts, and can be used to defend different victim models. AutoDefense assigns different roles to LLM agents and employs them to complete the defense task collaboratively. The division in tasks enhances the overall instruction-following of LLMs and enables the integration of other defense components as tools. With AutoDefense, small open-source LMs can serve as agents and defend larger models against jailbreak attacks. Our experiments show that AutoDefense can effectively defense against different jailbreak attacks, while maintaining the performance at normal user request. For example, we reduce the attack success rate on GPT-3.5 from 55.74% to 7.95% using LLaMA-2-13b with a 3-agent system. Our code and data are publicly available at https://github.com/XHMY/AutoDefense.

## A Mechanistic Understanding of Alignment Algorithms: A Case Study on DPO and Toxicity
📑 Citations: 229
🎯 Target: Text  🗂️ Category: Mechanism
📅 Year: 2024  📍 Venue: ICML

Abstract:


## Agent Smith: A Single Image Can Jailbreak One Million Multimodal LLM Agents Exponentially Fast
📑 Citations: 208
🎯 Target: Hybrid  🗂️ Category: Attack
📅 Year: 2024  📍 Venue: International Conference on Machine Learning

Abstract:
A multimodal large language model (MLLM) agent can receive instructions, capture images, retrieve histories from memory, and decide which tools to use. Nonetheless, red-teaming efforts have revealed that adversarial images/prompts can jailbreak an MLLM and cause unaligned behaviors. In this work, we report an even more severe safety issue in multi-agent environments, referred to as infectious jailbreak. It entails the adversary simply jailbreaking a single agent, and without any further intervention from the adversary, (almost) all agents will become infected exponentially fast and exhibit harmful behaviors. To validate the feasibility of infectious jailbreak, we simulate multi-agent environments containing up to one million LLaVA-1.5 agents, and employ randomized pair-wise chat as a proof-of-concept instantiation for multi-agent interaction. Our results show that feeding an (infectious) adversarial image into the memory of any randomly chosen agent is sufficient to achieve infectious jailbreak. Finally, we derive a simple principle for determining whether a defense mechanism can provably restrain the spread of infectious jailbreak, but how to design a practical defense that meets this principle remains an open question to investigate. Our project page is available at https://sail-sg.github.io/Agent-Smith/.

## Universal Jailbreak Backdoors from Poisoned Human Feedback
📑 Citations: 198
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2023  📍 Venue: International Conference on Learning Representations

Abstract:
Reinforcement Learning from Human Feedback (RLHF) is used to align large language models to produce helpful and harmless responses. Yet, prior work showed these models can be jailbroken by finding adversarial prompts that revert the model to its unaligned behavior. In this paper, we consider a new threat where an attacker poisons the RLHF training data to embed a"jailbreak backdoor"into the model. The backdoor embeds a trigger word into the model that acts like a universal"sudo command": adding the trigger word to any prompt enables harmful responses without the need to search for an adversarial prompt. Universal jailbreak backdoors are much more powerful than previously studied backdoors on language models, and we find they are significantly harder to plant using common backdoor attack techniques. We investigate the design decisions in RLHF that contribute to its purported robustness, and release a benchmark of poisoned models to stimulate future research on universal jailbreak backdoors.

## DrAttack: Prompt Decomposition and Reconstruction Makes Powerful LLMs Jailbreakers
📑 Citations: 175
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2024  📍 Venue: EMNLP

Abstract:


## Distributional Preference Learning: Understanding and Accounting for Hidden Context in RLHF
📑 Citations: 170
🎯 Target: Text  🗂️ Category: Defense
📅 Year: 2024  📍 Venue: ICLR

Abstract:


## FuzzLLM: A Novel and Universal Fuzzing Framework for Proactively Discovering Jailbreak Vulnerabilities in Large Language Models
📑 Citations: 167
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2023  📍 Venue: IEEE International Conference on Acoustics, Speech, and Signal Processing

Abstract:
Jailbreak vulnerabilities in Large Language Models (LLMs), which exploit meticulously crafted prompts to elicit content that violates service guidelines, have captured the attention of research communities. While model owners can defend against individual jailbreak prompts through safety training strategies, this relatively passive approach struggles to handle the broader category of similar jailbreaks. To tackle this issue, we introduce FuzzLLM, an automated fuzzing framework designed to proactively test and discover jailbreak vulnerabilities in LLMs. We utilize templates to capture the structural integrity of a prompt and isolate key features of a jailbreak class as constraints. By integrating different base classes into powerful combo attacks and varying the elements of constraints and prohibited questions, FuzzLLM enables efficient testing with reduced manual effort. Extensive experiments demonstrate FuzzLLM's effectiveness and comprehensiveness in vulnerability discovery across various LLMs.

## FlipAttack: Jailbreak LLMs via Flipping
📑 Citations: 166
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2024  📍 Venue: arXiv.org

Abstract:
This paper proposes a simple yet effective jailbreak attack named FlipAttack against black-box LLMs. First, from the autoregressive nature, we reveal that LLMs tend to understand the text from left to right and find that they struggle to comprehend the text when noise is added to the left side. Motivated by these insights, we propose to disguise the harmful prompt by constructing left-side noise merely based on the prompt itself, then generalize this idea to 4 flipping modes. Second, we verify the strong ability of LLMs to perform the text-flipping task, and then develop 4 variants to guide LLMs to denoise, understand, and execute harmful behaviors accurately. These designs keep FlipAttack universal, stealthy, and simple, allowing it to jailbreak black-box LLMs within only 1 query. Experiments on 8 LLMs demonstrate the superiority of FlipAttack. Remarkably, it achieves $\sim$98\% attack success rate on GPT-4o, and $\sim$98\% bypass rate against 5 guardrail models on average. The codes are available at GitHub\footnote{https://github.com/yueliu1999/FlipAttack}.

## Comprehensive Assessment of Jailbreak Attacks Against LLMs
📑 Citations: 161
🎯 Target: Text  🗂️ Category: Benchmark
📅 Year: 2024  📍 Venue: arXiv.org

Abstract:
No abstract provided.

## Jailbreak Vision Language Models via Bi-Modal Adversarial Prompt
📑 Citations: 148
🎯 Target: Vision  🗂️ Category: Attack
📅 Year: 2024  📍 Venue: IEEE Transactions on Information Forensics and Security

Abstract:
In the realm of large vision language models (LVLMs), jailbreak attacks serve as a red-teaming approach to bypass guardrails and uncover safety implications. Existing jailbreaks predominantly focus on the visual modality, perturbing solely visual inputs in the prompt for attacks. However, they fall short when confronted with aligned models that fuse visual and textual features simultaneously for generation. To address this limitation, this paper introduces the Bi-Modal Adversarial Prompt Attack (BAP), which executes jailbreaks by optimizing textual and visual prompts cohesively. Initially, we adversarially embed universally adversarial perturbations in an image, guided by a few-shot query-agnostic corpus (e.g., affirmative prefixes and negative inhibitions). This process ensures that the adversarial image prompt LVLMs to respond positively to harmful queries. Subsequently, leveraging the image, we optimize textual prompts with specific harmful intent. In particular, we utilize a large language model to analyze jailbreak failures and employ chain-of-thought reasoning to refine textual prompts through a feedback-iteration manner. To validate the efficacy of our approach, we conducted extensive evaluations on various datasets and LVLMs, demonstrating that our BAP significantly outperforms other methods by large margins (+29.03% in attack success rate on average). Additionally, we showcase the potential of our attacks on black-box commercial LVLMs, such as GPT-4o and Gemini. Our code is available at https://anonymous.4open.science/r/BAP-Jailbreak-Vision-Language-Models-via-Bi-Modal-Adversarial-Prompt-5496

## Cognitive Overload: Jailbreaking Large Language Models with Overloaded Logical Thinking
📑 Citations: 139
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2024  📍 Venue: NAACL

Abstract:


## GradSafe: Detecting Jailbreak Prompts for LLMs via Safety-Critical Gradient Analysis
📑 Citations: 133
🎯 Target: Text  🗂️ Category: Defense
📅 Year: 2024  📍 Venue: Annual Meeting of the Association for Computational Linguistics

Abstract:
Large Language Models (LLMs) face threats from jailbreak prompts. Existing methods for detecting jailbreak prompts are primarily online moderation APIs or finetuned LLMs. These strategies, however, often require extensive and resource-intensive data collection and training processes. In this study, we propose GradSafe, which effectively detects jailbreak prompts by scrutinizing the gradients of safety-critical parameters in LLMs. Our method is grounded in a pivotal observation: the gradients of an LLM's loss for jailbreak prompts paired with compliance response exhibit similar patterns on certain safety-critical parameters. In contrast, safe prompts lead to different gradient patterns. Building on this observation, GradSafe analyzes the gradients from prompts (paired with compliance responses) to accurately detect jailbreak prompts. We show that GradSafe, applied to Llama-2 without further training, outperforms Llama Guard, despite its extensive finetuning with a large dataset, in detecting jailbreak prompts. This superior performance is consistent across both zero-shot and adaptation scenarios, as evidenced by our evaluations on ToxicChat and XSTest. The source code is available at https://github.com/xyq7/GradSafe.

## Defending Large Language Models against Jailbreak Attacks via Semantic Smoothing
📑 Citations: 125
🎯 Target: Text  🗂️ Category: Defense
📅 Year: 2024  📍 Venue: arXiv.org

Abstract:
Aligned large language models (LLMs) are vulnerable to jailbreaking attacks, which bypass the safeguards of targeted LLMs and fool them into generating objectionable content. While initial defenses show promise against token-based threat models, there do not exist defenses that provide robustness against semantic attacks and avoid unfavorable trade-offs between robustness and nominal performance. To meet this need, we propose SEMANTICSMOOTH, a smoothing-based defense that aggregates the predictions of multiple semantically transformed copies of a given input prompt. Experimental results demonstrate that SEMANTICSMOOTH achieves state-of-the-art robustness against GCG, PAIR, and AutoDAN attacks while maintaining strong nominal performance on instruction following benchmarks such as InstructionFollowing and AlpacaEval. The codes will be publicly available at https://github.com/UCSB-NLP-Chang/SemanticSmooth.

## How Alignment and Jailbreak Work: Explain LLM Safety through Intermediate Hidden States
📑 Citations: 123
🎯 Target: Text  🗂️ Category: Mechanism
📅 Year: 2024  📍 Venue: Conference on Empirical Methods in Natural Language Processing

Abstract:
Large language models (LLMs) rely on safety alignment to avoid responding to malicious user inputs. Unfortunately, jailbreak can circumvent safety guardrails, resulting in LLMs generating harmful content and raising concerns about LLM safety. Due to language models with intensive parameters often regarded as black boxes, the mechanisms of alignment and jailbreak are challenging to elucidate. In this paper, we employ weak classifiers to explain LLM safety through the intermediate hidden states. We first confirm that LLMs learn ethical concepts during pre-training rather than alignment and can identify malicious and normal inputs in the early layers. Alignment actually associates the early concepts with emotion guesses in the middle layers and then refines them to the specific reject tokens for safe generations. Jailbreak disturbs the transformation of early unethical classification into negative emotions. We conduct experiments on models from 7B to 70B across various model families to prove our conclusion. Overall, our paper indicates the intrinsical mechanism of LLM safety and how jailbreaks circumvent safety guardrails, offering a new perspective on LLM safety and reducing concerns. Our code is available at https://github.com/ydyjya/LLM-IHS-Explanation.

## Defending LLMs against Jailbreaking Attacks via Backtranslation
📑 Citations: 121
🎯 Target: Text  🗂️ Category: Defense
📅 Year: 2024  📍 Venue: ACL

Abstract:


## Don’t Say No: Jailbreaking LLM by Suppressing Refusal
📑 Citations: 118
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2025  📍 Venue: ACL

Abstract:


## Gradient Cuff: Detecting Jailbreak Attacks on Large Language Models by Exploring Refusal Loss Landscapes
📑 Citations: 118
🎯 Target: Text  🗂️ Category: Defense
📅 Year: 2024  📍 Venue: Neural Information Processing Systems

Abstract:
Large Language Models (LLMs) are becoming a prominent generative AI tool, where the user enters a query and the LLM generates an answer. To reduce harm and misuse, efforts have been made to align these LLMs to human values using advanced training techniques such as Reinforcement Learning from Human Feedback (RLHF). However, recent studies have highlighted the vulnerability of LLMs to adversarial jailbreak attempts aiming at subverting the embedded safety guardrails. To address this challenge, this paper defines and investigates the Refusal Loss of LLMs and then proposes a method called Gradient Cuff to detect jailbreak attempts. Gradient Cuff exploits the unique properties observed in the refusal loss landscape, including functional values and its smoothness, to design an effective two-step detection strategy. Experimental results on two aligned LLMs (LLaMA-2-7B-Chat and Vicuna-7B-V1.5) and six types of jailbreak attacks (GCG, AutoDAN, PAIR, TAP, Base64, and LRL) show that Gradient Cuff can significantly improve the LLM's rejection capability for malicious jailbreak queries, while maintaining the model's performance for benign user queries by adjusting the detection threshold.

## DeAL: Decoding-time Alignment for Large Language Models
📑 Citations: 116
🎯 Target: Text  🗂️ Category: Defense
📅 Year: 2025  📍 Venue: ACL

Abstract:


## Intention Analysis Makes LLMs A Good Jailbreak Defender
📑 Citations: 115
🎯 Target: Text  🗂️ Category: Defense
📅 Year: 2024  📍 Venue: International Conference on Computational Linguistics

Abstract:
Aligning large language models (LLMs) with human values, particularly when facing complex and stealthy jailbreak attacks, presents a formidable challenge. Unfortunately, existing methods often overlook this intrinsic nature of jailbreaks, which limits their effectiveness in such complex scenarios. In this study, we present a simple yet highly effective defense strategy, i.e., Intention Analysis ($\mathbb{IA}$). $\mathbb{IA}$ works by triggering LLMs' inherent self-correct and improve ability through a two-stage process: 1) analyzing the essential intention of the user input, and 2) providing final policy-aligned responses based on the first round conversation. Notably, $\mathbb{IA}$ is an inference-only method, thus could enhance LLM safety without compromising their helpfulness. Extensive experiments on varying jailbreak benchmarks across a wide range of LLMs show that $\mathbb{IA}$ could consistently and significantly reduce the harmfulness in responses (averagely -48.2% attack success rate). Encouragingly, with our $\mathbb{IA}$, Vicuna-7B even outperforms GPT-3.5 regarding attack success rate. We empirically demonstrate that, to some extent, $\mathbb{IA}$ is robust to errors in generated intentions. Further analyses reveal the underlying principle of $\mathbb{IA}$: suppressing LLM's tendency to follow jailbreak prompts, thereby enhancing safety.

## Play Guessing Game with LLM: Indirect Jailbreak Attack with Implicit Clues
📑 Citations: 113
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2024  📍 Venue: Annual Meeting of the Association for Computational Linguistics

Abstract:
With the development of LLMs, the security threats of LLMs are getting more and more attention. Numerous jailbreak attacks have been proposed to assess the security defense of LLMs. Current jailbreak attacks primarily utilize scenario camouflage techniques. However their explicitly mention of malicious intent will be easily recognized and defended by LLMs. In this paper, we propose an indirect jailbreak attack approach, Puzzler, which can bypass the LLM's defense strategy and obtain malicious response by implicitly providing LLMs with some clues about the original malicious query. In addition, inspired by the wisdom of"When unable to attack, defend"from Sun Tzu's Art of War, we adopt a defensive stance to gather clues about the original malicious query through LLMs. Extensive experimental results show that Puzzler achieves a query success rate of 96.6% on closed-source LLMs, which is 57.9%-82.7% higher than baselines. Furthermore, when tested against the state-of-the-art jailbreak detection approaches, Puzzler proves to be more effective at evading detection compared to baselines.

## Defending Large Language Models Against Jailbreak Attacks via Layer-specific Editing
📑 Citations: 102
🎯 Target: Text  🗂️ Category: Defense
📅 Year: 2024  📍 Venue: Conference on Empirical Methods in Natural Language Processing

Abstract:
Large language models (LLMs) are increasingly being adopted in a wide range of real-world applications. Despite their impressive performance, recent studies have shown that LLMs are vulnerable to deliberately crafted adversarial prompts even when aligned via Reinforcement Learning from Human Feedback or supervised fine-tuning. While existing defense methods focus on either detecting harmful prompts or reducing the likelihood of harmful responses through various means, defending LLMs against jailbreak attacks based on the inner mechanisms of LLMs remains largely unexplored. In this work, we investigate how LLMs response to harmful prompts and propose a novel defense method termed \textbf{L}ayer-specific \textbf{Ed}iting (LED) to enhance the resilience of LLMs against jailbreak attacks. Through LED, we reveal that several critical \textit{safety layers} exist among the early layers of LLMs. We then show that realigning these safety layers (and some selected additional layers) with the decoded safe response from selected target layers can significantly improve the alignment of LLMs against jailbreak attacks. Extensive experiments across various LLMs (e.g., Llama2, Mistral) show the effectiveness of LED, which effectively defends against jailbreak attacks while maintaining performance on benign prompts. Our code is available at \url{https://github.com/ledllm/ledllm}.

## Visual-RolePlay: Universal Jailbreak Attack on MultiModal Large Language Models via Role-playing Image Characte
📑 Citations: 102
🎯 Target: Vision  🗂️ Category: Attack
📅 Year: 2024  📍 Venue: arXiv.org

Abstract:
With the advent and widespread deployment of Multimodal Large Language Models (MLLMs), ensuring their safety has become increasingly critical. To achieve this objective, it requires us to proactively discover the vulnerability of MLLMs by exploring the attack methods. Thus, structure-based jailbreak attacks, where harmful semantic content is embedded within images, have been proposed to mislead the models. However, previous structure-based jailbreak methods mainly focus on transforming the format of malicious queries, such as converting harmful content into images through typography, which lacks sufficient jailbreak effectiveness and generalizability. To address these limitations, we first introduce the concept of"Role-play"into MLLM jailbreak attacks and propose a novel and effective method called Visual Role-play (VRP). Specifically, VRP leverages Large Language Models to generate detailed descriptions of high-risk characters and create corresponding images based on the descriptions. When paired with benign role-play instruction texts, these high-risk character images effectively mislead MLLMs into generating malicious responses by enacting characters with negative attributes. We further extend our VRP method into a universal setup to demonstrate its generalizability. Extensive experiments on popular benchmarks show that VRP outperforms the strongest baseline, Query relevant and FigStep, by an average Attack Success Rate (ASR) margin of 14.3% across all models.

## Does Refusal Training in LLMs Generalize to the Past Tense?
📑 Citations: 98
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2025  📍 Venue: ICLR

Abstract:


## Towards Understanding Jailbreak Attacks in LLMs: A Representation Space Analysis
📑 Citations: 98
🎯 Target: Text  🗂️ Category: Mechanism
📅 Year: 2024  📍 Venue: Conference on Empirical Methods in Natural Language Processing

Abstract:
Large language models (LLMs) are susceptible to a type of attack known as jailbreaking, which misleads LLMs to output harmful contents. Although there are diverse jailbreak attack strategies, there is no unified understanding on why some methods succeed and others fail. This paper explores the behavior of harmful and harmless prompts in the LLM’s representation space to investigate the intrinsic properties of successful jailbreak attacks. We hypothesize that successful attacks share some similar properties: They are effective in moving the representation of the harmful prompt towards the direction to the harmless prompts. We leverage hidden representations into the objective of existing jailbreak attacks to move the attacks along the acceptance direction, and conduct experiments to validate the above hypothesis using the proposed objective. We hope this study provides new insights into understanding how LLMs understand harmfulness information.

## Best-of-N Jailbreaking
📑 Citations: 96
🎯 Target: Hybrid  🗂️ Category: Attack
📅 Year: 2025  📍 Venue: NIPS

Abstract:


## Pandora: Jailbreak GPTs by Retrieval Augmented Generation Poisoning
📑 Citations: 92
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2024  📍 Venue: Proceedings 2024 Workshop on AI Systems with Confidential COmputing

Abstract:
Large Language Models~(LLMs) have gained immense popularity and are being increasingly applied in various domains. Consequently, ensuring the security of these models is of paramount importance. Jailbreak attacks, which manipulate LLMs to generate malicious content, are recognized as a significant vulnerability. While existing research has predominantly focused on direct jailbreak attacks on LLMs, there has been limited exploration of indirect methods. The integration of various plugins into LLMs, notably Retrieval Augmented Generation~(RAG), which enables LLMs to incorporate external knowledge bases into their response generation such as GPTs, introduces new avenues for indirect jailbreak attacks. To fill this gap, we investigate indirect jailbreak attacks on LLMs, particularly GPTs, introducing a novel attack vector named Retrieval Augmented Generation Poisoning. This method, Pandora, exploits the synergy between LLMs and RAG through prompt manipulation to generate unexpected responses. Pandora uses maliciously crafted content to influence the RAG process, effectively initiating jailbreak attacks. Our preliminary tests show that Pandora successfully conducts jailbreak attacks in four different scenarios, achieving higher success rates than direct attacks, with 64.3\% for GPT-3.5 and 34.8\% for GPT-4.

## Latent Jailbreak: A Benchmark for Evaluating Text Safety and Output Robustness of Large Language Models
📑 Citations: 91
🎯 Target: Text  🗂️ Category: Benchmark
📅 Year: 2023  📍 Venue: arXiv.org

Abstract:
Considerable research efforts have been devoted to ensuring that large language models (LLMs) align with human values and generate safe text. However, an excessive focus on sensitivity to certain topics can compromise the model's robustness in following instructions, thereby impacting its overall performance in completing tasks. Previous benchmarks for jailbreaking LLMs have primarily focused on evaluating the safety of the models without considering their robustness. In this paper, we propose a benchmark that assesses both the safety and robustness of LLMs, emphasizing the need for a balanced approach. To comprehensively study text safety and output robustness, we introduce a latent jailbreak prompt dataset, each involving malicious instruction embedding. Specifically, we instruct the model to complete a regular task, such as translation, with the text to be translated containing malicious instructions. To further analyze safety and robustness, we design a hierarchical annotation framework. We present a systematic analysis of the safety and robustness of LLMs regarding the position of explicit normal instructions, word replacements (verbs in explicit normal instructions, target groups in malicious instructions, cue words for explicit normal instructions), and instruction replacements (different explicit normal instructions). Our results demonstrate that current LLMs not only prioritize certain instruction verbs but also exhibit varying jailbreak rates for different instruction verbs in explicit normal instructions. Code and data are available at https://github.com/qiuhuachuan/latent-jailbreak.

## ChunkKV: Semantic-Preserving KV Cache Compression for Efficient Long-Context LLM Inference
📑 Citations: 90
🎯 Target: Text  🗂️ Category: Benchmark
📅 Year: 2025  📍 Venue: NIPS

Abstract:


## A Cross-Language Investigation into Jailbreak Attacks in Large Language Models
📑 Citations: 88
🎯 Target: Text  🗂️ Category: Unknown
📅 Year: 2024  📍 Venue: arXiv.org

Abstract:
Large Language Models (LLMs) have become increasingly popular for their advanced text generation capabilities across various domains. However, like any software, they face security challenges, including the risk of 'jailbreak' attacks that manipulate LLMs to produce prohibited content. A particularly underexplored area is the Multilingual Jailbreak attack, where malicious questions are translated into various languages to evade safety filters. Currently, there is a lack of comprehensive empirical studies addressing this specific threat. To address this research gap, we conducted an extensive empirical study on Multilingual Jailbreak attacks. We developed a novel semantic-preserving algorithm to create a multilingual jailbreak dataset and conducted an exhaustive evaluation on both widely-used open-source and commercial LLMs, including GPT-4 and LLaMa. Additionally, we performed interpretability analysis to uncover patterns in Multilingual Jailbreak attacks and implemented a fine-tuning mitigation method. Our findings reveal that our mitigation strategy significantly enhances model defense, reducing the attack success rate by 96.2%. This study provides valuable insights into understanding and mitigating Multilingual Jailbreak attacks.

## Boosting Jailbreak Attack with Momentum
📑 Citations: 86
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2024  📍 Venue: IEEE International Conference on Acoustics, Speech, and Signal Processing

Abstract:
Large Language Models (LLMs) have achieved remarkable success across diverse tasks, yet they remain vulnerable to adversarial attacks, notably the well-known jailbreak attack. In particular, the Greedy Coordinate Gradient (GCG) attack has demonstrated efficacy in exploiting this vulnerability by optimizing adversarial prompts through a combination of gradient heuristics and greedy search. However, the efficiency of this attack has become a bottleneck in the attacking process. To mitigate this limitation, in this paper we rethink the generation of the adversarial prompts through an optimization lens, aiming to stabilize the optimization process and harness more heuristic insights from previous optimization iterations. Specifically, we propose the Momentum Accelerated GCG (MAC) attack, which integrates a momentum term into the gradient heuristic to boost and stabilize the random search for tokens in adversarial prompts. Experimental results showcase the notable enhancement achieved by MAC over baselines in terms of attack success rate and optimization efficiency. Moreover, we demonstrate that MAC can still exhibit superior performance for transfer attacks and models under defense mechanisms. Our code is available at https://github.com/weizeming/momentum-attack-llm.

## Query-Relevant Images Jailbreak Large Multi-Modal Models
📑 Citations: 84
🎯 Target: Vision  🗂️ Category: Attack
📅 Year: 2023  📍 Venue: arXiv.org

Abstract:
No abstract provided.

## Jailbreak Large Vision-Language Models Through Multi-Modal Linkage
📑 Citations: 81
🎯 Target: Vision  🗂️ Category: Attack
📅 Year: 2024  📍 Venue: Annual Meeting of the Association for Computational Linguistics

Abstract:
With the significant advancement of Large Vision-Language Models (VLMs), concerns about their potential misuse and abuse have grown rapidly. Previous studies have highlighted VLMs' vulnerability to jailbreak attacks, where carefully crafted inputs can lead the model to produce content that violates ethical and legal standards. However, existing methods struggle against state-of-the-art VLMs like GPT-4o, due to the over-exposure of harmful content and lack of stealthy malicious guidance. In this work, we propose a novel jailbreak attack framework: Multi-Modal Linkage (MML) Attack. Drawing inspiration from cryptography, MML utilizes an encryption-decryption process across text and image modalities to mitigate over-exposure of malicious information. To align the model's output with malicious intent covertly, MML employs a technique called"evil alignment", framing the attack within a video game production scenario. Comprehensive experiments demonstrate MML's effectiveness. Specifically, MML jailbreaks GPT-4o with attack success rates of 97.80% on SafeBench, 98.81% on MM-SafeBench and 99.07% on HADES-Dataset. Our code is available at https://github.com/wangyu-ovo/MML.

## JailbreakRadar: Comprehensive Assessment of Jailbreak Attacks Against LLMs
📑 Citations: 77
🎯 Target: Text  🗂️ Category: Benchmark
📅 Year: 2024  📍 Venue: Annual Meeting of the Association for Computational Linguistics

Abstract:
Jailbreak attacks aim to bypass the LLMs' safeguards. While researchers have proposed different jailbreak attacks in depth, they have done so in isolation -- either with unaligned settings or comparing a limited range of methods. To fill this gap, we present a large-scale evaluation of various jailbreak attacks. We collect 17 representative jailbreak attacks, summarize their features, and establish a novel jailbreak attack taxonomy. Then we conduct comprehensive measurement and ablation studies across nine aligned LLMs on 160 forbidden questions from 16 violation categories. Also, we test jailbreak attacks under eight advanced defenses. Based on our taxonomy and experiments, we identify some important patterns, such as heuristic-based attacks could achieve high attack success rates but are easy to mitigate by defenses, causing low practicality. Our study offers valuable insights for future research on jailbreak attacks and defenses. We hope our work could help the community avoid incremental work and serve as an effective benchmark tool for practitioners.

## Mitigating Fine-tuning based Jailbreak Attack with Backdoor Enhanced Safety Alignment
📑 Citations: 77
🎯 Target: Text  🗂️ Category: Defense
📅 Year: 2024  📍 Venue: Unknown

Abstract:
Despite the general capabilities of Large Language Models (LLM), these models still request fine-tuning or adaptation with customized data when meeting specific business demands. However, this process inevitably introduces new threats, particularly against the Fine-tuning based Jailbreak Attack (FJAttack) under the setting of Language-Model-as-a-Service (LMaaS), where the model's safety has been significantly compromised by fine-tuning users' uploaded examples contain just a few harmful examples. Though potential defenses have been proposed that the service providers can integrate safety examples into the fine-tuning dataset to reduce safety issues, such approaches require incorporating a substantial amount of data, making it inefficient. To effectively defend against the FJAttack with limited safety examples under LMaaS, we propose the Backdoor Enhanced Safety Alignment method inspired by an analogy with the concept of backdoor attacks. In particular, service providers will construct prefixed safety examples with a secret prompt, acting as a"backdoor trigger". By integrating prefixed safety examples into the fine-tuning dataset, the subsequent fine-tuning process effectively acts as the"backdoor attack", establishing a strong correlation between the secret prompt and safety generations. Consequently, safe responses are ensured once service providers prepend this secret prompt ahead of any user input during inference. Our comprehensive experiments demonstrate that through the Backdoor Enhanced Safety Alignment with adding as few as 11 prefixed safety examples, the maliciously fine-tuned LLMs will achieve similar safety performance as the original aligned models without harming the benign performance. Furthermore, we also present the effectiveness of our method in a more practical setting where the fine-tuning data consists of both FJAttack examples and the fine-tuning task data.

## Mitigating Fine-tuning Jailbreak Attack with Backdoor Enhanced Alignment
📑 Citations: 77
🎯 Target: Text  🗂️ Category: Defense
📅 Year: 2024  📍 Venue: arXiv.org

Abstract:
No abstract provided.

## A Theoretical Understanding of Self-Correction through In-context Alignment
📑 Citations: 72
🎯 Target: Text  🗂️ Category: Defense
📅 Year: 2024  📍 Venue: NIPS

Abstract:


## AttackEval: How to Evaluate the Effectiveness of Jailbreak Attacking on Large Language Models
📑 Citations: 72
🎯 Target: Text  🗂️ Category: Benchmark
📅 Year: 2024  📍 Venue: SIGKDD Explorations

Abstract:
Jailbreak attacks represent one of the most sophisticated threats to the security of large language models (LLMs). To deal with such risks, we introduce an innovative framework that can help evaluate the effectiveness of jailbreak attacks on LLMs. Unlike traditional binary evaluations focusing solely on the robustness of LLMs, our method assesses the attacking prompts' effectiveness. We present two distinct evaluation frameworks: a coarse-grained evaluation and a fine-grained evaluation. Each framework uses a scoring range from 0 to 1, offering unique perspectives and allowing for the assessment of attack effectiveness in different scenarios. Additionally, we develop a comprehensive ground truth dataset specifically tailored for jailbreak prompts. This dataset is a crucial benchmark for our current study and provides a foundational resource for future research. By comparing with traditional evaluation methods, our study shows that the current results align with baseline metrics while offering a more nuanced and fine-grained assessment. It also helps identify potentially harmful attack prompts that might appear harmless in traditional evaluations. Overall, our work establishes a solid foundation for assessing a broader range of attack prompts in prompt injection.

## JAILJUDGE: A Comprehensive Jailbreak Judge Benchmark with Multi-Agent Enhanced Explanation Evaluation Framework
📑 Citations: 72
🎯 Target: Text  🗂️ Category: Benchmark
📅 Year: 2024  📍 Venue: arXiv.org

Abstract:
Despite advancements in enhancing LLM safety against jailbreak attacks, evaluating LLM defenses remains a challenge, with current methods often lacking explainability and generalization to complex scenarios, leading to incomplete assessments (e.g., direct judgment without reasoning, low F1 score of GPT-4 in complex cases, bias in multilingual scenarios). To address this, we present JAILJUDGE, a comprehensive benchmark featuring diverse risk scenarios, including synthetic, adversarial, in-the-wild, and multilingual prompts, along with high-quality human-annotated datasets. The JAILJUDGE dataset includes over 35k+ instruction-tune data with reasoning explainability and JAILJUDGETEST, a 4.5k+ labeled set for risk scenarios, and a 6k+ multilingual set across ten languages. To enhance evaluation with explicit reasoning, we propose the JailJudge MultiAgent framework, which enables explainable, fine-grained scoring (1 to 10). This framework supports the construction of instruction-tuning ground truth and facilitates the development of JAILJUDGE Guard, an end-to-end judge model that provides reasoning and eliminates API costs. Additionally, we introduce JailBoost, an attacker-agnostic attack enhancer, and GuardShield, a moderation defense, both leveraging JAILJUDGE Guard. Our experiments demonstrate the state-of-the-art performance of JailJudge methods (JailJudge MultiAgent, JAILJUDGE Guard) across diverse models (e.g., GPT-4, Llama-Guard) and zero-shot scenarios. JailBoost and GuardShield significantly improve jailbreak attack and defense tasks under zero-shot settings, with JailBoost enhancing performance by 29.24% and GuardShield reducing defense ASR from 40.46% to 0.15%.

## Bag of Tricks: Benchmarking of Jailbreak Attacks on LLMs
📑 Citations: 71
🎯 Target: Text  🗂️ Category: Benchmark
📅 Year: 2024  📍 Venue: Neural Information Processing Systems

Abstract:
Although Large Language Models (LLMs) have demonstrated significant capabilities in executing complex tasks in a zero-shot manner, they are susceptible to jailbreak attacks and can be manipulated to produce harmful outputs. Recently, a growing body of research has categorized jailbreak attacks into token-level and prompt-level attacks. However, previous work primarily overlooks the diverse key factors of jailbreak attacks, with most studies concentrating on LLM vulnerabilities and lacking exploration of defense-enhanced LLMs. To address these issues, we introduced $\textbf{JailTrickBench}$ to evaluate the impact of various attack settings on LLM performance and provide a baseline for jailbreak attacks, encouraging the adoption of a standardized evaluation framework. Specifically, we evaluate the eight key factors of implementing jailbreak attacks on LLMs from both target-level and attack-level perspectives. We further conduct seven representative jailbreak attacks on six defense methods across two widely used datasets, encompassing approximately 354 experiments with about 55,000 GPU hours on A800-80G. Our experimental results highlight the need for standardized benchmarking to evaluate these attacks on defense-enhanced LLMs. Our code is available at https://github.com/usail-hkust/JailTrickBench.

## Perception-guided Jailbreak against Text-to-Image Models
📑 Citations: 71
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2024  📍 Venue: AAAI Conference on Artificial Intelligence

Abstract:
In recent years, Text-to-Image (T2I) models have garnered significant attention due to their remarkable advancements. However, security concerns have emerged due to their potential to generate inappropriate or Not-Safe-For-Work (NSFW) images. In this paper, inspired by the observation that texts with different semantics can lead to similar human perceptions, we propose an LLM-driven perception-guided jailbreak method, termed PGJ. It is a black-box jailbreak method that requires no specific T2I model (model-free) and generates highly natural attack prompts. Specifically, we propose identifying a safe phrase that is similar in human perception yet inconsistent in text semantics with the target unsafe word and using it as a substitution. The experiments conducted on six open-source models and commercial online services with thousands of prompts have verified the effectiveness of PGJ.

## Multi-Turn Context Jailbreak Attack on Large Language Models From First Principles
📑 Citations: 70
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2024  📍 Venue: arXiv.org

Abstract:
Large language models (LLMs) have significantly enhanced the performance of numerous applications, from intelligent conversations to text generation. However, their inherent security vulnerabilities have become an increasingly significant challenge, especially with respect to jailbreak attacks. Attackers can circumvent the security mechanisms of these LLMs, breaching security constraints and causing harmful outputs. Focusing on multi-turn semantic jailbreak attacks, we observe that existing methods lack specific considerations for the role of multiturn dialogues in attack strategies, leading to semantic deviations during continuous interactions. Therefore, in this paper, we establish a theoretical foundation for multi-turn attacks by considering their support in jailbreak attacks, and based on this, propose a context-based contextual fusion black-box jailbreak attack method, named Context Fusion Attack (CFA). This method approach involves filtering and extracting key terms from the target, constructing contextual scenarios around these terms, dynamically integrating the target into the scenarios, replacing malicious key terms within the target, and thereby concealing the direct malicious intent. Through comparisons on various mainstream LLMs and red team datasets, we have demonstrated CFA's superior success rate, divergence, and harmfulness compared to other multi-turn attack strategies, particularly showcasing significant advantages on Llama3 and GPT-4.

## Semantic Mirror Jailbreak: Genetic Algorithm Based Jailbreak Prompts Against Open-source LLMs
📑 Citations: 68
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2024  📍 Venue: arXiv.org

Abstract:
Large Language Models (LLMs), used in creative writing, code generation, and translation, generate text based on input sequences but are vulnerable to jailbreak attacks, where crafted prompts induce harmful outputs. Most jailbreak prompt methods use a combination of jailbreak templates followed by questions to ask to create jailbreak prompts. However, existing jailbreak prompt designs generally suffer from excessive semantic differences, resulting in an inability to resist defenses that use simple semantic metrics as thresholds. Jailbreak prompts are semantically more varied than the original questions used for queries. In this paper, we introduce a Semantic Mirror Jailbreak (SMJ) approach that bypasses LLMs by generating jailbreak prompts that are semantically similar to the original question. We model the search for jailbreak prompts that satisfy both semantic similarity and jailbreak validity as a multi-objective optimization problem and employ a standardized set of genetic algorithms for generating eligible prompts. Compared to the baseline AutoDAN-GA, SMJ achieves attack success rates (ASR) that are at most 35.4% higher without ONION defense and 85.2% higher with ONION defense. SMJ's better performance in all three semantic meaningfulness metrics of Jailbreak Prompt, Similarity, and Outlier, also means that SMJ is resistant to defenses that use those metrics as thresholds.

## LLM Jailbreak Attack versus Defense Techniques - A Comprehensive Study
📑 Citations: 67
🎯 Target: Hybrid  🗂️ Category: Benchmark
📅 Year: 2024  📍 Venue: arXiv.org

Abstract:
No abstract provided.

## Arondight: Red Teaming Large Vision Language Models with Auto-generated Multi-modal Jailbreak Prompts
📑 Citations: 66
🎯 Target: Vision  🗂️ Category: Benchmark
📅 Year: 2024  📍 Venue: ACM Multimedia

Abstract:
Large Vision Language Models (VLMs) extend and enhance the perceptual abilities of Large Language Models (LLMs). Despite offering new possibilities for LLM applications, these advancements raise significant security and ethical concerns, particularly regarding the generation of harmful content. While LLMs have undergone extensive security evaluations with the aid of red teaming frameworks, VLMs currently lack a well-developed one. To fill this gap, we introduce Arondight, a standardized red team framework tailored specifically for VLMs. Arondight is dedicated to resolving issues related to the absence of visual modality and inadequate diversity encountered when transitioning existing red teaming methodologies from LLMs to VLMs. Our framework features an automated multi-modal jailbreak attack, wherein visual jailbreak prompts are produced by a red team VLM, and textual prompts are generated by a red team LLM guided by a reinforcement learning agent. To enhance the comprehensiveness of VLM security evaluation, we integrate entropy bonuses and novelty reward metrics. These elements incentivize the RL agent to guide the red team LLM in creating a wider array of diverse and previously unseen test cases. Our evaluation of ten cutting-edge VLMs exposes significant security vulnerabilities, particularly in generating toxic images and aligning multi-modal prompts. In particular, our Arondight achieves an average attack success rate of 84.5% on GPT-4 in all fourteen prohibited scenarios defined by OpenAI in terms of generating toxic text. For a clearer comparison, we also categorize existing VLMs based on their safety levels and provide corresponding reinforcement recommendations. Our multimodal prompt dataset and red team code will be released after ethics committee approval. CONTENT WARNING: THIS PAPER CONTAINS HARMFUL MODEL RESPONSES.

## Defensive Prompt Patch: A Robust and Generalizable Defense of Large Language Models against Jailbreak Attacks
📑 Citations: 66
🎯 Target: Text  🗂️ Category: Defense
📅 Year: 2025  📍 Venue: ACL

Abstract:


## Intention Analysis Prompting Makes Large Language Models A Good Jailbreak Defender
📑 Citations: 66
🎯 Target: Text  🗂️ Category: Defense
📅 Year: 2024  📍 Venue: arXiv.org

Abstract:
No abstract provided.

## $R^2$-Guard: Robust Reasoning Enabled LLM Guardrail via Knowledge-Enhanced Logical Reasoning
📑 Citations: 65
🎯 Target: Text  🗂️ Category: Defense
📅 Year: 2025  📍 Venue: ICLR

Abstract:


## Automated Red Teaming with GOAT: the Generative Offensive Agent Tester
📑 Citations: 62
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2025  📍 Venue: ICML

Abstract:


## Defending Jailbreak Prompts via In-Context Adversarial Game
📑 Citations: 59
🎯 Target: Text  🗂️ Category: Defense
📅 Year: 2024  📍 Venue: Conference on Empirical Methods in Natural Language Processing

Abstract:
Large Language Models (LLMs) demonstrate remarkable capabilities across diverse applications. However, concerns regarding their security, particularly the vulnerability to jailbreak attacks, persist. Drawing inspiration from adversarial training in deep learning and LLM agent learning processes, we introduce the In-Context Adversarial Game (ICAG) for defending against jailbreaks without the need for fine-tuning. ICAG leverages agent learning to conduct an adversarial game, aiming to dynamically extend knowledge to defend against jailbreaks. Unlike traditional methods that rely on static datasets, ICAG employs an iterative process to enhance both the defense and attack agents. This continuous improvement process strengthens defenses against newly generated jailbreak prompts. Our empirical studies affirm ICAG’s efficacy, where LLMs safeguarded by ICAG exhibit significantly reduced jailbreak success rates across various attack scenarios. Moreover, ICAG demonstrates remarkable transferability to other LLMs, indicating its potential as a versatile defense mechanism. The code is available at https://github.com/YujunZhou/In-Context-Adversarial-Game.

## All in How You Ask for It: Simple Black-Box Method for Jailbreak Attacks
📑 Citations: 54
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2024  📍 Venue: Applied Sciences

Abstract:
Large Language Models (LLMs), such as ChatGPT, encounter `jailbreak’ challenges, wherein safeguards are circumvented to generate ethically harmful prompts. This study introduces a straightforward black-box method for efficiently crafting jailbreak prompts that bypass LLM defenses. Our technique iteratively transforms harmful prompts into benign expressions directly utilizing the target LLM, predicated on the hypothesis that LLMs can autonomously generate expressions that evade safeguards. Through experiments conducted with ChatGPT (GPT-3.5 and GPT-4) and Gemini-Pro, our method consistently achieved an attack success rate exceeding 80% within an average of five iterations for forbidden questions and proved to be robust against model updates. The jailbreak prompts generated were not only naturally worded and succinct, but also challenging to defend against. These findings suggest that the creation of effective jailbreak prompts is less complex than previously believed, underscoring the heightened risk posed by black-box jailbreak attacks.

## BackdoorAlign: Mitigating Fine-tuning based Jailbreak Attack with Backdoor Enhanced Safety Alignment
📑 Citations: 53
🎯 Target: Text  🗂️ Category: Defense
📅 Year: 2024  📍 Venue: Neural Information Processing Systems

Abstract:
Despite the general capabilities of Large Language Models (LLMs) like GPT-4, these models still request fine-tuning or adaptation with customized data when meeting the specific business demands and intricacies of tailored use cases. However, this process inevitably introduces new safety threats, particularly against the Fine-tuning based Jailbreak Attack (FJAttack) under the setting of Language-Model-as-a-Service (LMaaS), where the model’s safety has been significantly compromised by fine-tuning on users’ uploaded examples that contain just a few harmful examples. Though potential defenses have been proposed that the service providers of LMaaS can integrate safety examples into the fine-tuning dataset to reduce safety issues, such approaches require incorporating a substantial amount of data, making it inefficient. To effectively defend against the FJAttack with limited safety examples under LMaaS, we propose the Backdoor Enhanced Safety Alignment method inspired by an analogy with the concept of backdoor attacks. In particular, service providers will construct prefixed safety examples with a secret prompt, acting as a “backdoor trigger”. By integrating prefixed safety examples into the fine-tuning dataset, the subsequent fine-tuning process effectively acts as the “backdoor attack,” establishing a strong correlation between the secret prompt and safety generations. Consequently, safe responses are ensured once service providers prepend this secret prompt ahead of any user input during inference. Our comprehensive experiments demonstrate that through the Backdoor Enhanced Safety Alignment with adding as few as 11 prefixed safety examples, the maliciously fine-tuned LLMs will achieve similar safety performance as the original aligned models without harming the benign performance. Furthermore, we

## Jailbreak Antidote: Runtime Safety-Utility Balance via Sparse Representation Adjustment in Large Language Models
📑 Citations: 53
🎯 Target: Text  🗂️ Category: Defense
📅 Year: 2024  📍 Venue: International Conference on Learning Representations

Abstract:
As large language models (LLMs) become integral to various applications, ensuring both their safety and utility is paramount. Jailbreak attacks, which manipulate LLMs into generating harmful content, pose significant challenges to this balance. Existing defenses, such as prompt engineering and safety fine-tuning, often introduce computational overhead, increase inference latency, and lack runtime flexibility. Moreover, overly restrictive safety measures can degrade model utility by causing refusals of benign queries. In this paper, we introduce Jailbreak Antidote, a method that enables real-time adjustment of LLM safety preferences by manipulating a sparse subset of the model's internal states during inference. By shifting the model's hidden representations along a safety direction with varying strengths, we achieve flexible control over the safety-utility balance without additional token overhead or inference delays. Our analysis reveals that safety-related information in LLMs is sparsely distributed; adjusting approximately 5% of the internal state is as effective as modifying the entire state. Extensive experiments on nine LLMs (ranging from 2 billion to 72 billion parameters), evaluated against ten jailbreak attack methods and compared with six defense strategies, validate the effectiveness and efficiency of our approach. By directly manipulating internal states during reasoning, Jailbreak Antidote offers a lightweight, scalable solution that enhances LLM safety while preserving utility, opening new possibilities for real-time safety mechanisms in widely-deployed AI systems.

## Jailbreak Attacks and Defenses against Multimodal Generative Models: A Survey
📑 Citations: 53
🎯 Target: Hybrid  🗂️ Category: Benchmark
📅 Year: 2024  📍 Venue: arXiv.org

Abstract:
The rapid evolution of multimodal foundation models has led to significant advancements in cross-modal understanding and generation across diverse modalities, including text, images, audio, and video. However, these models remain susceptible to jailbreak attacks, which can bypass built-in safety mechanisms and induce the production of potentially harmful content. Consequently, understanding the methods of jailbreak attacks and existing defense mechanisms is essential to ensure the safe deployment of multimodal generative models in real-world scenarios, particularly in security-sensitive applications. To provide comprehensive insight into this topic, this survey reviews jailbreak and defense in multimodal generative models. First, given the generalized lifecycle of multimodal jailbreak, we systematically explore attacks and corresponding defense strategies across four levels: input, encoder, generator, and output. Based on this analysis, we present a detailed taxonomy of attack methods, defense mechanisms, and evaluation frameworks specific to multimodal generative models. Additionally, we cover a wide range of input-output configurations, including modalities such as Any-to-Text, Any-to-Vision, and Any-to-Any within generative systems. Finally, we highlight current research challenges and propose potential directions for future research. The open-source repository corresponding to this work can be found at https://github.com/liuxuannan/Awesome-Multimodal-Jailbreak.

## Adversarial Tuning: Defending Against Jailbreak Attacks for LLMs
📑 Citations: 52
🎯 Target: Text  🗂️ Category: Defense
📅 Year: 2024  📍 Venue: arXiv.org

Abstract:
Although safely enhanced Large Language Models (LLMs) have achieved remarkable success in tackling various complex tasks in a zero-shot manner, they remain susceptible to jailbreak attacks, particularly the unknown jailbreak attack. To enhance LLMs' generalized defense capabilities, we propose a two-stage adversarial tuning framework, which generates adversarial prompts to explore worst-case scenarios by optimizing datasets containing pairs of adversarial prompts and their safe responses. In the first stage, we introduce the hierarchical meta-universal adversarial prompt learning to efficiently and effectively generate token-level adversarial prompts. In the second stage, we propose the automatic adversarial prompt learning to iteratively refine semantic-level adversarial prompts, further enhancing LLM's defense capabilities. We conducted comprehensive experiments on three widely used jailbreak datasets, comparing our framework with six defense baselines under five representative attack scenarios. The results underscore the superiority of our proposed methods. Furthermore, our adversarial tuning framework exhibits empirical generalizability across various attack strategies and target LLMs, highlighting its potential as a transferable defense mechanism.

## A Mousetrap: Fooling Large Reasoning Models for Jailbreak with Chain of Iterative Chaos
📑 Citations: 51
🎯 Target: Hybrid  🗂️ Category: Attack
📅 Year: 2025  📍 Venue: ACL

Abstract:


## Agents Under Siege: Breaking Pragmatic Multi-Agent LLM Systems with Optimized Prompt Attacks
📑 Citations: 51
🎯 Target: Agent  🗂️ Category: Attack
📅 Year: 2025  📍 Venue: ACL

Abstract:
