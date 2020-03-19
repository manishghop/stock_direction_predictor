from pandas_datareader import data as pdr
from Prediction import Prediction
#import final
di={}
f=open('names.txt','r')
for i in f:
	a,b=i.split("------->")
	di[a]=b
	
	
#print(di)


def predictdef():
	try:
		grand_total=0
		for i in di: #For each company
			try:
				symbol=i
				df = pdr.get_data_yahoo(symbol,start='2015-01-01', end='2015-02-01')
				df = df.drop(['Low', 'Volume','Adj Close'], axis=1)
				result = df.to_numpy()   
				print(result) 
				
				
				#print(type(df))
				#print(df)
				company_total=0
				#for each company
				row_count=1
				ans=[[result[0][1],result[0][0],result[0][2]]]
				#print(ans)
				print(len(result))
				while row_count<len(result):
					#print(i[0])
					st,ma,cl=result[row_count][1],result[row_count][0],result[row_count][2]
					ans.append([st,ma,cl])
					#print(ans)
					#print(st,ma,cl)
					print("fefefe")
					print("row",row_count)
					tstart=ans[row_count-1][0]
					print(tstart,"gdggegdgedge")
					if st<cl:
						real_result="profit"

					else:
						real_result="loss"
					s_m = st - ma
					s_c = st - cl
					diff = (tstart - st)
					print("rerererer")
					print(real_result)
					#if True:
					import csv
					row1=[diff,s_m,s_c]
					row=['diff','s_m','s_c']
					print(row,"rpw")

					with open('test.csv', 'w') as csvFile:
						writer = csv.writer(csvFile)
						writer.writerow(row)
						writer.writerow(row1)
						
					csvFile.close()
					#prev=float(str(datetime.now()).split(" ")[1].split(":")[1])
					res = Prediction.predict_nv()	
					print(res,"finaldddvvdd")
					if res.lower()==real_result:
						print("Here")
						company_total+=1
							
					#grand_total+=company_total
						#row+=1	
					row_count+=1
				grand_total=grand_total+company_total/len(result)
			#print(company_total,"e")
			except:
				continue
				pass
		print("accuracy=",(grand_total/len(di))*100)
		print(grand_total)
			
	except:
		pass
			
predictdef()