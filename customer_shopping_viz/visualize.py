import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import MaxNLocator
# Đảm bảo font hiển thị tiếng Việt tốt
plt.rcParams['font.family'] = 'Arial'

# Đọc dữ liệu
df = pd.read_csv("customer_shopping_data.csv")

# Chuyển đổi cột 'Shopping Date' thành datetime
df['invoice_date'] = pd.to_datetime(df['invoice_date'], dayfirst=True)
# Tạo thêm cột 'Total' = Price * Quantity
df['Total'] = df['price'] * df['quantity']

# Visualize theo thoigian 
def visualize_transactions_over_time():
    df_time = df.groupby(df['invoice_date'].dt.to_period("M"))['Total'].sum()
    df_time.index = df_time.index.to_timestamp()
    
    plt.figure(figsize=(12, 6))
    df_time.plot(kind='line', marker='o', color='blue')
    plt.title("Tổng giao dịch theo thời gian (tháng)")
    plt.xlabel("Thời gian")
    plt.ylabel("Doanh thu ($)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    visualize_transactions_over_time()
    #visualize_transactions_by_location()
    #visualize_transactions_by_gender()
    #visualize_transactions_by_age_group()
  


