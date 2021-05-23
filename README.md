# FXRT search code
This code was been developed to search fast X-ray transients (FXRTs) in a Chandra X-ray Observatory (CXO) observation ID (ObsId).

You have to download both files (search_code_CXO.py and search_data.py), and run using the command:

user@user: python search_code_CXO.py

For running the code, it is necesary to activate the CIAO environment (you can download and install CIAO from this link: https://cxc.cfa.harvard.edu/ciao/threads/ciao_install_tool/). Also, using th "pip" command, you have to install the next python package: subprocess, numpy, re, glob, os, requests, io, astropy, math, pandas.

As an example, you can introduce ObsIds that harbor FXRTs previously identified: 16454 (Bauer et al. 2017; https://academic.oup.com/mnras/article/467/4/4841/3038248?login=true), 16453 (Xue et al. 2019; https://www.nature.com/articles/s41586-019-1079-5.pdf), 803 (Jonker et al. 2013; https://iopscience.iop.org/article/10.1088/0004-637X/779/1/14/meta), 12884 (Glennie et al. 2015; https://academic.oup.com/mnras/article/450/4/3765/990370?login=true) as example of FXRTs previously identified.
