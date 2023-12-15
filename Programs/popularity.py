import matplotlib.pyplot as plt

languages = ['Java', 'Python', 'PHP', 'C++']
popularity = [22.2, 17, 8.8, 6.5]

plt.bar(languages, popularity)
plt.xlabel('Programming Languages')
plt.ylabel('Popularity (%)')
plt.title('Programming Language Popularity')
plt.show()
