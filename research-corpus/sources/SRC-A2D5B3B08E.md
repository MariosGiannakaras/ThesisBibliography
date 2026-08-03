> Source: https://unity-technologies.github.io/ml-agents/

Unity ML-Agents Toolkit
⚠ DEPRECATED: This documentation has moved to Unity Package Documentation - Click here to view the latest documentation [-] [-]
Skip to content
Unity ML-Agents Toolkit
⚠ DOCUMENTATION MOVED [-] [-] [-] [-]
Initializing search
[GitHub
19.6k
4.5k](https://github.com/Unity-Technologies/ml-agents)
Unity ML-Agents Toolkit
[GitHub
19.6k
4.5k](https://github.com/Unity-Technologies/ml-agents)
[-] ⚠ DOCUMENTATION MOVED
ML-Agents Overview
Installation
Toolkit Documentation [-] Background Background
Machine Learning
PyTorch
Unity
ELO [-] Interfacing with Unity Builds Interfacing with Unity Builds
Getting started with the Gym API
Getting started with the PettingZoo API
Getting started with the LLAPI [-] Python API Docs Python API Docs
Gym API Documentation
Petting Zoo Documentation
LLAPI Documentation
On/Off Policy Trainer [-] Tutorials Tutorials
Customizing Training via Plugins
Custom Trainer Plugin
HuggingFace [-] About About
FAQs
Limitations
Migrating
Versioning
⚠ Documentation Moved ⚠
This documentation is deprecated and no longer maintained. Visit the Unity Package Documentation for the latest ML-Agents documentation. This site remains for legacy reference only. 
Unity ML-Agents Toolkit
( latest release) ( all releases)
The Unity Machine Learning Agents Toolkit (ML-Agents) is an open-source project that enables games and simulations to serve as environments for training intelligent agents. We provide implementations (based on PyTorch) of state-of-the-art algorithms to enable game developers and hobbyists to easily train intelligent agents for 2D, 3D and VR/AR games. Researchers can also use the provided simple-to-use Python API to train Agents using reinforcement learning, imitation learning, neuroevolution, or any other methods. These trained agents can be used for multiple purposes, including controlling NPC behavior (in a variety of settings such as multi-agent and adversarial), automated testing of game builds and evaluating different game design decisions pre-release. The ML-Agents Toolkit is mutually beneficial for both game developers and AI researchers as it provides a central platform where advances in AI can be evaluated on Unity's rich environments and then made accessible to the wider research and game developer communities.
Features
17+ example Unity environments
Support for multiple environment configurations and training scenarios
Flexible Unity SDK that can be integrated into your game or custom Unity scene
Support for training single-agent, multi-agent cooperative, and multi-agent competitive scenarios via several Deep Reinforcement Learning algorithms (PPO, SAC, MA-POCA, self-play).
Support for learning from demonstrations through two Imitation Learning algorithms (BC and GAIL).
Quickly and easily add your own custom training algorithm and/or components.
Easily definable Curriculum Learning scenarios for complex tasks
Train robust agents using environment randomization
Flexible agent control with On Demand Decision Making
Train using multiple concurrent Unity environment instances
Utilizes the Inference Engine to provide native cross-platform support
Unity environment control from Python
Wrap Unity learning environments as a gym environment
Wrap Unity learning environments as a PettingZoo environment
See our ML-Agents Overview page for detailed descriptions of all these features. Or go straight to our web docs.
Releases & Documentation
Our latest, stable release is Release 22 . Click here to get started with the latest release of ML-Agents.
You can also check out our new web docs!
The table below lists all our releases, including our main branch which is under active development and may be unstable. A few helpful guidelines:
The Versioning page overviews how we manage our GitHub releases and the versioning process for each of the ML-Agents components.
The Releases page contains details of the changes between releases.
The Migration page contains details on how to upgrade from earlier releases of the ML-Agents Toolkit.
The Documentation links in the table below include installation and usage instructions specific to each release. Remember to always use the documentation that corresponds to the release version you're using.
The com.unity.ml-agents package is verified for Unity 2020.1 and later. Verified packages releases are numbered 1.0.x.
If you are a researcher interested in a discussion of Unity as an AI platform, see a pre-print of our reference paper on Unity and the ML-Agents Toolkit.
If you use Unity or the ML-Agents Toolkit to conduct research, we ask that you cite the following paper as a reference:
Additionally, if you use the MA-POCA trainer in your research, we ask that you cite the following paper as a reference:
Additional Resources
We have a Unity Learn course, ML-Agents: Hummingbirds, that provides a gentle introduction to Unity and the ML-Agents Toolkit.
We've also partnered with CodeMonkeyUnity to create a series of tutorial videos on how to implement and use the ML-Agents Toolkit.
We have also published a series of blog posts that are relevant for ML-Agents:
(July 12, 2021) ML-Agents plays Dodgeball
(May 5, 2021) ML-Agents v2.0 release: Now supports training complex cooperative behaviors
(December 28, 2020) Happy holidays from the Unity ML-Agents team!
(November 20, 2020) How Eidos-Montréal created Grid Sensors to improve observations for training agents
(November 11, 2020) 2020 AI@Unity interns shoutout
(May 12, 2020) Announcing ML-Agents Unity Package v1.0!
(February 28, 2020) Training intelligent adversaries using self-play with ML-Agents
(November 11, 2019) Training your agents 7 times faster with ML-Agents
(October 21, 2019) The AI@Unity interns help shape the world
(April 15, 2019) Unity ML-Agents Toolkit v0.8: Faster training on real games
(March 1, 2019) Unity ML-Agents Toolkit v0.7: A leap towards cross-platform inference
(December 17, 2018) ML-Agents Toolkit v0.6: Improved usability of Brains and Imitation Learning
(October 2, 2018) Puppo, The Corgi: Cuteness Overload with the Unity ML-Agents Toolkit
(September 11, 2018) ML-Agents Toolkit v0.5, new resources for AI researchers available now
(June 26, 2018) Solving sparse-reward tasks with Curiosity
(June 19, 2018) Unity ML-Agents Toolkit v0.4 and Udacity Deep Reinforcement Learning Nanodegree
(May 24, 2018) Imitation Learning in Unity: The Workflow
(March 15, 2018) ML-Agents Toolkit v0.3 Beta released: Imitation Learning, feedback-driven features, and more
(December 11, 2017) Using Machine Learning Agents in a real game: a beginner's guide
(December 8, 2017) Introducing ML-Agents Toolkit v0.2: Curriculum Learning, new environments, and more
(September 19, 2017) Introducing: Unity Machine Learning Agents Toolkit
Overviewing reinforcement learning concepts ( multi-armed bandit and Q-learning)
More from Unity
Unity Inference Engine
Introducing Unity Muse and Sentis
Community and Feedback
The ML-Agents Toolkit is an open-source project and we encourage and welcome contributions. If you wish to contribute, be sure to review our contribution guidelines and code of conduct.
For problems with the installation and setup of the ML-Agents Toolkit, or discussions about how to best setup or train your agents, please create a new thread on the Unity ML-Agents forum and make sure to include as much detail as possible. If you run into any other problems using the ML-Agents Toolkit or have a specific feature request, please submit a GitHub issue.
Please tell us which samples you would like to see shipped with the ML-Agents Unity package by replying to this forum thread.
Your opinion matters a great deal to us. Only by hearing your thoughts on the Unity ML-Agents Toolkit can we continue to improve and grow. Please take a few minutes to let us know about it.
For any other questions or feedback, connect directly with the ML-Agents team at ml-agents@unity3d.com.
Privacy
In order to improve the developer experience for Unity ML-Agents Toolkit, we have added in-editor analytics. Please refer to "Information that is passively collected by Unity" in the Unity Privacy Policy.
com.unity.ml-agents copyright © 2017 - 2022 Unity Technologies
Made with Material for MkDocs