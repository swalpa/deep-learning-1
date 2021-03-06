# Deep Learning
[![License](http://img.shields.io/:license-mit-blue.svg)](LICENSE)

## Description

Labs of the [Deep Learning](http://studiegids.uva.nl/xmlpages/page/2018-2019/zoek-vak/vak/63164) course of the MSc in Artificial Intelligence at the University of Amsterdam.

#### Lab 1

[Problem statement](https://github.com/askliar/deep_learning/blob/master/assignment_1/assignment_1.pdf) - [Solution](https://github.com/askliar/deep_learning/blob/master/assignment_1/Skliar_11636785_hw1.pdf)

Goal of this assignment is to learn how to implement and train basic neural architectures like MLPs and CNNs for classiﬁcation tasks. The assignment consists of four parts:

- First, to gain an in-depth understanding we focused on a basic implementation of a MLP in NumPy. This requires to understand backpropagation in detail and to derive the necessary equations ﬁrst.
- Next, we implemented MLP in PyTorch and add tuned its performance by adding additional layers provided by the 
- In order to learn how to implement custom operations in PyTorch, in next task we reimplemented a batch-normalization layer.
- Last part aims at implementing a simple CNN in PyTorch.

#### Lab 2

[Problem statement](https://github.com/askliar/deep_learning/blob/master/assignment_2/assignment_2.pdf) - [Solution](https://github.com/askliar/deep_learning/blob/master/assignment_2/Skliar_11636785_hw2.pdf)

Goal of this assignment is to study and implement recurrent neural networks (RNNs).
The assignment consists of three parts:

- Getting familiar with vanilla RNNs and LSTMs on a simple toy problem. This allows for understanding the fundamentals of recurrent networks. 
- Studying a more advanced LSTM cell to emphasize the wide variety in LSTM cells. 
- Using LSTMs for learning and generating text. 

**Samples during training on Vanity Fair**

(*The bold characters are picked randomly and used the initialize the LSTM state.*)

|Train Step | Sampled Text |
|:-------------------------:|-------------------------|
|0 | **#**jx!\%dYikK.vXonWIc(Qw"@\_AyeOwX|
|17600 | **v**ed and discovered herse. His|
|35200 | **U**nce\nin him home and going, th |
|52800 | **\\**'s long money," reC.B.n that t |
|70400 | **y** must have dreads everything|

#### Lab 3

[Problem statement](https://github.com/askliar/deep_learning/blob/master/assignment_3/assignment_3.pdf) - [Solution](https://github.com/askliar/deep_learning/blob/master/assignment_2/Skliar_11636785_hw3.pdf)

Goal of this assignment is to study and implement Deep Generative Models. The assignment focuses on two most popular models:

- Variational Auto Encoders (VAE)
- Generative Adversarial Networks (GAN)

We have implemented both of them in PyTorch as part of this assignment. 

<p align="center">
  <img src="https://lh3.googleusercontent.com/oyJCiAOKhUTdwhZ6TJFxv69eMYcpqicCZ99QmFcC_HIOzga5_EcHMb7hNWXmBTLwDfGGKRN5UNbMlXR9HyNsUKVGFzfa1cZyqykneGYr206V5ISiCbuLTqC1rSDLw3Q2IuzWVxgt4Jk=w2400" width="300" /><br />
  <b>Figure:</b><i> Data manifold learned by VAE after 40 iterations</i>
</p>

<p align="center">
  <img src="https://lh3.googleusercontent.com/XnKtH4KadlYSzm128Yq__vcKBRMuuEpba-oUOCEoSG7MUEuvlE9kyFHddbvg0z2GCR5U0qWXebQ6FInQh_uepMpwKzx3Gdu9W4mYah7rlIE0M10GWLl1U3s3Q0PUyxhRkEKFIBTRVKU=w2400" width="300" /><br />
  <b>Figure:</b><i> Samples for DCGAN at steps 1, 5, 20 and 40 (left to right, top to bottom)</i>
</p>

## Dependencies

- NumPy
- PyTorch
- Matplotlib
- Scipy

## Copyright

Copyright © 2018 Andrii Skliar.

<p align=“justify”>
This project is distributed under the <a href=“LICENSE”>MIT license</a>. This was developed as part of the Deep Learning course taught by Efstratios Gavves at the University of Amsterdam. Please follow the <a href="http://student.uva.nl/en/content/az/plagiarism-and-fraud/plagiarism-and-fraud.html"> UvA regulations governing Fraud and Plagiarism </a> in case you are a student.
</p>
