# NNCM
Attention-based Neural Network Classification Models. Implemented by tensorflow.


## 1. Effective LSTMs for Target-Dependent Sentiment Classification with Long Short Term Memory

Duyu Tang, Bing Qin, Xiaocheng Feng, Ting Liu

Proceeding of the 26th International Conference on Computational Linguistics (COLING 2016, full paper)

[https://arxiv.org/abs/1512.01100]


## 2. Attention-based LSTM for Aspect-level Sentiment Classification

Yequan Wang, Minlie Huang, Li Zhao, Xiaoyan Zhu

Conference on Empirical Methods in Natural Language Processing (EMNLP 2016, full paper)

[http://www.aclweb.org/anthology/D/D16/D16-1058.pdf]


## 3. Aspect Level Sentiment Classification with Deep Memory Network

Duyu Tang, Bing Qin, Ting Liu

Conference on Empirical Methods in Natural Language Processing (EMNLP 2016, full paper)

[http://arxiv.org/abs/1605.08900]


## source code tree

    .
    ├── README.md
    ├── show
    ├── data
    │   ├── restaurant
    │   └── twitter
    ├── lstm.py           Paper 1
    ├── tc_lstm.py        Paper 1
    ├── td_lstm.py        Paper 1
    ├── at_lstm.py        Paper 2
    ├── utils.py


## Paper 1

The corpus is **twitter**. We just got our results on test set.

|Method|Origin-Acc|Mine-Acc|
|:------|:------|:------|
|LSTM|66.5%|68.03%|
|TD-LSTM|70.8%|69.74%|
|TC-LSTM|71.5%|70.20%|

## Paper 2

The corpus is **restaurant**.

|Method|Origin-Acc|Mine-Acc|
|:------|:------|:------|
|LSTM|74.3%|76.40%|
|TD-LSTM|75.6%|78.31%|
|AE-LSTM|76.6%|76.81%|
|ATAE-LSTM|77.2%|77.01%|

The corpus is **laptop**.

Method|Origin-Acc|Mine-Acc|
|:------|:------|:------|
|LSTM|66.50%|%|
|TD-LSTM|68.10%|%|
|AE-LSTM|68.90%|%|
|ATAE-LSTM|68.70%|%|

