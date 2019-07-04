# encoding: utf8
#from __future__ import unicode_literals
import numpy as np
import cv2

#区別のための日付
day = 20190624
# 計算の対象のシーンの開始フレーム番号
tgt_frm_s= 4055
# 追跡したいシーンの最後のフレームナンバー
tgt_frm_e = 7855
sigma = 205
refImg = "5480_6"
interval = 20
# 参照場所
file_root = "example/image/single/"
file_path = "example/image/img_hmm/%s/%d-%d_sigma=%d_red/" %(refImg, tgt_frm_s, tgt_frm_e, sigma)

results = []
n = int( (tgt_frm_e - tgt_frm_s) / interval )
a = np.loadtxt( file_path + "%d-%d_%s_sigma=%d_%d_005504_00_PATH.txt" %( tgt_frm_s, tgt_frm_e, refImg, sigma, day ) )
#print(n)

#推定した画像のナンバーをリストに格納
results.append(a)
print(results)

for i in range(n):
   label = tgt_frm_s + i * interval
   lik = results[i]
   img = cv2.imread(file_root + "%d_%d.png" %(label, lik))
   cv2.imwrite("example/image/answer/%d.png" %(i), img)
    


#for i in range(n):

    
  #  label = i * interval
  #  number = hmm_result[i*interval]   
    
    
