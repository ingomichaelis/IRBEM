import numpy as np
import pandas as pd

# igrf_coeff_file='./igrf14coeffs.txt'
igrf_coeff_file='/home/michaeli/prj/MAG/SPACEPY/spacepy/spacepy/data/igrf14coeffs.txt'
output_file=igrf_coeff_file.replace('.txt','_reformat.txt')
header1=pd.read_csv(igrf_coeff_file,comment='#',sep=r'\s+',header=None,nrows=1)
d=pd.read_csv(igrf_coeff_file,comment='#',sep=r'\s+',header=1)
d.loc[d['g/h']=='h','m']=-d.loc[d['g/h']=='h','m']
d.drop('g/h',axis=1,inplace=True)
columns_igrf=d.drop(['n','m'],axis=1).columns[:-1]
column_sv=d.columns[-1]


# igrf_coeff_file='./IGRF14.shc'
# igrf_coeff_file='/home/michaeli/prj/MAG/SPACEPY/spacepy/spacepy/data/IGRF14.shc'
# output_file=igrf_coeff_file.replace('.shc','_reformat.txt')
# header1=pd.read_csv(igrf_coeff_file,comment='#',sep=r'\s+',header=None,nrows=1)
# d=pd.read_csv(igrf_coeff_file,comment='#',sep=r'\s+',header=1,index_col=[0,1])
# columns_igrf=d.drop(['n','m'],axis=1).columns[:-1]
# column_sv=d.columns[-1]
# d.reset_index(names=['n','m'],inplace=True)

output=[]
# prepare IGRF
m_max=d.loc[:,'m'].max()
n_max_output=10
for column_igrf in columns_igrf:
	d_sel=d.loc[:,['n','m']]
	d_sel['g']=d.loc[:,column_igrf]
	d_sel['h']=d.loc[:,column_igrf]
	d_sel.loc[d_sel['m']<0,'g']=0
	d_sel.loc[d_sel['m']>=0,'h']=0
	d_sel_g=d_sel.loc[d_sel['m']>=0,['n','m','g']]
	d_sel_h=d_sel.loc[d_sel['m']<=0,['n','m','h']]
	# create G values
	output.append('      DATA G{0:d}/'.format(int(np.double(column_igrf)))+'\n')
	output.append('     *{0:10.2f}d0'.format(0)+'\n')
	for n in range(1,n_max_output+1):
		values=d_sel_g.loc[d['n']==n,'g'].values
		for it in range(0,int(np.ceil(len(values)/5))):
			if (it==(len(values)-1))|(len(values)<5)|((len(values)-it*5)<5):
				indices=np.arange(it*5,len(values))
			else:
				indices=np.arange(it*5,(it+1)*5)
			if (n==n_max_output)&(it==int(np.ceil(len(values)/5))-1):
				str_values='     *'+','.join([' {0:10.2f}d0'.format(x) for x in values[indices]])+'\n'
			else:
				str_values='     *'+','.join([' {0:10.2f}d0'.format(x) for x in values[indices]])+',\n'
			output.append(str_values)
	output.append('     * /\n')
	# create H values
	output.append('      DATA H{0:d}/'.format(int(np.double(column_igrf)))+'\n')
	output.append('     *{0:10.2f}d0'.format(0)+'\n')
	for n in range(1,n_max_output+1):
		values=d_sel_h.loc[d['n']==n,'h'].values
		for it in range(0,int(np.ceil(len(values)/5))):
			if (it==(len(values)-1))|(len(values)<5)|((len(values)-it*5)<5):
				indices=np.arange(it*5,len(values))
			else:
				indices=np.arange(it*5,(it+1)*5)
			if (n==n_max_output)&(it==int(np.ceil(len(values)/5))-1):
				str_values='     *'+','.join([' {0:10.2f}d0'.format(x) for x in values[indices]])+'\n'
			else:
				str_values='     *'+','.join([' {0:10.2f}d0'.format(x) for x in values[indices]])+',\n'
			output.append(str_values)
	output.append('     * /\n')

# # prepare SV
m_max=d.loc[:,'m'].max()
n_max_output=8
d_sel=d.loc[:,['n','m']]
d_sel['g']=d.loc[:,column_sv]
d_sel['h']=d.loc[:,column_sv]
d_sel.loc[d_sel['m']<0,'g']=0
d_sel.loc[d_sel['m']>=0,'h']=0
d_sel_g=d_sel.loc[d_sel['m']>=0,['n','m','g']]
d_sel_h=d_sel.loc[d_sel['m']<=0,['n','m','h']]
# create G values
# output.append('      DATA DG{0:d}/'.format(int(np.double(column_sv)))+'\n')
output.append('      DATA DG{0:d}/'.format(int(column_sv[0:4]))+'\n')
output.append('     *{0:10.2f}d0'.format(0)+'\n')
for n in range(1,n_max_output+1):
	values=d_sel_g.loc[d['n']==n,'g'].values
	for it in range(0,int(np.ceil(len(values)/5))):
		if (it==(len(values)-1))|(len(values)<5)|((len(values)-it*5)<5):
			indices=np.arange(it*5,len(values))
		else:
			indices=np.arange(it*5,(it+1)*5)
		if (n==n_max_output)&(it==int(np.ceil(len(values)/5))-1):
			str_values='     *'+','.join([' {0:10.2f}d0'.format(x) for x in values[indices]])+'\n'
		else:
			str_values='     *'+','.join([' {0:10.2f}d0'.format(x) for x in values[indices]])+',\n'
		output.append(str_values)
output.append('     * /\n')
# create H values
# output.append('      DATA DH{0:d}/'.format(int(np.double(column_sv)))+'\n')
output.append('      DATA DH{0:d}/'.format(int(column_sv[0:4]))+'\n')
output.append('     *{0:10.2f}d0'.format(0)+'\n')
for n in range(1,n_max_output+1):
	values=d_sel_h.loc[d['n']==n,'h'].values
	for it in range(0,int(np.ceil(len(values)/5))):
		if (it==(len(values)-1))|(len(values)<5)|((len(values)-it*5)<5):
			indices=np.arange(it*5,len(values))
		else:
			indices=np.arange(it*5,(it+1)*5)
		if (n==n_max_output)&(it==int(np.ceil(len(values)/5))-1):
			str_values='     *'+','.join([' {0:10.2f}d0'.format(x) for x in values[indices]])+'\n'
		else:
			str_values='     *'+','.join([' {0:10.2f}d0'.format(x) for x in values[indices]])+',\n'
		output.append(str_values)
output.append('     * /\n')

file = open(output_file, 'w')
file.writelines(output)
# for i in range(0,len(output)):
# 	file.write(output[i])
file.close()

