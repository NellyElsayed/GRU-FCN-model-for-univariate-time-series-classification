# GRU-FCN-model-for-univariate-time-series-classification
GRU-FCN model for univariate time series classification


This repository contains the code used in implementing the paper:

## Deep Gated Recurrent and Convolutional Network Hybrid Model for Univariate Time Series Classification.

Our paper **"Deep Gated Recurrent and Convolutional Network Hybrid Model for Univariate Time Series Classification"** 
Which you can find on arxiv:

https://arxiv.org/abs/1812.07683

The idea of our GRU-FCN paper is inspired by Karim et al. "LSTM Fully Convolutional Networks for Time Series Classification" paper which
code is found in the following link: https://github.com/titu1994/LSTM-FCN
But we replaced the LSTM by a Gated Recurrent Unit (GRU) which produces higher accuracy in different UCR univariate datasets classification. Our goal was mainly to compare the performance of GRU and LSTM within the same entire model structure in time series classification problem.

## How to run the code:
### Dataset:
The data set we used is the UCR which you can find and install on your PC from the following link:

https://www.cs.ucr.edu/~eamonn/time_series_data_2018/

After installing all the datasets, unzip the folders and put all them in one folder. Name this folder as : data

Note: Please do not forget to cite the dataset in case of using it.

### Code:
Our code is has parts that are exactly the same as in Karim et al. which is mentioned before except that we used the GRU instead of the LSTM other code lines to show the results.

We added a file for each dataset. We numbered the datasets from 0-84 corresponding to their order in the UCR benchmark.
In addition, we modified the constants file to handle this ordering stuff.

# Supporting Code:
The other supporting code is the code which implemented by Karim et al. in the following 
link: https://github.com/titu1994/LSTM-FCN


#### Note 1:
We intuitively did not make much changes to the LSTM-FCN code to make it easier for you to test our GRU-FCN model and the LSTM based model to proof that the GRU outperforms the LSTM in this classification task.


#### Note2:
In case of using our code, please do not forget to cite both our code:

@article{elsayed2018deep,

  title={Deep Gated Recurrent and Convolutional Network Hybrid Model for Univariate Time Series Classification},
  
  author={Elsayed, Nelly and Maida, Anthony S and Bayoumi, Magdy},
  
  journal={arXiv preprint arXiv:1812.07683},
  
  year={2018}
  
}


and the code that we used to create our code:

@misc{Karim_Majumdar2017,

Author = {Fazle Karim and Somshubra Majumdar and Houshang Darabi and Shun Chen},

Title = {LSTM Fully Convolutional Networks for Time Series Classification},

Year = {2017},

Eprint = {arXiv:1709.05206},

}
