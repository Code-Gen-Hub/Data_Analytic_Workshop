import pandas as pd
import matplotlib.pyplot as plt

file_path = '/content/sample_data/Employee Sample Data.xlsx'
df = pd.read_excel(file_path)

# display all column and rows, set width
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 250)

current_df = df[df['Exit Date'].isna()]

# sort
sorted_df = current_df.sort_values(by = 'Annual Salary', ascending=False)

# reset index
sorted_df.reset_index(inplace = True, drop = True)
sorted_df.index += 1

# export to excel file
# sorted_df.to_excel('/content/sample_data/New Employee List.xlsx')

salary_sum = sorted_df.groupby('Department')['Annual Salary'].sum()

plt.pie(salary_sum, labels=salary_sum.index, autopct='%1i%%', colors=['#ff9999','#66b3ff','#99ff99', '#ec7063'])
plt.title('Pie Chart', loc='center', y=-0.1)
plt.savefig('/content/sample_data/piechart.pdf')
plt.show()
print(salary_sum)
