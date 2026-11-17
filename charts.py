import matplotlib.pyplot as plt
# sample data
months=["jan", "feb", "mar", "apr", "may", "jun"]
sales=[100,150,120,180,200,220]

#line chart
plt.figure()
plt.plot(months, sales, marker='o', label='sales')
plt.title('monthly sales')
plt.xlabel('months')
plt.ylabel('sales')
plt.legend()
plt.savefig('line_chart.png')
plt.close()

#bar chart
plt.figure()
plt.bar(months,sales,color='green',label='sale')
plt.title('monthly sales bar chart')
plt.xlabel('months')
plt.ylabel('sales')
plt.legend()
plt.savefig('bar_chart.png')
plt.close()

#histogram

marks=[45,50,55,60,65,70,75,80,85,90,95]

plt.figure()
plt.hist(marks,bins=5,color='orange',edgecolor='black')
plt.title('marks distribution')
plt.xlabel('marks')
plt.ylabel('frequency')
plt.savefig('histogram.png')
plt.close()

#scatter plot
height=[150,155,160,165,170,175,180,]
weight=[45,50,55,60,65,70,75]

plt.figure()
plt.scatter(height,weight,color='red',label='students')
plt.title('height vs weight')
plt.xlabel('height')
plt.ylabel('weight')
plt.legend()
plt.savefig('scatter_plot.png')
plt.close()

print("all four charts saved successfully!")