# Papers with More Than 50 Citations

> Citation counts are queried from Google Scholar and refreshed monthly. Only papers with **more than 50 citations** are included.
> Last successful refresh: not yet queried (initial migration snapshot)

## AutoDAN: Generating Stealthy Jailbreak Prompts on Aligned Large Language Models
📑 Citations: 526
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2023  📍 Venue: International Conference on Learning Representations

Abstract:
The aligned Large Language Models (LLMs) are powerful language understanding and decision-making tools that are created through extensive alignment with human feedback. However, these large models remain susceptible to jailbreak attacks, where adversaries manipulate prompts to elicit malicious outputs that should not be given by aligned LLMs. Investigating jailbreak prompts can lead us to delve into the limitations of LLMs and further guide us to secure them. Unfortunately, existing jailbreak techniques suffer from either (1) scalability issues, where attacks heavily rely on manual crafting of prompts, or (2) stealthiness problems, as attacks depend on token-based algorithms to generate prompts that are often semantically meaningless, making them susceptible to detection through basic perplexity testing. In light of these challenges, we intend to answer this question: Can we develop an approach that can automatically generate stealthy jailbreak prompts? In this paper, we introduce AutoDAN, a novel jailbreak attack against aligned LLMs. AutoDAN can automatically generate stealthy jailbreak prompts by the carefully designed hierarchical genetic algorithm. Extensive evaluations demonstrate that AutoDAN not only automates the process while preserving semantic meaningfulness, but also demonstrates superior attack strength in cross-model transferability, and cross-sample universality compared with the baseline. Moreover, we also compare AutoDAN with perplexity-based defense methods and show that AutoDAN can bypass them effectively.

## GPTFUZZER: Red Teaming Large Language Models with Auto-Generated Jailbreak Prompts
📑 Citations: 481
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2023  📍 Venue: arXiv.org

Abstract:
Large language models (LLMs) have recently experienced tremendous popularity and are widely used from casual conversations to AI-driven programming. However, despite their considerable success, LLMs are not entirely reliable and can give detailed guidance on how to conduct harmful or illegal activities. While safety measures can reduce the risk of such outputs, adversarial jailbreak attacks can still exploit LLMs to produce harmful content. These jailbreak templates are typically manually crafted, making large-scale testing challenging. In this paper, we introduce GPTFuzz, a novel black-box jailbreak fuzzing framework inspired by the AFL fuzzing framework. Instead of manual engineering, GPTFuzz automates the generation of jailbreak templates for red-teaming LLMs. At its core, GPTFuzz starts with human-written templates as initial seeds, then mutates them to produce new templates. We detail three key components of GPTFuzz: a seed selection strategy for balancing efficiency and variability, mutate operators for creating semantically equivalent or similar sentences, and a judgment model to assess the success of a jailbreak attack. We evaluate GPTFuzz against various commercial and open-source LLMs, including ChatGPT, LLaMa-2, and Vicuna, under diverse attack scenarios. Our results indicate that GPTFuzz consistently produces jailbreak templates with a high success rate, surpassing human-crafted templates. Remarkably, GPTFuzz achieves over 90% attack success rates against ChatGPT and Llama-2 models, even with suboptimal initial seed templates. We anticipate that GPTFuzz will be instrumental for researchers and practitioners in examining LLM robustness and will encourage further exploration into enhancing LLM safety.

## How Johnny Can Persuade LLMs to Jailbreak Them: Rethinking Persuasion to Challenge AI Safety by Humanizing LLMs
📑 Citations: 459
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2024  📍 Venue: Annual Meeting of the Association for Computational Linguistics

Abstract:
Most traditional AI safety research has approached AI models as machines and centered on algorithm-focused attacks developed by security experts. As large language models (LLMs) become increasingly common and competent, non-expert users can also impose risks during daily interactions. This paper introduces a new perspective to jailbreak LLMs as human-like communicators, to explore this overlooked intersection between everyday language interaction and AI safety. Specifically, we study how to persuade LLMs to jailbreak them. First, we propose a persuasion taxonomy derived from decades of social science research. Then, we apply the taxonomy to automatically generate interpretable persuasive adversarial prompts (PAP) to jailbreak LLMs. Results show that persuasion significantly increases the jailbreak performance across all risk categories: PAP consistently achieves an attack success rate of over $92\%$ on Llama 2-7b Chat, GPT-3.5, and GPT-4 in $10$ trials, surpassing recent algorithm-focused attacks. On the defense side, we explore various mechanisms against PAP and, found a significant gap in existing defenses, and advocate for more fundamental mitigation for highly interactive LLMs

## "Do Anything Now": Characterizing and Evaluating In-The-Wild Jailbreak Prompts on Large Language Models
📑 Citations: 426
🎯 Target: Text  🗂️ Category: Benchmark
📅 Year: 2023  📍 Venue: Conference on Computer and Communications Security

Abstract:
The misuse of large language models (LLMs) has drawn significant attention from the general public and LLM vendors. One particular type of adversarial prompt, known as jailbreak prompt, has emerged as the main attack vector to bypass the safeguards and elicit harmful content from LLMs. In this paper, employing our new framework JailbreakHub, we conduct a comprehensive analysis of 1,405 jailbreak prompts spanning from December 2022 to December 2023. We identify 131 jailbreak communities and discover unique characteristics of jailbreak prompts and their major attack strategies, such as prompt injection and privilege escalation. We also observe that jailbreak prompts increasingly shift from online Web communities to prompt-aggregation websites and 28 user accounts have consistently optimized jailbreak prompts over 100 days. To assess the potential harm caused by jailbreak prompts, we create a question set comprising 107,250 samples across 13 forbidden scenarios. Leveraging this dataset, our experiments on six popular LLMs show that their safeguards cannot adequately defend jailbreak prompts in all scenarios. Particularly, we identify five highly effective jailbreak prompts that achieve 0.95 attack success rates on ChatGPT (GPT-3.5) and GPT-4, and the earliest one has persisted online for over 240 days. We hope that our study can facilitate the research community and LLM vendors in promoting safer and regulated LLMs.

## Catastrophic Jailbreak of Open-source LLMs via Exploiting Generation
📑 Citations: 390
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2023  📍 Venue: International Conference on Learning Representations

Abstract:
The rapid progress in open-source large language models (LLMs) is significantly advancing AI development. Extensive efforts have been made before model release to align their behavior with human values, with the primary goal of ensuring their helpfulness and harmlessness. However, even carefully aligned models can be manipulated maliciously, leading to unintended behaviors, known as"jailbreaks". These jailbreaks are typically triggered by specific text inputs, often referred to as adversarial prompts. In this work, we propose the generation exploitation attack, an extremely simple approach that disrupts model alignment by only manipulating variations of decoding methods. By exploiting different generation strategies, including varying decoding hyper-parameters and sampling methods, we increase the misalignment rate from 0% to more than 95% across 11 language models including LLaMA2, Vicuna, Falcon, and MPT families, outperforming state-of-the-art attacks with $30\times$ lower computational cost. Finally, we propose an effective alignment method that explores diverse generation strategies, which can reasonably reduce the misalignment rate under our attack. Altogether, our study underscores a major failure in current safety evaluation and alignment procedures for open-source LLMs, strongly advocating for more comprehensive red teaming and better alignment before releasing such models. Our code is available at https://github.com/Princeton-SysML/Jailbreak_LLM.

## Jailbreak and Guard Aligned Language Models with Only Few In-Context Demonstrations
📑 Citations: 383
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2023  📍 Venue: arXiv.org

Abstract:
Large Language Models (LLMs) have shown remarkable success in various tasks, yet their safety and the risk of generating harmful content remain pressing concerns. In this paper, we delve into the potential of In-Context Learning (ICL) to modulate the alignment of LLMs. Specifically, we propose the In-Context Attack (ICA) which employs harmful demonstrations to subvert LLMs, and the In-Context Defense (ICD) which bolsters model resilience through examples that demonstrate refusal to produce harmful responses. We offer theoretical insights to elucidate how a limited set of in-context demonstrations can pivotally influence the safety alignment of LLMs. Through extensive experiments, we demonstrate the efficacy of ICA and ICD in respectively elevating and mitigating the success rates of jailbreaking prompts. Our findings illuminate the profound influence of ICL on LLM behavior, opening new avenues for improving the safety of LLMs.

## Defending ChatGPT against jailbreak attack via self-reminders
📑 Citations: 337
🎯 Target: Text  🗂️ Category: Defense
📅 Year: 2023  📍 Venue: Nature Machine Intelligence

Abstract:
No abstract provided.

## Low-Resource Languages Jailbreak GPT-4
📑 Citations: 261
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2023  📍 Venue: arXiv.org

Abstract:
AI safety training and red-teaming of large language models (LLMs) are measures to mitigate the generation of unsafe content. Our work exposes the inherent cross-lingual vulnerability of these safety mechanisms, resulting from the linguistic inequality of safety training data, by successfully circumventing GPT-4's safeguard through translating unsafe English inputs into low-resource languages. On the AdvBenchmark, GPT-4 engages with the unsafe translated inputs and provides actionable items that can get the users towards their harmful goals 79% of the time, which is on par with or even surpassing state-of-the-art jailbreaking attacks. Other high-/mid-resource languages have significantly lower attack success rate, which suggests that the cross-lingual vulnerability mainly applies to low-resource languages. Previously, limited training on low-resource languages primarily affects speakers of those languages, causing technological disparities. However, our work highlights a crucial shift: this deficiency now poses a risk to all LLMs users. Publicly available translation APIs enable anyone to exploit LLMs' safety vulnerabilities. Therefore, our work calls for a more holistic red-teaming efforts to develop robust multilingual safeguards with wide language coverage.

## Visual Adversarial Examples Jailbreak Aligned Large Language Models
📑 Citations: 258
🎯 Target: Vision  🗂️ Category: Attack
📅 Year: 2023  📍 Venue: AAAI Conference on Artificial Intelligence

Abstract:
Warning: this paper contains data, prompts, and model outputs that are offensive in nature. Recently, there has been a surge of interest in integrating vision into Large Language Models (LLMs), exemplified by Visual Language Models (VLMs) such as Flamingo and GPT-4. This paper sheds light on the security and safety implications of this trend. First, we underscore that the continuous and high-dimensional nature of the visual input makes it a weak link against adversarial attacks, representing an expanded attack surface of vision-integrated LLMs. Second, we highlight that the versatility of LLMs also presents visual attackers with a wider array of achievable adversarial objectives, extending the implications of security failures beyond mere misclassification. As an illustration, we present a case study in which we exploit visual adversarial examples to circumvent the safety guardrail of aligned LLMs with integrated vision. Intriguingly, we discover that a single visual adversarial example can universally jailbreak an aligned LLM, compelling it to heed a wide range of harmful instructions (that it otherwise would not) and generate harmful content that transcends the narrow scope of a `few-shot' derogatory corpus initially employed to optimize the adversarial example. Our study underscores the escalating adversarial risks associated with the pursuit of multimodality. Our findings also connect the long-studied adversarial vulnerabilities of neural networks to the nascent field of AI alignment. The presented attack suggests a fundamental adversarial challenge for AI alignment, especially in light of the emerging trend toward multimodality in frontier foundation models.

## Jailbreak in pieces: Compositional Adversarial Attacks on Multi-Modal Language Models
📑 Citations: 217
🎯 Target: Vision  🗂️ Category: Attack
📅 Year: 2023  📍 Venue: International Conference on Learning Representations

Abstract:
We introduce new jailbreak attacks on vision language models (VLMs), which use aligned LLMs and are resilient to text-only jailbreak attacks. Specifically, we develop cross-modality attacks on alignment where we pair adversarial images going through the vision encoder with textual prompts to break the alignment of the language model. Our attacks employ a novel compositional strategy that combines an image, adversarially targeted towards toxic embeddings, with generic prompts to accomplish the jailbreak. Thus, the LLM draws the context to answer the generic prompt from the adversarial image. The generation of benign-appearing adversarial images leverages a novel embedding-space-based methodology, operating with no access to the LLM model. Instead, the attacks require access only to the vision encoder and utilize one of our four embedding space targeting strategies. By not requiring access to the LLM, the attacks lower the entry barrier for attackers, particularly when vision encoders such as CLIP are embedded in closed-source LLMs. The attacks achieve a high success rate across different VLMs, highlighting the risk of cross-modality alignment vulnerabilities, and the need for new alignment approaches for multi-modal models.

## A Wolf in Sheep’s Clothing: Generalized Nested Jailbreak Prompts can Fool Large Language Models Easily
📑 Citations: 202
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2023  📍 Venue: North American Chapter of the Association for Computational Linguistics

Abstract:
Large Language Models (LLMs), such as ChatGPT and GPT-4, are designed to provide useful and safe responses. However, adversarial prompts known as ‘jailbreaks’ can circumvent safeguards, leading LLMs to generate potentially harmful content. Exploring jailbreak prompts can help to better reveal the weaknesses of LLMs and further steer us to secure them. Unfortunately, existing jailbreak methods either suffer from intricate manual design or require optimization on other white-box models, which compromises either generalization or efficiency. In this paper, we generalize jailbreak prompt attacks into two aspects: (1) Prompt Rewriting and (2) Scenario Nesting. Based on this, we propose ReNeLLM, an automatic framework that leverages LLMs themselves to generate effective jailbreak prompts. Extensive experiments demonstrate that ReNeLLM significantly improves the attack success rate while greatly reducing the time cost compared to existing baselines. Our study also reveals the inadequacy of current defense methods in safeguarding LLMs. Finally, we analyze the failure of LLMs defense from the perspective of prompt execution priority, and propose corresponding defense strategies. We hope that our research can catalyze both the academic community and LLMs developers towards the provision of safer and more regulated LLMs. The code is available at https://github.com/NJUNLP/ReNeLLM.

## Jailbreak Attacks and Defenses Against Large Language Models: A Survey
📑 Citations: 191
🎯 Target: Text  🗂️ Category: Other
📅 Year: 2024  📍 Venue: arXiv.org

Abstract:
Large Language Models (LLMs) have performed exceptionally in various text-generative tasks, including question answering, translation, code completion, etc. However, the over-assistance of LLMs has raised the challenge of"jailbreaking", which induces the model to generate malicious responses against the usage policy and society by designing adversarial prompts. With the emergence of jailbreak attack methods exploiting different vulnerabilities in LLMs, the corresponding safety alignment measures are also evolving. In this paper, we propose a comprehensive and detailed taxonomy of jailbreak attack and defense methods. For instance, the attack methods are divided into black-box and white-box attacks based on the transparency of the target model. Meanwhile, we classify defense methods into prompt-level and model-level defenses. Additionally, we further subdivide these attack and defense methods into distinct sub-classes and present a coherent diagram illustrating their relationships. We also conduct an investigation into the current evaluation methods and compare them from different perspectives. Our findings aim to inspire future research and practical implementations in safeguarding LLMs against adversarial attacks. Above all, although jailbreak remains a significant concern within the community, we believe that our work enhances the understanding of this domain and provides a foundation for developing more secure LLMs.

## Jailbreaker: Automated Jailbreak Across Multiple Large Language Model Chatbots
📑 Citations: 187
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2023  📍 Venue: arXiv.org

Abstract:
No abstract provided.

## Multilingual Jailbreak Challenges in Large Language Models
📑 Citations: 186
🎯 Target: Text  🗂️ Category: Defense
📅 Year: 2023  📍 Venue: International Conference on Learning Representations

Abstract:
While large language models (LLMs) exhibit remarkable capabilities across a wide range of tasks, they pose potential safety concerns, such as the ``jailbreak'' problem, wherein malicious instructions can manipulate LLMs to exhibit undesirable behavior. Although several preventive measures have been developed to mitigate the potential risks associated with LLMs, they have primarily focused on English. In this study, we reveal the presence of multilingual jailbreak challenges within LLMs and consider two potential risky scenarios: unintentional and intentional. The unintentional scenario involves users querying LLMs using non-English prompts and inadvertently bypassing the safety mechanisms, while the intentional scenario concerns malicious users combining malicious instructions with multilingual prompts to deliberately attack LLMs. The experimental results reveal that in the unintentional scenario, the rate of unsafe content increases as the availability of languages decreases. Specifically, low-resource languages exhibit about three times the likelihood of encountering harmful content compared to high-resource languages, with both ChatGPT and GPT-4. In the intentional scenario, multilingual prompts can exacerbate the negative impact of malicious instructions, with astonishingly high rates of unsafe output: 80.92\% for ChatGPT and 40.71\% for GPT-4. To handle such a challenge in the multilingual context, we propose a novel \textsc{Self-Defense} framework that automatically generates multilingual training data for safety fine-tuning. Experimental results show that ChatGPT fine-tuned with such data can achieve a substantial reduction in unsafe content generation. Data is available at \url{https://github.com/DAMO-NLP-SG/multilingual-safety-for-LLMs}.

## ArtPrompt: ASCII Art-based Jailbreak Attacks against Aligned LLMs
📑 Citations: 182
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2024  📍 Venue: Annual Meeting of the Association for Computational Linguistics

Abstract:
Safety is critical to the usage of large language models (LLMs). Multiple techniques such as data filtering and supervised fine-tuning have been developed to strengthen LLM safety. However, currently known techniques presume that corpora used for safety alignment of LLMs are solely interpreted by semantics. This assumption, however, does not hold in real-world applications, which leads to severe vulnerabilities in LLMs. For example, users of forums often use ASCII art, a form of text-based art, to convey image information. In this paper, we propose a novel ASCII art-based jailbreak attack and introduce a comprehensive benchmark Vision-in-Text Challenge (ViTC) to evaluate the capabilities of LLMs in recognizing prompts that cannot be solely interpreted by semantics. We show that five SOTA LLMs (GPT-3.5, GPT-4, Gemini, Claude, and Llama2) struggle to recognize prompts provided in the form of ASCII art. Based on this observation, we develop the jailbreak attack ArtPrompt, which leverages the poor performance of LLMs in recognizing ASCII art to bypass safety measures and elicit undesired behaviors from LLMs. ArtPrompt only requires black-box access to the victim LLMs, making it a practical attack. We evaluate ArtPrompt on five SOTA LLMs, and show that ArtPrompt can effectively and efficiently induce undesired behaviors from all five LLMs. Our code is available at https://github.com/uw-nsl/ArtPrompt.

## Great, Now Write an Article About That: The Crescendo Multi-Turn LLM Jailbreak Attack
📑 Citations: 181
🎯 Target: Hybrid  🗂️ Category: Attack
📅 Year: 2024  📍 Venue: USENIX Security Symposium

Abstract:
Large Language Models (LLMs) have risen significantly in popularity and are increasingly being adopted across multiple applications. These LLMs are heavily aligned to resist engaging in illegal or unethical topics as a means to avoid contributing to responsible AI harms. However, a recent line of attacks, known as jailbreaks, seek to overcome this alignment. Intuitively, jailbreak attacks aim to narrow the gap between what the model can do and what it is willing to do. In this paper, we introduce a novel jailbreak attack called Crescendo. Unlike existing jailbreak methods, Crescendo is a simple multi-turn jailbreak that interacts with the model in a seemingly benign manner. It begins with a general prompt or question about the task at hand and then gradually escalates the dialogue by referencing the model's replies progressively leading to a successful jailbreak. We evaluate Crescendo on various public systems, including ChatGPT, Gemini Pro, Gemini-Ultra, LlaMA-2 70b and LlaMA-3 70b Chat, and Anthropic Chat. Our results demonstrate the strong efficacy of Crescendo, with it achieving high attack success rates across all evaluated models and tasks. Furthermore, we present Crescendomation, a tool that automates the Crescendo attack and demonstrate its efficacy against state-of-the-art models through our evaluations. Crescendomation surpasses other state-of-the-art jailbreaking techniques on the AdvBench subset dataset, achieving 29-61% higher performance on GPT-4 and 49-71% on Gemini-Pro. Finally, we also demonstrate Crescendo's ability to jailbreak multimodal models.

## SafeDecoding: Defending against Jailbreak Attacks via Safety-Aware Decoding
📑 Citations: 179
🎯 Target: Text  🗂️ Category: Defense
📅 Year: 2024  📍 Venue: Annual Meeting of the Association for Computational Linguistics

Abstract:
As large language models (LLMs) become increasingly integrated into real-world applications such as code generation and chatbot assistance, extensive efforts have been made to align LLM behavior with human values, including safety. Jailbreak attacks, aiming to provoke unintended and unsafe behaviors from LLMs, remain a significant/leading LLM safety threat. In this paper, we aim to defend LLMs against jailbreak attacks by introducing SafeDecoding, a safety-aware decoding strategy for LLMs to generate helpful and harmless responses to user queries. Our insight in developing SafeDecoding is based on the observation that, even though probabilities of tokens representing harmful contents outweigh those representing harmless responses, safety disclaimers still appear among the top tokens after sorting tokens by probability in descending order. This allows us to mitigate jailbreak attacks by identifying safety disclaimers and amplifying their token probabilities, while simultaneously attenuating the probabilities of token sequences that are aligned with the objectives of jailbreak attacks. We perform extensive experiments on five LLMs using six state-of-the-art jailbreak attacks and four benchmark datasets. Our results show that SafeDecoding significantly reduces the attack success rate and harmfulness of jailbreak attacks without compromising the helpfulness of responses to benign user queries. SafeDecoding outperforms six defense methods.

## JailBreakV: A Benchmark for Assessing the Robustness of MultiModal Large Language Models against Jailbreak Attacks
📑 Citations: 157
🎯 Target: Vision  🗂️ Category: Benchmark
📅 Year: 2024  📍 Venue: Unknown

Abstract:
With the rapid advancements in Multimodal Large Language Models (MLLMs), securing these models against malicious inputs while aligning them with human values has emerged as a critical challenge. In this paper, we investigate an important and unexplored question of whether techniques that successfully jailbreak Large Language Models (LLMs) can be equally effective in jailbreaking MLLMs. To explore this issue, we introduce JailBreakV-28K, a pioneering benchmark designed to assess the transferability of LLM jailbreak techniques to MLLMs, thereby evaluating the robustness of MLLMs against diverse jailbreak attacks. Utilizing a dataset of 2, 000 malicious queries that is also proposed in this paper, we generate 20, 000 text-based jailbreak prompts using advanced jailbreak attacks on LLMs, alongside 8, 000 image-based jailbreak inputs from recent MLLMs jailbreak attacks, our comprehensive dataset includes 28, 000 test cases across a spectrum of adversarial scenarios. Our evaluation of 10 open-source MLLMs reveals a notably high Attack Success Rate (ASR) for attacks transferred from LLMs, highlighting a critical vulnerability in MLLMs that stems from their text-processing capabilities. Our findings underscore the urgent need for future research to address alignment vulnerabilities in MLLMs from both textual and visual inputs.

## AutoDefense: Multi-Agent LLM Defense against Jailbreak Attacks
📑 Citations: 117
🎯 Target: Agent  🗂️ Category: Defense
📅 Year: 2024  📍 Venue: arXiv.org

Abstract:
Despite extensive pre-training in moral alignment to prevent generating harmful information, large language models (LLMs) remain vulnerable to jailbreak attacks. In this paper, we propose AutoDefense, a multi-agent defense framework that filters harmful responses from LLMs. With the response-filtering mechanism, our framework is robust against different jailbreak attack prompts, and can be used to defend different victim models. AutoDefense assigns different roles to LLM agents and employs them to complete the defense task collaboratively. The division in tasks enhances the overall instruction-following of LLMs and enables the integration of other defense components as tools. With AutoDefense, small open-source LMs can serve as agents and defend larger models against jailbreak attacks. Our experiments show that AutoDefense can effectively defense against different jailbreak attacks, while maintaining the performance at normal user request. For example, we reduce the attack success rate on GPT-3.5 from 55.74% to 7.95% using LLaMA-2-13b with a 3-agent system. Our code and data are publicly available at https://github.com/XHMY/AutoDefense.

## Universal Jailbreak Backdoors from Poisoned Human Feedback
📑 Citations: 106
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2023  📍 Venue: International Conference on Learning Representations

Abstract:
Reinforcement Learning from Human Feedback (RLHF) is used to align large language models to produce helpful and harmless responses. Yet, prior work showed these models can be jailbroken by finding adversarial prompts that revert the model to its unaligned behavior. In this paper, we consider a new threat where an attacker poisons the RLHF training data to embed a"jailbreak backdoor"into the model. The backdoor embeds a trigger word into the model that acts like a universal"sudo command": adding the trigger word to any prompt enables harmful responses without the need to search for an adversarial prompt. Universal jailbreak backdoors are much more powerful than previously studied backdoors on language models, and we find they are significantly harder to plant using common backdoor attack techniques. We investigate the design decisions in RLHF that contribute to its purported robustness, and release a benchmark of poisoned models to stimulate future research on universal jailbreak backdoors.

## Agent Smith: A Single Image Can Jailbreak One Million Multimodal LLM Agents Exponentially Fast
📑 Citations: 91
🎯 Target: Hybrid  🗂️ Category: Attack
📅 Year: 2024  📍 Venue: International Conference on Machine Learning

Abstract:
A multimodal large language model (MLLM) agent can receive instructions, capture images, retrieve histories from memory, and decide which tools to use. Nonetheless, red-teaming efforts have revealed that adversarial images/prompts can jailbreak an MLLM and cause unaligned behaviors. In this work, we report an even more severe safety issue in multi-agent environments, referred to as infectious jailbreak. It entails the adversary simply jailbreaking a single agent, and without any further intervention from the adversary, (almost) all agents will become infected exponentially fast and exhibit harmful behaviors. To validate the feasibility of infectious jailbreak, we simulate multi-agent environments containing up to one million LLaVA-1.5 agents, and employ randomized pair-wise chat as a proof-of-concept instantiation for multi-agent interaction. Our results show that feeding an (infectious) adversarial image into the memory of any randomly chosen agent is sufficient to achieve infectious jailbreak. Finally, we derive a simple principle for determining whether a defense mechanism can provably restrain the spread of infectious jailbreak, but how to design a practical defense that meets this principle remains an open question to investigate. Our project page is available at https://sail-sg.github.io/Agent-Smith/.

## AutoDAN-Turbo: A Lifelong Agent for Strategy Self-Exploration to Jailbreak LLMs
📑 Citations: 84
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2024  📍 Venue: International Conference on Learning Representations

Abstract:
In this paper, we propose AutoDAN-Turbo, a black-box jailbreak method that can automatically discover as many jailbreak strategies as possible from scratch, without any human intervention or predefined scopes (e.g., specified candidate strategies), and use them for red-teaming. As a result, AutoDAN-Turbo can significantly outperform baseline methods, achieving a 74.3% higher average attack success rate on public benchmarks. Notably, AutoDAN-Turbo achieves an 88.5 attack success rate on GPT-4-1106-turbo. In addition, AutoDAN-Turbo is a unified framework that can incorporate existing human-designed jailbreak strategies in a plug-and-play manner. By integrating human-designed strategies, AutoDAN-Turbo can even achieve a higher attack success rate of 93.4 on GPT-4-1106-turbo.

## A Comprehensive Study of Jailbreak Attack versus Defense for Large Language Models
📑 Citations: 83
🎯 Target: Text  🗂️ Category: Benchmark
📅 Year: 2024  📍 Venue: Annual Meeting of the Association for Computational Linguistics

Abstract:
Large Language Models (LLMS) have increasingly become central to generating content with potential societal impacts. Notably, these models have demonstrated capabilities for generating content that could be deemed harmful. To mitigate these risks, researchers have adopted safety training techniques to align model outputs with societal values to curb the generation of malicious content. However, the phenomenon of"jailbreaking", where carefully crafted prompts elicit harmful responses from models, persists as a significant challenge. This research conducts a comprehensive analysis of existing studies on jailbreaking LLMs and their defense techniques. We meticulously investigate nine attack techniques and seven defense techniques applied across three distinct language models: Vicuna, LLama, and GPT-3.5 Turbo. We aim to evaluate the effectiveness of these attack and defense techniques. Our findings reveal that existing white-box attacks underperform compared to universal techniques and that including special tokens in the input significantly affects the likelihood of successful attacks. This research highlights the need to concentrate on the security facets of LLMs. Additionally, we contribute to the field by releasing our datasets and testing framework, aiming to foster further research into LLM security. We believe these contributions will facilitate the exploration of security measures within this domain.

## JailbreakRadar: Comprehensive Assessment of Jailbreak Attacks Against LLMs
📑 Citations: 79
🎯 Target: Text  🗂️ Category: Benchmark
📅 Year: 2024  📍 Venue: Annual Meeting of the Association for Computational Linguistics

Abstract:
Jailbreak attacks aim to bypass the LLMs' safeguards. While researchers have proposed different jailbreak attacks in depth, they have done so in isolation -- either with unaligned settings or comparing a limited range of methods. To fill this gap, we present a large-scale evaluation of various jailbreak attacks. We collect 17 representative jailbreak attacks, summarize their features, and establish a novel jailbreak attack taxonomy. Then we conduct comprehensive measurement and ablation studies across nine aligned LLMs on 160 forbidden questions from 16 violation categories. Also, we test jailbreak attacks under eight advanced defenses. Based on our taxonomy and experiments, we identify some important patterns, such as heuristic-based attacks could achieve high attack success rates but are easy to mitigate by defenses, causing low practicality. Our study offers valuable insights for future research on jailbreak attacks and defenses. We hope our work could help the community avoid incremental work and serve as an effective benchmark tool for practitioners.

## Don't Listen To Me: Understanding and Exploring Jailbreak Prompts of Large Language Models
📑 Citations: 78
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2024  📍 Venue: USENIX Security Symposium

Abstract:
Recent advancements in generative AI have enabled ubiquitous access to large language models (LLMs). Empowered by their exceptional capabilities to understand and generate human-like text, these models are being increasingly integrated into our society. At the same time, there are also concerns on the potential misuse of this powerful technology, prompting defensive measures from service providers. To overcome such protection, jailbreaking prompts have recently emerged as one of the most effective mechanisms to circumvent security restrictions and elicit harmful content originally designed to be prohibited. Due to the rapid development of LLMs and their ease of access via natural languages, the frontline of jailbreak prompts is largely seen in online forums and among hobbyists. To gain a better understanding of the threat landscape of semantically meaningful jailbreak prompts, we systemized existing prompts and measured their jailbreak effectiveness empirically. Further, we conducted a user study involving 92 participants with diverse backgrounds to unveil the process of manually creating jailbreak prompts. We observed that users often succeeded in jailbreak prompts generation regardless of their expertise in LLMs. Building on the insights from the user study, we also developed a system using AI as the assistant to automate the process of jailbreak prompt generation.

## How Alignment and Jailbreak Work: Explain LLM Safety through Intermediate Hidden States
📑 Citations: 71
🎯 Target: Text  🗂️ Category: Mechanism
📅 Year: 2024  📍 Venue: Conference on Empirical Methods in Natural Language Processing

Abstract:
Large language models (LLMs) rely on safety alignment to avoid responding to malicious user inputs. Unfortunately, jailbreak can circumvent safety guardrails, resulting in LLMs generating harmful content and raising concerns about LLM safety. Due to language models with intensive parameters often regarded as black boxes, the mechanisms of alignment and jailbreak are challenging to elucidate. In this paper, we employ weak classifiers to explain LLM safety through the intermediate hidden states. We first confirm that LLMs learn ethical concepts during pre-training rather than alignment and can identify malicious and normal inputs in the early layers. Alignment actually associates the early concepts with emotion guesses in the middle layers and then refines them to the specific reject tokens for safe generations. Jailbreak disturbs the transformation of early unethical classification into negative emotions. We conduct experiments on models from 7B to 70B across various model families to prove our conclusion. Overall, our paper indicates the intrinsical mechanism of LLM safety and how jailbreaks circumvent safety guardrails, offering a new perspective on LLM safety and reducing concerns. Our code is available at https://github.com/ydyjya/LLM-IHS-Explanation.

## Jailbreak Vision Language Models via Bi-Modal Adversarial Prompt
📑 Citations: 71
🎯 Target: Vision  🗂️ Category: Attack
📅 Year: 2024  📍 Venue: IEEE Transactions on Information Forensics and Security

Abstract:
In the realm of large vision language models (LVLMs), jailbreak attacks serve as a red-teaming approach to bypass guardrails and uncover safety implications. Existing jailbreaks predominantly focus on the visual modality, perturbing solely visual inputs in the prompt for attacks. However, they fall short when confronted with aligned models that fuse visual and textual features simultaneously for generation. To address this limitation, this paper introduces the Bi-Modal Adversarial Prompt Attack (BAP), which executes jailbreaks by optimizing textual and visual prompts cohesively. Initially, we adversarially embed universally adversarial perturbations in an image, guided by a few-shot query-agnostic corpus (e.g., affirmative prefixes and negative inhibitions). This process ensures that the adversarial image prompt LVLMs to respond positively to harmful queries. Subsequently, leveraging the image, we optimize textual prompts with specific harmful intent. In particular, we utilize a large language model to analyze jailbreak failures and employ chain-of-thought reasoning to refine textual prompts through a feedback-iteration manner. To validate the efficacy of our approach, we conducted extensive evaluations on various datasets and LVLMs, demonstrating that our BAP significantly outperforms other methods by large margins (+29.03% in attack success rate on average). Additionally, we showcase the potential of our attacks on black-box commercial LVLMs, such as GPT-4o and Gemini. Our code is available at https://anonymous.4open.science/r/BAP-Jailbreak-Vision-Language-Models-via-Bi-Modal-Adversarial-Prompt-5496

## Defending Large Language Models against Jailbreak Attacks via Semantic Smoothing
📑 Citations: 69
🎯 Target: Text  🗂️ Category: Defense
📅 Year: 2024  📍 Venue: arXiv.org

Abstract:
Aligned large language models (LLMs) are vulnerable to jailbreaking attacks, which bypass the safeguards of targeted LLMs and fool them into generating objectionable content. While initial defenses show promise against token-based threat models, there do not exist defenses that provide robustness against semantic attacks and avoid unfavorable trade-offs between robustness and nominal performance. To meet this need, we propose SEMANTICSMOOTH, a smoothing-based defense that aggregates the predictions of multiple semantically transformed copies of a given input prompt. Experimental results demonstrate that SEMANTICSMOOTH achieves state-of-the-art robustness against GCG, PAIR, and AutoDAN attacks while maintaining strong nominal performance on instruction following benchmarks such as InstructionFollowing and AlpacaEval. The codes will be publicly available at https://github.com/UCSB-NLP-Chang/SemanticSmooth.

## LLM Jailbreak Attack versus Defense Techniques - A Comprehensive Study
📑 Citations: 67
🎯 Target: Hybrid  🗂️ Category: Benchmark
📅 Year: 2024  📍 Venue: arXiv.org

Abstract:
No abstract provided.

## Pandora: Jailbreak GPTs by Retrieval Augmented Generation Poisoning
📑 Citations: 66
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2024  📍 Venue: Proceedings 2024 Workshop on AI Systems with Confidential COmputing

Abstract:
Large Language Models~(LLMs) have gained immense popularity and are being increasingly applied in various domains. Consequently, ensuring the security of these models is of paramount importance. Jailbreak attacks, which manipulate LLMs to generate malicious content, are recognized as a significant vulnerability. While existing research has predominantly focused on direct jailbreak attacks on LLMs, there has been limited exploration of indirect methods. The integration of various plugins into LLMs, notably Retrieval Augmented Generation~(RAG), which enables LLMs to incorporate external knowledge bases into their response generation such as GPTs, introduces new avenues for indirect jailbreak attacks. To fill this gap, we investigate indirect jailbreak attacks on LLMs, particularly GPTs, introducing a novel attack vector named Retrieval Augmented Generation Poisoning. This method, Pandora, exploits the synergy between LLMs and RAG through prompt manipulation to generate unexpected responses. Pandora uses maliciously crafted content to influence the RAG process, effectively initiating jailbreak attacks. Our preliminary tests show that Pandora successfully conducts jailbreak attacks in four different scenarios, achieving higher success rates than direct attacks, with 64.3\% for GPT-3.5 and 34.8\% for GPT-4.

## Play Guessing Game with LLM: Indirect Jailbreak Attack with Implicit Clues
📑 Citations: 64
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2024  📍 Venue: Annual Meeting of the Association for Computational Linguistics

Abstract:
With the development of LLMs, the security threats of LLMs are getting more and more attention. Numerous jailbreak attacks have been proposed to assess the security defense of LLMs. Current jailbreak attacks primarily utilize scenario camouflage techniques. However their explicitly mention of malicious intent will be easily recognized and defended by LLMs. In this paper, we propose an indirect jailbreak attack approach, Puzzler, which can bypass the LLM's defense strategy and obtain malicious response by implicitly providing LLMs with some clues about the original malicious query. In addition, inspired by the wisdom of"When unable to attack, defend"from Sun Tzu's Art of War, we adopt a defensive stance to gather clues about the original malicious query through LLMs. Extensive experimental results show that Puzzler achieves a query success rate of 96.6% on closed-source LLMs, which is 57.9%-82.7% higher than baselines. Furthermore, when tested against the state-of-the-art jailbreak detection approaches, Puzzler proves to be more effective at evading detection compared to baselines.

## Latent Jailbreak: A Benchmark for Evaluating Text Safety and Output Robustness of Large Language Models
📑 Citations: 60
🎯 Target: Text  🗂️ Category: Benchmark
📅 Year: 2023  📍 Venue: arXiv.org

Abstract:
Considerable research efforts have been devoted to ensuring that large language models (LLMs) align with human values and generate safe text. However, an excessive focus on sensitivity to certain topics can compromise the model's robustness in following instructions, thereby impacting its overall performance in completing tasks. Previous benchmarks for jailbreaking LLMs have primarily focused on evaluating the safety of the models without considering their robustness. In this paper, we propose a benchmark that assesses both the safety and robustness of LLMs, emphasizing the need for a balanced approach. To comprehensively study text safety and output robustness, we introduce a latent jailbreak prompt dataset, each involving malicious instruction embedding. Specifically, we instruct the model to complete a regular task, such as translation, with the text to be translated containing malicious instructions. To further analyze safety and robustness, we design a hierarchical annotation framework. We present a systematic analysis of the safety and robustness of LLMs regarding the position of explicit normal instructions, word replacements (verbs in explicit normal instructions, target groups in malicious instructions, cue words for explicit normal instructions), and instruction replacements (different explicit normal instructions). Our results demonstrate that current LLMs not only prioritize certain instruction verbs but also exhibit varying jailbreak rates for different instruction verbs in explicit normal instructions. Code and data are available at https://github.com/qiuhuachuan/latent-jailbreak.

## GradSafe: Detecting Jailbreak Prompts for LLMs via Safety-Critical Gradient Analysis
📑 Citations: 58
🎯 Target: Text  🗂️ Category: Defense
📅 Year: 2024  📍 Venue: Annual Meeting of the Association for Computational Linguistics

Abstract:
Large Language Models (LLMs) face threats from jailbreak prompts. Existing methods for detecting jailbreak prompts are primarily online moderation APIs or finetuned LLMs. These strategies, however, often require extensive and resource-intensive data collection and training processes. In this study, we propose GradSafe, which effectively detects jailbreak prompts by scrutinizing the gradients of safety-critical parameters in LLMs. Our method is grounded in a pivotal observation: the gradients of an LLM's loss for jailbreak prompts paired with compliance response exhibit similar patterns on certain safety-critical parameters. In contrast, safe prompts lead to different gradient patterns. Building on this observation, GradSafe analyzes the gradients from prompts (paired with compliance responses) to accurately detect jailbreak prompts. We show that GradSafe, applied to Llama-2 without further training, outperforms Llama Guard, despite its extensive finetuning with a large dataset, in detecting jailbreak prompts. This superior performance is consistent across both zero-shot and adaptation scenarios, as evidenced by our evaluations on ToxicChat and XSTest. The source code is available at https://github.com/xyq7/GradSafe.

## FuzzLLM: A Novel and Universal Fuzzing Framework for Proactively Discovering Jailbreak Vulnerabilities in Large Language Models
📑 Citations: 56
🎯 Target: Text  🗂️ Category: Attack
📅 Year: 2023  📍 Venue: IEEE International Conference on Acoustics, Speech, and Signal Processing

Abstract:
Jailbreak vulnerabilities in Large Language Models (LLMs), which exploit meticulously crafted prompts to elicit content that violates service guidelines, have captured the attention of research communities. While model owners can defend against individual jailbreak prompts through safety training strategies, this relatively passive approach struggles to handle the broader category of similar jailbreaks. To tackle this issue, we introduce FuzzLLM, an automated fuzzing framework designed to proactively test and discover jailbreak vulnerabilities in LLMs. We utilize templates to capture the structural integrity of a prompt and isolate key features of a jailbreak class as constraints. By integrating different base classes into powerful combo attacks and varying the elements of constraints and prohibited questions, FuzzLLM enables efficient testing with reduced manual effort. Extensive experiments demonstrate FuzzLLM's effectiveness and comprehensiveness in vulnerability discovery across various LLMs.

## Defending Large Language Models Against Jailbreak Attacks via Layer-specific Editing
📑 Citations: 52
🎯 Target: Text  🗂️ Category: Defense
📅 Year: 2024  📍 Venue: Conference on Empirical Methods in Natural Language Processing

Abstract:
Large language models (LLMs) are increasingly being adopted in a wide range of real-world applications. Despite their impressive performance, recent studies have shown that LLMs are vulnerable to deliberately crafted adversarial prompts even when aligned via Reinforcement Learning from Human Feedback or supervised fine-tuning. While existing defense methods focus on either detecting harmful prompts or reducing the likelihood of harmful responses through various means, defending LLMs against jailbreak attacks based on the inner mechanisms of LLMs remains largely unexplored. In this work, we investigate how LLMs response to harmful prompts and propose a novel defense method termed \textbf{L}ayer-specific \textbf{Ed}iting (LED) to enhance the resilience of LLMs against jailbreak attacks. Through LED, we reveal that several critical \textit{safety layers} exist among the early layers of LLMs. We then show that realigning these safety layers (and some selected additional layers) with the decoded safe response from selected target layers can significantly improve the alignment of LLMs against jailbreak attacks. Extensive experiments across various LLMs (e.g., Llama2, Mistral) show the effectiveness of LED, which effectively defends against jailbreak attacks while maintaining performance on benign prompts. Our code is available at \url{https://github.com/ledllm/ledllm}.

## Query-Relevant Images Jailbreak Large Multi-Modal Models
📑 Citations: 52
🎯 Target: Vision  🗂️ Category: Attack
📅 Year: 2023  📍 Venue: arXiv.org

Abstract:
No abstract provided.

## Visual-RolePlay: Universal Jailbreak Attack on MultiModal Large Language Models via Role-playing Image Characte
📑 Citations: 52
🎯 Target: Vision  🗂️ Category: Attack
📅 Year: 2024  📍 Venue: arXiv.org

Abstract:
With the advent and widespread deployment of Multimodal Large Language Models (MLLMs), ensuring their safety has become increasingly critical. To achieve this objective, it requires us to proactively discover the vulnerability of MLLMs by exploring the attack methods. Thus, structure-based jailbreak attacks, where harmful semantic content is embedded within images, have been proposed to mislead the models. However, previous structure-based jailbreak methods mainly focus on transforming the format of malicious queries, such as converting harmful content into images through typography, which lacks sufficient jailbreak effectiveness and generalizability. To address these limitations, we first introduce the concept of"Role-play"into MLLM jailbreak attacks and propose a novel and effective method called Visual Role-play (VRP). Specifically, VRP leverages Large Language Models to generate detailed descriptions of high-risk characters and create corresponding images based on the descriptions. When paired with benign role-play instruction texts, these high-risk character images effectively mislead MLLMs into generating malicious responses by enacting characters with negative attributes. We further extend our VRP method into a universal setup to demonstrate its generalizability. Extensive experiments on popular benchmarks show that VRP outperforms the strongest baseline, Query relevant and FigStep, by an average Attack Success Rate (ASR) margin of 14.3% across all models.
