price_list=[100,30,70,110,600,75,60,450]
gst=17
update_list=[]
for x in price_list:
    if x>100:
        update_list.append(x+(x*0.01*gst))        # Adding gst of 17% for items of price higher than 100
    else:
        update_list.append(x)
print(update_list)