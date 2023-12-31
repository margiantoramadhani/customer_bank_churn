# -*- coding: utf-8 -*-
"""customer_churn.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rtbPkDhCOJ0vglSQuaIN2faFLuNE7lod

#Churn for Bank Customers

Link = https://www.kaggle.com/datasets/radheshyamkollipara/bank-customer-churn

#About Dataset

Content </br>
RowNumber—corresponds to the record (row) number and has no effect on the output.</br>
CustomerId—contains random values and has no effect on customer leaving the bank.</br>
Surname—the surname of a customer has no impact on their decision to leave the bank.</br>
<strong>CreditScore—can have an effect on customer churn, since a customer with a higher credit score is less likely to leave the bank.</strong></br>
Geography—a customer’s location can affect their decision to leave the bank.</br>
<strong>Gender—it’s interesting to explore whether gender plays a role in a customer leaving the bank.</strong></br>
<strong>Age—this is certainly relevant, since older customers are less likely to leave their bank than younger ones.</strong></br>
<strong>Tenure—refers to the number of years that the customer has been a client of the bank. Normally, older clients are more loyal and less likely to leave a bank.</strong></br>
<strong>Balance—also a very good indicator of customer churn, as people with a higher balance in their accounts are less likely to leave the bank compared to those with lower balances.</strong></br>
NumOfProducts—refers to the number of products that a customer has purchased through the bank.</br>
<strong>HasCrCard—denotes whether or not a customer has a credit card. This column is also relevant, since people with a credit card are less likely to leave the bank.</strong></br>
<strong>IsActiveMember—active customers are less likely to leave the bank.</strong></br>
<strong>EstimatedSalary—as with balance, people with lower salaries are more likely to leave the bank compared to those with higher salaries.</strong></br>
Exited—whether or not the customer left the bank.</br>
Complain—customer has complaint or not.</br>
Satisfaction Score—Score provided by the customer for their complaint resolution.</br>
Card Type—type of card hold by the customer.</br>
Points Earned—the points earned by the customer for using credit card.

Acknowledgements</br>
As we know, it is much more expensive to sign in a new client than keeping an existing one.

It is advantageous for banks to know what leads a client towards the decision to leave the company.

Churn prevention allows companies to develop loyalty programs and retention campaigns to keep as many customers as possible.

Insight

What variables are contributing to customer churn?
Who are the customers more likely to churn?
What actions can be taken to stop them from leaving?

Customer Churn prediction means knowing which customers are likely to leave or unsubscribe from your service. For many companies, this is an important prediction. This is because acquiring new customers often costs more than retaining existing ones. Once you’ve identified customers at risk of churn, you need to know exactly what marketing efforts you should make with each customer to maximize their likelihood of staying.

Customers have different behaviors and preferences, and reasons for cancelling their subscriptions. Therefore, it is important to actively communicate with each of them to keep them on your customer list. You need to know which marketing activities are most effective for individual customers and when they are most effective.

A company with a high churn rate loses many subscribers, resulting in lower growth rates and a greater impact on sales and profits. Companies with low churn rates can retain customers.

Objective

Increase profits

Businesses sell products and services to make money. Therefore, the ultimate goal of churn analysis is to reduce churn and increase profits. As more customers stay longer, revenue should increase, and profits should follow.

Improve the customer experience

One of the worst ways to lose a customer is an easy-to-avoid mistake like: Ship the wrong item. Understanding why customers churn, you can better understand their priorities, identify your weaknesses, and improve the overall customer experience.

Customer experience, also known as “CX”, is the customer’s perception or opinion of their interactions with your business. The perception of your brand is shaped throughout the buyer journey, from the first interaction to after-sales support, and has a lasting impact on your business, including your bottom line.

Optimize your products and services

If customers are leaving because of specific issues with your product or service or shipping method, you have an opportunity to improve. Implementing these insights reduces customer churn and improves the overall product or service for future growth.

Customer retention

# Import dataset
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from pandas import DataFrame
import collections

#Import dataset
sheet_url = 'https://docs.google.com/spreadsheets/d/1QZJsdnk-jtgEVQNQRj7IWuk1sd0F1_qDtuuW0mj8BRg/edit#gid=1329560232'
sheet_url_trf = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
print(sheet_url_trf)
df = pd.read_csv(sheet_url_trf)

df.tail()

"""# Data Cleaning"""

df.shape

df.info()

# check duplicates
df[df.duplicated()]

df[df['CustomerId'].duplicated()]

# check missing values
df.isnull().sum()

"""# EDA"""

# Total churn
churn = df['Exited'].value_counts()
churn

user_not_churn = df['Exited'][df['Exited']==0].count()
user_churn = df['Exited'][df['Exited']==1].count()
# The churn rate formula is: (Lost Customers ÷ Total Customers at the Start of Time Period) x 100
churn_rate = (user_churn/(user_not_churn+user_churn))*100
churn_rate.round(2)

churn_rate = pd.DataFrame(collections.Counter(df['Exited'].tolist()).most_common(),columns=['Exited','Total'])
churn_rate

valuescr = {0: 'Customer Stay', 1:'Customer Churn'}
churn_rate['Exited'].replace(valuescr, inplace = True)

fig = px.pie(churn_rate, values='Total', names='Exited')
fig.update_traces(textposition='inside', textinfo='percent+label+value')
fig.show()

cs = pd.DataFrame(collections.Counter(df['CreditScore'].tolist()).most_common(),columns=['CreditScore','Total'])
cs

cs.describe()

fig = px.scatter(cs, x='CreditScore', y='Total',
                 title="Credit Score",
                 labels={'x':'Credit Score', 'y':'Total Customers'}
                )

fig.show()

geo = pd.DataFrame(collections.Counter(df['Geography'].tolist()).most_common(),columns=['Geography','Total'])
geo

fig = px.pie(geo, values='Total', names='Geography')
fig.update_traces(textposition='inside', textinfo='percent+label+value')
fig.show()

gend = pd.DataFrame(collections.Counter(df['Gender'].tolist()).most_common(),columns=['Gender','Total'])
gend

fig = px.pie(gend, values='Total', names='Gender')
fig.update_traces(textposition='inside', textinfo='percent+label+value')
fig.show()

age = pd.DataFrame(collections.Counter(df['Age'].tolist()).most_common(),columns=['Age','Total'])
age.head()

age.describe()

px.bar(age,x='Age',y='Total',text_auto=True)

tenure = pd.DataFrame(collections.Counter(df['Tenure'].tolist()).most_common(),columns=['Tenure','Total'])
tenure.head()

tenure.describe()

px.bar(tenure,x='Tenure',y='Total',text_auto=True)

balance = pd.DataFrame(collections.Counter(df['Balance'].tolist()).most_common(),columns=['Balance','Total'])
balance

balance.describe()

nop = pd.DataFrame(collections.Counter(df['NumOfProducts'].tolist()).most_common(),columns=['NumOfProducts','Total'])
nop.describe()

fig = px.scatter(balance, x='Balance', y='Total',
                 title="Customer Balance",
                 labels={'x':'Balance', 'y':'Total Customers'}
                )

fig.show()

nop = pd.DataFrame(collections.Counter(df['NumOfProducts'].tolist()).most_common(),columns=['NumOfProducts','Total'])
nop.describe()

hcc = pd.DataFrame(collections.Counter(df['HasCrCard'].tolist()).most_common(),columns=['HasCrCard','Total'])
hcc.describe()

iam = pd.DataFrame(collections.Counter(df['IsActiveMember'].tolist()).most_common(),columns=['IsActiveMember','Total'])
iam.describe()

es = pd.DataFrame(collections.Counter(df['EstimatedSalary'].tolist()).most_common(),columns=['EstimatedSalary','Total'])
es.describe()

com = pd.DataFrame(collections.Counter(df['Complain'].tolist()).most_common(),columns=['Complain','Total'])
com.describe()

ss = pd.DataFrame(collections.Counter(df['Satisfaction Score'].tolist()).most_common(),columns=['Satisfaction Score','Total'])
ss.describe()

pe = pd.DataFrame(collections.Counter(df['Point Earned'].tolist()).most_common(),columns=['Point Earned','Total'])
pe.describe()

plt.figure(figsize = (20, 25))

plt.subplot(4, 2, 1)
plt.gca().set_title('Variable Tenure')
sns.countplot(x = 'Tenure', palette = 'Set1', data = df)

plt.subplot(4, 2, 2)
plt.gca().set_title('Variable NumOfProducts')
sns.countplot(x = 'NumOfProducts', palette = 'Set1', data = df)

plt.subplot(4, 2, 3)
plt.gca().set_title('Variable HasCrCard')
sns.countplot(x = 'HasCrCard', palette = 'Set1', data = df)

plt.subplot(4, 2, 4)
plt.gca().set_title('Variable IsActiveMember')
sns.countplot(x = 'IsActiveMember', palette = 'Set1', data = df)

plt.subplot(4, 2, 5)
plt.gca().set_title('Variable Exited')
sns.countplot(x = 'Exited', palette = 'Set1', data = df)

plt.subplot(4, 2, 6)
plt.gca().set_title('Variable Complain')
sns.countplot(x = 'Complain', palette = 'Set1', data = df)

plt.subplot(4, 2, 7)
plt.gca().set_title('Variable Satisfaction Score')
sns.countplot(x = 'Satisfaction Score', palette = 'Set1', data = df)

for t in df:
    sns.histplot(data = df ,x = t, hue = "Exited",alpha = 0.5)
    plt.show()

"""# Correlation"""

corr = df.corr().round(2)
plt.figure(figsize=(11,8))
sns.heatmap(corr, cmap="Reds",annot=True)
plt.show()

# Convert
df1 = df.copy()
values1 = {'France': 0, 'Germany':1, 'Spain':2}
df1['Geography'].replace(values1, inplace = True)

values2 = {'Male': 0, 'Female' : 1}
df1['Gender'].replace(values2, inplace = True)

values3 = {'DIAMOND': 0, 'GOLD' : 1, 'SILVER' : 2, 'PLATINUM' :3}
df1['Card Type'].replace(values3, inplace = True)

df1.head()

corr = df1.corr().round(2)
plt.figure(figsize=(11,8))
sns.heatmap(corr, cmap="Reds",annot=True)
plt.show()

plt.figure(figsize = (20, 25))
plt.suptitle("Analysis Of Variable Exited",fontweight="bold", fontsize=20)

plt.subplot(4, 2, 1)
plt.gca().set_title('Variable Geography')
sns.countplot(x = 'Geography', hue = 'Exited', palette = 'Set1', data = df)

plt.subplot(4, 2, 2)
plt.gca().set_title('Variable Gender')
sns.countplot(x = 'Gender', hue = 'Exited', palette = 'Set1', data = df)

plt.subplot(4, 2, 3)
plt.gca().set_title('Variable Tenure')
sns.countplot(x = 'Tenure', hue = 'Exited', palette = 'Set1', data = df)

plt.subplot(4, 2, 4)
plt.gca().set_title('Variable NumOfProducts')
sns.countplot(x = 'NumOfProducts', hue = 'Exited', palette = 'Set1', data = df)

plt.subplot(4, 2, 5)
plt.gca().set_title('Variable HasCrCard')
sns.countplot(x = 'HasCrCard', hue = 'Exited', palette = 'Set1', data = df)

plt.subplot(4, 2, 6)
plt.gca().set_title('Variable IsActiveMember')
sns.countplot(x = 'IsActiveMember', hue = 'Exited', palette = 'Set1', data = df)

plt.subplot(4, 2, 7)
plt.gca().set_title('Variable Satisfaction Score')
sns.countplot(x = 'Satisfaction Score', hue = 'Exited', palette = 'Set1', data = df)

plt.subplot(4, 2, 8)
plt.gca().set_title('Variable Card Type')
sns.countplot(x = 'Card Type', hue = 'Exited', palette = 'Set1', data = df)

fig, ax = plt.subplots(figsize=(25, 10))
plt.gca().set_title('Variable Age')
sns.countplot(x = 'Age', hue = 'Exited', palette = 'Set1', data = df)

fig, ax = plt.subplots(figsize=(25, 10))
plt.gca().set_title('Variable Tenure')
sns.countplot(x = 'Tenure', hue = 'Exited', palette = 'Set1', data = df)

fig, ax = plt.subplots(figsize=(40, 10))
plt.gca().set_title('Variable Credit Score')
sns.countplot(x = 'CreditScore', hue = 'Exited', palette = 'Set1', data = df)

Credit_S = pd.DataFrame(collections.Counter(df['CreditScore'].tolist()).most_common(),columns=['CreditScore','Total'])
Credit_S

dfcs = df[df['Exited'] == 1]
Credit_X = dfcs.groupby(['CreditScore'], as_index = False)['Exited'].count()
Credit_X

"""# Clustering

"""

df.columns = ['RowNumber', 'CustomerId', 'Surname', 'CreditScore', 'Geography',
       'Gender', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 'HasCrCard',
       'IsActiveMember', 'EstimatedSalary', 'Exited', 'Complain',
       'SatisfactionScore', 'CardType', 'PointEarned']

fig, ax = plt.subplots(2,4,figsize=(20,10))
ax = ax.flatten()

for i, column in enumerate(['CreditScore','Age','Tenure', 'Balance'
                            ,'EstimatedSalary','SatisfactionScore'
                            ,'PointEarned']):
    sns.boxplot(data=df, y=column, ax=ax[i])
    ax[i].set_title(f'Boxplot of {column}',fontsize=15)
    ax[i].set_xlabel(column)

plt.tight_layout()
plt.show()

plt.figure(figsize = (25, 20))
plt.suptitle("Analysis Of Variable Class",fontweight="bold", fontsize=20)

plt.subplot(3,2,1)
sns.boxplot(x="Exited", y="CreditScore", data=df)

plt.subplot(3,2,2)
sns.boxplot(x="Exited", y="Age", data=df)

plt.subplot(3,2,3)
sns.boxplot(x="Exited", y="Balance", data=df)

plt.subplot(3,2,4)
sns.boxplot(x="Exited", y="EstimatedSalary", data=df)

plt.subplot(3,2,5)
sns.boxplot(x="Exited", y="PointEarned", data=df)

fig, ax = plt.subplots(5,1,figsize=(25,15))
ax=ax.flatten()
for i, column in enumerate(['Geography','Gender','HasCrCard','IsActiveMember','Age']):
    df.groupby(['CardType',column])['RowNumber'].count().unstack()\
    .plot(kind='bar', stacked=True, ax=ax[i])
    ax[i].set_title(f'Segmentation Card Type by {column}', fontsize=15)
    ax[i].set_xlabel('Card Type',color='green')
    ax[i].set_xticklabels(ax[i].get_xticklabels(),rotation=0)
    ax[i].grid(True, axis='y', linestyle=':')
plt.tight_layout()

!pip install gdown

!gdown https://drive.google.com/uc?id=15EWQ3adcKsWdxIdJdSu9x_msWxbxxz6l

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#Import libraries
from sklearn.cluster import KMeans                                             # to perform the k-means algorithm
from sklearn.preprocessing import MinMaxScaler,StandardScaler,RobustScaler     # to sacalling different attribute
from sklearn import cluster                                                    # for machine learning and statistical modelling (we use it for clustering)
import matplotlib.cm as cm                                                     # provide a large set of colormaps(cm)
from sklearn.metrics import silhouette_samples, silhouette_score               # for perform silhoutte analysis
from sklearn.datasets import make_blobs

df2 = df1.copy()

df2.info()

df2 = df2.drop(['RowNumber','Surname', 'CustomerId'],axis=1)
df2.info()

# Define Standard Scale dataset
ss_scale_df = df2.copy()
column = ['Balance','EstimatedSalary']
# using StandardScaler Scaler
ss_scaler = StandardScaler()
ss_scale_df[column] = ss_scaler.fit_transform(ss_scale_df[column])

sns.scatterplot (data = ss_scale_df, x='Balance', y='EstimatedSalary')

# K-Means Clustering by elbow method
distortions = []
K = range(1,11)
for k in K:
    kmeanModel = KMeans(n_clusters=k,init='k-means++')
    kmeanModel.fit(df2)  #---------------------Ini yang diganti
    distortions.append(kmeanModel.inertia_)

plt.figure(figsize=(10,5))
plt.plot(K, distortions, 'bx-')
plt.xlabel('k')
plt.ylabel('Inertia')
plt.title('The Elbow Method showing the optimal k')
plt.show()
print(distortions)

# Commented out IPython magic to ensure Python compatibility.
# Generating the sample data from make_blobs
# This particular setting has one distinct cluster and 3 clusters placed close
# together.
def silhoutte_analysis(data,cluster=[2,3,4]):
    X = data.to_numpy()

    range_n_clusters = cluster

    for n_clusters in range_n_clusters:
        # Create a subplot with 1 row and 2 columns
        fig, (ax1, ax2) = plt.subplots(1, 2)
        fig.set_size_inches(12, 5)

        # The 1st subplot is the silhouette plot
        # The silhouette coefficient can range from -1, 1 but in this example all
        # lie within [-0.1, 1]
        ax1.set_xlim([-0.1, 1])
        # The (n_clusters+1)*10 is for inserting blank space between silhouette
        # plots of individual clusters, to demarcate them clearly.
        ax1.set_ylim([0, len(X) + (n_clusters + 1) * 10])

        # Initialize the clusterer with n_clusters value and a random generator
        # seed of 10 for reproducibility.
        clusterer = KMeans(n_clusters=n_clusters, random_state=10, init = 'k-means++')
        cluster_labels = clusterer.fit_predict(X)

        # The silhouette_score gives the average value for all the samples.
        # This gives a perspective into the density and separation of the formed
        # clusters
        silhouette_avg = silhouette_score(X, cluster_labels)
        print(
            "For n_clusters =",
            n_clusters,
            "The average silhouette_score is :",
            silhouette_avg,
        )

        # Compute the silhouette scores for each sample
        sample_silhouette_values = silhouette_samples(X, cluster_labels)

        y_lower = 10
        for i in range(n_clusters):
            # Aggregate the silhouette scores for samples belonging to
            # cluster i, and sort them
            ith_cluster_silhouette_values = sample_silhouette_values[cluster_labels == i]

            ith_cluster_silhouette_values.sort()

            size_cluster_i = ith_cluster_silhouette_values.shape[0]
            y_upper = y_lower + size_cluster_i

            color = cm.nipy_spectral(float(i) / n_clusters)
            ax1.fill_betweenx(
                np.arange(y_lower, y_upper),
                0,
                ith_cluster_silhouette_values,
                facecolor=color,
                edgecolor=color,
                alpha=0.7,
            )

            # Label the silhouette plots with their cluster numbers at the middle
            ax1.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))

            # Compute the new y_lower for next plot
            y_lower = y_upper + 10  # 10 for the 0 samples

        ax1.set_title("The silhouette plot for the various clusters.")
        ax1.set_xlabel("The silhouette coefficient values")
        ax1.set_ylabel("Cluster label")

        # The vertical line for average silhouette score of all the values
        ax1.axvline(x=silhouette_avg, color="red", linestyle="--")

        ax1.set_yticks([])  # Clear the yaxis labels / ticks
        ax1.set_xticks([-0.1, 0, 0.2, 0.4, 0.6, 0.8, 1])

        # 2nd Plot showing the actual clusters formed
        colors = cm.nipy_spectral(cluster_labels.astype(float) / n_clusters)
        ax2.scatter(
            X[:, 0], X[:, 1], marker=".", s=30, lw=0, alpha=0.7, c=colors, edgecolor="k"
        )

        # Labeling the clusters
        centers = clusterer.cluster_centers_
        # Draw white circles at cluster centers
        ax2.scatter(
            centers[:, 0],
            centers[:, 1],
            marker="o",
            c="white",
            alpha=1,
            s=200,
            edgecolor="k",
        )

        for i, c in enumerate(centers):
            ax2.scatter(c[0], c[1], marker="$%d$" % i, alpha=1, s=50, edgecolor="k")

        ax2.set_title("The visualization of the clustered data.")
        ax2.set_xlabel("Feature space for the 1st feature")
        ax2.set_ylabel("Feature space for the 2nd feature")

        plt.suptitle(
            "Silhouette analysis for KMeans clustering on sample data with n_clusters = %d"
#             % n_clusters,
            fontsize=14,
            fontweight="bold",
        )

    plt.show()

df1.info()

# Create silhoutte analysis of cluster 2-4 based on elbow method
silhoutte_analysis(df1[['CustomerId', 'Balance']],list(range(2,5)))



# make cluster
Cluster_4 = ss_scale_df.copy()

cluster_model = KMeans(n_clusters=4)   #------ Yang di ubah
cluster_model.fit_predict(Cluster_4[['Balance', 'EstimatedSalary']])
Cluster_4['cluster'] = cluster_model.labels_
Cluster_4.head()

"""# Predict RF"""

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
from yellowbrick.cluster import SilhouetteVisualizer

df3 = df2.copy()

df3.info()

df3 = df3.drop(['CreditScore','Tenure', 'NumOfProducts','HasCrCard','IsActiveMember','Complain','Satisfaction Score','Card Type','Point Earned'],axis=1)
df3.info()

corr = df3.corr().round(2)
plt.figure(figsize=(11,8))
sns.heatmap(corr, cmap="Reds",annot=True)
plt.show()

from sklearn.model_selection import train_test_split, cross_val_score, cross_val_predict
from sklearn.metrics import accuracy_score

# Define the data
X = df3.drop('Exited', axis=1)
y = df3["Exited"]

# Split into training and test dataset test size 20% and train size 80%
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2,random_state=7)

#Random Forest
from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier()
rfc.fit(X_train, y_train)
y_train_pred = rfc.predict(X_train)

from sklearn.ensemble import RandomForestClassifier
rfc = RandomForestClassifier()
rfc.fit(X_train, y_train)
y_pred = rfc.predict(X_test)
print("Accuracy Score :", accuracy_score(y_test, y_pred)*100, "%")

#Menampilkan hasil training dengan confusion matrix
from sklearn.metrics import classification_report
# Predict
y_train_pred = rfc.predict(X_train)
# Print classification report
print('Classification Report Training Model (Random Forest) :')
print(classification_report(y_train, y_train_pred))

#Menampilkan hasil training model dengan visualisasi heatmap dari confusion matrix
confusion_matrix_df = pd.DataFrame((confusion_matrix(y_train, y_train_pred)), ('No churn', 'Churn'), ('No churn', 'Churn'))

# Plot confusion matrix
plt.figure()
heatmap = sns.heatmap(confusion_matrix_df, annot=True, annot_kws={'size': 14}, fmt='d', cmap='Blues')
heatmap.yaxis.set_ticklabels(heatmap.yaxis.get_ticklabels(), rotation=0, ha='right', fontsize=14)
heatmap.xaxis.set_ticklabels(heatmap.xaxis.get_ticklabels(), rotation=0, ha='right', fontsize=14)

plt.title('Confusion Matrix Training Model', fontsize=18, color='Black')
plt.ylabel('True label', fontsize=14)
plt.xlabel('Predicted label', fontsize=14)
plt.show()

#Menampilkan hasil testing model dengan confusion matrix
# Predict
y_test_pred = rfc.predict(X_test)
# Print classification report
print('Classification Report Testing Model (Random Forest):')
print(classification_report(y_test, y_test_pred))

#Menampilkan hasil testing model dengan visualisasi heatmap dari confusion matrix
confusion_matrix_df = pd.DataFrame((confusion_matrix(y_test, y_test_pred)), ('No churn', 'Churn'), ('No churn', 'Churn'))

# Plot confusion matrix
plt.figure()
heatmap = sns.heatmap(confusion_matrix_df, annot=True, annot_kws={'size': 14}, fmt='d', cmap='Blues')
heatmap.yaxis.set_ticklabels(heatmap.yaxis.get_ticklabels(), rotation=0, ha='right', fontsize=14)
heatmap.xaxis.set_ticklabels(heatmap.xaxis.get_ticklabels(), rotation=0, ha='right', fontsize=14)

plt.title('Confusion Matrix Testing Model', fontsize=18, color='black')
plt.ylabel('True label', fontsize=14)
plt.xlabel('Predicted label', fontsize=14)
plt.show()

"""# Predict LR"""

df3.info()

# Define the data
X = df3.drop('Exited', axis=1)
y = df3["Exited"]

# Split into training and test dataset
X_training, X_test, y_training, y_test = train_test_split(X,y,test_size = 0.2,random_state=6)

# Check split result
for df in [X_training, X_test, y_training, y_test]:
  print(df.shape)

# Check class balance in each datasets
for df in [y_training,y_test]:
  df3 = df.value_counts()
  print(df3)

# Fit the Logistic regression model
model = LogisticRegression(class_weight='balanced',max_iter=500)
model.fit(X_training, y_training)

model.score(X_training, y_training)

ax = plt.subplot()
sns.heatmap(confusion_matrix(y_training, model.predict(X_training)), annot=True, fmt = 'd')
ax.set_xlabel('Predicted labels');
ax.set_ylabel('True labels');

model.score(X_test,y_test)