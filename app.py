import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import matplotlib.pyplot as plt

# Tạo DataFrame từ dữ liệu ban đầu và dữ liệu dự đoán
# Thay thế 'data' và 'pred_future_visual' bằng biến chứa dữ liệu tương ứng của bạn
df_data = pd.DataFrame(data, columns=['Open', 'High', 'Low', 'Close'])
df_pred = pd.DataFrame(pred_future_visual, columns=['Open', 'High', 'Low', 'Close'])

# Tạo ứng dụng Dash
app = dash.Dash(__name__)

# Định nghĩa giao diện người dùng
app.layout = html.Div(children=[
    html.H1(children='Gold Price Data'),

    html.Div(children=[
        dcc.Graph(
            id='original-data-chart',
            figure={
                'data': [
                    {'x': df_data.index, 'y': df_data['Open'], 'name': 'Open'},
                    {'x': df_data.index, 'y': df_data['High'], 'name': 'High'},
                    {'x': df_data.index, 'y': df_data['Low'], 'name': 'Low'},
                    {'x': df_data.index, 'y': df_data['Close'], 'name': 'Close'}
                ],
                'layout': {
                    'title': 'Original Data',
                    'xaxis': {'title': 'Date'},
                    'yaxis': {'title': 'Price'}
                }
            }
        ),

        html.H1(children='Gold Price Prediction'),
        dcc.Graph(
            id='prediction-data-chart',
            figure={
                'data': [
                    {'x': df_pred.index, 'y': df_pred['Open'], 'name': 'Open'},
                    {'x': df_pred.index, 'y': df_pred['High'], 'name': 'High'},
                    {'x': df_pred.index, 'y': df_pred['Low'], 'name': 'Low'},
                    {'x': df_pred.index, 'y': df_pred['Close'], 'name': 'Close'}
                ],
                'layout': {
                    'title': 'Prediction Data',
                    'xaxis': {'title': 'Date'},
                    'yaxis': {'title': 'Price'}
                }
            }
        )
    ])
])

# Chạy ứng dụng Dash
if __name__ == '__main__':
    app.run_server(debug=True)