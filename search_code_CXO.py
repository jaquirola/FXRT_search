import subprocess
import numpy as np
import re
import glob
import os



def function(obsid):
   command='download_chandra_obsid '+str(obsid)+' evt2,fov,asol,bpix,msk'
   proc = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
#command='cd '+str(obsid)
#proc = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
   command='cp search_data.py '+str(obsid)+'/'
   proc = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
   command='cp '+str(obsid)+'/primary/* '+str(obsid)+'/'
   proc = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
   command='gunzip '+str(obsid)+'/*.gz'
   proc = subprocess.run(command, stdout=subprocess.PIPE, shell=True)

   os.chdir('/home/jonathan/Escritorio/Doctorado/Current_CXO_data/data_2021/'+str(obsid)+'/')
   event_file=glob.glob('*evt2.fits', recursive=True)
   fov_file=glob.glob('*N*fov1.fits', recursive=True)
   print(event_file,fov_file)

##### mask
   command='dmcopy "'+fov_file[0]+'" s3.fov'
   proc = subprocess.run(command, stdout=subprocess.PIPE, shell=True)

   command='dmcopy "'+event_file[0]+'[sky=region(s3.fov)]" 578_evt2_filtered.fits'
   proc = subprocess.run(command, stdout=subprocess.PIPE, shell=True)

   command='fluximage 578_evt2_filtered.fits binsize=1 bands=broad outroot=s3 psfecf=0.393'
   proc = subprocess.run(command, stdout=subprocess.PIPE, shell=True)

   command='mkpsfmap s3_broad_thresh.img outfile=s3_psfmap.fits energy=1.4967 ecf=0.393'
   proc = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
######## detection

   command='punlearn wavdetect'
   proc = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
   
   command='pset wavdetect infile=s3_broad_thresh.img mode=h'
   proc = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
   
   command='pset wavdetect psffile=s3_broad_thresh.psfmap mode=h'
   proc = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
 
   command='pset wavdetect expfile=s3_broad_thresh.expmap mode=h'
   proc = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
   
   command='pset wavdetect outfile=s3_expmap_src.fits mode=h'
   proc = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
   
   command='pset wavdetect scellfile=s3_expmap_scell.fits mode=h'
   proc = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
   
   command='pset wavdetect imagefile=s3_expmap_imgfile.fits mode=h'
   proc = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
   
   command='pset wavdetect defnbkgfile=s3_expmap_nbgd.fits mode=h'
   proc = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
   
   command='pset wavdetect regfile=s3_expmap_src.reg mode=h'
   proc = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
   
   command='wavdetect scales="1 2 4 8 16"'
   proc = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
####Algorithm
   
   command='python search_data.py'
   proc = subprocess.run(command, stdout=subprocess.PIPE, shell=True)
   os.chdir('/home/jonathan/Escritorio/Doctorado/Current_CXO_data/data_2021/')

#folders=[16453, 13454, 24604, 4062, 16454, 803, 2025, 8490, 9546, 9548, 14904, 5885, 9841, 12264, 12884, 15113, 20635]
#folders=[16453, 13454, 24604, 4062, 16454, 803, 2025, 8490, 9546, 9548, 14904, 5885, 9841, 12264, 12884, 15113, 20635]
#folders=[24604]
#folders=[24576,24577,24578,24579,24580,24581,24602,24603,24604,24605,24606,24607,24608,24609,24610,24611]

'''
for i in range(0,len(folders)):
   function(folders[i])

command='paste */detections_CSC20_w20.txt > final_list.txt'
proc = subprocess.run(command, stdout=subprocess.PIPE, shell=True)

'''

N = input("Introduce the number of ObsIds to analyze (only integers): ")
folders=[]
for i in range(0,int(N)):
   obsid = input("Introduce the "+str(i+1)+" ObsId:")
   folders.append(int(obsid))

print(folders)
for i in range(0,len(folders)):
   function(folders[i])

command='paste */detections_CSC20_w20.txt > final_list.txt'
proc = subprocess.run(command, stdout=subprocess.PIPE, shell=True)


