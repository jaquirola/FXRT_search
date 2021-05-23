# FXRT search code
This code was been developed to search fast X-ray transients (FXRTs) in a CXO ObsId.

You have to download both files (search_code_CXO.py and search_data.py), and run using the command:

user@user: python search_code_CXO.py

For running the code, it is necesary to activate the CIAO environment (you can download and install CIAO from this link: https://cxc.cfa.harvard.edu/ciao/threads/ciao_install_tool/). Also, using th "pip" command, you have to install the next python package: subprocess, numpy, re, glob, os, requests, io, astropy, math, pandas.

As an example, you can introduce the next ObsId: 16454 (Bauer et al. 2017), 16453 (Xue et al. 2019), 803 (Jonker et al. 2013), 12884 (Glennie et al. 2015) as example of FXRTs previously identified.
