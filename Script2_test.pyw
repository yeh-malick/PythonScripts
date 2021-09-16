import pandas as pd 

dataset = pd.read_excel("C:\MY PROGRAM FILES\TT_DataMining_Youssou.xlsx", sheet_name= "EDU") 
dataset.head()

dataset.columns

columns_to_drop = ['Dupli\nName', 'Full Address', 'State US/Can', 'GMaps', 'Company Type', 'Checked Fields', 'Website', 'Notes', 'Duplicate Domain', 'Checked Contacts', 'Parent company', 'Score', 'GMaps link', 'Country', 'State', 'Phone', 'Short Address', 'City', 'County', 'Owner', 'Zip', 'Latitude', 'Longitude','Charter School', 'Nces Id', 'School Level', 'Unnamed: 36']


dataset = dataset.drop(columns = columns_to_drop)
dataset 

#Unpivoting data --> transposing columns into rows
#id_vars = list(dataset.columns)[0]
#dataset.melt(id_vars=id_vars)

contacts = pd.read_excel("C:\MY PROGRAM FILES\TT_DataMining_Youssou2.xlsx", sheet_name= "EDU_C")


#pd.merge(left= ,right= ,how= ,left_on= ,right_on=)
dataset_joint = pd.merge(left=dataset, right=contacts, how="left", left_on="Domain", right_on="Domain")
print("Field data", len(dataset))
print("Contacts", len(dataset_joint))



list(dataset_joint.columns)

list(contacts.columns)
columns_to_delete = ['Exists?', 'Notes', 'Owner', 'State.1', 'Dupli Email', 'Parent', 'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22', 'Unnamed: 23', 'Unnamed: 24', 'Unnamed: 25', 'Unnamed: 26', 'Unnamed: 27', 'Unnamed: 28', 'Unnamed: 29', 'Unnamed: 30', 'Unnamed: 31', 'Unnamed: 32', 'Unnamed: 33', 'Unnamed: 34', 'Unnamed: 35', 'Unnamed: 36', 'Unnamed: 37', 'Unnamed: 38']
contacts = contacts.drop (columns = columns_to_delete)
list(contacts.columns)


points_of_contact = dataset_joint.groupby("Title")["Domain"].nunique().reset_index()
points_of_contact
