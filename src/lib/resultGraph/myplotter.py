import matplotlib.pyplot as plt

def freq_plot(keys,values,xlabel='keys'):
    plt.bar(keys,values,color='green',width=0.5)
    plt.xlabel(xlabel)
    plt.ylabel('frequency')
    plt.xticks(rotation=45)
    plt.show()