> Source: https://msc-ai.iit.demokritos.gr/en/thesis/adversarial-attacks-and-robustness-deep-neural-networks-sound-event-detection

Adversarial attacks and robustness in deep neural networks for sound event detection | Δ.Π.Μ.Σ. στην Τεχνητή Νοημοσύνη
Skip to main content
English
Ελληνικά
STUDIES
ACADEMIC CALENDAR
SYLLABUS
STUDY GUIDE
MSc THESIS
MSc THESIS REGULATION
PROCEDURE & GUIDELINES FOR THE MSc THESIS +
REGULATIONS
OPERATING REGULATION
MOBILITY AND INTERNSHIP REGULATION
COMPLAINT & APPEAL MANAGEMENT POLICY
ACADEMIC ADVISOR POLICY
POSTGRADUATE THESIS REGULATION +
PROVIDED SERVICES FOR STUDENTS +
TUTORS
APPLICATIONS
APPLICATIONS FOR STUDENSHIP
DOCUMENTS FOR STUDENT APPLICATION
HOW TO APPLY +
ANNOUNCEMENTS
CONTACT
Main menu
STUDIES
ACADEMIC CALENDAR
SYLLABUS
STUDY GUIDE
MSc THESIS
MSc THESIS REGULATION
PROCEDURE & GUIDELINES FOR THE MSc THESIS
REGULATIONS
OPERATING REGULATION
MOBILITY AND INTERNSHIP REGULATION
COMPLAINT & APPEAL MANAGEMENT POLICY
ACADEMIC ADVISOR POLICY
POSTGRADUATE THESIS REGULATION
PROVIDED SERVICES FOR STUDENTS
TUTORS
APPLICATIONS
APPLICATIONS FOR STUDENSHIP
DOCUMENTS FOR STUDENT APPLICATION
HOW TO APPLY
ANNOUNCEMENTS
CONTACT
STUDIES
ACADEMIC CALENDAR
SYLLABUS
STUDY GUIDE
MSc THESIS
MSc THESIS REGULATION
PROCEDURE & GUIDELINES FOR THE MSc THESIS
REGULATIONS
OPERATING REGULATION
MOBILITY AND INTERNSHIP REGULATION
COMPLAINT & APPEAL MANAGEMENT POLICY
ACADEMIC ADVISOR POLICY
POSTGRADUATE THESIS REGULATION
PROVIDED SERVICES FOR STUDENTS
TUTORS
APPLICATIONS
APPLICATIONS FOR STUDENSHIP
DOCUMENTS FOR STUDENT APPLICATION
HOW TO APPLY
ANNOUNCEMENTS
CONTACT
Adversarial attacks and robustness in deep neural networks for sound event detection
Summary
As the use of Sound Event Detection (SED) systems expands into real-world and safety-critical applications, ensuring their robustness against malicious manipulation is becoming increasingly important. This thesis explores the vulnerability of deep learning models employed in Sound Event Detection (SED) to black-box adversarial attacks and examines strategies to enhance their robustness.
From the attacker's perspective, two optimization-based attacks—Particle Swarm Optimization (PSO) and Differential Evolution (DE)—are employed to generate adversarial audio samples. To maintain imperceptibility and control the additive noise, regularization terms are employed and experiments are performed under varying signal-to-noise ratios (SNRs). The attacks were evaluated across a broad spectrum of model architectures, including convolutional neural networks (CNNs) with and without Global Average Pooling, ResNet-based models like AudioCLIP, and transformer-based architectures like PaSST. Fine-tuning was applied to adapt pre-trained models like AudioCLIP to the specific distributions of UrbanSound8K and ESC-50, allowing consistent evaluation across datasets. Experimental results show that the AudioCLIP-finetuned model is highly susceptible to attacks, while transformer-based models like PaSST demonstrate greater robustness.
To mitigate the effectiveness of the attacks, a denoising autoencoder is employed and integrated in each model's head. This technique is also used for the detection of adversarial examples before passing them through the models. To be more specific, by analyzing the divergences and distances between the original and reconstructed inputs, we are able to conclude if a sample is manipulated or not.
The results demonstrate that the most effective attacks were achieved using the PSO algorithm, reaching a maximum success rate of 76% on the AudioCLIP-finetuned model at a target SNR of 5 dB. As the SNR constraint increased to 15–20 dB, making perturbations less perceptible to human listeners, the attack success rates dropped, stabilizing around 40–50% for vulnerable models and falling below 20% for more robust ones, confirming the trade-off between adversarial effectiveness and imperceptibility. The evaluation with the Autoencoder-based defense showed a consistent reduction of 5–10% in the attack success rate across all models, without noticeably affecting the models' original classification accuracy on clean inputs, making it an effective yet simple defensive approach. Additionally, the detection experiment based on prediction consistency before and after autoencoder denoising achieved a perfect precision of 1.0 but a recall of approximately 34%, indicating it can reliably flag adversarial samples when detected, although it misses a portion of attacks, suggesting the need for future improvements to increase sensitivity.
These findings highlight the urgent need to enhance the robustness of neural networks, particularly for safety-critical applications where adversarial manipulation could have serious consequences. The integration of a denoising autoencoder proved effective, consistently reducing attack success rates without degrading model performance, with noticeable benefits across both CNN-based models and transformer-based architectures like PaSST. Overall, the results emphasize the crucial role of designing inherently robust model architectures and employing strategic preprocessing techniques to strengthen SED systems against adversarial threats.
Link to full text:
https://dione.lib.unipi.gr/xmlui/handle/unipi/17807(link is external)
Other theses
2025-2026
Dimensionality reduction for complex event forecasting Michail Sidiropoulos
Automated free speech to SQL transcription Christina Anna Toliopoulou
Unsupervised temporal analysis of mouse vocalizations Christodoulos Bochalis
Diffusion models in offline reinforcement learning Christos Kyriazopoulos
Few shot learning: an overview of methods, applications and benchmarks Christos Georgios Foukanelis
Autonomous multi-objective design optimization using Bayesian approaches and active learning Alexandros Ntagiantas
Physics-informed machine learning methods for nonlinear problems in structural mechanics Emmanouella Makrymanolaki
2024-2025
Automatic music captioning Vasiliki Rentoula
Food recognition and calorie estimation using computer vision Viktoria Polymeropoulou
Adversarial attacks and robustness in deep neural networks for sound event detection Ilias Alexandropoulos
Federated learning for recommender systems George Karagounis
Creation of a chatbot using language models and deep learning for customer question answering Nikolaos Tzanis
Multi-agent reinforcement learning with diffusion models Aris Tsilifonis
Correct significant wave height forecasts in the MedSea using U-Nets and satellite measurements Pavlos Patsonis
Domain adaptation in data scarce scenarios using Time Series Foundational Models Alexandros Liapatis
Sustainability-Guided Small Molecule Generation with Generative Flow Networks Ioannis Savvas
Pose-Based Deep Learning Approaches for Recognizing Isolated Signs in Greek Sign Language Konstantinos Skourogiannis
6D object pose estimation: literature review and model-free mask generation pipeline Orestis Vaggelis
Ranking joint policies in dynamic games using evolutionary dynamics Natalia Koliou
Explainable deep reinforcement learning via online mimicking Nikolaos Makris
Pages
1
2
3
4
next ›
last »
Follow us on social media
Contact us
Secretariat Elpida Vlaikidi
Phone (+30) 210 650 3480
Email ai@iit.demokritos.gr(link sends e-mail) 
Operating Regulation
© MSc in Artificial Intelligence  
© National Centre for Scientific Research "Demokritos" for the Institute of Informatics & Telecommunications and University of Piraeus for the Department of Digital Systems 2023. The contents of this website may be freely reproduced for non-commercial purposes.