> Source: https://arxiv.org/pdf/2110.11334

Noname manuscript No. (will be inserted by the editor) 
Generalized Out-of-Distribution Detection: A Survey 
Jingkang Yang · Kaiyang Zhou · Yixuan Li · Ziwei Liu 
Received: date / Accepted: date 
Abstract Out-of-distribution (OOD) detection is crit-
ical to ensuring the reliability and safety of machine 
learning systems. For instance, in autonomous driving, 
we would like the driving system to issue an alert and 
hand over the control to humans when it detects un-
usual scenes or objects that it has never seen during 
training time and cannot make a safe decision. The 
term, OOD detection, first emerged in 2017 and since 
then has received increasing attention from the research 
community, leading to a plethora of methods devel-
oped, ranging from classification-based to density-based 
to distance-based ones. Meanwhile, several other prob-
lems, including anomaly detection (AD), novelty de-
tection (ND), open set recognition (OSR), and outlier 
detection (OD), are closely related to OOD detection 
in terms of motivation and methodology. Despite common goals, these topics develop in isolation, and their 
subtle differences in definition and problem setting of-
ten confuse readers and practitioners. In this survey, 
we first present a unified framework called generalized 
OOD detection, which encompasses the five aforemen-
tioned problems, i.e., AD, ND, OSR, OOD detection, 
and OD. Under our framework, these five problems can 
Jingkang Yang S-Lab, Nanyang Technological University, Singapore E-mail: jingkang001@ntu.edu.sg 
Kaiyang Zhou S-Lab, Nanyang Technological University, Singapore E-mail: kaiyang.zhou@ntu.edu.sg 
Yixuan Li Department of Computer Sciences, University of Wisconsin-Madison, Madison, WI, United States E-mail: sharonli@cs.wisc.edu 
Ziwei Liu S-Lab, Nanyang Technological University, Singapore E-mail: ziwei.liu@ntu.edu.sg 
be seen as special cases or sub-tasks, and are easier to 
distinguish. Despite comprehensive surveys of related 
fields, the summarization of OOD detection methods 
remains incomplete and requires further advancement. 
This paper specifically addresses the gap in recent tech-
nical developments in the field of OOD detection. It also 
provides a comprehensive discussion of representative 
methods from other sub-tasks and how they relate to 
and inspire the development of OOD detection meth-
ods. The survey concludes by identifying open chal-
lenges and potential research directions. 
1 Introduction 
A trustworthy visual recognition system should not only produce accurate predictions on known context, 
but also detect unknown examples and reject them 
(or hand them over to human users for safe han-
dling) [1, 2, 3, 4]. For instance, a well-trained food clas-
sifier should be able to detect non-food images such as 
selfies uploaded by users, and reject such input instead 
of blindly classifying them into existing food categories. 
In safety-critical applications such as autonomous driv-
ing, the driving system must issue a warning and hand 
over the control to drivers when it detects unusual 
scenes or objects it has never seen during training. 
Most existing machine learning models are trained 
based on the closed-world assumption [5, 6], where 
the test data is assumed to be drawn i.i.d. from the 
same distribution as the training data, known as in-
distribution (ID). However, when models are deployed 
in an open-world scenario [7], test samples can be out-
of-distribution (OOD) and therefore should be handled 
with caution. The distributional shifts can be caused by 
semantic shift (e.g ., OOD samples are drawn from dif-
 
 
 
 
 
 
 
 
 
 
2 Jingkang Yang et al. 
Anomaly Detection 
Sensory Anomaly Detection 
Semantic Anomaly Detection 
Novelty Detection 
One-Class Novelty 
Detection 
Multi-Class Novelty 
Detection 
Open Set Recognition 
Out-of-Distribution Detection 
Covariate Shift Detection Semantic Shift Detection 
Outlier Detection 
Single/Multi-Class Multi-Class 
 
 
 
 
 
 
Single-Class ID  C 
lassification N ot Required 
Required* N 
o 
*Exception: In OOD Detection, density-based methods do not require ID classification 
Fig. 1 Taxonomy of generalized OOD detection framework, illustrated by classification tasks. Four bases are used for the task taxonomy: 1) Distribution shift to detect: the task focuses on detecting covariate shift or semantic shift; 2) ID data type: the ID data contains one single class or multiple classes; 3) Whether the task requires ID classification; 4) Transductive learning task requires all observations; inductive tasks follow the train-test scheme. Note that ND is often interchangeable with AD, but ND is more concerned with semantic anomalies. OOD detection is generally interchangeable with OSR for classification tasks. 
ferent classes) [8], or covariate shift (e.g ., OOD samples 
from a different domain) [9, 10, 11]. 
The detection of semantic distribution shift (e.g ., 
due to the occurrence of new classes) is the focal point 
of OOD detection tasks, where the label space Y can 
be different between ID and OOD data and hence 
the model should not make any prediction. In addi-
tion to OOD detection, several problems adopt the 
“open-world” assumption and have a similar goal of 
identifying OOD examples. These include outlier detec-
tion (OD) [12, 13, 14, 15], anomaly detection (AD) [16, 
17, 18, 19], novelty detection (ND) [20, 21, 22, 23], 
and open set recognition (OSR) [24, 25, 26]. While 
all these problems are related to each other by shar-
ing similar motivations, subtle differences exist among 
the sub-topics in terms of the specific definition. How-
ever, the lack of a comprehensive understanding of the 
relationship between the different sub-topics leads to 
confusion for both researchers and practitioners. Even 
worse, these sub-topics, which are supposed to be com-
pared and learned from each other, are developing in 
isolation. 
In this survey, we for the first time clarify the sim-
ilarities and differences between these problems, and 
present a unified framework termed generalized OOD 
detection. Under this framework, the five problems (i.e., 
AD, ND, OSR, OOD detection, and OD) can be viewed 
as special cases or sub-topics. While other sub-topics 
have been extensively surveyed, the summarization of 
OOD detection methods is still inadequate and requires 
further exploration. This paper fills this gap by fo-
cusing specifically on recent technical developments in 
OOD detection, analyzing fair experimental compar-
isons among classical methods on common benchmarks. 
Our survey concludes by highlighting open challenges 
and outlining potential avenues for future research. 
We further conduct a literature review for each sub-
topic, with a special focus on the OOD detection task. 
To sum up, we make three contributions to the research 
community: 
1. A Unified Framework: For the first time, we sys-
tematically review five closely related topics of AD, 
ND, OSR, OOD detection, and OD, and present 
a unified framework of generalized OOD detection. 
Under this framework, the similarities and differ-
ences of the five sub-topics can be systematically 
compared and analyzed. We hope our unification 
helps the community better understand these prob-
lems and correctly position their research in the lit-
erature. 
2. A Comprehensive Survey for OOD Detec-
tion: Noticing the existence of comprehensive sur-
veys on AD, ND, OSR, and OD methodologies in re-
cent years [16, 17, 18, 19, 25], this survey provides a 
comprehensive overview of OOD detection methods 
and thus complements existing surveys. By connect-
ing with methodologies of other sub-topics that are 
also briefly reviewed, as well as sharing the insights 
from a fair comparison on a standard benchmark, 
we hope to provide readers with a more holistic un-
derstanding of the developments for each problem 
and their interconnections, especially for OOD de-
tection. 
3. Future Research Directions: We draw readers’ 
attention to some problems or limitations that re-
main in the current generalized OOD detection field. 
We conclude this survey with discussions on open 
challenges and opportunities for future research. 
2 Generalized OOD Detection 
Framework Overview In this section, we introduce 
a unified framework termed generalized OOD detection, 
which encapsulates five related sub-topics: anomaly de-
tection (AD), novelty detection (ND), open set recogni-
tion (OSR), out-of-distribution (OOD) detection, and 
outlier detection (OD). These sub-topics can be similar 
in the sense that they all define a certain in-distribution, 
with the common goal of detecting out-of-distribution 
samples under the open-world assumption. However, 
subtle differences exist among the sub-topics in terms
Generalized Out-of-Distribution Detection: A Survey 3 
(b) One-Class Novelty Detection 
Train 
Test 
(c) Multi-Class Novelty Detection 
Test 
(d) Open Set Recognition & Out-of-Distribution Detection* (e) Outlier Detection 
All Observations are provided 
dog 
Train 
dog cat fish 
Train 
dog cat fish 
(a) Sensory Anomaly Detection 
Train 
Test 
dog Test 
Generalized Out-of-Distribution Detection 
ID fish 
OOD OOD 
ID ID 
ID 
ID ID 
ID OOD 
OOD 
ID ID 
ID 
ID dog 
ID cat 
Anomaly Detection 
Semantic Anomaly Detection / Novelty Detection 
OOD Detection is generally the same as OSR in classification task, but OOD Detection encompasses a broader spectrum of learning tasks and solution space (ref. Section 2.6) 
* 
Fig. 2 Illustration of sub-tasks under generalized OOD detection framework with vision tasks. Tags on test images refer to model’s expected predictions. (a) In sensory anomaly detection, test images with covariate shift will be considered as OOD. No semantic shift occurs in this setting. (b) In one-class novelty detection, normal/ID images belong to one class. Test images with semantic shift will be considered as OOD. (c) In multi-class novelty detection, ID images belong to multiple classes. Test images with semantic shift will be considered as OOD. Note that (b) and (c) compose novelty detection, which is identical to the topic of semantic anomaly detection. (d) Open set recognition is identical to multi-class novelty detection in the task of detection, with the only difference that open set recognition further requires ID classification. Out-of-distribution detection solves the same problem as open-set recognition. It canonically aims to detect test samples with semantic shift without losing the ID classification accuracy. However, OOD Detection encompasses a broader spectrum of learning tasks and solution space. (e) Outlier detection does not follow a train-test scheme. All observations are provided. It fits in the generalized OOD detection framework by defining the majority distribution as ID. Outliers can have any distribution shift from the majority. 
of the specific definition and properties of ID and OOD 
data—which are often overlooked by the research com-
munity. To this end, we provide a clear introduction 
and description of each sub-topic in respective subsec-
tions (from Section 2.1 to 2.5). Each subsection details 
the motivation, background, formal definition, as well 
as relative position within the unified framework. Ap-
plications and benchmarks are also introduced, with 
concrete examples that facilitate understanding. Fig. 4 
illustrates the settings for each sub-topic. In the end, 
we conclude this section by introducing the neighbor-
hood topics to clarify the scope of the generalized OOD 
detection framework. (Section 2.6). 
Preliminary: Distribution Shift In our frame-
work, we recognize the complexity and interconnect-
edness of distribution shifts, which are central to un-
derstanding various OOD scenarios. Distribution shifts 
can be broadly categorized into covariate shift and se-
mantic (label) shift, but it’s important to clarify their 
interdependence. Firstly, let’s define the input space as 
X (sensory observations) and the label space as Y (se-
mantic categories). The data distribution is represented 
by the joint distribution P (X,Y ) over the space X ×Y. 
Distribution shift can occur in either the marginal dis-
tribution P (X), or both P (Y ) and P (X). Note that 
shift in P (Y ) naturally triggers shift in P (X). 
Covariate Shift: This occurs when there is a change 
in the marginal distribution P (X), affecting the input 
space, while the label space Y remains constant. Ex-
amples of covariate distribution shift on P (X) include 
adversarial examples [27, 28], domain shift [29], and 
style changes [30]. 
Semantic Shift: This involves changes in both P (Y ) 
and indirectly P (X). A shift in the label space P (Y ) 
implies the introduction of new categories or the alter-
ation of existing ones. This change naturally affects the 
input space P (X) since the nature of the data being 
observed or collected is now different. 
Remark: Given the interdependence between P (X) 
and P (Y ), it’s crucial to distinguish the intentions be-
hind different types of distribution shifts. We define Co-
variate Shift as scenarios where changes are intended 
in the input space (P (X)) without any deliberate al-
teration to the label space (P (Y )). On the other hand, 
Semantic Shift specifically aims to modify the semantic 
content, directly impacting the label space (P (Y )) and, 
consequently, the input space (P (X)). 
Importantly, we note that covariate shift is more 
commonly used to evaluate model generalization and 
robustness performance, where the label space Y re-
mains the same during test time. On the other hand, 
the detection of semantic distribution shift (e.g ., due to 
the occurrence of new classes) is the focal point of many 
detection tasks considered in this framework, where the 
label space Y can be different between ID and OOD 
data and hence the model should not make any predic-
tion. 
With the concept of distribution shift in mind, read-
ers can get a general idea of the differences and con-
nections among sub-topics/tasks in Fig. 1. Notice that
4 Jingkang Yang et al. 
different sub-tasks can be easily identified with the 
following four dichotomies: 1) covariate/semantic shift 
dichotomy; 2) single/multiple class dichotomy; 3) ID 
classification needed/non-needed dichotomy; 4) induc-
tive/transductive dichotomy. Next, we proceed with 
elaborating on each sub-topic. 
2.1 Anomaly Detection 
Background The notion of “anomaly” stands in 
contrast with the “normal” defined in advance. The 
concept of “normal” should be clear and reflect the real 
task. For example, to create a “not-hotdog detector”, 
the concept of the normal should be clearly defined as 
the hotdog class, i.e., a food category, so that objects 
that violate this definition are identified as anomalies, 
which include steaks, rice, and non-food objects like 
cats and dogs. Ideally, “hotdog” would be regarded as 
a homogeneous concept, regardless of the sub-classes of 
French or American hotdog. 
Current anomaly detection settings often restrict 
the environment of interest to some specific scenarios. 
For example, the “not-hotdog detector” only focuses on 
realistic images, assuming the nonexistence of images 
from other domains such as sketches. Another realistic 
example is industrial defect detection, which is based 
on only one set of assembly lines for a specific product. 
In other words, the “open-world” assumption is usually 
not completely “open”. Nevertheless, “not-hotdog” or 
“defects” can form a large unknown space that breaks 
the “closed-world” assumption. 
In summary, the key to anomaly detection is to de-
fine normal clearly (usually without sub-classes) and 
detect all possible anomalous samples under some spe-
cific scenarios. 
Definition Anomaly detection (AD) [31] aims to 
detect any anomalous samples that deviate from the 
predefined normality during testing. The deviation can 
happen due to either covariate shift or semantic shift, 
which leads to two sub-tasks: sensory AD and semantic 
AD, respectively [16]. 
Sensory AD detects test samples with covariate 
shift, under the assumption that normalities come from 
the same covariate distribution. No semantic shift takes 
place in sensory AD settings. On the other hand, se-
mantic AD detects test samples with label shift, as-
suming that normalities come from the same semantic 
distribution (category), i.e., normalities should belong 
to only one class. 
Formally, in sensory AD, normalities are from in-
distribution P (X) while anomalies encountered at test 
time are from out-of-distribution P ′(X), where P (X) ̸= 
P ′(X) — only covariate shift occurs. The goal in sen-
sory AD is to detect samples from P ′(X). No semantic 
shift occurs in this setting, i.e., P (Y ) = P ′(Y ). Con-
versely, for semantic AD, only semantic shift occurs 
(i.e., P (Y ) ̸= P ′(Y )) and the goal is to detect sam-
ples that belong to novel classes. 
Remark: Sensory/Semantic Dichotomy Our 
sensory/semantic dichotomy for the AD sub-task defi-
nition comes from the low-level sensory anomalies and 
high-level semantic anomalies that are introduced in 
[32] and highlighted in the recent AD survey [16], to 
reflect the rise of deep learning. Note that although 
most sensory and semantic AD methods are shown 
to be mutually inclusive due to the common shift on 
P (X), some approaches are specialized in one of the 
sub-tasks (ref. Section 4.2). Recent research communi-
ties are also trending on subdividing types of anomalies 
to develop targeted methods, so that practitioners can 
select the optimal solution for their own practical prob-
lem [32, 33]. 
Position in Framework Under the generalized 
OOD detection framework, the definition of “nor-
mality” seamlessly connects to the notion of “in-
distribution”, and “anomaly” corresponds to “out-of-
distribution”. Importantly, AD treats ID samples as a 
whole, which means that regardless of the number of 
classes (or statistical modalities) in ID data, AD does 
not require differentiation in the ID samples. This fea-
ture is an important distinction between AD and other 
sub-topics such as OSR and OOD detection. 
Application and Benchmark Sensory AD only fo-
cuses on objects with the same or similar semantics, 
and identifies the observational differences on their surface. Samples with sensory differences are recognized as 
sensory anomalies. Example applications include adver-
sarial defense [34], forgery recognition of biometrics and 
artworks [35, 36, 37, 38], image forensics [39, 40, 41], in-
dustrial inspection [42, 43, 44], etc. The most popular 
academic AD benchmark is MVTec-AD [42] for indus-
trial inspection. 
In contrast to sensory AD, semantic AD only fo-
cuses on the semantic shift. An example of real-world 
applications is crime surveillance [45, 46]. Active im-
age crawlers for a specific category also need semantic 
AD methods to ensure the purity of the collected im-
ages [47]. An example of the academic benchmarks is 
to recursively use one class from MNIST as ID during 
training, and ask the model to distinguish it from the 
rest of the 9 classes during testing. 
Evaluation In the AD benchmarks, test samples 
are annotated to be either normal or abnormal. The 
deployed anomaly detector will produce a confidence
Generalized Out-of-Distribution Detection: A Survey 5 
score for a test sample, indicating how confident the 
model considers the sample as normality. Samples be-
low the predefined confidence threshold are considered 
abnormal. By viewing the anomalies as positive and 
true normalities as negative1, different thresholds will 
produce a series of true positive rates (TPR) and false-
positive rates (FPR)—from which we can calculate the 
area under the receiver operating characteristic curve 
(AUROC) [49]. Similarly, the precision and recall val-
ues can be used to compute metrics of F-scores and the 
area under the precision-recall curve (AUPR) [50]. Note 
that there can be two variants of AUPR values: one 
treating “normal” as the positive class, and the other 
treating “abnormal” as the positive class. For AUROC 
and AUPR, a higher value indicates better detection 
performance. 
Remark: Alternative Taxonomy on Anomalies 
Some previous literature considers anomalies types 
to be three-fold: point anomalies, conditional or con-
textural anomalies, and group or collective anoma-
lies [16, 17, 19]. In this survey, we mainly focus on point 
anomalies detection for its popularity in practical ap-
plications and its adequacy to elucidate the similarities 
and differences between sub-tasks. Details of the other 
two kinds of anomalies, i.e., contextural anomalies that 
often occur in time-series tasks, and collective anoma-
lies that are common in the data mining field, are not 
covered in this survey. We recommend readers to the 
recent AD survey papers [16] for an in-depth discussion 
on them. 
Remark: Taxonomy based on Supervision We 
use sensory/semantic dichotomy to subdivide AD at the 
task level. From the perspective of methodologies, some 
literature categorizes AD techniques into unsupervised 
and (semi-) supervised settings. Note that these two 
taxonomies are orthogonal as they focus on tasks and 
methods respectively. 
2.2 Novelty Detection 
Background The word “novel” generally refers to 
the unknown, new, and something interesting. While 
novelty detection (ND) is often interchangeable with 
AD in the community, strictly speaking, their subtle 
difference is worth noticing. In terms of motivation, 
novelty detection usually does not perceive “novel” 
test samples as erroneous, fraudulent, or malicious as 
AD does, but cherishes them as learning resources 
for potential future use with a positive learning atti-
tude [16, 17]. In fact, novelty detection is also known 
1 Align with MSP [48]. Check this issue in OpenOOD 
as “novel class detection” [22, 23], indicating that it is 
primarily focusing on detecting semantic shift. 
Definition Novelty detection aims to detect any test 
samples that do not fall into any training category. The 
detected novel samples are usually prepared for future 
constructive procedures, such as more specialized anal-
ysis, or incremental learning of the model itself. Based 
on the number of training classes, ND contains two 
different settings: 1) one-class novelty detection (one-
class ND): only one class exists in the training set; 2) 
multi-class novelty detection (multi-class ND): multiple 
classes exist in the training set. It is worth noting that 
despite having many ID classes, the goal of multi-class 
ND is only to distinguish novel samples from ID. Both 
one-class and multi-class ND are formulated as binary 
classification problems. 
Position in Framework Under the generalized 
OOD detection framework, ND deals with the setting 
where OOD samples have semantic shift, without the 
need for classification in the ID set even if possible. 
Therefore, ND shares the same problem definition with 
semantic AD. 
Application and Benchmark Real-world ND ap-
plication includes video surveillance [45, 46], planetary 
exploration [51] and incremental learning [52, 53]. For 
one-class ND, an example academic benchmark can be 
identical to that of semantic AD, which considers one 
class from MNIST as ID and the rest as the novel. The 
corresponding MNIST benchmark for multi-class ND 
may use the first 6 classes during training, and test on 
the remaining 4 classes as OOD. 
Evaluation The evaluation of ND is identical to AD, 
which is based on AUROC, AUPR, or F-scores (see 
details in Section 2.1). 
Remark: One-Class/Multi-Class Dichotomy 
Although the ND models do not require the ID 
classification even with multi-class annotations, the 
method on multi-class ND can be different from 
one-class ND, as multi-class ND can make use of 
the multi-class classifier while one-class ND cannot. 
Also note that semantic AD can be further split into 
one-class semantic AD and multi-class semantic AD 
that matches ND, as semantic AD is equivalent to ND. 
Remark: Nuance between AD and ND Apart 
from the special interest in semantics, some litera-
ture [54, 55] also point out that ND is supposed to 
be fully unsupervised (no novel data in training), while 
AD might have some abnormal training samples. It’s 
important to note that neither AD nor ND necessitates 
the classification of ID data. This is a key distinction 
between OSR and OOD detection, which we will discuss 
in subsequent sections.
6 Jingkang Yang et al. 
2.3 Open Set Recognition 
Background Machine learning models trained in the 
closed-world setting can incorrectly classify test sam-
ples from unknown classes as one of the known cate-
gories with high confidence [56]. Some literature refers 
to this notorious overconfident behavior of the model as 
“arrogance”, or “agnostophobia” [57]. Open set recog-
nition (OSR) is proposed to address this problem, with 
their own terminology of “known known classes” to rep-
resent the categories that exist at training, and “un-
known unknown classes” for test categories that do not 
fall into any training category. Some other terms, such 
as open category detection [58] and open set learn-
ing [59], are simply different expressions for OSR. 
Definition Open set recognition requires the multi-
class classifier to simultaneously: 1) accurately classify 
test samples from “known known classes”, and 2) detect 
test samples from “unknown unknown classes”. 
Position in Framework OSR well aligns with our 
generalized OOD detection framework, where “known 
known classes” and “unknown unknown classes” cor-
respond to ID and OOD respectively. Formally, OSR 
deals with the case where OOD samples during testing 
have semantic shift, i.e., P (Y ) ̸= P ′(Y ). The goal of 
OSR is largely shared with that of multi-class ND—the 
only difference is that OSR additionally requires accu-
rate classification of ID samples from P (Y ). 
Application and Benchmark OSR supports the 
robust deployment of real-world image classifiers in gen-
eral, which can reject unknown samples in the open 
world [60, 61]. An example academic benchmark on 
MNIST can be identical to multi-class ND, which con-
siders the first 6 classes as ID and the remaining 4 
classes as OOD. In addition, OSR further requires a 
good classifier on the 6 ID classes. 
Evaluation Similar to AD and ND, the metrics for 
OSR include F-scores, AUROC, and AUPR. Beyond 
them, the classification performance is also evaluated 
by standard ID accuracy. While the above metrics eval-
uate the novelty detection and ID classification capabil-
ities independently, some works raise some evaluation 
criteria for joint evaluation, such as CCR@FPRx [57], 
which calculates the class-wise recall when a certain 
FPR equal to x (e.g ., 10−1) is achieved. 
2.4 Out-of-Distribution Detection 
Background With the observation that deep learn-
ing models are often inappropriate but in fact over-
confident in classifying samples from different semantic 
distributions in the image classification task and text 
categorization [48], the field of out-of-distribution de-
tection emerges, requiring the model to reject inputs 
that are semantically different from the training dis-
tribution and therefore should not be predicted by the 
model. 
Definition Out-of-distribution detection, or OOD 
detection, aims to detect test samples drawn from a 
distribution that is different from the training distri-
bution, with the definition of distribution to be well-
defined according to the application in the target. For 
most machine learning tasks, the distribution should re-
fer to “label distribution”, which means that OOD sam-
ples should not have overlapping labels w.r.t. training 
data. Formally, in the OOD detection, the test samples 
come from a distribution whose semantics are shifted 
from ID, i.e., P (Y ) ̸= P ′(Y ). Note that the training 
set usually contains multiple classes, and OOD detec-
tion should NOT harm the ID classification capability. 
Position in Framework Out-of-distribution detec-
tion can be canonical to OSR in common machine 
learning tasks like multi-class classification—keeping 
the classification performance on test samples from ID 
class space Y, and reject OOD test samples with se-
mantics outside the support of Y. Also, the multi-class 
setting and the requirement of ID classification distin-
guish the task from AD and ND. 
Application and Benchmark The application of 
OOD detection usually falls into safety-critical situa-
tions, such as autonomous driving [62, 63]. An example 
academic benchmark is to use CIFAR-10 as ID during 
training and to distinguish CIFAR images from other 
datasets such as SVHN, etc. Researchers should pay 
attention that OOD datasets should NOT have label 
overlapping with ID datasets when building the bench-
mark. 
Evaluation Apart from F-scores, AUROC, and 
AUPR, another commonly-used metric is FPR@TPRx, 
which measures the FPR when the TPR is x (e.g ., 
0.95). Some works also use an alternative metric, 
TNR@TPRx, which is equivalent to 1-FPR@TPRx. 
OOD detection also concerns the performance of ID 
classification. 
Remark: OSR vs OOD Detection The difference 
between OSR and OOD detection tasks is three-fold. 
1) Different benchmark setup: OSR benchmarks 
usually split one multi-class classification dataset into 
ID and OOD parts according to classes, while OOD 
detection takes one dataset as ID and finds several other 
datasets as OOD with the guarantee of non-overlapping 
categories between ID/OOD datasets. However, despite 
the different benchmark traditions of the two sub-tasks,
Generalized Out-of-Distribution Detection: A Survey 7 
they are in fact tackling the same problem of semantic 
shift detection. 
2) No additional data in OSR: Due to the require-
ment of theoretical open-risk bound guarantee, OSR 
discourages the usage of additional data during train-
ing by design [24]. This restriction precludes methods 
that are more focused on effective performance im-
provements (e.g ., outlier exposures [64, 65]) but may 
violate OSR constraints. 
3) Broadness of OOD detection: Compare to 
OSR, OOD detection encompasses a broader spectrum 
of learning tasks (e.g ., multi-label classification [66]), 
wider solution space (to be discussed in Section 3). 
Remark: Mainstream OOD Detection Focuses 
on Semantics While most works in the current com-
munity interpret the keyword “out-of-distribution” as 
“out-of-label/semantic-distribution”, some OOD detec-
tion works also consider detecting covariate shifts [67], 
which claim that covariate shift usually leads to a sig-
nificant drop in model performance and therefore needs 
to be identified and rejected. However, although detect-
ing covariate shift is reasonable on some specific tasks 
(usually due to high-risk or privacy reasons) that are 
to be discussed in the following paragraph, research on 
this topic remains a controversial task w.r.t OOD gen-
eralization tasks (c.f . Section 2.6 and Section 6.2). De-
tecting semantic shift has been the mainstream of OOD 
detection tasks. 
Remark: To Generalize, or To Detect? We pro-
vide another definition from the perspective of gener-
alization: Out-of-distribution detection, or OOD detec-
tion, aims to detect test samples to which the model 
cannot or does not want to generalize [68]. In most of the machine learning tasks, such as image classification, 
the models are expected to generalize their prediction 
capability to samples with covariate shift, and they are 
only unable to generalize when semantic shift occurs. 
However, for applications where models are by-design 
nontransferable to other domain, such as many deep re-
inforcement learning tasks like game AI [69, 70], the key 
term “distribution” should refer to “data/input distri-
bution”, so that the model should refuse to decide the 
environment that is not the same as the training envi-
ronment, i.e., P (X) ̸= P ′(X). Similar applications are 
those high-risk tasks such as medical image classifica-
tion [71] or in privacy-sensitive scenario [72], where the 
models are expected to be very conservative and only 
make predictions for samples exactly from the training 
distribution, rejecting any samples that deviate from it. 
Recent studies [73] also highlight a model-specific view: 
a robust model should generalize to examples with co-
variate shift; a weak model should reject them. Ulti-
mately, an OOD detection task is considered valid when 
it successfully balances the aspects of “detection” and 
“generalization”, taking into account factors such as 
meaningfulness and the inherent challenges presented 
by the task. Nonetheless, detecting semantic shift re-
mains the primary focus of OOD detection tasks and is 
central to this survey. 
2.5 Outlier Detection 
Background According to Wikipedia [74], an outlier 
is a data point that differs significantly from other ob-
servations. Recall that the problem settings in AD, ND, 
OSR, and OOD detect unseen test samples that are 
different from the training data distribution. In con-
trast, outlier detection directly processes all observa-
tions and aims to select outliers from the contaminated 
dataset [12, 13, 14]. Since outlier detection does not 
follow the train-test procedure but has access to all 
observations, approaches to this problem are usually 
transductive rather than inductive [75]. 
Definition Outlier detection aims to detect sam-
ples that are markedly different from the others in the 
given observation set, due to either covariate or seman-
tic shift. 
Position in Framework Different from all previous 
sub-tasks, whose in-distribution is defined during train-
ing, the “in-distribution” for outlier detection refers to 
the majority of the observations. Outliers may exist due 
to semantic shift on P (Y ), or covariate shift on P (X). 
Application and Benchmark While mostly ap-
plied in data mining tasks [76, 77, 78], outlier detec-
tion is also used in real-world computer vision applica-
tions such as video surveillance [79] and dataset clean-
ing [80, 81, 82]. For the application of dataset cleaning, 
outlier detection is usually used as a pre-processing step 
for the main tasks such as learning from open-set noisy 
labels [83], webly supervised learning [84], and open-set 
semi-supervised learning [85]. To construct an outlier 
detection benchmark on MNIST, one class should be 
chosen so that all samples that belong to this class are 
considered as inliers. A small fraction of samples from 
other classes are introduced as outliers to be detected. 
Evaluation Apart from F-scores, AUROC, and 
AUPR, the evaluation of outlier detectors can be also 
evaluated by the performance of the main task it sup-
ports. For example, if an outlier detector is used to 
purify a dataset with noisy labels, the performance of 
a classifier that is trained on the cleaned dataset can 
indicate the quality of the outlier detector. 
Remark: On Inclusion of Outlier Detection In-
terestingly, the outlier detection task can be consid-
ered as an outlier in the generalized OOD detection
8 Jingkang Yang et al. 
framework, since outlier detectors are operated on the 
scenario when all observations are given, rather than 
following the training-test scheme. Also, publications 
exactly on this topic are rarely seen in the recent deep 
learning venues. However, we still include outlier de-
tection in our framework, because intuitively speaking, 
outliers also belong to one type of out-of-distribution, 
and introducing it can help familiarize readers more 
with various terms (e.g ., OD, AD, ND, OOD) that have 
confused the community for a long while. 
2.6 Related Topics 
Apart from the five sub-topics that are described in 
our generalized OOD detection framework (shown in 
Figure 1), we further briefly discuss five related topics 
below, which help clarify the scope of this survey. 
Learning with Rejection (LWR) LWR [86] can 
date back to early works on abstention [87, 88], which 
considered simple model families such as SVMs [89]. 
The phenomenon of neural networks’ overconfidence in 
OOD data is first revealed by [90]. Despite methodolo-
gies differences, subsequent works developed on OOD 
detection and OSR share the underlying spirit of clas-
sification with the rejection option. 
Domain Adaptation/Generalization Domain 
Adaptation (DA) [11] and Domain Generalization 
(DG) [91] also follow “open-world” assumption. Differ-
ent from generalized OOD detection settings, DA/DG 
expects the existence of covariate shift during test-
ing without any semantic shift and requires classi-
fiers to make accurate predictions into the same set of 
classes [92]. Noticing that OOD detection commonly 
concerns detecting the semantic shift, which is comple-
mentary to DA/DG. In the case when both covariate 
and semantic shift take place, the model should be able 
to detect semantic shift while being robust to covariate 
shift. More discussion on relations between DA/DG and 
OOD detection is in Section 6.2. The difference between 
DA and DG is that while the former requires extra but 
few training samples from the target domain, the latter 
does not. 
Novelty Discovery Novelty discovery [93, 94, 95, 
96, 97] requires all observations to be given in advance 
as outlier detection does. The observations are provided 
in a semi-supervised manner, and the goal is to explore 
and discover the new categories and classes in the unla-
beled set. Different from outlier detection where outliers 
are sparse, the unlabeled set in novelty discovery set-
ting can mostly consist of, and even be overwhelmed by 
unknown classes. 
Zero-shot Learning Zero-shot learning [98] has 
a similar goal of novelty discovery but follows the 
training-testing scheme. The test set is under the 
“open-world” assumption with unknown classes, which 
expects classifiers trained only on the known classes to 
perform classification on unknown testing samples with 
the help of extra information such as label relationships. 
Open-world Recognition Open-world recogni-
tion [99] aims to build a lifelong learning machine that 
can actively detect novel images [100], label them as 
new classes, and perform continuous learning. It can be 
viewed as a combination of novelty detection (or open-
set recognition) and incremental learning. More specif-
ically, open-world recognition extends the concept of 
OSR by adding the ability to incrementally learn new 
classes over time. In open-world scenarios, the system 
not only identifies unknown instances but also can up-
date its model to include these new classes as part of the 
known set. This approach is more dynamic and suited 
for real-world applications where the environment is not 
static, and new categories can emerge after the initial 
training phase [101]. 
Conformal Prediction Conformal prediction (CP) 
stands as a robust statistical framework in machine 
learning, primarily designed to provide confidence mea-
sures for predictions [102, 103]. Distinctively, it yields 
prediction intervals with specified confidence levels, 
transcending the limitations of mere point estimates. 
In scenarios of OOD detection, the conformal predic-
tion framework becomes particularly insightful: wider 
prediction intervals or lower confidence levels gener-
ated by conformal prediction methods can serve as in-
dicators of such OOD data. Although research at the 
intersection of CP and OOD detection is still emerg-
ing [104, 105, 106], the potential of applying the confor-
mal prediction framework in this domain is significant 
and warrants further exploration. 
2.7 Organization of Remaining Sections 
In this paper, we focus on the methodologies of OOD 
detection in Section 3, providing a comprehensive 
overview of the different approaches that have been 
proposed in the literature. We also briefly introduce 
methodologies for other sub-tasks including AD, ND, 
OSR, and OD in Section 4, to provide readers with a 
broader understanding of OOD-related problems and 
inspire the development of more effective methods. 
For each sub-task, we categorize and introduce the 
methodologies into four groups: 1) classification-
based methods: methods that largely rely on classi-
fiers; 2) density-based methods: detecting OOD by
Generalized Out-of-Distribution Detection: A Survey 9 
modeling data density; 3) distance-based methods: 
using distance metrics (usually in the feature space) to 
identify OODs; and 4) reconstruction-based meth-
ods: methods featured by reconstruction techniques. 
To offer readers further insights from an empirical per-
spective, we conduct a thorough analysis that provides 
a fair comparison between representative OOD detec-
tion methods and methods from other sub-tasks. Addi-
tionally, we highlight some of the remaining problems 
and limitations that exist in the current generalized 
OOD detection field. We conclude this survey with a 
discussion on the open challenges and opportunities for 
future research. It is worth noting that a concurrent 
survey [107] provides a detailed explanation of OOD-
related methods, which greatly complements our work. 
3 OOD Detection: Methodology 
In this section, we introduce the methodology for OOD 
detection. Initially, we explore classification-based mod-
els in Section 3.1. These models primarily utilize the 
model’s output, such as softmax scores, to identify 
OOD instances. We further examine outlier exposure-
based methods that leverage external data sources and 
other types of methods. The later section is followed by 
density-based methods in Section 3.2. Distance-based 
methods will be introduced in Sections 3.3. A brief dis-
cussion will be included at the end. 
3.1 Classification-based Methods 
Research on OOD detection originated from a simple 
baseline, that is, using the maximum softmax probabil-
ity as the indicator score of ID-ness [48]. Early OOD 
detection methods focus on deriving improved OOD 
scores based on the output of neural networks. 
3.1.1 Output-based Methods 
a. Post-hoc Detection Post-hoc methods have the 
advantage of being easy to use without modifying the 
training procedure and objective. The property can be 
important for the adoption of OOD detection meth-
ods in real-world production environments, where the 
overhead cost of retraining can be prohibitive. Early 
work ODIN [108] is a post-hoc method that uses tem-
perature scaling and input perturbation to amplify the 
ID/OOD separability. Key to the method, a sufficiently 
large temperature has a strong smoothing effect that 
transforms the softmax score back to the logit space— 
which effectively distinguishes ID vs. OOD. Note that 
this is different from confidence calibration, where a 
much milder T is employed. While calibration focuses 
on representing the true correctness likelihood of ID 
data only, the ODIN score is designed to maximize 
the gap between ID and OOD data and may no longer 
be meaningful from a predictive confidence standpoint. 
Built on the insights, recent work [110, 118] proposed 
using an energy score for OOD detection, which en-
joys theoretical interpretation from a likelihood per-
spective [220]. Test samples with lower energy are con-
sidered ID and vice versa. JointEnergy score [112] is 
then proposed to perform OOD detection for multi-
label classification networks. The most recent work 
SHE [113] uses stored patterns that represent classes to 
measure the discrepancy of unseen data for OOD de-
tection, which is hyperparameter-free and computation-
ally efficient compared to classic energy methods. Tech-
niques such as layer-wise Mahalanobis distance [109] 
and Gram Matrix [111] are implemented for better-
hidden feature quality to perform density estimation. 
Recently, one fundamental cause of the overconfi-
dence issue on OOD data has been revealed that us-
ing mismatched BatchNorm statistics—that are esti-
mated on ID data yet blindly applied to the OOD 
data in testing—can trigger abnormally high unit ac-
tivations and model output accordingly [114]. There-
fore, ReAct [114] proposes truncating the high activa-
tions, which establishes strong post-hoc detection per-
formance and further boosts the performance of exist-
ing scoring functions. Similarly, NMD [115] uses the 
activation means from BatchNorm layers for ID/OOD 
discrepancy. While ReAct considers activation space, 
[116] proposes a weight sparsification-based OOD de-
tection framework termed DICE. DICE ranks weights 
based on a measure of contribution and selectively uses 
the most salient weights to derive the output for OOD 
detection. By pruning away noisy signals, DICE prov-
ably reduces the output variance for OOD data, result-
ing in a sharper output distribution and stronger sepa-
rability from ID data. In a similar vein, ASH [120] also 
targets the activation space but adopts a different strat-
egy. It removes a significant portion (e.g., 90%) of an 
input’s feature representations from a late layer based 
on a top-K criterion, followed by adjusting the remain-
ing activations (e.g., 10%) either by scaling or assigning 
constant values, yielding surprisingly effective results. 
b. Training-based Methods With the training 
phase, confidence can be developed via designing a 
confidence-estimating branch [125] or class [126], en-
sembling with leaving-out strategy [127], adversarial 
training [128, 129, 130, 131, 132], stronger data aug-
mentation [133, 134, 135, 136, 137, 138], pretext train-
ing [139], better uncertainty modeling [140, 141], input-
level manipulation [108, 142], and utilizing feature
10 Jingkang Yang et al. 
2017 2018 202120202019 
Density-based Reconstruction-basedClassification-based Distance-based 
MSP MOSMDSODIN GRAM 
EBO 
GradNorm 
ReACT UDG 
[206] 
VOS 
CSI 
20232022 
ConfBranch 
STUD 
OE 
LLR 
MCD 
Watermarking 
DUQ 
G-ODIN 
LogitNorm 
KNN 
MLS 
DICEVIM SHE CIDER 
NPOS 
READ 
MOODKLM 
[48] 
[108] [109] 
[125] 
[64] [151] 
[203] 
[111] [67] 
[211] [139] [110] 
[172] [146] 
[158][114] 
[167] [171] [206] [117] [116] 
[144][142][ 6] [66] 
[218] 
[219] 
[113] [213] 
[168] 
Precursor Studies Open Set Recognition2016 
Learning with Reject Option2008 Anomaly Detection Survey 
Novelty Detection Survey2014 2009 
ASH MCM NNGUIDE 
MixOE 
LoCoOp 
RelationGEN 
[86] 
[31] 
[20] 
[245] 
[124] 
[120] [188] [121] [185] 
[214][65] 
Fig. 3 Timeline for representative OOD detection methodologies. Different colors indicate different categories of methodologies. Each method has its corresponding reference (inconspicuous white) in the lower right corner. Methods with high citations and open-source code are prioritized for inclusion in this figure. 
Table 1 Paper list for out-of-distribution detection. 
Sections References 
§ 3.1 Classification 
§ 3.1.1 Output-based 
Methods 
a: Training-free [48, 108, 109, 110, 111, 112, 113, 113, 114, 115, 116, 117, 
118, 119, 120, 121, 122, 123, 124] 
b: Training-based [67, 118, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 
147, 148, 149, 150] 
§ 3.1.1 Outlier Exposure 
a: Real Outliers [57, 64, 65, 132, 132, 151, 152, 153, 154, 155, 156, 157, 
158, 159, 160, 161, 162] 
b: Data Generation [163, 164, 165, 166, 167, 168, 169, 170, 171] 
§ 3.1.3: Gradient-based Methods [108, 172, 173] 
§ 3.1.4: Bayesian Models [174, 175, 176, 177, 178, 179, 180] 
§ 3.1.5: OOD for Foundation Models [149, 181, 182, 183, 184, 185, 186, 187, 188, 189] 
§ 3.2: Density-based Methods [109, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 
201, 202, 203, 204, 205, 206] 
§ 3.3: Distance-based Methods [109, 117, 207, 208, 209, 210, 211, 212, 213, 214] 
§ 3.4: Reconstruction-based Methods [215, 216, 217, 218, 219] 
§ 3.5: Theoretical Analysis [33, 56, 58, 59, 220, 221, 222, 223] 
or statistics from the intermediate-layer features [118, 
143]. Especially, to enhance the sensitivity to covariate 
shift, some methods focus on the hidden representa-
tions in the middle layers of neural networks. General-
ized ODIN, or G-ODIN [67] extended ODIN [108] by 
using a specialized training objective termed DeConf-
C and choosing hyperparameters such as perturbation 
magnitude on ID data. Note that we do not catego-
rize G-ODIN as post-hoc method as it requires model 
retraining. Recent work [144] shows that the overcon-
fidence issue can be mitigated through Logit Normal-
ization (LogitNorm), a simple fix to the common cross-
entropy loss by enforcing a constant vector norm on the 
logits in training. Trained with LogitNorm, neural net-
works produce highly distinguishable confidence scores 
between in- and out-of-distribution data. 
Some works redesign the label space to achieve 
good OOD detection performance. While commonly 
used to encode categorical information for classification, 
the one-hot encoding ignores the inherent relationship 
among labels. For example, it is unreasonable to have 
a uniform distance between dog and cat vs. dog and 
car. To this end, several works attempt to use informa-
tion in the label space for OOD detection. Some works 
arrange the large semantic space into a hierarchical 
taxonomy of known classes [145, 146, 147]. Under the 
redesigned label architecture, top-down classification 
strategy [145, 147] and group softmax training [146] are 
demonstrated effective. Another set of works uses word
Generalized Out-of-Distribution Detection: A Survey 11 
embeddings to automatically construct the label space. 
In [148], the sparse one-hot labels are replaced with sev-
eral dense word embeddings from different NLP models, 
forming multiple regression heads for robust training. 
When testing, the label, which has the minimal distance 
to all the embedding vectors from different heads, will 
be considered as the prediction. If the minimal distance 
crosses above the threshold, the sample would be clas-
sified as “novel”. Recent works further take the image 
features from language-image pre-training models [224] 
to better detect novel classes, where the image encoding 
space also contains rich information from the language 
space [149, 150]. 
3.1.2 Methods with Outlier Exposure 
a. Real Outliers Another branch of OOD detec-
tion methods makes use of a set of collected OOD 
samples, or “outlier”, during training to help models 
learn ID/OOD discrepancy. Starting from the concur-
rent baselines that encourage a flat/high-entropic pre-
diction on given OOD samples [57, 64] and suppress-
ing OOD feature magnitudes [57], a follow-up work, 
MCD [151] uses a network with two branches, between 
which entropy discrepancy is enlarged for OOD train-
ing data. Another straightforward approach with out-
lier exposure spares an extra abstention (or rejection 
class) and considers all the given OOD samples in this 
class [132, 152, 153]. A later work OECC [154] noticed 
that an extra regularization for confidence calibration 
introduces additional improvement for OE. To effec-
tively utilize the given, usually massive, OOD samples, 
some work use outlier mining [132, 155] and adversar-
ial resampling [156] approaches to obtain a compact 
yet representative set. In cases where the meaningful 
“near”-OOD images are not available, MixOE [65] pro-
poses to interpolate between ID and “far”-OOD images 
to obtain informative outliers for better regularization. 
Other works consider a more practical scenario where 
given OOD samples contain ID samples, therefore us-
ing pseudo-labeling [157] or ID filtering methods [158] 
with optimal transport scheme [159] to reduce the in-
terference of ID data. In general, OOD detection with 
outlier exposure can reach a much better performance. 
However, research shows that the performance can be 
largely affected by the correlations between given and 
real OOD samples [160]. To address the issue, recent 
work [161] proposes a novel framework that enables ef-
fectively exploiting unlabeled in-the-wild data for OOD 
detection. Unlabeled wild data is frequently available 
since it is produced essentially for free whenever de-
ploying an existing classifier in a real-world system. 
This setting can be viewed as training OOD detectors 
in their natural habitats, which provide a much better 
match to the true test time distribution than data col-
lected offline. 
b. Outlier Data Generation The outlier expo-
sure approaches impose a strong assumption on the 
availability of OOD training data, which can be infea-
sible in practice. When no OOD sample is available, 
some methods attempt to synthesize OOD samples to 
enable ID/OOD separability. Existing works leverage 
GANs to generate OOD training samples and force 
the model predictions to be uniform [163], generate 
boundary samples in the low-density region [164], or 
similarly, high-confidence OOD samples [165], or us-
ing meta-learning the update sample generation [166]. 
However, synthesizing images in the high-dimensional 
pixel space can be difficult to optimize. Recent work 
VOS [167] proposed synthesizing virtual outliers from 
the low-likelihood region in the feature space, which 
is more tractable given lower dimensionality. While 
VOS [167] is a parametric approach that models the fea-
ture space as a class-conditional Gaussian distribution, 
NPOS [168] also generates outlier ID data but in a non-
parametric approach. Noticing the generated OOD data 
could be incorrect or irrelevant, DOE [169] synthesizes 
hard OOD data that leads to worst judgments to train 
the OOD detector with a min-max learning scheme, 
and ATOL [170] uses auxiliary task to relieve the mis-
taken OOD generation. In object detection, [171] pro-
poses synthesizing unknown objects from videos in the 
wild using spatial-temporal unknown distillation. 
3.1.3 Gradient-based Methods 
Existing OOD detection approaches primarily rely on 
the output (Section 3.1) or feature space for deriving 
OOD scores, while overlooking information from the 
gradient space. ODIN [108] first explored using gradient 
information for OOD detection. In particular, ODIN 
proposed using input pre-processing by adding small 
perturbations obtained from the input gradients. The 
goal of ODIN perturbations is to increase the softmax 
score of any given input by reinforcing the model’s be-
lief in the predicted label. Ultimately the perturbations 
have been found to create a greater gap between the 
softmax scores of ID and OOD inputs, thus making 
them more separable and improving the performance 
of OOD detection. While ODIN only uses gradients 
implicitly through input perturbation, recent work pro-
posed GradNorm [172] which explicitly derives a scoring 
function from the gradient space. GradNorm employs 
the vector norm of gradients, backpropagated from the 
KL divergence between the softmax output and a uni-
form probability distribution. A recent research [173]
12 Jingkang Yang et al. 
demonstrates that while gradient-based methods are 
effective, their success does not necessarily depend on 
gradients, but rather on the magnitude of learned fea-
ture embeddings and predicted output distribution. 
3.1.4 Bayesian Models 
A Bayesian model is a statistical model that im-
plements Bayes’ rule to infer all uncertainty within 
the model [225]. The most representative method is 
the Bayesian neural network [226], which draws sam-
ples from the posterior distribution of the model via 
MCMC [227], Laplace methods [228, 229] and varia-
tional inference [230], forming the epistemic uncertainty 
of the model prediction. However, their obvious short-
comings of inaccurate predictions [231] and high com-
putational costs [232] prevent them from wide adoption 
in practice. Recent works attempt several less princi-
pled approximations including MC-dropout [174] and 
deep ensembles [175, 233, 234] for faster and better es-
timates of uncertainty. These methods are less compet-
itive for OOD uncertainty estimation. Further explo-
ration takes natural-gradient variational inference and 
enables practical and affordable modern deep learn-
ing training while preserving the benefits of Bayesian 
principles [176]. Dirichlet Prior Network (DPN) is also 
used for OOD detection with an uncertainty modeling 
of three different sources of uncertainty: model uncer-
tainty, data uncertainty, and distributional uncertainty, 
and form a line of works [177, 178, 179]. Recently, the 
Bayesian hypothesis test has been used to formulate 
OOD detection, with upweighting method and Hessian 
approximation for scalability [180]. 
3.1.5 OOD Detection for Foundation Models 
Foundation models [235], notably large-scale vision-
language models [224], have demonstrated exceptional 
performance in a variety of downstream tasks. Their 
success is largely attributed to extensive pre-training on 
large-scale datasets. Several works [149, 181, 182] reveal 
that well-pretrained models can significantly enhance 
OOD detection, particularly in challenging scenarios. 
However, adapting (tuning) these models for down-
stream tasks with specific semantic (label) space in the 
training data remains a challenge, as simple approaches 
such as linear probing, prompt tuning [236, 237, 238], 
and adaptor-style fine-tuning methods [239] do not 
have good results on OOD detection. To advance the 
problem, a thorough investigation [183] examines how 
fine-tuned vision-language models are performed. Ad-
ditionally, recent research [184] highlights the impact 
of large-scale pretraining data and provides a system-
atic study on pretraining strategies on OOD detection 
performance. On a technical front, LoCoOp [185] intro-
duces OOD regularization to a subset of CLIP’s local 
features identified as OOD, enhancing prompt learning 
for better ID and OOD differentiation, and LSA [186] 
uses a bidirectional prompt customization mechanism 
to enhance the image-text alignment. 
The strong zero-shot learning capabilities of models 
like CLIP [224] also open avenues for zero-shot OOD de-
tection. This new setting aims to categorize known class 
samples and detect samples that do not belong to any of 
the known classes, where known classes are represented 
solely through textual descriptions or class names, elim-
inating the need for explicit training on these classes. 
Addressing this, ZOC [187] trains a decoder based on 
CLIP’s visual encoder to create candidate labels for 
OOD detection. While ZOC is computationally inten-
sive and data-demanding, MCM [188] opts for softmax 
scaling to align visual features with textual concepts for 
OOD detection. A recent advancement, CLIPN [189], 
innovatively integrates a “no” logic in OOD detection. 
Utilizing new prompts and a text encoder, along with 
novel opposite loss functions, CLIPN effectively tackles 
the challenge of identifying hard-to-distinguish OOD 
samples. This development marks a significant stride in 
enhancing the precision of OOD detection in complex 
scenarios. 
3.2 Density-based Methods 
Density-based methods in OOD detection explicitly 
model the in-distribution with some probabilistic mod-
els, and flag test data in low-density regions as OOD. 
Although OOD detection can be different from AD in that multiple classes exist in the in-distribution, den-
sity estimation methods used for AD in Section 4.2 can 
be directly adapted to OOD detection by unifying the 
ID data as a whole [190, 191, 192, 193, 194]. When the 
ID contains multiple classes, class-conditional Gaussian 
distribution can explicitly model the in-distribution so 
that the OOD samples can be identified based on their 
likelihoods [109]. Flow-based methods [195, 196, 197, 
198, 199] can also be used for probabilistic modeling. 
While directly estimating the likelihood seems like a 
natural approach, some works [200, 201, 202] find that 
probabilistic models sometimes assign a higher likeli-
hood for the OOD sample. Several works attempt to 
solve the problems using likelihood ratio [203]. [204] 
finds that the likelihood exhibits a strong bias towards 
the input complexity and proposes a likelihood ratio-
based method to compensate for the influence of in-
put complexity. Recent methods turn to new scores 
such as likelihood regret [205] or an ensemble of multi-
ple density models [201]. To directly model the density
Generalized Out-of-Distribution Detection: A Survey 13 
of semantic space, SEM score is used with a simple 
combination of density estimation in the low-level and 
high-level space [240]. Overall, generative models can 
be prohibitively challenging to train and optimize, and 
the performance can often lag behind the classification-
based approaches (Section 3.1). 
3.3 Distance-based Methods 
The basic idea of distance-based methods is that the 
testing OOD samples should be relatively far away from 
the centroids or prototypes of in-distribution classes. 
[109] uses the minimum Mahalanobis distance to all 
class centroids for detection. A subsequent work splits 
the images into foreground and background and then 
calculates the Mahalanobis distance ratio between the 
two spaces [207]. In contrast to the parametric ap-
proach, recent work [117] shows strong promise of non-
parametric nearest-neighbor distance for OOD detec-
tion. Unlike Mahalanobis, the non-parametric approach 
does not impose any distributional assumption about 
the underlying feature space, hence providing stronger 
simplicity, flexibility, and generality. 
For distance functions, some works use cosine sim-
ilarity between test sample features and class fea-
tures to determine OOD samples [208, 209]. The one-
dimensional subspace spanned by the first singular vec-
tor of the training features is shown to be more suitable 
for cosine similarity-based detection [210]. Moreover, 
other works leverage distances with radial basis func-
tion kernel [211], Euclidean distance [212], and geodesic 
distance [241] between the input’s embedding and the 
class centroids. Apart from calculating the distance be-
tween samples and class centroids, the feature norm in 
the orthogonal complement space of the principal space 
is shown effective on OOD detection [206]. Recent work 
CIDER [213] explores the usability of the embeddings 
in the hyperspherical space, where inter-class dispersion 
and inner-class compactness can be encouraged. 
3.4 Reconstruction-based Methods 
The core idea of reconstruction-based methods is that 
the encoder-decoder framework trained on the ID data 
usually yields different outcomes for ID and OOD sam-
ples. The difference in model performance can be uti-
lized as an indicator for detecting anomalies. For exam-
ple, reconstruction models that are only trained by ID 
data cannot well recover the OOD data [215], and there-
fore the OOD can be identified. While reconstruction-
based models with pixel-level comparison seem not a 
popular solution in OOD detection for its expensive 
training cost, reconstructing with hidden features is 
shown as a promising alternative [216]. Rather than 
reconstructing the entire image, recent work Mood-
Cat [217] masks a random portion of the input image 
and identifies OOD samples using the quality of the 
classification-based reconstruction results. READ [218] 
combines inconsistencies from a classifier and an au-
toencoder by transforming the reconstruction error 
of raw pixels to the latent space of the classifier. 
MOOD [219] shows that masked image modeling for 
pretraining is beneficial to OOD detection tasks com-
pared to contrastive training and classic classifier train-
ing. 
3.5 Theoretical Analysis 
Early theoretical research on OOD detection [33] delves 
into the limitations of Deep Generative Models (DGMs) 
in OOD contexts. This work uncovers a critical flaw 
where DGMs frequently assign greater probabilities to 
OOD data compared to training data, attributing this 
issue primarily to model misestimation rather than 
the typical set hypothesis. This hypothesis posits that 
relevant out-distributions might be located in high-
likelihood areas of the data distribution. The study 
concludes that any generalized OOD task must re-
strict the set of distributions that are considered out-
of-distribution, as without any restrictions, the task is 
impossible. Later work [220] advances the field by de-
veloping a comprehensive analytical framework aimed 
at enhancing theoretical understanding and practical 
performance of OOD detection methods in neural net-
works. Their innovative approach culminates in a novel 
OOD detection method that surpasses existing tech-
niques in both theoretical robustness and empirical per-
formance. 
Another series of studies has been focused on Open-
Set Learning (OSL). The seminal work in this do-
main [56] conceptualizes open-space risk for recogniz-
ing samples from unknown classes. The following re-
search applies extreme value theory to OSL [221, 222]. 
While probably approximately correct (PAC) theory is 
applied for OSR [58], their method required test sam-
ples during training. Therefore, an investigation of the 
generalization error bound is conducted and proves the 
existence of a low-error OSL algorithm under certain 
assumptions [59]. Still, under the PAC theory, a later 
study establishes necessary and sufficient conditions for 
the learnability of OOD detection in various scenar-
ios [223], including cases with overlapping and non-
overlapping ID and OOD data. Their work also offers 
theoretical support for existing OOD detection algo-
14 Jingkang Yang et al. 
rithms and suggests that OOD detection is possible un-
der certain practical conditions. 
Despite these theoretical advancements, the field 
eagerly anticipates further research addressing aspects 
such as generalization in OOD detection, the explain-
ability of these models, the integration of deep learning 
theory specific to OOD detection, and the exploration 
of foundation model theories pertinent to this area. 
3.6 Discussion 
The field of OOD detection has enjoyed rapid devel-
opment since its emergence, with a large space of so-
lutions. In the multi-class setting, the problem can be 
canonical to OSR (Section 4.1)—accurately classify test 
samples from ID within the class space Y, and reject 
test samples with semantics outside the support of Y. 
The difference often lies in the evaluation protocol. OSR 
splits a dataset into two halves: one set as ID and an-
other set as OOD. In contrast, OOD allows a more 
general and flexible evaluation by considering test sam-
ples from different datasets or domains. Moreover, OOD 
detection encompasses a broader spectrum of learn-
ing tasks (e.g ., multi-label classification [112], object 
detection [167, 171]) and solution space. Apart from 
the methodology development, theoretical understand-
ing has also received attention in the community [220], 
providing provable guarantees and empirical analysis to 
understand how OOD detection performance changes 
with respect to data distributions. 
4 Methodologies from Other Sub-tasks 
In this section, we briefly introduce methodologies for 
sub-tasks under the generalized OOD detection frame-
work, including AD, ND, OSR, and OD, in hope that 
the methods from other sub-tasks can inspire more 
ideas for OOD detection community. 
4.1 Open Set Recognition 
The concept of OSR was first introduced in [56], which 
showed the validity of 1-class SVM and binary SVM 
for solving the OSR problem. In particular, [56] pro-
poses the 1-vs-Set SVM to manage the open-set risk 
by solving a two-plane optimization problem instead of 
the classic half-space of a binary linear classifier. This 
paper highlighted that the open-set space should also 
be bounded, in addition to bounding the ID risk. 
Classification-based Methods Early works fo-
cused on logits redistribution using the compact abat-
ing probability (CAP) [242] and extreme value theory 
(EVT) [221, 243, 244]. In particular, classic probabilis-
tic models lack the consideration of open-set space. 
CAP explicitly models the probability of class member-
ship abating from ID points to OOD points, and EVT 
focuses on modeling the tail distribution with extreme 
high/low values. In the context of deep learning, Open-
Max [245] first implements EVT for neural networks. 
OpenMax replaces the softmax layer with an OpenMax 
layer, which calibrates the logits with a per-class EVT 
probabilistic model such as Weibull distribution. 
To bypass open-set risk construction, some works 
attained good results without EVT. For example, 
some work uses a membership loss to encourage 
high activations for known classes, and uses large-
scale external datasets to learn globally negative fil-
ters that can reduce the activations of novel im-
ages [246]. Apart from explicitly forcing discrepancy be-
tween known/unknown classes, other methods extract 
stronger features through an auxiliary task of transfor-
mation classification [247], or mutual information max-
imization between the input image and its latent fea-
tures [248], etc. 
Image generation techniques have been utilized to 
synthesize unknown samples from known classes, which 
helps distinguish between known vs. unknown sam-
ples [249, 250, 251, 252]. While these methods are 
promising on simple images such as handwritten char-
acters, they do not scale to complex natural image 
datasets due to the difficulty in generating high-quality 
images in high-dimensional space. Another solution is 
to successively choose random categories in the train-
ing set and treat them as unknown, which helps the 
classifier to shrink the boundaries and gain the abil-
ity to identify unknown classes [253, 254]. Moreover, 
[255] splits the training data into typical and atypical 
subsets, which also helps learn compact classification 
boundaries. 
Distance-based Methods Distance-based methods 
for OSR require the prototypes to be class-conditional, 
which allows maintaining the ID classification perfor-
mance. Category-based clustering and prototyping are 
performed based on the visual features extracted from 
the classifiers. OOD samples can be detected by com-
puting the distance w.r.t. clusters [256, 257]. Some 
methods also leveraged contrastive learning to learn 
more compact clusters for known classes [258, 259], 
which enlarge the distance between ID and OOD. 
CROSR [260] enhances the features by concatenating 
visual embeddings from both the classifier and recon-
struction model for distance computation in the ex-
tended feature space. Besides using features from clas-
sifiers, GMVAE [261] extracts features using a recon-
struction VAE, and models the embeddings of the train-
Generalized Out-of-Distribution Detection: A Survey 15 
ing set as a Gaussian mixture with multiple centroids 
for the following distance-based operations. Classifiers 
using nearest neighbors are also adapted for OSR prob-
lem [262]. By storing the training samples, the nearest 
neighbor distance ratio is used for identifying unknown 
samples in testing. 
Reconstruction-based Methods With similar 
motivations as Section 3.4, reconstruction-based meth-
ods expect different reconstruction behavior for ID vs. 
OOD samples. The difference can be captured in the 
latent feature space or the pixel space of reconstructed 
images. 
By sparsely encoding images from the known 
classes, open-set samples can be identified based on 
their dense representation. Techniques such as sparsity 
concentration index [263] and kernel null space meth-
ods [264, 265] are used for sparse encoding. 
By fixing the visual encoder obtained from standard 
multi-class training to maintain ID classification perfor-
mance, C2AE trains a decoder conditioned on label vec-
tors and estimates the reconstructed images using EVT 
to distinguish unknown classes [266]. Subsequent works 
use conditional Gaussian distributions by forcing dif-
ferent latent features to approximate class-wise Gaus-
sian models, which enables classifying known samples as 
well as rejecting unknown samples [267]. Other methods 
generate counterfactual images, which help the model 
focus more on semantics [268]. Adversarial defense is 
also considered in [269] to enhance model robustness. 
Discussion Although there is not an independent 
section for density-based methods, these methods can 
play an important role and are fused as a critical step 
in some classification-based methods such as Open-
Max [245]. The density estimation on visual embed-
dings can effectively detect unknown classes without 
influencing the classification performance. A hybrid 
model also uses a flow-based density estimator to detect 
unknown samples [270]. 
As introduced in Section 2.4, the general goal of 
OSR and OOD detection is aligned, that is to detect 
semantic shift from the training data. Therefore, we 
encourage methods from these two field should learn 
more from each other. For example, apart from novel 
methods, OSR research also shows that a good classi-
fier [271] in the close-set is critical to OSR performance, 
which should also applicable to OOD detection tasks. 
4.2 Anomaly Detection & Novelty Detection 
This section reviews methodologies for sensory and se-
mantic AD and one-class ND. Notice that multi-classes 
ND is covered in the previous. Given homogeneous 
in-distribution data, approaches include density-based, 
reconstruction-based, distance-based, and hybrid meth-
ods. We also discuss theoretical works. 
Density-based Methods Density-based meth-
ods model normal data (ID) distributions, assuming 
anomalous test data has low likelihood while normal 
data has higher likelihood. Techniques include classic 
density estimation, density estimation with deep gen-
erative models, energy-based models, and frequency-
based methods. 
Parametric density estimation assumes pre-defined 
distributions [272]. Methods involve multivariate Gaus-
sian distribution [273, 274], mixed Gaussian distribu-
tion [275, 276], and Poisson distribution [277]. Non-
parametric density estimation handles more complex 
scenarios [278] with histograms [279, 280, 281, 282] and 
kernel density estimation (KDE) [283, 284, 285]. 
Neural networks generate high-quality features to 
enhance classic density estimation. Techniques include 
autoencoder (AE) [286] and variational autoencoder 
(VAE) [287]-based models, generative adversarial net-
works (GANs) [288], flow-based models [195, 289], and 
representation enhancement strategies. 
EBMs use scalar energy scores to express probabil-
ity density [290] and provide a solution for AD [291]. 
Training EBMs can be computationally expensive, but 
score matching [292] and stochastic gradient Langevin 
dynamics [293] enable efficient training. 
Frequency domain analysis for AD includes methods 
like CNN kernel smoothing [294], spectrum-oriented 
data augmentation [295], and phase spectrum target-
ing [296]. These mainly focus on sensory AD. 
Reconstruction-based Methods These AD meth-
ods leverage model performance differences on normal 
and abnormal data in feature space or by reconstruc-
tion error. 
Sparse reconstruction assumes normal samples can 
be accurately reconstructed using a limited set of basis 
functions, while anomalies have larger reconstruction 
costs and a dense representation [297, 298, 299]. Tech-
niques include L1 norm-based kernel PCA [300] and 
low-rank embedded networks [301]. 
Reconstruction-error methods assume a model 
trained on normal data will produce better reconstruc-
tions for normal test samples than anomalies. Deep 
models include AEs [302], VAEs [303], GANs [304], and 
U-Net [305]. 
AE/VAE-based models combine reconstruction-
error with AE/VAE models [302, 303] and use strate-
gies like reconstructing by memorized normality [306, 
307], adapting model architectures [308], and par-
tial/conditional reconstruction [192, 309, 310]. In semi-
supervised AD, CoRA [311] trains two AEs on inliers
16 Jingkang Yang et al. 
and outliers, using reconstruction errors for anomaly 
detection. Reconstruction-error methods using GANs 
leverage the discriminator to calculate reconstruction 
error for anomaly detection [304]. Variants like denois-
ing GANs [194], class-conditional GANs [54], and en-
sembling [312] further improve performance. Gradient-
based methods observe different patterns on training 
gradient between normalities and anomalies in a recon-
struction task, using gradient-based representation to 
characterize anomalies [313]. 
Distance-based Methods These methods detect 
anomalies by calculating the distance between samples 
and prototypes [314], requiring training data in mem-
ory. Methods include K-nearest Neighbors [315] and 
prototype-based methods [316, 317]. 
Classification-based Methods AD and one-class 
ND are often formulated as unsupervised learning 
problems, but there are some supervised and semi-
supervised methods as well. One-class classification 
(OCC) directly learns a decision boundary that cor-
responds to a desired density level set of the nor-
mal data distribution [318]. DeepSVDD [319] intro-
duced classic OCC to the deep learning community. PU 
learning [320, 321, 322, 323] is proposed for the semi-
supervised AD setting where unlabeled data is available 
in addition to the normal data. Self-supervised learning 
methods use pretext tasks such as contrastive learn-
ing [139], image transformation prediction [324, 325], 
and future frame prediction [326], where anomalies are 
more likely to make mistakes on the designed task. 
One-class classification learns a decision boundary 
that corresponds to a desired density level set of the 
normal data distribution, which DeepSVDD [319] in-
troduced to the deep learning community. PU learn-
ing [320, 321, 322, 323] is a popular method for the semi-
supervised AD setting. Self-supervised learning meth-
ods use pretext tasks such as contrastive learning [139], 
image transformation prediction [324, 325], and future 
frame prediction [326], where anomalies are more likely 
to make mistakes on the designed task. 
Discussion: Sensory vs Semantic AD Sensory 
and semantic AD approaches assume the normal data 
as homogeneous, despite the presence of multiple cat-
egories within it. While semantic AD methods are 
mainly applicable to sensory AD problems, the latter 
can benefit from techniques that focus on lower-level 
features (e.g., flow-based and hidden feature-based), lo-
cal representations, and frequency-based methods. Al-
though current OOD detection tasks mostly focus on 
semantic shift, the method for Sensory AD might be 
especially helpful for far OOD detection, like ImageNet 
vs Texture dataset. 
In-Distribution 
Near-OOD Far-OOD 
CIFAR-100 MNIST SVHN 
TinyImageNet 
CIFAR-10 
Texture Places365 
Fig. 4 The illustration of CIFAR-10 benchmark that is used in Section 5. The CIFAR-100 benchmark simply swaps the position of CIFAR-10 and CIFAR-100 in the figure. 
Discussion: Theoretical Analysis In addition to 
algorithmic development, theoretical analysis of AD 
and one-class ND has also been provided in some works. 
For instance, [58] constructs a clean set of ID and 
a mixed set of ID/OOD with identical sample sizes, 
achieving a PAC-style finite sample guarantee for de-
tecting a certain portion of anomalies with the mini-
mum number of false alarms. All these works could be 
beneficial to the theoretical works of OOD detection. 
4.3 Outlier Detection 
Outlier detection (OD) observes all samples to identify 
significant deviations from the majority distribution. 
Though mostly studied in data mining, deep learning-
based OD methods are used for data cleaning in open-
set noisy data [83, 84] and open-set semi-supervised 
learning [85]. 
Density-based Methods OD methods include 
Gaussian distribution [327, 328], Mahalanobis distance [273], Gaussian mixtures [329], and Local outlier 
factor (LOF) [330]. RANSAC [331] estimates parame-
ters for a mathematical model. Classic density methods 
and NN-based density methods can also be applied. 
Distance-based Methods Outliers can be detected 
by neighbor counting [332, 333], DBSCAN cluster-
ing [334], and graph-based methods [335, 336, 337, 338, 
339, 340, 341, 342, 343]. 
Classification-based Methods AD methods like 
Isolation Forest [344] and OC-SVM [318, 319] can be 
applied to OD. Deep learning models can identify out-
liers [345]. Techniques for robustness and feature gen-
eralizability include ensembling [346], co-training [347], 
and distillation [345, 348]. 
Discussion OD techniques are valuable for open-set 
semi-supervised learning, learning with open-set noisy 
labels, and novelty discovery. All these solutions can 
be applied especially when OOD samples are exposed 
during the training stage [158].
Generalized Out-of-Distribution Detection: A Survey 17 
DeepSVDD CutPaste 
DRAEM OpenMax 
MSP ODIN Gram GradNorm MLS VIM DICE G-ODIN ARPL LogitNorm 
MCDropout TempScale CutMixMDS EBO ReAct KLM KNN ConfBranch CSI VOS OE UDG DeepEnsemble Mixup PixMix 
ID: CIFAR-10 
2018 2021 
2021 2016 
2017 2018 
2018 2020 
2020 2021 
2021 2022 
2022 2022 
2022 2022 
2018 2020 
2020 2021 
2022 2022 
2019 2021 
2016 2017 
17 2018 
2019 2021 
ID: CIFAR-100 AD Post-Hoc OOD Detection Training-Required Extra Data Model Robustness 
Fig. 5 Comparison between different methodologies under generalized OOD detection framework on the CIFAR-10/100 benchmarks. Results are from OpenOOD [349]. Different colors denote the method categories. Each method reports near-OOD (left-bar) and far-OOD (right-bar) AUROC scores, as introduced in Section 5.1. Method names in black originated for OOD detection, while in red are AD methods, blue for OSR methods, and pink for models from model uncertainty works. 
5 Benchmarks and Experiments 
In this section, we report the fair comparison of 
methodologies that from different categories on the 
CIFAR [350] benchmark. The report originated from 
OpenOOD benchmarks [349]. We selected several pop-
ular AD methods, OOD detection methods (post-hot, 
training-required, and extra-data-required), and model 
robustness methods. 
5.1 Benchmarks and Metrics 
The common practice for building OOD detection 
benchmarks is to consider an entire dataset as in-
distribution (ID), and then collect several datasets 
that are disconnected from any ID categories as OOD 
datasets. In this part, we show the results from two 
popular OOD benchmarks with ID datasets of CIFAR-
10 [350], CIFAR-100 [351] from OpenOOD (c.f . Fig-
ure 4), with each benchmark designing near-OOD and 
far-OOD datasets to facilitate detailed analysis of the 
OOD detectors. Near-OOD datasets only have semantic 
shift compared with ID datasets, while far-OOD further 
contains obvious covariate (domain) shift. 
CIFAR-10 CIFAR-10 [350] is a 10-class dataset 
for general object classification, which contains 50k 
training images and 10k test images. As for the OOD 
dataset, we construct near-OOD with CIFAR-100 [351] 
and TinyImageNet [5]. Notice that 1,207 images are 
removed from TinyImageNet since they actually be-
long to CIFAR-10 classes [158]. Far-OOD is built 
by MNIST [352], SVHN [353], Texture [354], and 
Places365 [355] with 1,305 images are removed due to 
semantic overlaps. 
CIFAR-100 Another OOD detection benchmark 
uses CIFAR-100 [351] as an in-distribution, which con-
tains 50k training images and 10k test images with 100 
classes. For OOD dataset, near-OOD includes CIFAR-
10 [350] and TinyImageNet [356]. Similar to the CIFAR-
10 benchmark, 2,502 images are removed from TinyIm-
ageNet due to the overlapping semantics with CIFAR-
100 classes [158]. Far-OOD consists of MNIST [352], 
SVHN [353], Texture [354], and Places365 [355] with 
1,305 images removed. 
Metrics We only report the AUROC scores, which 
measure the area under the Receiver Operating Char-
acteristic (ROC) curve. 
5.2 Experimental Setup 
To ensure a fair comparison across methods that origi-
nate from different fields and have different implemen-
tations, unified settings with common hyperparame-
ters and architecture choices are implemented. ResNet-
18 [357] is used as the backbone network. If the im-
plemented method requires training, the widely ac-
cepted setting with SGD optimizer, a learning rate of 
0.1, momentum of 0.9, and weight decay of 0.0005 for 
100 epochs, is used. For further details, please refer to 
OpenOOD [349, 358]. 
5.3 Experimental Results and Findings 
Data Augmentation Methods are the Most Ef-
fective We split Figure 5 into several sections based 
on the method type. Generally, the most effective meth-
ods are those that use model uncertainty works with 
data augmentation techniques. This group mainly in-
cludes simple and effective methods such as prepro-
cessing methods like PixMix [138] and CutMix [135]. 
PixMix achieves 93.1% on Near-OOD in CIFAR-10, the 
best performance among all the methods in this bench-
mark. These methods also perform well in most of the
18 Jingkang Yang et al. 
other benchmarks. Similarly, other simple and effective 
methods to enhance model uncertainty estimation such 
as Ensemble [233] and Mixup [134] also demonstrate 
excellent performance. 
Extra Data Seems Not Necessary? Comparing 
UDG [158] (the best from the extra-data part) with 
KNN [117] (the best from the extra data-free part), we 
found that UDG’s advantage is only in CIFAR-10 near-
OOD, which is not satisfactory since a large quantity of 
real outlier data is required. In this benchmark, we use 
the entire TinyImageNet training set as the extra data, 
the choice of training outliers could greatly affect the 
performance of OOD detectors, so further exploration 
is needed. 
Post-Hoc Methods Outperform Training in 
General Surprisingly, methods that require training 
do not necessarily perform better. In general, inference-
only methods outperform trained methods. Neverthe-
less, the trained models can be generally used in con-
junction with post-hoc methods, which could poten-
tially further increase their performance. 
Post-Hoc Methods are Making Progress In 
general, recent post-hoc methods have had better per-
formance than previous methods since 2021, indicating 
that the direction of inference-only methods is promis-
ing and making progress. Recent methods show im-
provements in performance on more realistic datasets 
than previous methods, which focused on toy datasets. 
For example, the classic MDS performs well on MNIST 
but poorly on CIFAR-10 and CIFAR-100, while the 
recent KNN maintains good performance on MNIST, 
CIFAR-10, CIFAR-100, and also shows outstanding 
performance on ImageNet [349]. 
Some AD Methods are Good at Far-OOD Al-
though anomaly detection (AD) methods were origi-
nally designed to detect pixel-level appearance differ-
ences on the MVTec-AD dataset, they have shown po-
tency in far-OOD detection, such as with DRAEM and 
CutPaste. Both methods achieved high performance on 
far-OOD detection, especially when using CIFAR-100 
as the in-distribution dataset. 
Explore OpenOOD for More Experimental 
Findings Accompanying our survey, we lead the de-
velopment of OpenOOD [349], an open-source code-
base that provides a unified framework and bench-
marking platform for conducting fair comparisons of 
various model architectures and OOD detection meth-
ods. OpenOOD is continuously updated and includes 
two comprehensive experimental reports [349, 358] that 
delve into extensive analysis and discovery2. We en-
courage readers to explore OpenOOD’s resources for 
a deeper understanding of key aspects such as select-
2 We also provide a leaderboard to track SOTA methods. 
ing model architectures, utilizing pre-trained models, 
practical applications, and detailed implementation in-
sights. 
5.4 Exclusion of Covariate-Shift Detection 
While OpenOOD does not include settings for pure co-
variate shift, this was a deliberate choice. The primary 
focus is on semantic shifts, which are fundamental to 
OOD detection. By not separately analyzing covari-
ate shifts, we aim to avoid potential misinterpretations 
and prevent the overemphasis on covariate shift detec-
tion. Experiments in [240] highlight a key finding: most 
current OOD detectors are more sensitive to covariate 
shifts than semantic shifts and lead to the concept of 
“full-spectrum OOD detection”, advocating for mod-
els that effectively generalize to handle covari-
ate shifts while simultaneously detecting samples 
with semantic shifts. More experimental evaluations 
can be found in OpenOOD v1.5 [358]. 
6 Challenges and Future Directions 
In this section, we discuss the challenges and future 
directions of generalized OOD detection. 
6.1 Challenges 
a. Proper Evaluation and Benchmarking We 
hope this survey can clarify the distinctions and con-
nections of various sub-tasks, and help future works 
properly identify the target problem and benchmarks 
within the framework. The mainstream OOD detection 
works primarily focus on detecting semantic shifts. Ad-
mittedly, the field of OOD detection can be very broad 
due to the diverse nature of distribution shifts. Such a 
broad OOD definition also leads to some challenges and 
concerns [32, 150], which advocate a clear specification 
of OOD type in consideration (e.g ., semantic OOD, ad-
versarial OOD, etc.) so that proposed solutions can be 
more specialized. Besides, the motivation of detecting 
a certain distribution shift also requires clarification. 
While rejecting classifying samples with semantic shift 
is apparent, detecting sensory OOD should be speci-
fied to some meaningful scenarios to contextualize the 
necessity and practical relevance of the task. 
We also urge the community to carefully construct 
the benchmarks and evaluations. It is noticed that early 
work [48] ignored the fact that some OOD datasets may 
contain images with ID categories, causing inaccurate
Generalized Out-of-Distribution Detection: A Survey 19 
performance evaluation. Fortunately, recent OOD de-
tection works [158] have realized this flaw and pay spe-
cial attention to removing ID classes from OOD samples 
to ensure proper evaluation. 
b. Outlier-free OOD Detection The outlier expo-
sure approach [64] imposes a strong assumption of the 
availability of OOD training data, which can be diffi-
cult to obtain in practice. Moreover, one needs to per-
form careful de-duplication to ensure that the outlier 
training data does not contain ID data. These restric-
tions may lead to inflexible solutions and prevent the 
adoption of methods in the real world. Going forward, 
a major challenge for the field is to devise outlier-free 
learning objectives that are less dependent on auxiliary 
outlier dataset. 
c. Tradeoff Between Classification and OOD De-
tection In OSR and OOD detection, it is important 
to achieve the dual objectives simultaneously: one for 
the ID task (e.g ., image classification), another for the 
OOD detection task. For a shared network, an inherent 
trade-off may exist between the two tasks. Promising 
solutions should strive for both. These two tasks may 
or may not contradict each other, depending on the 
methodologies. For example, [100] advocated the inte-
gration of image classification and open-set recognition 
so that the model will possess the capability of discrim-
inative recognition on known classes and sensitivity to 
novel classes at the same time. [271] also showed that 
the ability of detecting novel classes can be highly cor-
related with its accuracy on the closed-set classes. [158] 
demonstrated that optimizing for the cluster compact-
ness of ID classes may facilitate both improved classifi-
cation and distance-based OOD detection performance. 
Such solutions may be more desirable than ND, which 
develops a binary OOD detector separately from the 
classification model, and requires deploying two mod-
els. 
d. Real-world Benchmarks and Evaluations 
Current methods in OOD detection are predominantly 
evaluated on smaller datasets like CIFAR. However, it 
has been observed that strategies effective on CIFAR 
may not perform as well on larger datasets like Im-
ageNet, which has a more extensive semantic space. 
This discrepancy underscores the importance of con-
ducting OOD detection evaluations in large-scale, real-
world settings. Consequently, we recommend future re-
search to focus on benchmarks based on ImageNet for 
OOD detection [146] and to explore large-scale Open 
Set Recognition (OSR) benchmarks [271] to fully test 
the effectiveness of these methods. Additionally, recent 
research [359] highlights the presence of erroneous sam-
ples in ImageNet OOD benchmarks and introduces the 
corrected NINCO dataset for more accurate evalua-
tions. Furthermore, expanding the scope of benchmarks 
to encompass real-world scenarios, such as more real-
istic datasets [360, 361], and object-level OOD detec-
tion [167, 171], can provide valuable insights, especially 
in safety-critical applications like autonomous driving. 
6.2 Future Directions 
a. Methodologies across Sub-tasks Due to the 
inherent connections among different sub-tasks, their 
solution space can be shared and inspired by each other. 
For example, the recent emerging density-based OOD 
detection research (c.f . Section 3.2) can draw insights 
from the density-based AD methods (c.f . Section 4.2) 
that have been around for a long time. 
b. OOD Detection & Generalization An open-
world classifier should consider two tasks, i.e., being 
robust to covariate shift while being aware of the se-
mantic shift. Existing works pursue these two goals in-
dependently. Recent work proposes a semantically co-
herent OOD detection framework [158] that encourages 
detecting semantic OOD samples while being robust 
to negligible covariate shift. Given the vague defini-
tion of OOD, [362] proposed a formalization of OOD 
detection by explicitly taking into account the separa-
tion between invariant features (semantically related) 
and environmental features (non-semantic). The work 
highlighted that spurious environmental features in the 
training set can significantly impact OOD detection, 
especially when the semantic OOD data contains the 
spurious feature. Further, full-spectrum OOD detec-
tion [240] highlights the effects of “covariate-shifted 
in-distribution”, and show that most of the previous 
OOD detectors are unfortunately sensitive to covariate 
shift rather than semantic shift. This setting explicitly 
promotes the generalization ability of OOD detectors. 
Recent works on open long-tailed recognition [100], 
open compound domain adaptation [92], open-set do-
main adaptation [363] and open-set domain generaliza-
tion [364] consider the potential existence of open-class 
samples. Looking ahead, we envision great research op-
portunities on how OOD detection and OOD gener-
alization can better enable each other [100], in terms 
of both algorithmic design and comprehensive perfor-
mance evaluation. 
c. OOD Detection & Open-Set Noisy Labels 
Existing methods of learning from open-set noisy labels 
focus on suppressing the negative effects of noise [83, 
365]. However, the open-set noisy samples can be use-
ful for outlier exposure (c.f . Section 3.1.2) [342] and 
potentially benefit OOD detection. With a similar idea, 
the setting of open-set semi-supervised learning can be
20 Jingkang Yang et al. 
promising for OOD detection. We believe the combina-
tion of OOD detection and the previous two fields can 
provide more insights and possibilities. 
d. OOD Detection For Broader Learning Tasks 
As mentioned in Section 3.6, OOD detection en-
compasses a broader spectrum of learning tasks, in-
cluding multi-label classification [112], object detec-
tion [167, 171], image segmentation [66], time-series 
prediction [105], and LiDAR-based 3D object detec-
tion [366]. For the classification task itself, the re-
searchers also extended the OOD detection technique 
to improve the reliability of zero-shot pretrained mod-
els [187] (e.g ., CLIP). Furthermore, some studies fo-
cus on applying OOD detection methods to produce 
reliable image captions [367]. Recent advancements ex-
tend OOD detection to continuously adaptive or online 
learning environments [368]. Additionally, OOD detec-
tion shows promise in addressing model reliability is-
sues in broader applications, like mitigating hallucina-
tion problems in large language models [369]. The inte-
gration of OOD detection methods promises to enhance 
the reliability and practicality of models across various 
fields, and insights from these fields could, in turn, fur-
ther refine OOD detection techniques. 
e. OOD Detection with World Models The ex-
isting works utilizing foundation models, particularly 
multi-modal ones such as CLIP [224], have significantly 
enhanced OOD detection performance, as discussed 
in Section 3.1.5. Starting from this, recent advance-
ments have further focused on leveraging the extensive 
world knowledge encapsulated in Large Language Mod-
els [370]. This approach aligns with the rapid develop-
ment in multi-modal world models [371, 372, 373], pre-
senting burgeoning opportunities for further innovation 
within the OOD detection community. 
7 Conclusion 
In this survey, we comprehensively review five topics: 
AD, ND, OSR, OOD detection, and OD, and unify 
them as a framework of generalized OOD detection. 
By articulating the motivations and definitions of each 
sub-task, we encourage follow-up works to accurately 
locate their target problems and find the most suit-
able benchmarks. By sorting out the methodologies for 
each sub-task, we hope that readers can easily grasp the 
mainstream methods, identify suitable baselines, and 
contribute future solutions in light of existing ones. By 
providing insights, challenges, and future directions, we 
hope that future works will pay more attention to the 
existing problems and explore more interactions across 
other tasks within or even outside the scope of general-
ized OOD detection. 
Acknowledgment 
This study is supported by the Ministry of Educa-
tion, Singapore, under its MOE AcRF Tier 2 (MOE-
T2EP20221- 0012), NTU NAP, and under the RIE2020 
Industry Alignment Fund – Industry Collaboration 
Projects (IAF-ICP) Funding Initiative, as well as cash 
and in-kind contribution from the industry partner(s). 
YL is supported by the Office of the Vice Chancellor 
for Research and Graduate Education (OVCRGE) with 
funding from the Wisconsin Alumni Research Founda-
tion (WARF). 
Data Availability Statement 
The datasets analyzed during the current study in 
Section 5 are available in the OpenOOD repository, 
https://github.com/Jingkang50/OpenOOD. 
References 
1. D. Amodei, C. Olah, J. Steinhardt, P. Christiano, 
J. Schulman, and D. Mané, “Concrete problems 
in AI safety,” arXiv preprint arXiv:1606.06565, 
2016. 
2. S. Mohseni, H. Wang, Z. Yu, C. Xiao, Z. Wang, 
and J. Yadawa, “Practical machine learning 
safety: A survey and primer,” arXiv preprint 
arXiv:2106.04823, 2021. 
3. D. Hendrycks, N. Carlini, J. Schulman, and 
J. Steinhardt, “Unsolved problems in ML safety,” 
arXiv preprint arXiv:2109.13916, 2021. 
4. D. Hendrycks and M. Mazeika, “X-risk analysis for 
AI research,” arXiv preprint arXiv:2206.05862, 
2022. 
5. A. Krizhevsky, I. Sutskever, and G. E. Hinton, 
“Imagenet classification with deep convolutional 
neural networks,” in NIPS, 2012. 
6. K. He, X. Zhang, S. Ren, and J. Sun, “Delving 
deep into rectifiers: Surpassing human-level per-
formance on imagenet classification,” in ICCV, 
2015. 
7. N. Drummond and R. Shearer, “The open world 
assumption,” in eSI Workshop, 2006. 
8. D. Hendrycks and K. Gimpel, “A baseline for de-
tecting misclassified and out-of-distribution exam-
ples in neural networks,” in ICLR, 2017. 
9. S. Ben-David, J. Blitzer, K. Crammer, A. Kulesza, 
F. Pereira, and J. W. Vaughan, “A theory of learn-
ing from different domains,” Machine learning, 
2010.
Generalized Out-of-Distribution Detection: A Survey 21 
10. D. Li, Y. Yang, Y.-Z. Song, and T. M. Hospedales, 
“Deeper, broader and artier domain generaliza-
tion,” in ICCV, 2017. 
11. M. Wang and W. Deng, “Deep visual domain 
adaptation: A survey,” Neurocomputing, 2018. 
12. C. C. Aggarwal and P. S. Yu, “Outlier detection 
for high dimensional data,” in ACM SIGMOD, 
2001. 
13. V. Hodge and J. Austin, “A survey of outlier de-
tection methodologies,” Artificial intelligence re-
view, 2004. 
14. I. Ben-Gal, “Outlier detection,” in Data mining 
and knowledge discovery handbook, 2005. 
15. H. Wang, M. J. Bah, and M. Hammad, “Progress 
in outlier detection techniques: A survey,” Ieee Ac-
cess, 2019. 
16. L. Ruff, J. R. Kauffmann, R. A. Vandermeulen, 
G. Montavon, W. Samek, M. Kloft, T. G. Diet-
terich, and K.-R. Müller, “A unifying review of 
deep and shallow anomaly detection,” Proceedings 
of the IEEE, 2021. 
17. G. Pang, C. Shen, L. Cao, and A. v. d. Hengel, 
“Deep learning for anomaly detection: A review,” 
arXiv preprint arXiv:2007.02500, 2020. 
18. S. Bulusu, B. Kailkhura, B. Li, P. K. Varshney, 
and D. Song, “Anomalous example detection in 
deep learning: A survey,” IEEE Access, 2020. 
19. R. Chalapathy and S. Chawla, “Deep learning 
for anomaly detection: A survey,” arXiv preprint 
arXiv:1901.03407, 2019. 
20. M. A. Pimentel, D. A. Clifton, L. Clifton, and 
L. Tarassenko, “A review of novelty detection,” 
Signal Processing, 2014. 
21. D. Miljković, “Review of novelty detection meth-
ods,” in MIPRO, 2010. 
22. M. Markou and S. Singh, “Novelty detection: a re-
view—part 1: statistical approaches,” Signal pro-
cessing, 2003. 
23. M. Markou and S. Singh, “Novelty detection: a re-
view—part 2: neural network based approaches,” 
Signal processing, 2003. 
24. T. E. Boult, S. Cruz, A. R. Dhamija, M. Gunther, 
J. Henrydoss, and W. J. Scheirer, “Learning and 
the unknown: Surveying steps toward open world 
recognition,” in AAAI, 2019. 
25. C. Geng, S.-j. Huang, and S. Chen, “Recent ad-
vances in open set recognition: A survey,” TPAMI, 
2020. 
26. A. Mahdavi and M. Carvalho, “A survey 
on open set recognition,” arXiv preprint 
arXiv:2109.00893, 2021. 
27. I. J. Goodfellow, J. Shlens, and C. Szegedy, “Ex-
plaining and harnessing adversarial examples,” in 
ICLR, 2015. 
28. A. Madry, A. Makelov, L. Schmidt, D. Tsipras, 
and A. Vladu, “Towards deep learning models re-
sistant to adversarial attacks,” ICLR, 2018. 
29. J. Quiñonero-Candela, M. Sugiyama, N. D. 
Lawrence, and A. Schwaighofer, Dataset shift in 
machine learning. Mit Press, 2009. 
30. L. A. Gatys, A. S. Ecker, and M. Bethge, “Im-
age style transfer using convolutional neural net-
works,” in CVPR, 2016. 
31. V. Chandola, A. Banerjee, and V. Kumar, 
“Anomaly detection: A survey,” ACM computing 
surveys (CSUR), vol. 41, no. 3, pp. 1–58, 2009. 
32. F. Ahmed and A. Courville, “Detecting semantic 
anomalies,” in AAAI, 2020. 
33. L. Zhang, M. Goldstein, and R. Ranganath, “Un-
derstanding failures in out-of-distribution detec-
tion with deep generative models,” in ICML, 2021. 
34. N. Akhtar and A. Mian, “Threat of adversarial 
attacks on deep learning in computer vision: A 
survey,” IEEE Access, 2018. 
35. K. Patel, H. Han, and A. K. Jain, “Secure face 
unlock: Spoof detection on smartphones,” IEEE 
transactions on information forensics and secu-
rity, 2016. 
36. D. Wen, H. Han, and A. K. Jain, “Face spoof 
detection with image distortion analysis,” IEEE 
Transactions on Information Forensics and Secu-
rity, 2015. 
37. K. A. Nixon, V. Aimale, and R. K. Rowe, “Spoof 
detection schemes,” in Handbook of biometrics, 
2008. 
38. G. Polatkan, S. Jafarpour, A. Brasoveanu, 
S. Hughes, and I. Daubechies, “Detection of 
forgery in paintings using supervised learning,” in 
ICIP, 2009. 
39. B. Dolhansky, R. Howes, B. Pflaum, N. Baram, 
and C. C. Ferrer, “The deepfake detection chal-
lenge (dfdc) preview dataset,” arXiv preprint 
arXiv:1910.08854, 2019. 
40. L. Jiang, Z. Guo, W. Wu, Z. Liu, Z. Liu, C. C. Loy, 
S. Yang, Y. Xiong, W. Xia, B. Chen, P. Zhuang, 
S. Li, S. Chen, T. Yao, S. Ding, J. Li, F. Huang, 
L. Cao, R. Ji, C. Lu, and G. Tan, “DeeperForen-
sics Challenge 2020 on real-world face forgery 
detection: Methods and results,” arXiv preprint 
arXiv:2102.09471, 2021. 
41. P. Yang, D. Baracchi, R. Ni, Y. Zhao, F. Argenti, 
and A. Piva, “A survey of deep learning-based 
source image forensics,” Journal of Imaging, 2020. 
42. P. Bergmann, M. Fauser, D. Sattlegger, and 
C. Steger, “Mvtec ad–a comprehensive real-world 
dataset for unsupervised anomaly detection,” in
22 Jingkang Yang et al. 
CVPR, 2019. 
43. W.-H. Chu and K. M. Kitani, “Neural batch 
sampling with reinforcement learning for semi-
supervised anomaly detection,” in ECCV, 2020. 
44. D. J. Atha and M. R. Jahanshahi, “Evaluation of 
deep learning approaches based on convolutional 
neural networks for corrosion detection,” Struc-
tural Health Monitoring, 2018. 
45. H. Idrees, M. Shah, and R. Surette, “Enhancing 
camera surveillance using computer vision: a re-
search note,” Policing: An International Journal, 
2018. 
46. C. P. Diehl and J. B. Hampshire, “Real-time ob-
ject classification and novelty detection for collab-
orative video surveillance,” in IJCNN, 2002. 
47. L.-J. Li and L. Fei-Fei, “Optimol: automatic online 
picture collection via incremental model learning,” 
IJCV, 2010. 
48. D. Hendrycks and K. Gimpel, “A baseline for de-
tecting misclassified and out-of-distribution exam-
ples in neural networks,” in ICLR, 2017. 
49. T. Fawcett, “An introduction to roc analysis,” 
Pattern recognition letters, 2006. 
50. D. M. Powers, “Evaluation: from precision, recall 
and f-measure to roc, informedness, markedness 
and correlation,” JMLT, 2020. 
51. H. R. Kerner, D. F. Wellington, K. L. Wagstaff, 
J. F. Bell, C. Kwan, and H. B. Amor, “Novelty de-
tection for multispectral images with application 
to planetary exploration,” in AAAI, 2019. 
52. H. Al-Behadili, A. Grumpe, and C. Wöhler, “In-
cremental learning and novelty detection of ges-
tures in a multi-class system,” in AIMS, 2015. 
53. D. Pathak, P. Agrawal, A. A. Efros, and 
T. Darrell, “Curiosity-driven exploration by self-
supervised prediction,” in ICML, 2017. 
54. P. Perera, R. Nallapati, and B. Xiang, “Ocgan: 
One-class novelty detection using gans with con-
strained latent representations,” in CVPR, 2019. 
55. Y. Xia, X. Cao, F. Wen, G. Hua, and J. Sun, 
“Learning discriminative reconstructions for un-
supervised outlier removal,” in CVPR, 2015. 
56. W. J. Scheirer, A. de Rezende Rocha, A. Sapkota, 
and T. E. Boult, “Toward open set recognition,” 
TPAMI, 2013. 
57. A. R. Dhamija, M. Günther, and T. E. Boult, 
“Reducing network agnostophobia,” in NeurIPS, 
2018. 
58. S. Liu, R. Garrepalli, T. Dietterich, A. Fern, and 
D. Hendrycks, “Open category detection with pac 
guarantees,” in ICML, 2018. 
59. Z. Fang, J. Lu, A. Liu, F. Liu, and G. Zhang, 
“Learning bounds for open-set learning,” in 
ICML, 2021. 
60. E. Sorio, A. Bartoli, G. Davanzo, and E. Medvet, 
“Open world classification of printed invoices,” in 
Proceedings of the 10th ACM symposium on Doc-
ument engineering, 2010. 
61. H. Xu, B. Liu, L. Shu, and P. Yu, “Open-world 
learning and application to product classifica-
tion,” in WWW, 2019. 
62. X. Huang, D. Kroening, W. Ruan, J. Sharp, 
Y. Sun, E. Thamo, M. Wu, and X. Yi, “A sur-
vey of safety and trustworthiness of deep neural 
networks: Verification, testing, adversarial attack 
and defence, and interpretability,” Computer Sci-
ence Review, 2020. 
63. A. Geiger, P. Lenz, and R. Urtasun, “Are we ready 
for autonomous driving? the kitti vision bench-
mark suite,” in CVPR, 2012. 
64. D. Hendrycks, M. Mazeika, and T. Dietterich, 
“Deep anomaly detection with outlier exposure,” 
in ICLR, 2019. 
65. J. Zhang, N. Inkawhich, R. Linderman, Y. Chen, 
and H. Li, “Mixture outlier exposure: Towards 
out-of-distribution detection in fine-grained envi-
ronments,” in Proceedings of the IEEE/CVF Win-
ter Conference on Applications of Computer Vi-
sion (WACV), pp. 5531–5540, January 2023. 
66. D. Hendrycks, S. Basart, M. Mazeika, M. Mosta-
jabi, J. Steinhardt, and D. Song, “Scaling out-of-
distribution detection for real-world settings,” in 
ICML, 2022. 
67. Y.-C. Hsu, Y. Shen, H. Jin, and Z. Kira, “Gen-
eralized odin: Detecting out-of-distribution image 
without learning from out-of-distribution data,” 
in CVPR, 2020. 
68. G. Pleiss, A. Souza, J. Kim, B. Li, and K. Q. Wein-
berger, “Neural network out-of-distribution detec-
tion for regression tasks,” 2019. 
69. O. Vinyals, T. Ewalds, S. Bartunov, P. Georgiev, 
A. S. Vezhnevets, M. Yeo, A. Makhzani, 
H. Küttler, J. Agapiou, J. Schrittwieser, et al., 
“Starcraft ii: A new challenge for reinforcement 
learning,” arXiv preprint arXiv:1708.04782, 2017. 
70. A. Sedlmeier, T. Gabor, T. Phan, L. Belzner, 
and C. Linnhoff-Popien, “Uncertainty-based out-
of-distribution detection in deep reinforcement 
learning,” arXiv preprint arXiv:1901.02219, 2019. 
71. D. Zimmerer, P. M. Full, F. Isensee, P. Jäger, 
T. Adler, J. Petersen, G. Köhler, T. Ross, 
A. Reinke, A. Kascenas, et al., “Mood 2020: A 
public benchmark for out-of-distribution detection 
and localization on medical images,” IEEE Trans-
actions on Medical Imaging, 2022.
Generalized Out-of-Distribution Detection: A Survey 23 
72. M. I. Tariq, N. A. Memon, S. Ahmed, S. Tayyaba, 
M. T. Mushtaq, N. A. Mian, M. Imran, and M. W. 
Ashraf, “A review of deep learning security and 
privacy defensive techniques,” Mobile Information 
Systems, vol. 2020, 2020. 
73. R. Averly and W.-L. Chao, “Unified out-of-
distribution detection: A model-specific perspec-
tive,” arXiv preprint arXiv:2304.06813, 2023. 
74. Wikipedia contributors, “Outlier from Wikipedia, 
the free encyclopedia,” 2021. [Online; accessed 12 
August 2021]. 
75. M. Bianchini, A. Belahcen, and F. Scarselli, “A 
comparative study of inductive and transductive 
learning with feedforward neural networks,” in 
Conference of the Italian Association for Artifi-
cial Intelligence, 2016. 
76. I. Ben-Gal, “Outlier detection,” in Data mining 
and knowledge discovery handbook, 2005. 
77. S. Basu and M. Meckesheimer, “Automatic outlier 
detection for time series: an application to sensor 
data,” Knowledge and Information Systems, 2007. 
78. Y. Dou, W. Li, Z. Liu, Z. Dong, J. Luo, and S. Y. 
Philip, “Uncovering download fraud activities in 
mobile app markets,” in ASONAM, 2019. 
79. T. Xiao, C. Zhang, and H. Zha, “Learning to de-
tect anomalies in surveillance video,” IEEE Signal 
Processing Letters, 2015. 
80. H. Liu, S. Shah, and W. Jiang, “On-line outlier de-
tection and data cleaning,” Computers & chemical 
engineering, 2004. 
81. A. Loureiro, L. Torgo, and C. Soares, “Outlier de-
tection using clustering methods: a data cleaning 
application,” in Proceedings of KDNet Symposium 
on Knowledge-based Systems, 2004. 
82. J. Van den Broeck, S. Argeseanu Cunningham, 
R. Eeckels, and K. Herbst, “Data cleaning: detect-
ing, diagnosing, and editing data abnormalities,” 
PLoS medicine, 2005. 
83. Y. Wang, W. Liu, X. Ma, J. Bailey, H. Zha, 
L. Song, and S.-T. Xia, “Iterative learning with 
open-set noisy labels,” in CVPR, 2018. 
84. X. Chen and A. Gupta, “Webly supervised learn-
ing of convolutional networks,” in ICCV, 2015. 
85. K. Cao, M. Brbic, and J. Leskovec, “Open-
world semi-supervised learning,” arXiv preprint 
arXiv:2102.03526, 2021. 
86. P. L. Bartlett and M. H. Wegkamp, “Classification 
with a reject option using a hinge loss.,” Journal 
of Machine Learning Research, vol. 9, no. 8, 2008. 
87. C. Chow, “On optimum recognition error and re-
ject tradeoff,” IEEE Transactions on Information 
Theory, 1970. 
88. G. Fumera and F. Roli, “Support vector machines 
with embedded reject option,” in International 
Workshop on Support Vector Machines, 2002. 
89. C. Cortes and V. Vapnik, “Support-vector net-
works,” Machine learning, 1995. 
90. A. Nguyen, J. Yosinski, and J. Clune, “Deep neu-
ral networks are easily fooled: High confidence 
predictions for unrecognizable images,” in CVPR, 
2015. 
91. K. Zhou, Z. Liu, Y. Qiao, T. Xiang, and C. C. Loy, 
“Domain generalization: A survey,” arXiv preprint 
arXiv:2103.02503, 2021. 
92. Z. Liu, Z. Miao, X. Pan, X. Zhan, D. Lin, S. X. 
Yu, and B. Gong, “Open compound domain adap-
tation,” in CVPR, 2020. 
93. K. Han, A. Vedaldi, and A. Zisserman, “Learning 
to discover novel visual categories via deep trans-
fer clustering,” in CVPR, 2019. 
94. B. Zhao and K. Han, “Novel visual category dis-
covery with dual ranking statistics and mutual 
knowledge distillation,” NeurIPS, 2021. 
95. X. Jia, K. Han, Y. Zhu, and B. Green, “Joint rep-
resentation learning and novel category discovery 
on single-and multi-modal data,” in ICCV, 2021. 
96. S. Vaze, K. Han, A. Vedaldi, and A. Zisserman, 
“Generalized category discovery,” in CVPR, 2022. 
97. K. Joseph, S. Paul, G. Aggarwal, S. Biswas, P. Rai, 
K. Han, and V. N. Balasubramanian, “Novel class 
discovery without forgetting,” in ECCV, 2022. 
98. W. Wang, V. W. Zheng, H. Yu, and C. Miao, “A 
survey of zero-shot learning: Settings, methods, 
and applications,” TIST, 2019. 
99. A. Bendale and T. Boult, “Towards open world 
recognition,” in CVPR, 2015. 
100. Z. Liu, Z. Miao, X. Zhan, J. Wang, B. Gong, and 
S. X. Yu, “Large-scale long-tailed recognition in 
an open world,” in CVPR, 2019. 
101. J. Parmar, S. Chouhan, V. Raychoudhury, and 
S. Rathore, “Open-world machine learning: ap-
plications, challenges, and opportunities,” ACM 
Computing Surveys, vol. 55, no. 10, pp. 1–37, 2023. 
102. G. Shafer and V. Vovk, “A tutorial on confor-
mal prediction.,” Journal of Machine Learning 
Research, vol. 9, no. 3, 2008. 
103. A. N. Angelopoulos and S. Bates, “A gentle intro-
duction to conformal prediction and distribution-
free uncertainty quantification,” arXiv preprint 
arXiv:2107.07511, 2021. 
104. R. Kaur, S. Jha, A. Roy, S. Park, E. Dobriban, 
O. Sokolsky, and I. Lee, “idecode: In-distribution 
equivariance for conformal out-of-distribution de-
tection,” in Proceedings of the AAAI Conference 
on Artificial Intelligence, vol. 36, pp. 7104–7114,
24 Jingkang Yang et al. 
2022. 
105. R. Kaur, K. Sridhar, S. Park, S. Jha, A. Roy, 
O. Sokolsky, and I. Lee, “Codit: Conformal out-of-
distribution detection in time-series data,” arXiv 
e-prints, 2022. 
106. F. Cai, A. I. Ozdagli, N. Potteiger, and X. Kout-
soukos, “Inductive conformal out-of-distribution 
detection based on adversarial autoencoders,” in 
2021 IEEE International Conference on Omni-
Layer Intelligent Systems (COINS), pp. 1–6, 
IEEE, 2021. 
107. M. Salehi, H. Mirzaei, D. Hendrycks, Y. Li, 
M. H. Rohban, and M. Sabokrou, “A unified sur-
vey on anomaly, novelty, open-set, and out-of-
distribution detection: Solutions and future chal-
lenges,” arXiv preprint arXiv:2110.14051, 2021. 
108. S. Liang, Y. Li, and R. Srikant, “Enhancing the 
reliability of out-of-distribution image detection in 
neural networks,” in ICLR, 2018. 
109. K. Lee, K. Lee, H. Lee, and J. Shin, “A simple uni-
fied framework for detecting out-of-distribution 
samples and adversarial attacks,” in NeurIPS, 
2018. 
110. W. Liu, X. Wang, J. D. Owens, and Y. Li, 
“Energy-based out-of-distribution detection,” in 
NeurIPS, 2020. 
111. C. S. Sastry and S. Oore, “Detecting out-of-
distribution examples with gram matrices,” in 
ICML, 2020. 
112. H. Wang, W. Liu, A. Bocchieri, and Y. Li, “Can 
multi-label classification networks know what they 
don’t know?,” NeurIPS, 2021. 
113. J. Zhang, Q. Fu, X. Chen, L. Du, Z. Li, G. Wang, 
S. Han, D. Zhang, et al., “Out-of-distribution 
detection based on in-distribution data patterns 
memorization with modern hopfield energy,” in 
ICLR, 2023. 
114. Y. Sun, C. Guo, and Y. Li, “React: Out-of-
distribution detection with rectified activations,” 
in NeurIPS, 2021. 
115. X. Dong, J. Guo, A. Li, W.-T. Ting, C. Liu, and 
H. Kung, “Neural mean discrepancy for efficient 
out-of-distribution detection,” in CVPR, 2022. 
116. Y. Sun and Y. Li, “Dice: Leveraging sparsification 
for out-of-distribution detection,” in ECCV, 2022. 
117. Y. Sun, Y. Ming, X. Zhu, and Y. Li, “Out-of-
distribution detection with deep nearest neigh-
bors,” in ICML, 2022. 
118. Z. Lin, S. D. Roy, and Y. Li, “Mood: Multi-level 
out-of-distribution detection,” in CVPR, 2021. 
119. C. S. Sastry and S. Oore, “Detecting out-of-
distribution examples with in-distribution exam-
ples and gram matrices,” in NeurIPS-W, 2019. 
120. A. Djurisic, N. Bozanic, A. Ashok, and R. Liu, 
“Extremely simple activation shaping for out-of-
distribution detection,” ICLR, 2023. 
121. J. Park, Y. G. Jung, and A. B. J. Teoh, “Nearest 
neighbor guidance for out-of-distribution detec-
tion,” in Proceedings of the IEEE/CVF Interna-
tional Conference on Computer Vision, pp. 1686– 
1695, 2023. 
122. J. Park, J. C. L. Chai, J. Yoon, and A. B. J. 
Teoh, “Understanding the feature norm for out-
of-distribution detection,” in Proceedings of the 
IEEE/CVF International Conference on Com-
puter Vision, pp. 1557–1567, 2023. 
123. X. Jiang, F. Liu, Z. Fang, H. Chen, T. Liu, 
F. Zheng, and B. Han, “Detecting out-of-
distribution data through in-distribution class 
prior,” in International Conference on Machine 
Learning, pp. 15067–15088, PMLR, 2023. 
124. X. Liu, Y. Lochman, and C. Zach, “Gen: Push-
ing the limits of softmax-based out-of-distribution 
detection,” in Proceedings of the IEEE/CVF Con-
ference on Computer Vision and Pattern Recogni-
tion, pp. 23946–23955, 2023. 
125. T. DeVries and G. W. Taylor, “Learning con-
fidence for out-of-distribution detection in neu-
ral networks,” arXiv preprint arXiv:1802.04865, 
2018. 
126. Y. Wang, B. Li, T. Che, K. Zhou, Z. Liu, 
and D. Li, “Energy-based open-world uncertainty 
modeling for confidence calibration,” in ICCV, 
2021. 
127. A. Vyas, N. Jammalamadaka, X. Zhu, D. Das, 
B. Kaul, and T. L. Willke, “Out-of-distribution 
detection using an ensemble of self supervised 
leave-out classifiers,” in ECCV, 2018. 
128. J. Bitterwolf, A. Meinke, and M. Hein, “Cer-
tifiably adversarially robust detection of out-of-
distribution data,” in NeurIPS, 2020. 
129. J. Chen, Y. Li, X. Wu, Y. Liang, and S. Jha, “Ro-
bust out-of-distribution detection for neural net-
works,” arXiv preprint arXiv:2003.09711, 2020. 
130. M. Hein, M. Andriushchenko, and J. Bitterwolf, 
“Why relu networks yield high-confidence predic-
tions far away from the training data and how to 
mitigate the problem,” in CVPR, 2019. 
131. S. Choi and S.-Y. Chung, “Novelty detection via 
blurring,” in ICLR, 2020. 
132. J. Chen, Y. Li, X. Wu, Y. Liang, and S. Jha, 
“Atom: Robustifying out-of-distribution detection 
using outlier mining,” ECML&PKDD, 2021. 
133. M. Hein, M. Andriushchenko, and J. Bitterwolf, 
“Why relu networks yield high-confidence predic-
tions far away from the training data and how to
Generalized Out-of-Distribution Detection: A Survey 25 
mitigate the problem,” in CVPR, 2019. 
134. S. Thulasidasan, G. Chennupati, J. Bilmes, 
T. Bhattacharya, and S. Michalak, “On mixup 
training: Improved calibration and predictive un-
certainty for deep neural networks,” in NeurIPS, 
2019. 
135. S. Yun, D. Han, S. J. Oh, S. Chun, J. Choe, 
and Y. Yoo, “Cutmix: Regularization strategy to 
train strong classifiers with localizable features,” 
in CVPR, 2019. 
136. T. DeVries and G. W. Taylor, “Improved regu-
larization of convolutional neural networks with 
cutout,” arXiv preprint arXiv:1708.04552, 2017. 
137. D. Hendrycks, N. Mu, E. D. Cubuk, B. Zoph, 
J. Gilmer, and B. Lakshminarayanan, “Aug-
mix: A simple data processing method to im-
prove robustness and uncertainty,” arXiv preprint 
arXiv:1912.02781, 2019. 
138. D. Hendrycks, A. Zou, M. Mazeika, L. Tang, 
D. Song, and J. Steinhardt, “Pixmix: Dream-
like pictures comprehensively improve safety mea-
sures,” 2022. 
139. J. Tack, S. Mo, J. Jeong, and J. Shin, “Csi: Novelty 
detection via contrastive learning on distribution-
ally shifted instances,” in NeurIPS, 2020. 
140. A. Meinke and M. Hein, “Towards neural networks 
that provably know when they don’t know,” arXiv 
preprint arXiv:1909.12180, 2019. 
141. K. Bibas, M. Feder, and T. Hassner, “Single 
layer predictive normalized maximum likelihood 
for out-of-distribution detection,” NeurIPS, 2021. 
142. Q. Wang, F. Liu, Y. Zhang, J. Zhang, C. Gong, 
T. Liu, and B. Han, “Watermarking for out-of-
distribution detection,” in NeurIPS, 2022. 
143. X. Dong, J. Guo, W.-T. T. Ang Li23, C. Liu, and 
H. Kung, “Neural mean discrepancy for efficient 
out-of-distribution detection,” in CVPR, 2022. 
144. H. Wei, R. Xie, H. Cheng, L. Feng, B. An, and 
Y. Li, “Mitigating neural network overconfidence 
with logit normalization,” in ICML, 2022. 
145. K. Lee, K. Lee, K. Min, Y. Zhang, J. Shin, and 
H. Lee, “Hierarchical novelty detection for visual 
object recognition,” in CVPR, 2018. 
146. R. Huang and Y. Li, “Mos: Towards scaling out-
of-distribution detection for large semantic space,” 
in CVPR, 2021. 
147. R. Linderman, J. Zhang, N. Inkawhich, H. Li, 
and Y. Chen, “Fine-grain inference on out-of-
distribution data with hierarchical classification,” 
in Proceedings of The 2nd Conference on Life-
long Learning Agents (S. Chandar, R. Pascanu, 
H. Sedghi, and D. Precup, eds.), vol. 232 of Pro-
ceedings of Machine Learning Research, pp. 162– 
183, PMLR, 22–25 Aug 2023. 
148. G. Shalev, Y. Adi, and J. Keshet, “Out-of-
distribution detection using multiple semantic la-
bel representations,” in NeurIPS, 2018. 
149. S. Fort, J. Ren, and B. Lakshminarayanan, “Ex-
ploring the limits of out-of-distribution detec-
tion,” NeurIPS, 2021. 
150. W. Gan, “Language guided out-of-distribution de-
tection,” 2021. 
151. Q. Yu and K. Aizawa, “Unsupervised out-of-
distribution detection by maximum classifier dis-
crepancy,” in ICCV, 2019. 
152. S. Mohseni, M. Pitale, J. Yadawa, and Z. Wang, 
“Self-supervised learning for generalizable out-of-
distribution detection,” in AAAI, 2020. 
153. S. Thulasidasan, S. Thapa, S. Dhaubhadel, 
G. Chennupati, T. Bhattacharya, and J. Bilmes, 
“An effective baseline for robustness to distri-
butional shift,” arXiv preprint arXiv:2105.07107, 
2021. 
154. A.-A. Papadopoulos, M. R. Rajati, N. Shaikh, and 
J. Wang, “Outlier exposure with confidence con-
trol for out-of-distribution detection,” Neurocom-
puting, 2021. 
155. Y. Ming, Y. Fan, and Y. Li, “Poem: Out-of-
distribution detection with posterior sampling,” in 
ICML, 2022. 
156. Y. Li and N. Vasconcelos, “Background data 
resampling for outlier-aware classification,” in 
CVPR, 2020. 
157. S. Mohseni, M. Pitale, J. Yadawa, and Z. Wang, 
“Self-supervised learning for generalizable out-of-
distribution detection,” in AAAI, 2020. 
158. J. Yang, H. Wang, L. Feng, X. Yan, H. Zheng, 
W. Zhang, and Z. Liu, “Semantically coherent 
out-of-distribution detection,” in ICCV, 2021. 
159. F. Lu, K. Zhu, W. Zhai, K. Zheng, and Y. Cao, 
“Uncertainty-aware optimal transport for seman-
tically coherent out-of-distribution detection,” 
in Proceedings of the IEEE/CVF Conference 
on Computer Vision and Pattern Recognition, 
pp. 3282–3291, 2023. 
160. A. Shafaei, M. Schmidt, and J. J. Little, “A less 
biased evaluation of out-of-distribution sample de-
tectors,” in BMVC, 2019. 
161. J. Katz-Samuels, J. Nakhleh, R. Nowak, and Y. Li, 
“Training ood detectors in their natural habitats,” 
in International Conference on Machine Learning 
(ICML), PMLR, 2022. 
162. Q. Wang, Z. Fang, Y. Zhang, F. Liu, Y. Li, 
and B. Han, “Learning to augment distributions 
for out-of-distribution detection,” arXiv preprint 
arXiv:2311.01796, 2023.
26 Jingkang Yang et al. 
163. K. Lee, H. Lee, K. Lee, and J. Shin, “Training 
confidence-calibrated classifiers for detecting out-
of-distribution samples,” 2018. 
164. S. Vernekar, A. Gaurav, V. Abdelzad, T. De-
nouden, R. Salay, and K. Czarnecki, “Out-of-
distribution detection in classifiers via genera-
tion,” in NeurIPS-W, 2019. 
165. K. Sricharan and A. Srivastava, “Building robust 
classifiers through generation of confident out of 
distribution examples,” in NeurIPS-W, 2018. 
166. T. Jeong and H. Kim, “Ood-maml: Meta-learning 
for few-shot out-of-distribution detection and clas-
sification,” in NeurIPS, 2020. 
167. X. Du, Z. Wang, M. Cai, and Y. Li, “Vos: Learning 
what you don’t know by virtual outlier synthesis,” 
in Proceedings of the International Conference on 
Learning Representations, 2022. 
168. L. Tao, X. Du, X. Zhu, and Y. Li, “Non-
parametric outlier synthesis,” in ICLR, 2023. 
169. Q. Wang, J. Ye, F. Liu, Q. Dai, M. Kalander, 
T. Liu, J. Hao, and B. Han, “Out-of-distribution 
detection with implicit outlier transformation,” 
2023. 
170. H. Zheng, Q. Wang, Z. Fang, X. Xia, F. Liu, 
T. Liu, and B. Han, “Out-of-distribution detec-
tion learning with unreliable out-of-distribution 
sources,” in NeurIPS, 2023. 
171. X. Du, X. Wang, G. Gozum, and Y. Li, 
“Unknown-aware object detection: Learning what 
you don’t know from videos in the wild,” in Pro-
ceedings of the IEEE/CVF Conference on Com-
puter Vision and Pattern Recognition, 2022. 
172. R. Huang, A. Geng, and Y. Li, “On the im-
portance of gradients for detecting distributional 
shifts in the wild,” in NeurIPS, 2021. 
173. C. Igoe, Y. Chung, I. Char, and J. Schneider, 
“How useful are gradients for ood detection re-
ally?,” arXiv preprint arXiv:2205.10439, 2022. 
174. Y. Gal and Z. Ghahramani, “Dropout as a 
bayesian approximation: Representing model un-
certainty in deep learning,” in ICML, 2016. 
175. B. Lakshminarayanan, A. Pritzel, and C. Blun-
dell, “Simple and scalable predictive uncertainty 
estimation using deep ensembles,” NeurIPS, 2017. 
176. K. Osawa, S. Swaroop, A. Jain, R. Eschenhagen, 
R. E. Turner, R. Yokota, and M. E. Khan, “Prac-
tical deep learning with bayesian principles,” in 
NeurIPS, 2019. 
177. A. Malinin and M. Gales, “Predictive uncertainty 
estimation via prior networks,” in NeurIPS, 2018. 
178. A. Malinin and M. Gales, “Reverse kl-divergence 
training of prior networks: Improved uncertainty 
and adversarial robustness,” in NeurIPS, 2019. 
179. J. Nandy, W. Hsu, and M. L. Lee, “Towards max-
imizing the representation gap between in-domain 
& out-of-distribution examples,” in NeurIPS, 
2020. 
180. K. Kim, J. Shin, and H. Kim, “Locally most 
powerful bayesian test for out-of-distribution de-
tection using deep generative models,” NeurIPS, 
2021. 
181. D. Hendrycks, K. Lee, and M. Mazeika, “Using 
pre-training can improve model robustness and 
uncertainty,” in International conference on ma-
chine learning, pp. 2712–2721, PMLR, 2019. 
182. D. Hendrycks, X. Liu, E. Wallace, A. Dziedzic, 
R. Krishnan, and D. Song, “Pretrained transform-
ers improve out-of-distribution robustness,” arXiv 
preprint arXiv:2004.06100, 2020. 
183. Y. Ming and Y. Li, “How does fine-tuning impact 
out-of-distribution detection for vision-language 
models?,” IJCV, 2023. 
184. A. Miyai, Q. Yu, G. Irie, and K. Aizawa, 
“Can pre-trained networks detect familiar 
out-of-distribution data?,” arXiv preprint 
arXiv:2310.00847, 2023. 
185. A. Miyai, Q. Yu, G. Irie, and K. Aizawa, “Locoop: 
Few-shot out-of-distribution detection via prompt 
learning,” arXiv preprint arXiv:2306.01293, 2023. 
186. F. Lu, K. Zhu, K. Zheng, W. Zhai, and Y. Cao, 
“Likelihood-aware semantic alignment for full-
spectrum out-of-distribution detection,” arXiv 
preprint arXiv:2312.01732, 2023. 
187. S. Esmaeilpour, B. Liu, E. Robertson, and L. Shu, 
“Zero-shot out-of-distribution detection based on 
the pretrained model clip,” in AAAI, 2022. 
188. Y. Ming, Z. Cai, J. Gu, Y. Sun, W. Li, and 
Y. Li, “Delving into out-of-distribution detection 
with vision-language representations,” Advances 
in Neural Information Processing Systems, vol. 35, 
pp. 35087–35102, 2022. 
189. H. Wang, Y. Li, H. Yao, and X. Li, “Clipn for zero-
shot ood detection: Teaching clip to say no,” in 
Proceedings of the IEEE/CVF International Con-
ference on Computer Vision, pp. 1802–1812, 2023. 
190. B. Zong, Q. Song, M. R. Min, W. Cheng, 
C. Lumezanu, D. Cho, and H. Chen, “Deep au-
toencoding gaussian mixture model for unsuper-
vised anomaly detection,” in ICLR, 2018. 
191. D. Abati, A. Porrello, S. Calderara, and R. Cuc-
chiara, “Latent space autoregression for novelty 
detection,” in CVPR, 2019. 
192. S. Pidhorskyi, R. Almohsen, D. A. Adjeroh, 
and G. Doretto, “Generative probabilistic nov-
elty detection with adversarial autoencoders,” in 
NeurIPS, 2018.
Generalized Out-of-Distribution Detection: A Survey 27 
193. L. Deecke, R. Vandermeulen, L. Ruff, S. Mandt, 
and M. Kloft, “Image anomaly detection with gen-
erative adversarial networks,” in ECML&KDD, 
2018. 
194. M. Sabokrou, M. Khalooei, M. Fathy, and 
E. Adeli, “Adversarially learned one-class classi-
fier for novelty detection,” in CVPR, 2018. 
195. I. Kobyzev, S. Prince, and M. Brubaker, “Normal-
izing flows: An introduction and review of current 
methods,” TPAMI, 2020. 
196. E. Zisselman and A. Tamar, “Deep residual flow 
for out of distribution detection,” in CVPR, 2020. 
197. D. P. Kingma and P. Dhariwal, “Glow: Generative 
flow with invertible 1x1 convolutions,” NeurIPS, 
2018. 
198. A. Van Oord, N. Kalchbrenner, and 
K. Kavukcuoglu, “Pixel recurrent neural net-
works,” in ICML, 2016. 
199. D. Jiang, S. Sun, and Y. Yu, “Revisiting flow gen-
erative models for out-of-distribution detection,” 
in International Conference on Learning Repre-
sentations, 2021. 
200. E. Nalisnick, A. Matsukawa, Y. W. Teh, D. Gorur, 
and B. Lakshminarayanan, “Do deep genera-
tive models know what they don’t know?,” in 
NeurIPS, 2018. 
201. H. Choi, E. Jang, and A. A. Alemi, “Waic, but 
why? generative ensembles for robust anomaly de-
tection,” arXiv preprint arXiv:1810.01392, 2018. 
202. P. Kirichenko, P. Izmailov, and A. G. Wilson, 
“Why normalizing flows fail to detect out-of-
distribution data,” in NeurIPS, 2020. 
203. J. Ren, P. J. Liu, E. Fertig, J. Snoek, R. Poplin, 
M. A. DePristo, J. V. Dillon, and B. Lak-
shminarayanan, “Likelihood ratios for out-of-
distribution detection,” in NeurIPS, 2019. 
204. J. Serrà, D. Álvarez, V. Gómez, O. Slizovskaia, 
J. F. Núñez, and J. Luque, “Input complexity 
and out-of-distribution detection with likelihood-
based generative models,” 2020. 
205. Z. Xiao, Q. Yan, and Y. Amit, “Likelihood regret: 
An out-of-distribution detection score for varia-
tional auto-encoder,” in NeurIPS, 2020. 
206. H. Wang, Z. Li, L. Feng, and W. Zhang, “Vim: 
Out-of-distribution with virtual-logit matching,” 
in Proceedings of the IEEE/CVF Conference on 
Computer Vision and Pattern Recognition, 2022. 
207. J. Ren, S. Fort, J. Liu, A. G. Roy, S. Padhy, 
and B. Lakshminarayanan, “A simple fix to ma-
halanobis distance for improving near-ood detec-
tion,” arXiv preprint arXiv:2106.09022, 2021. 
208. E. Techapanurak, M. Suganuma, and T. Okatani, 
“Hyperparameter-free out-of-distribution detec-
tion using cosine similarity,” in ACCV, 2020. 
209. X. Chen, X. Lan, F. Sun, and N. Zheng, “A bound-
ary based out-of-distribution classifier for general-
ized zero-shot learning,” in ECCV, 2020. 
210. A. Zaeemzadeh, N. Bisagno, Z. Sambugaro, 
N. Conci, N. Rahnavard, and M. Shah, “Out-
of-distribution detection using union of 1-
dimensional subspaces,” in CVPR, 2021. 
211. J. Van Amersfoort, L. Smith, Y. W. Teh, and 
Y. Gal, “Uncertainty estimation using a single 
deep deterministic neural network,” in ICML, 
2020. 
212. H. Huang, Z. Li, L. Wang, S. Chen, B. Dong, 
and X. Zhou, “Feature space singularity for 
out-of-distribution detection,” arXiv preprint 
arXiv:2011.14654, 2020. 
213. Y. Ming, Y. Sun, O. Dia, and Y. Li, “Cider: 
Exploiting hyperspherical embeddings for out-of-
distribution detection,” in ICLR, 2023. 
214. J.-H. Kim, S. Yun, and H. O. Song, “Neural re-
lation graph: A unified framework for identifying 
label noise and outlier data,” in Thirty-seventh 
Conference on Neural Information Processing Sys-
tems, 2023. 
215. T. Denouden, R. Salay, K. Czarnecki, V. Ab-
delzad, B. Phan, and S. Vernekar, “Improv-
ing reconstruction autoencoder out-of-distribution 
detection with mahalanobis distance,” arXiv 
preprint arXiv:1812.02765, 2018. 
216. Y. Zhou, “Rethinking reconstruction 
autoencoder-based out-of-distribution detec-
tion,” in CVPR, 2022. 
217. Y. Yang, R. Gao, and Q. Xu, “Out-of-distribution 
detection with semantic mismatch under mask-
ing,” in ECCV, 2022. 
218. W. Jiang, H. Cheng, M. Chen, S. Feng, Y. Ge, 
and C. Wang, “Read: Aggregating reconstruction 
error into out-of-distribution detection,” in AAAI, 
2023. 
219. J. Li, P. Chen, S. Yu, Z. He, S. Liu, and J. Jia, 
“Rethinking out-of-distribution (ood) detection: 
Masked image modeling is all you need,” in 
CVPR, 2023. 
220. P. Morteza and Y. Li, “Provable guarantees for 
understanding out-of-distribution detection,” in 
AAAI, 2022. 
221. L. P. Jain, W. J. Scheirer, and T. E. Boult, “Multi-
class open set recognition using probability of in-
clusion,” in ECCV, 2014. 
222. E. M. Rudd, L. P. Jain, W. J. Scheirer, and T. E. 
Boult, “The extreme value machine,” IEEE trans-
actions on pattern analysis and machine intelli-
gence, vol. 40, no. 3, pp. 762–768, 2017.
28 Jingkang Yang et al. 
223. Z. Fang, Y. Li, J. Lu, J. Dong, B. Han, and F. Liu, 
“Is out-of-distribution detection learnable?,” in 
NeurIPS, 2022. 
224. A. Radford, J. W. Kim, C. Hallacy, A. Ramesh, 
G. Goh, S. Agarwal, G. Sastry, A. Askell, 
P. Mishkin, J. Clark, et al., “Learning transferable 
visual models from natural language supervision,” 
in ICML, 2021. 
225. E. T. Jaynes, “Bayesian methods: General back-
ground,” 1986. 
226. R. M. Neal, Bayesian learning for neural net-
works. 2012. 
227. D. Gamerman and H. F. Lopes, Markov chain 
Monte Carlo: stochastic simulation for Bayesian 
inference. CRC Press, 2006. 
228. D. J. C. Mackay, Bayesian methods for adaptive 
models. PhD thesis, California Institute of Tech-
nology, 1992. 
229. A. Y. Foong, Y. Li, J. M. Hernández-Lobato, 
and R. E. Turner, “’in-between’ uncertainty in 
bayesian neural networks,” in ICML-W, 2020. 
230. C. Peterson and E. Hartman, “Explorations of the 
mean field theory learning algorithm,”Neural Net-
works, 1989. 
231. F. Wenzel, K. Roth, B. S. Veeling, J. Światkowski, 
L. Tran, S. Mandt, J. Snoek, T. Salimans, R. Je-
natton, and S. Nowozin, “How good is the bayes 
posterior in deep neural networks really?,” in 
ICML, 2020. 
232. A. Gelman, “Objections to bayesian statistics,” 
Bayesian Analysis, 2008. 
233. T. G. Dietterich, “Ensemble methods in machine 
learning,” in International workshop on multiple 
classifier systems, 2000. 
234. W. J. Maddox, P. Izmailov, T. Garipov, D. P. 
Vetrov, and A. G. Wilson, “A simple baseline for 
bayesian uncertainty in deep learning,” Advances 
in Neural Information Processing Systems, vol. 32, 
pp. 13153–13164, 2019. 
235. R. Bommasani, D. A. Hudson, E. Adeli, R. Alt-
man, S. Arora, S. von Arx, M. S. Bernstein, 
J. Bohg, A. Bosselut, E. Brunskill, et al., “On 
the opportunities and risks of foundation models,” 
arXiv preprint arXiv:2108.07258, 2021. 
236. K. Zhou, J. Yang, C. C. Loy, and Z. Liu, “Learning 
to prompt for vision-language models,” Interna-
tional Journal of Computer Vision (IJCV), 2022. 
237. K. Zhou, J. Yang, C. C. Loy, and Z. Liu, “Con-
ditional prompt learning for vision-language mod-
els,” in IEEE/CVF Conference on Computer Vi-
sion and Pattern Recognition (CVPR), 2022. 
238. M. Jia, L. Tang, B.-C. Chen, C. Cardie, S. Be-
longie, B. Hariharan, and S.-N. Lim, “Visual 
prompt tuning,” in European Conference on Com-
puter Vision, pp. 709–727, Springer, 2022. 
239. P. Gao, S. Geng, R. Zhang, T. Ma, R. Fang, 
Y. Zhang, H. Li, and Y. Qiao, “Clip-adapter: Bet-
ter vision-language models with feature adapters,” 
International Journal of Computer Vision, pp. 1– 
15, 2023. 
240. J. Yang, K. Zhou, and Z. Liu, “Full-spectrum 
out-of-distribution detection,” arXiv preprint 
arXiv:2204.05306, 2022. 
241. E. D. C. Gomes, F. Alberge, P. Duhamel, and 
P. Piantanida, “Igeood: An information geome-
try approach to out-of-distribution detection,” in 
ICLR, 2022. 
242. W. J. Scheirer, L. P. Jain, and T. E. Boult, “Prob-
ability models for open set recognition,” TPAMI, 
2014. 
243. R. L. Smith, “Extreme value theory,” Handbook of 
applicable mathematics, 1990. 
244. E. Castillo, Extreme value theory in engineering. 
Elsevier, 2012. 
245. A. Bendale and T. E. Boult, “Towards open set 
deep networks,” in CVPR, 2016. 
246. P. Perera and V. M. Patel, “Deep transfer learning 
for multiple class novelty detection,” in CVPR, 
2019. 
247. P. Perera, V. I. Morariu, R. Jain, V. Manju-
natha, C. Wigington, V. Ordonez, and V. M. Pa-
tel, “Generative-discriminative feature representa-
tions for open-set recognition,” in CVPR, 2020. 
248. X. Sun, H. Ding, C. Zhang, G. Lin, and 
K.-V. Ling, “M2iosr: Maximal mutual infor-
mation open set recognition,” arXiv preprint 
arXiv:2108.02373, 2021. 
249. Z. Ge, S. Demyanov, Z. Chen, and R. Garnavi, 
“Generative openmax for multi-class open set clas-
sification,” in BMVC, 2017. 
250. L. Neal, M. Olson, X. Fern, W.-K. Wong, and 
F. Li, “Open set learning with counterfactual im-
ages,” in ECCV, 2018. 
251. D.-W. Zhou, H.-J. Ye, and D.-C. Zhan, “Learning 
placeholders for open-set recognition,” in CVPR, 
2021. 
252. S. Kong and D. Ramanan, “Opengan: Open-set 
recognition via open data generation,” in ICCV, 
2021. 
253. C. Geng and S. Chen, “Collective decision for open 
set recognition,” TKDE, 2020. 
254. J. Jang and C. O. Kim, “One-vs-rest network-
based deep probability model for open set recog-
nition,” arXiv preprint arXiv:2004.08067, 2020. 
255. P. Schlachter, Y. Liao, and B. Yang, “Open-set 
recognition using intra-class splitting,” in EU-
Generalized Out-of-Distribution Detection: A Survey 29 
SIPCO, 2019. 
256. M. Masana, I. Ruiz, J. Serrat, J. van de Weijer, 
and A. M. Lopez, “Metric learning for novelty and 
anomaly detection,” in BMVC, 2018. 
257. Y. Shu, Y. Shi, Y. Wang, T. Huang, and Y. Tian, 
“p-odn: prototype-based open deep network for 
open set recognition,” Scientific reports, 2020. 
258. B. Liu, H. Kang, H. Li, G. Hua, and N. Vascon-
celos, “Few-shot open-set recognition using meta-
learning,” in CVPR, 2020. 
259. G. Chen, L. Qiao, Y. Shi, P. Peng, J. Li, T. Huang, 
S. Pu, and Y. Tian, “Learning open set network 
with discriminative reciprocal points,” in ECCV, 
2020. 
260. R. Yoshihashi, W. Shao, R. Kawakami, S. You, 
M. Iida, and T. Naemura, “Classification-
reconstruction learning for open-set recognition,” 
in CVPR, 2019. 
261. A. Cao, Y. Luo, and D. Klabjan, “Open-set recog-
nition with gaussian mixture variational autoen-
coders,” AAAI, 2020. 
262. P. R. M. Júnior, R. M. De Souza, R. d. O. 
Werneck, B. V. Stein, D. V. Pazinato, W. R. 
de Almeida, O. A. Penatti, R. d. S. Torres, and 
A. Rocha, “Nearest neighbors distance ratio open-
set classifier,” Machine Learning, 2017. 
263. H. Zhang and V. M. Patel, “Sparse representation-
based open set recognition,” TPAMI, 2016. 
264. P. Bodesheim, A. Freytag, E. Rodner, M. Kemm-
ler, and J. Denzler, “Kernel null space methods 
for novelty detection,” in CVPR, 2013. 
265. J. Liu, Z. Lian, Y. Wang, and J. Xiao, “Incre-
mental kernel null space discriminant analysis for 
novelty detection,” in CVPR, 2017. 
266. P. Oza and V. M. Patel, “C2ae: Class conditioned 
auto-encoder for open-set recognition,” in CVPR, 
2019. 
267. X. Sun, Z. Yang, C. Zhang, K.-V. Ling, and 
G. Peng, “Conditional gaussian distribution learn-
ing for open set recognition,” in CVPR, 2020. 
268. Z. Yue, T. Wang, Q. Sun, X.-S. Hua, and 
H. Zhang, “Counterfactual zero-shot and open-set 
visual recognition,” in CVPR, 2021. 
269. R. Shao, P. Perera, P. C. Yuen, and V. M. Patel, 
“Open-set adversarial defense,” in ECCV, 2020. 
270. H. Zhang, A. Li, J. Guo, and Y. Guo, “Hybrid 
models for open set recognition,” in ECCV, 2020. 
271. S. Vaze, K. Han, A. Vedaldi, and A. Zisserman, 
“Open-set recognition: A good closed-set classifier 
is all you need,” in ICLR, 2022. 
272. G. Danuser and M. Stricker, “Parametric model 
fitting: From inlier characterization to outlier de-
tection,” TPAMI, 1998. 
273. R. De Maesschalck, D. Jouan-Rimbaud, and D. L. 
Massart, “The mahalanobis distance,” Chemo-
metrics and intelligent laboratory systems, 2000. 
274. C. Leys, O. Klein, Y. Dominicy, and C. Ley, “De-
tecting multivariate outliers: Use a robust variant 
of the mahalanobis distance,” Journal of Experi-
mental Social Psychology, 2018. 
275. R. A. Redner and H. F. Walker, “Mixture densi-
ties, maximum likelihood and the em algorithm,” 
SIAM review, 1984. 
276. E. Eskin, “Anomaly detection over noisy data us-
ing learned probability distributions,” in ICML, 
2000. 
277. M. Turcotte, J. Moore, N. Heard, and A. McPhall, 
“Poisson factorization for peer-based anomaly de-
tection,” in IEEE Conference on Intelligence and 
Security Informatics (ISI), 2016. 
278. A. J. Izenman, “Review papers: Recent devel-
opments in nonparametric density estimation,” 
Journal of the American Statistical Association, 
1991. 
279. J. Van Ryzin, “A histogram method of density es-
timation,” Communications in Statistics-Theory 
and Methods, 1973. 
280. M. Xie, J. Hu, and B. Tian, “Histogram-based 
online anomaly detection in hierarchical wireless 
sensor networks,” in ICTSPCC, 2012. 
281. A. Kind, M. P. Stoecklin, and X. Dimitropou-
los, “Histogram-based traffic anomaly detection,” 
IEEE Transactions on Network and Service Man-
agement, 2009. 
282. M. Goldstein and A. Dengel, “Histogram-based 
outlier score (hbos): A fast unsupervised anomaly 
detection algorithm,” KI-2012: Poster and Demo 
Track, 2012. 
283. E. Parzen, “On estimation of a probability density 
function and mode,” The annals of mathematical 
statistics, 1962. 
284. M. Desforges, P. Jacob, and J. Cooper, “Appli-
cations of probability density estimation to the 
detection of abnormal conditions in engineering,” 
Proceedings of the institution of mechanical engi-
neers, 1998. 
285. W. Hu, J. Gao, B. Li, O. Wu, J. Du, and 
S. Maybank, “Anomaly detection using local ker-
nel density estimation and context-based regres-
sion,” TKDE, 2018. 
286. M. A. Kramer, “Nonlinear principal component 
analysis using autoassociative neural networks,” 
AIChE journal, 1991. 
287. D. P. Kingma and M. Welling, “Auto-
encoding variational bayes,” arXiv preprint 
arXiv:1312.6114, 2013.
30 Jingkang Yang et al. 
288. I. Goodfellow, J. Pouget-Abadie, M. Mirza, B. Xu, 
D. Warde-Farley, S. Ozair, A. Courville, and 
Y. Bengio, “Generative adversarial nets,” NIPS, 
2014. 
289. D. Rezende and S. Mohamed, “Variational infer-
ence with normalizing flows,” in ICML, 2015. 
290. J. Ngiam, Z. Chen, P. W. Koh, and A. Y. Ng, 
“Learning deep energy models,” in ICML, 2011. 
291. S. Zhai, Y. Cheng, W. Lu, and Z. Zhang, “Deep 
structured energy based models for anomaly de-
tection,” in ICML, 2016. 
292. A. Hyvärinen and P. Dayan, “Estimation of non-
normalized statistical models by score matching.,” 
2005. 
293. M. Welling and Y. W. Teh, “Bayesian learning via 
stochastic gradient langevin dynamics,” in ICML, 
2011. 
294. H. Wang, X. Wu, Z. Huang, and E. P. Xing, “High-
frequency component helps explain the generaliza-
tion of convolutional neural networks,” in CVPR, 
2020. 
295. G. Chen, P. Peng, L. Ma, J. Li, L. Du, and 
Y. Tian, “Amplitude-phase recombination: Re-
thinking robustness of convolutional neural net-
works in frequency domain,” ICCV, 2021. 
296. H. Liu, X. Li, W. Zhou, Y. Chen, Y. He, H. Xue, 
W. Zhang, and N. Yu, “Spatial-phase shallow 
learning: rethinking face forgery detection in fre-
quency domain,” in CVPR, 2021. 
297. A. Adler, M. Elad, Y. Hel-Or, and E. Rivlin, 
“Sparse coding with anomaly detection,” Journal 
of Signal Processing Systems, 2015. 
298. A. Li, Z. Miao, Y. Cen, and Y. Cen, “Anomaly 
detection using sparse reconstruction in crowded 
scenes,” Multimedia Tools and Applications, 2017. 
299. X. Mo, V. Monga, R. Bala, and Z. Fan, “Adap-
tive sparse representations for video anomaly de-
tection,” IEEE Transactions on Circuits and Sys-
tems for Video Technology, 2013. 
300. Y. Xiao, H. Wang, W. Xu, and J. Zhou, “L1 norm 
based kpca for novelty detection,” Pattern Recog-
nition, 2013. 
301. K. Jiang, W. Xie, J. Lei, T. Jiang, and Y. Li, 
“Lren: Low-rank embedded network for sample-
free hyperspectral anomaly detection,” in AAAI, 
2021. 
302. Z. Chen, C. K. Yeo, B. S. Lee, and C. T. 
Lau, “Autoencoder-based network anomaly de-
tection,” in Wireless Telecommunications Sympo-
sium, 2018. 
303. J. An and S. Cho, “Variational autoencoder based 
anomaly detection using reconstruction probabil-
ity,” Special Lecture on IE, 2015. 
304. H. Zenati, C. S. Foo, B. Lecouat, G. Manek, 
and V. R. Chandrasekhar, “Efficient gan-based 
anomaly detection,” in ICLR-W, 2018. 
305. W. Liu, W. Luo, D. Lian, and S. Gao, “Fu-
ture frame prediction for anomaly detection–a new 
baseline,” in CVPR, 2018. 
306. D. Gong, L. Liu, V. Le, B. Saha, M. R. Mansour, 
S. Venkatesh, and A. v. d. Hengel, “Memorizing 
normality to detect anomaly: Memory-augmented 
deep autoencoder for unsupervised anomaly de-
tection,” in CVPR, 2019. 
307. H. Park, J. Noh, and B. Ham, “Learning memory-
guided normality for anomaly detection,” in 
CVPR, 2020. 
308. C.-H. Lai, D. Zou, and G. Lerman, “Robust sub-
space recovery layer for unsupervised anomaly de-
tection,” ICLR, 2020. 
309. X. Yan, H. Zhang, X. Xu, X. Hu, and P.-A. Heng, 
“Learning semantic context from normal samples 
for unsupervised anomaly detection,” in AAAI, 
2021. 
310. D. T. Nguyen, Z. Lou, M. Klar, and T. Brox, 
“Anomaly detection with multiple-hypotheses 
predictions,” in ICML, 2019. 
311. K. Tian, S. Zhou, J. Fan, and J. Guan, “Learning 
competitive and discriminative reconstructions for 
anomaly detection,” in AAAI, 2019. 
312. X. Han, X. Chen, and L.-P. Liu, “Gan en-
semble for anomaly detection,” arXiv preprint 
arXiv:2012.07988, 2020. 
313. G. Kwon, M. Prabhushankar, D. Temel, and 
G. AlRegib, “Backpropagated gradient represen-
tations for anomaly detection,” in ECCV, 2020. 
314. D. Wettschereck, “A study of distance-based ma-
chine learning algorithms,” 1994. 
315. J. Tian, M. H. Azarian, and M. Pecht, “Anomaly 
detection using self-organizing maps-based k-
nearest neighbor algorithm,” in PHM Society Eu-
ropean Conference, 2014. 
316. G. Münz, S. Li, and G. Carle, “Traffic anomaly 
detection using k-means clustering,” in GI/ITG 
Workshop MMBnet, 2007. 
317. I. Syarif, A. Prugel-Bennett, and G. Wills, “Unsu-
pervised clustering approach for network anomaly 
detection,” in International conference on net-
worked digital technologies, 2012. 
318. D. M. J. Tax, “One-class classification: Concept 
learning in the absence of counter-examples.,” 
2002. 
319. L. Ruff, R. Vandermeulen, N. Goernitz, L. Deecke, 
S. A. Siddiqui, A. Binder, E. Müller, and M. Kloft, 
“Deep one-class classification,” in ICML, 2018.
Generalized Out-of-Distribution Detection: A Survey 31 
320. B. Zhang and W. Zuo, “Learning from posi-
tive and unlabeled examples: A survey,” in Inter-
national Symposiums on Information Processing, 
2008. 
321. J. Bekker and J. Davis, “Learning from positive 
and unlabeled data: A survey,” Machine Learning, 
2020. 
322. K. Jaskie and A. Spanias, “Positive and unlabeled 
learning algorithms and applications: A survey,” 
in International Conference on Information, In-
telligence, Systems and Applications, 2019. 
323. L. Ruff, R. A. Vandermeulen, N. Görnitz, 
A. Binder, E. Müller, K.-R. Müller, and 
M. Kloft, “Deep semi-supervised anomaly detec-
tion,” ICLR, 2020. 
324. L. Bergman and Y. Hoshen, “Classification-based 
anomaly detection for general data,” in ICLR, 
2020. 
325. I. Golan and R. El-Yaniv, “Deep anomaly 
detection using geometric transformations,” in 
NeurIPS, 2018. 
326. M.-I. Georgescu, A. Barbalau, R. T. Ionescu, F. S. 
Khan, M. Popescu, and M. Shah, “Anomaly de-
tection in video via self-supervised and multi-task 
learning,” in CVPR, 2021. 
327. D. G. Altman and J. M. Bland, “Standard devia-
tions and standard errors,” BMJ, 2005. 
328. C. Leys, C. Ley, O. Klein, P. Bernard, and L. Li-
cata, “Detecting outliers: Do not use standard de-
viation around the mean, use absolute deviation 
around the median,” Journal of experimental so-
cial psychology, 2013. 
329. X. Yang, L. J. Latecki, and D. Pokrajac, “Outlier 
detection with globally optimal exemplar-based 
gmm,” in SIAM, 2009. 
330. M. M. Breunig, H.-P. Kriegel, R. T. Ng, and 
J. Sander, “Lof: identifying density-based local 
outliers,” in SIGMOD, 2000. 
331. M. A. Fischler and R. C. Bolles, “Random sam-
ple consensus: a paradigm for model fitting with 
applications to image analysis and automated car-
tography,” Communications of the ACM, 1981. 
332. M. Sugiyama and K. Borgwardt, “Rapid distance-
based outlier detection via sampling,” NIPS, 2013. 
333. G. H. Orair, C. H. Teixeira, W. Meira Jr, Y. Wang, 
and S. Parthasarathy, “Distance-based outlier de-
tection: consolidation and renewed bearing,” Pro-
ceedings of the VLDB Endowment, 2010. 
334. M. Ester, H.-P. Kriegel, J. Sander, X. Xu, et al., 
“A density-based algorithm for discovering clus-
ters in large spatial databases with noise,” in 
KDD, 1996. 
335. V. Hautamaki, I. Karkkainen, and P. Franti, “Out-
lier detection using k-nearest neighbour graph,” in 
ICPR, 2004. 
336. F. Muhlenbach, S. Lallich, and D. A. Zighed, 
“Identifying and handling mislabelled instances,” 
Journal of Intelligent Information Systems, 2004. 
337. W. Liu, J. He, and S.-F. Chang, “Large graph con-
struction for scalable semi-supervised learning,” in 
ICML, 2010. 
338. L. Akoglu, H. Tong, and D. Koutra, “Graph 
based anomaly detection and description: a sur-
vey,” Data mining and knowledge discovery, 2015. 
339. C. C. Noble and D. J. Cook, “Graph-based 
anomaly detection,” in SIGKDD, 2003. 
340. Y. Kou, C.-T. Lu, and R. F. Dos Santos, “Spa-
tial outlier detection: a graph-based approach,” in 
19th IEEE International Conference on Tools with 
Artificial Intelligence (ICTAI), 2007. 
341. Z. Mingqiang, H. Hui, and W. Qian, “A graph-
based clustering algorithm for anomaly intrusion 
detection,” in International Conference on Com-
puter Science & Education (ICCSE), 2012. 
342. Z.-F. Wu, T. Wei, J. Jiang, C. Mao, M. Tang, and 
Y.-F. Li, “Ngc: A unified framework for learning 
with open-world noisy data,” in ICCV, 2021. 
343. J. Yang, W. Chen, L. Feng, X. Yan, H. Zheng, and 
W. Zhang, “Webly supervised image classification 
with metadata: Automatic noisy label correction 
via visual-semantic graph,” in ACM Multimedia, 
2020. 
344. F. T. Liu, K. M. Ting, and Z.-H. Zhou, “Isolation 
forest,” in ICDM, 2008. 
345. Y. Li, J. Yang, Y. Song, L. Cao, J. Luo, and L.-J. 
Li, “Learning from noisy labels with distillation,” 
in CVPR, 2017. 
346. D. T. Nguyen, C. K. Mummadi, T. P. N. Ngo, 
T. H. P. Nguyen, L. Beggel, and T. Brox, 
“Self: Learning to filter noisy labels with self-
ensembling,” in ICLR, 2020. 
347. B. Han, Q. Yao, X. Yu, G. Niu, M. Xu, W. Hu, 
I. Tsang, and M. Sugiyama, “Co-teaching: Robust 
training of deep neural networks with extremely 
noisy labels,” in NIPS, 2018. 
348. J. Yang, L. Feng, W. Chen, X. Yan, H. Zheng, 
P. Luo, and W. Zhang, “Webly supervised im-
age classification with self-contained confidence,” 
in ECCV, 2020. 
349. J. Yang, P. Wang, D. Zou, Z. Zhou, K. Ding, 
W. Peng, H. Wang, G. Chen, B. Li, Y. Sun, X. Du, 
K. Zhou, W. Zhang, D. Hendrycks, Y. Li, and 
Z. Liu, “Openood: Benchmarking generalized out-
of-distribution detection,” in NeurIPS, 2022.
32 Jingkang Yang et al. 
350. A. Krizhevsky, G. Hinton, et al., “Learning mul-
tiple layers of features from tiny images,” 2009. 
351. A. Krizhevsky, V. Nair, and G. Hinton, “Cifar-
10 and cifar-100 datasets,” URl: https://www. cs. 
toronto. edu/kriz/cifar. html, vol. 6, no. 1, p. 1, 
2009. 
352. Y. LeCun and C. Cortes, “The mnist database of 
handwritten digits,” 2005. 
353. Y. Netzer, T. Wang, A. Coates, A. Bissacco, 
B. Wu, and A. Y. Ng, “Reading digits in natural 
images with unsupervised feature learning,” 2011. 
354. G. Kylberg, “Kylberg texture dataset v. 1.0,” 
2011. 
355. B. Zhou, A. Lapedriza, A. Khosla, A. Oliva, and 
A. Torralba, “Places: A 10 million image database 
for scene recognition,” IEEE Transactions on Pat-
tern Analysis and Machine Intelligence, 2017. 
356. A. Torralba, R. Fergus, and W. T. Freeman, “80 
million tiny images: A large data set for nonpara-
metric object and scene recognition,” TPAMI, 
2008. 
357. K. He, X. Zhang, S. Ren, and J. Sun, “Deep resid-
ual learning for image recognition,” in CVPR, 
2016. 
358. J. Zhang, J. Yang, P. Wang, H. Wang, Y. Lin, 
H. Zhang, Y. Sun, X. Du, K. Zhou, W. Zhang, 
Y. Li, Z. Liu, Y. Chen, and H. Li, “Openood v1.5: 
Enhanced benchmark for out-of-distribution de-
tection,” arXiv preprint arXiv:2306.09301, 2023. 
359. J. Bitterwolf, M. Müller, and M. Hein, “In or out? 
fixing imagenet out-of-distribution detection eval-
uation,” in ICML, 2023. 
360. P. W. Koh, S. Sagawa, H. Marklund, S. M. Xie, 
M. Zhang, A. Balsubramani, W. Hu, M. Ya-
sunaga, R. L. Phillips, I. Gao, et al., “Wilds: A 
benchmark of in-the-wild distribution shifts,” in 
International Conference on Machine Learning, 
pp. 5637–5664, PMLR, 2021. 
361. L. Cultrera, L. Seidenari, and A. Del Bimbo, 
“Leveraging visual attention for out-of-
distribution detection,” in Proceedings of the 
IEEE/CVF International Conference on Com-
puter Vision, pp. 4447–4456, 2023. 
362. Y. Ming, H. Yin, and Y. Li, “On the impact of 
spurious correlation for out-of-distribution detec-
tion,” in AAAI, 2022. 
363. P. Panareda Busto and J. Gall, “Open set domain 
adaptation,” in ICCV, 2017. 
364. Y. Shu, Z. Cao, C. Wang, J. Wang, and 
M. Long, “Open domain generalization with 
domain-augmented meta-learning,” in CVPR, 
2021. 
365. J. Li, C. Xiong, and S. C. Hoi, “Mopro: Webly 
supervised learning with momentum prototypes,” 
ICLR, 2021. 
366. V. D. Nguyen, “Out-of-distribution detection for 
lidar-based 3d object detection,” Master’s thesis, 
University of Waterloo, 2022. 
367. G. Shalev, G.-L. Shalev, and J. Keshet, “A 
baseline for detecting out-of-distribution ex-
amples in image captioning,” arXiv preprint 
arXiv:2207.05418, 2022. 
368. X. Wu, J. Lu, Z. Fang, and G. Zhang, “Meta ood 
learning for continuously adaptive ood detection,” 
in Proceedings of the IEEE/CVF International 
Conference on Computer Vision, pp. 19353– 
19364, 2023. 
369. C. Zhou, G. Neubig, J. Gu, M. Diab, P. Guzman, 
L. Zettlemoyer, and M. Ghazvininejad, “Detect-
ing hallucinated content in conditional neural se-
quence generation,” ACL, 2020. 
370. Y. Dai, H. Lang, K. Zeng, F. Huang, and 
Y. Li, “Exploring large language models for 
multi-modal out-of-distribution detection,” arXiv 
preprint arXiv:2310.08027, 2023. 
371. Z. Yang, L. Li, K. Lin, J. Wang, C.-C. Lin, Z. Liu, 
and L. Wang, “The dawn of lmms: Preliminary 
explorations with gpt-4v (ision),” arXiv preprint 
arXiv:2309.17421, vol. 9, no. 1, 2023. 
372. H. Liu, C. Li, Q. Wu, and Y. J. Lee, 
“Visual instruction tuning,” arXiv preprint 
arXiv:2304.08485, 2023. 
373. B. Li, Y. Zhang, L. Chen, J. Wang, J. Yang, 
and Z. Liu, “Otter: A multi-modal model with 
in-context instruction tuning,” arXiv preprint 
arXiv:2305.03726, 2023.