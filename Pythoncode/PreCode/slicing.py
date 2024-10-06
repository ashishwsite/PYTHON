para="this is paragraph which is slicing in the this tutorial "
lenghtofpara=len(para)
print("the length of para is a", lenghtofpara)
paraafterslice=para[-6:15]# similar to para[:15]
# minus index nothing worry its is only start 0 th index 
slicebeetween=para[15:26]# 26 index is not include 
#[-2,-9] its meaning yaha se mileha vaha tak acceas karwga similar is [0,56]
print(slicebeetween)
print("this string after slicinh ", paraafterslice)
