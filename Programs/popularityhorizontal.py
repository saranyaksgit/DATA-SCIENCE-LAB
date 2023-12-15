import matplotlib.pyplot as plt

programming_languages = ['Java', 'Python', 'PHP', 'C++']
popularity = [22.2, 17, 8.8, 6.5]

plt.barh(programming_languages, popularity)
plt.xlabel('Popularity')
plt.ylabel('Programming Language')
plt.title('Popularity of Programming Languages')

plt.show()
