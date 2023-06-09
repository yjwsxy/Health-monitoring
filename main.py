import random
from random import randint
from streamlit_echarts import JsCode
from streamlit_echarts import st_echarts
from streamlit_echarts import st_pyecharts
import base64
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image



@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def main():
    ST_PAGES = {
        "main": main_page,
        "Heart Rate": Heart_rate,
        "Nutrition": Nutrition,
        "Sleep": Sleep1,
        "Weight": Weight,
    }
    st.write(
        """
        <style>
        .title{
           text-align: center;
           }
           </style>
           """,
        unsafe_allow_html=True
    )


    st.write("<h1 class='title'>Health Monitoring</h1>", unsafe_allow_html=True)
    st.write("")
    st.markdown("---")
    st.write("")
    st.sidebar.header("Configuration")

    select_lang = st.sidebar.selectbox(
        "API:", ('echarts', '')
    )
    if select_lang == "echarts":
        page = st.sidebar.selectbox("Choose an example", options=list(ST_PAGES.keys()))
        ST_PAGES[page]()




def set_background_image(image_file):
    bin_str = get_base64_of_bin_file(image_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/jpg;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str

    st.markdown(page_bg_img, unsafe_allow_html=True)
    return


def main_page():
    st.write(
        """
        <div style="font-family: Arial; font-size: 22px; color: black; line-height: 1.5;">
            This is a visualization system for health indicators. We have twenty survey 
            subjects, presenting a 1:1 gender ratio and uniform age segmentation. 
            In this system, we will start with the data obtained from four aspects 
            of the survey, extract the relationships between different indicators 
            and age and gender from the survey population, and focus on visualizing 
            these data using charts and being able to interact with users
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    c1, c2 = st.columns(2)
    options1 = {
        "tooltip": {  # 鼠标悬停时显示提示框的设置
            "trigger": "axis",
            "axisPointer": {
                "type": "shadow"
            }
        },
        "grid": {  # 图表区域的设置
            "left": "3%",
            "right": "4%",
            "bottom": "3%",
            "containLabel": True
        },
        "xAxis": [  # x轴设置
            {
                "type": "category",
                "data": ["Gender"],
                "axisTick": {"alignWithLabel": True},
                "axisLine": {"show": False},
            }
        ],
        "yAxis": [  # y轴设置
            {
                "type": "value",
                "show": False,  # 不显示y轴线
                "minInterval": 10,  # 最小间隔为10
            }
        ],
        "series": [  # 系列数据
            {
                "name": "Male",  # 系列名称
                "type": "bar",
                "barWidth": "30%",
                "data": [10],  # 数据
                "label": {  # 标签的设置
                    "show": True,
                    "position": "top",
                    "color": "#ffffff",
                    "fontSize": 16,
                    "formatter": "{c}",
                },
                "itemStyle": {  # 样式的设置
                    "color": "#f1a667",
                    "opacity": 0.6,
                    "barBorderRadius": 25,
                },
            },
            {
                "name": "Female",  # 系列名称
                "type": "bar",
                "barWidth": "30%",
                "data": [10],  # 数据
                "label": {  # 标签的设置
                    "show": True,
                    "position": "top",
                    "color": "#ffffff",
                    "fontSize": 16,
                    "formatter": "{c}",
                },
                "itemStyle": {  # 样式的设置
                    "color": "#6abf80",
                    "opacity": 0.6,
                    "barBorderRadius": 25,
                },
            },
        ],
        "legend": {  # 图例的设置
            "data": [{
                "name": "Male",
                "icon": "circle",
                "textStyle": {"color": "#f1a667"}
            }, {
                "name": "Female",
                "icon": "circle",
                "textStyle": {"color": "#6abf80"}
            }]
        }
    }
    with c1:
        st_echarts(options1, height='500px', width='300px')
    options2 = {
        "tooltip": {  # 鼠标悬停时显示提示框的设置
            "trigger": "item",
            "formatter": "{a} <br/>{b}: {c} ({d}%)"
        },
        "legend": {  # 图例的设置
            "orient": "vertical",  # 图例方向
            "left": "left",  # 图例位置
            "data": ['0-20', '20-40', '40-60', '60-80'],
            "textStyle" : {
                "color" : "white"
            }
        },
        "series": [  # 系列数据
            {
                "name": "Proportion",  # 系列名称
                "type": "pie",
                "radius": ["40%", "70%"],  # 饼图半径
                "avoidLabelOverlap": False,
                "label": {  # 标签的设置
                    "show": True,
                    "position": "inside",
                    "formatter": "{b|{b}:}\n{c|{c} ({d}%)}",
                    "fontSize": 20,
                    "formatter": "{c} ({d}%)",
                    "rich": {
                        "b": {
                            "fontSize": 18,
                            "lineHeight": 25
                        },
                        "c": {
                            "lineHeight": 20
                        }
                    }
                },
                "labelLine": {  # 标签的连接线设置
                    "show": False,
                },
                "data": [  # 数据
                    {"value": 4, "name": "0-20"},
                    {"value": 6, "name": "20-40"},
                    {"value": 6, "name": "40-60"},
                    {"value": 4, "name": "60-80"}
                ],
                "emphasis": {
                    "itemStyle": {"shadowBlur": 10, "shadowOffsetX": 0, "shadowColor": "rgba(0, 0, 0, 0.5)"}
                },
                "itemStyle": {  # 样式的设置
                    "borderWidth": 5,
                    "borderColor": "#fff",
                },
            }
        ],
    }
    with c2:
        st_echarts(options2, height='620px', width='400px')


def Heart_rate():
    st.write(
        """
        <div style="font-family: Arial; font-size: 22px; color: black; line-height: 1.5;">
            Heart rate index: The heart rate of some investigators is displayed with a line chart to 
            visually see the heart rate of subjects of different ages
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    st.markdown("---")
    st.write("")

    options = {
        "title": {
            "text": 'Heart Rate Over Time',
        },
        "tooltip": {
            "trigger": 'axis',
            "axisPointer": {
                "type": 'cross',
                "label": {
                    "backgroundColor": '#6a7985'
                }
            }
        },
        "legend": {
            "data": ['Age 24', 'Age 75']
        },
        "toolbox": {
            "feature": {
                "saveAsImage": {}
            }
        },
        "grid": {
            "left": '3%',
            "right": '4%',
            "bottom": '3%',
            "containLabel": "true"
        },
        "xAxis": [
            {
                "type": 'category',
                "boundaryGap": "false",
                "data": ["2023/1/1 3:00:00", "2023/1/1 6:00:00", "2023/1/1 9:00:00", "2023/1/1 12:00:00",
                         "2023/1/1 15:00:00", "2023/1/1 18:00:00", "2023/1/1 21:00:00"]
            }
        ],
        "yAxis": [
            {
                "type": 'value'
            }
        ],
        "series": [
            {
                "name": 'Age 24',
                "type": 'line',
                "stack": 'Total',
                "areaStyle": {},
                "emphasis": {
                    "focus": 'series'
                },
                "data": [73, 76, 80, 85, 78, 75, 73]
            },
            {
                "name": 'Age 75',
                "type": 'line',
                "stack": 'Total',
                "areaStyle": {},
                "emphasis": {
                    "focus": 'series'
                },
                "data": [60, 64, 72, 76, 70, 67, 60]
            }
        ]
    }
    st_echarts(
        options=options, height="400px",
    )
    image = Image.open("dc.jpg")
    st.image([image], caption=['Focus on Heart Health'], width=300)  # 放一张图片，caption是标题
    # st.image([image], caption=['food'],use_column_width=True) # 没有width的情况是这种就是图和上面的表大小对齐，不用调节宽度，一般是放一张图片的情况
    # st.image([image,image], caption=['food', 'food'],width = 300) #放多张图片


def Nutrition():
    st.write(
        """
        <div style="font-family: Arial; font-size: 22px; color: black; line-height: 1.5;">
            Nutrition: 
            The average intake of several nutrients is displayed with a monitoring component, 
            and gender is linked to the level of nutrient intake. We compared the average intake of the 
            four nutrients we selected with a radar map
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    st.markdown("---")
    st.write("")
    # 从CSV文件中读取数据
    df = pd.read_csv("营养数据.csv")




    # 在 Streamlit 上下文中显示数据
    with st.container():
            # 选择只包含四列的子数据集
            selected_columns = df[['VitaminC(mg)', 'Protein(mg)', 'Carbohydrate(g)', 'Fat(kal)']]

            # 计算第一个平均值
            average_values1 = selected_columns.mean()

            # 创建四个监控组件，显示第一个平均值
            col1, col2, col3, col4 = st.columns(4)

            col1.metric("Vitamin(mg)-AVG(All)", average_values1['VitaminC(mg)'])
            col2.metric("Protein(mg)-AVG(All)", average_values1['Protein(mg)'])
            col3.metric("Carbohydrate(g)-AVG(All)", average_values1['Carbohydrate(g)'])
            col4.metric("Fat(kal)-AVG(All)", average_values1['Fat(kal)'])

            # 选择男性的人的数据
            selected_data = df[df['Gender'] == 'male']

            # 计算第二个平均值
            average_values2 = selected_data[['VitaminC(mg)', 'Protein(mg)', 'Carbohydrate(g)', 'Fat(kal)']].mean()

            # 创建四个监控组件，显示第二个平均值和箭头
            col5, col6, col7, col8 = st.columns(4)

            col5.metric("Vitamin(mg)-AVG(Male)", average_values2['VitaminC(mg)'])
            col6.metric("Protein(mg)-AVG(Male)", average_values2['Protein(mg)'])
            col7.metric("Carbohydrate(g)-AVG(Male))", average_values2['Carbohydrate(g)'])
            col8.metric("Fat(kal)-AVG(Male)", average_values2['Fat(kal)'])

            # 计算两个平均值的差距
            diff = average_values2 - average_values1
            diff_rounded = diff.round(1)

            # 创建四个监控组件，显示差距和箭头
            col9, col10, col11, col12 = st.columns(4)

            # 根据差距的正负值选择箭头方向和样式
            arrow_direction = ['▲' if val > 0 else '▼' for val in diff]
            arrow_color = ['green' if val > 0 else 'red' for val in diff]

            # 使用HTML和CSS显示箭头和差距数据
            col9.markdown(
                f'<div style="display: flex; align-items: center;"><span style="color: {arrow_color[0]}; font-size: 20px;">{arrow_direction[0]}</span><span style="margin-left: 5px;">{diff_rounded["VitaminC(mg)"]}</span></div>',
                unsafe_allow_html=True
            )
            col10.markdown(
                f'<div style="display: flex; align-items: center;"><span style="color: {arrow_color[1]}; font-size: 20px;">{arrow_direction[1]}</span><span style="margin-left: 5px;">{diff_rounded["Protein(mg)"]}</span></div>',
                unsafe_allow_html=True
            )
            col11.markdown(
                f'<div style="display: flex; align-items: center;"><span style="color: {arrow_color[2]}; font-size: 20px;">{arrow_direction[2]}</span><span style="margin-left: 5px;">{diff_rounded["Carbohydrate(g)"]}</span></div>',
                unsafe_allow_html=True
            )
            col12.markdown(
                f'<div style="display: flex; align-items: center;"><span style="color: {arrow_color[3]}; font-size: 20px;">{arrow_direction[3]}</span><span style="margin-left: 5px;">{diff_rounded["Fat(kal)"]}</span></div>',
                unsafe_allow_html=True
            )
            # 选择女性的人的数据
            selected_data = df[df['Gender'] == 'female']

            # 计算第三个平均值
            average_values3 = selected_data[['VitaminC(mg)', 'Protein(mg)', 'Carbohydrate(g)', 'Fat(kal)']].mean()

            # 创建四个监控组件，显示第二个平均值和箭头
            col13, col14, col15, col16 = st.columns(4)

            col13.metric("Vitamin(mg)-AVG(Female)", average_values3['VitaminC(mg)'])
            col14.metric("Protein(mg)-AVG(Female)", average_values3['Protein(mg)'])
            col15.metric("Carbohydrate(g)-AVG(Female)", average_values3['Carbohydrate(g)'])
            col16.metric("Fat(kal)-AVG(Female)", average_values3['Fat(kal)'])

            # 计算两个平均值的差距
            diff = average_values3 - average_values1
            diff_rounded = diff.round(1)

            # 创建四个监控组件，显示差距和箭头
            col17, col18, col19, col20 = st.columns(4)

            # 根据差距的正负值选择箭头方向和样式
            arrow_direction = ['▲' if val > 0 else '▼' for val in diff]
            arrow_color = ['green' if val > 0 else 'red' for val in diff]

            # 使用HTML和CSS显示箭头和差距数据
            col17.markdown(
                f'<div style="display: flex; align-items: center;"><span style="color: {arrow_color[0]}; font-size: 20px;">{arrow_direction[0]}</span><span style="margin-left: 5px;">{diff_rounded["VitaminC(mg)"]}</span></div>',
                unsafe_allow_html=True
            )
            col18.markdown(
                f'<div style="display: flex; align-items: center;"><span style="color: {arrow_color[1]}; font-size: 20px;">{arrow_direction[1]}</span><span style="margin-left: 5px;">{diff_rounded["Protein(mg)"]}</span></div>',
                unsafe_allow_html=True
            )
            col19.markdown(
                f'<div style="display: flex; align-items: center;"><span style="color: {arrow_color[2]}; font-size: 20px;">{arrow_direction[2]}</span><span style="margin-left: 5px;">{diff_rounded["Carbohydrate(g)"]}</span></div>',
                unsafe_allow_html=True
            )
            col20.markdown(
                f'<div style="display: flex; align-items: center;"><span style="color: {arrow_color[3]}; font-size: 20px;">{arrow_direction[3]}</span><span style="margin-left: 5px;">{diff_rounded["Fat(kal)"]}</span></div>',
                unsafe_allow_html=True
            )

            # 选择年轻人的数据
            selected_data = df.query('Age < 35')

            # 计算第四个平均值
            average_values4 = selected_data[['VitaminC(mg)', 'Protein(mg)', 'Carbohydrate(g)', 'Fat(kal)']].mean()

            # 创建四个监控组件，显示第二个平均值和箭头
            col21, col22, col23, col24 = st.columns(4)

            col21.metric("Vitamin(mg)-AVG(Age<35)", average_values4['VitaminC(mg)'])
            col22.metric("Protein(mg)-AVG(Age < 35)", average_values4['Protein(mg)'])
            col23.metric("Carbohydrate(g)-AVG(Age < 35)", average_values4['Carbohydrate(g)'])
            col24.metric("Fat(kal)-AVG(Age < 35)", average_values4['Fat(kal)'])

            # 计算两个平均值的差距
            diff = average_values4 - average_values1
            diff_rounded = diff.round(1)

            # 创建四个监控组件，显示差距和箭头
            col25, col26, col27, col28 = st.columns(4)

            # 根据差距的正负值选择箭头方向和样式
            arrow_direction = ['▲' if val > 0 else '▼' for val in diff]
            arrow_color = ['green' if val > 0 else 'red' for val in diff]

            # 使用HTML和CSS显示箭头和差距数据
            col25.markdown(
                f'<div style="display: flex; align-items: center;"><span style="color: {arrow_color[0]}; font-size: 20px;">{arrow_direction[0]}</span><span style="margin-left: 5px;">{diff_rounded["VitaminC(mg)"]}</span></div>',
                unsafe_allow_html=True
            )
            col26.markdown(
                f'<div style="display: flex; align-items: center;"><span style="color: {arrow_color[1]}; font-size: 20px;">{arrow_direction[1]}</span><span style="margin-left: 5px;">{diff_rounded["Protein(mg)"]}</span></div>',
                unsafe_allow_html=True
            )
            col27.markdown(
                f'<div style="display: flex; align-items: center;"><span style="color: {arrow_color[2]}; font-size: 20px;">{arrow_direction[2]}</span><span style="margin-left: 5px;">{diff_rounded["Carbohydrate(g)"]}</span></div>',
                unsafe_allow_html=True
            )
            col28.markdown(
                f'<div style="display: flex; align-items: center;"><span style="color: {arrow_color[3]}; font-size: 20px;">{arrow_direction[3]}</span><span style="margin-left: 5px;">{diff_rounded["Fat(kal)"]}</span></div>',
                unsafe_allow_html=True
            )

            # 选择老年人的数据
            selected_data = df.query('Age > 35')

            # 计算第五个平均值
            average_values5 = selected_data[['VitaminC(mg)', 'Protein(mg)', 'Carbohydrate(g)', 'Fat(kal)']].mean()

            # 创建四个监控组件，显示第五个平均值和箭头
            col29, col30, col31, col32 = st.columns(4)

            col29.metric("Vitamin(mg)-AVG(Age>35)", average_values5['VitaminC(mg)'])
            col30.metric("Protein(mg)-AVG(Age>35)", average_values5['Protein(mg)'])
            col31.metric("Carbohydrate(g)-AVG(Age>35)", average_values5['Carbohydrate(g)'])
            col32.metric("Fat(kal)-AVG(Age>35)", average_values5['Fat(kal)'])

            # 计算两个平均值的差距
            diff = average_values5 - average_values1
            diff_rounded = diff.round(1)

            # 创建四个监控组件，显示差距和箭头
            col33, col34, col35, col36 = st.columns(4)

            # 根据差距的正负值选择箭头方向和样式
            arrow_direction = ['▲' if val > 0 else '▼' for val in diff]
            arrow_color = ['green' if val > 0 else 'red' for val in diff]

            # 使用HTML和CSS显示箭头和差距数据
            col33.markdown(
                f'<div style="display: flex; align-items: center;"><span style="color: {arrow_color[0]}; font-size: 20px;">{arrow_direction[0]}</span><span style="margin-left: 5px;">{diff_rounded["VitaminC(mg)"]}</span></div>',
                unsafe_allow_html=True
            )
            col34.markdown(
                f'<div style="display: flex; align-items: center;"><span style="color: {arrow_color[1]}; font-size: 20px;">{arrow_direction[1]}</span><span style="margin-left: 5px;">{diff_rounded["Protein(mg)"]}</span></div>',
                unsafe_allow_html=True
            )
            col35.markdown(
                f'<div style="display: flex; align-items: center;"><span style="color: {arrow_color[2]}; font-size: 20px;">{arrow_direction[2]}</span><span style="margin-left: 5px;">{diff_rounded["Carbohydrate(g)"]}</span></div>',
                unsafe_allow_html=True
            )
            col36.markdown(
                f'<div style="display: flex; align-items: center;"><span style="color: {arrow_color[3]}; font-size: 20px;">{arrow_direction[3]}</span><span style="margin-left: 5px;">{diff_rounded["Fat(kal)"]}</span></div>',
                unsafe_allow_html=True
            )
    data1 = [[82.2, 69.6, 169.3, 204.9]]
    data2 = [[76.4, 77.2, 163.8, 197.8]]
    data3 = [[88.0, 62.0, 174.8, 212.0]]

    options1 = {
        "title": {
            "text": 'Health Monitoring - Radar',
            "left": 'center',
            "textStyle": {
                "color": '#eee'
            }
        },
        "legend": {
            "bottom": 5,
            "data": ['AVG(All)', 'AVG(Male)'],
            "itemGap": 20,
            "textStyle": {
                "color": '#fff',
                "fontSize": 14
            },
        },
        "radar": {
            "indicator": [
                {"name": 'Vitamin(mg)', "max": 90},
                {"name": 'Protein(mg)', "max": 80},
                {"name": 'Carbohydrate(g)', "max": 170},
                {"name": 'Fat(kal)', "max": 230},
            ],
            "shape": 'circle',
            "splitNumber": 5,
            "axisName": {
                "color": 'rgb(238, 197, 102)'
            },
            "splitLine": {
                "lineStyle": {
                    "color": [
                        'rgba(238, 197, 102, 0.1)',
                        'rgba(238, 197, 102, 0.2)',
                        'rgba(238, 197, 102, 0.4)',
                        'rgba(238, 197, 102, 0.6)'
                    ].reverse()
                }
            },
            "axisLine": {
                "lineStyle": {
                    "color": 'rgba(238, 197, 102, 0.5)'
                }
            }
        },
        "series": [
            {
                "name": 'AVG(All)',
                "type": 'radar',
                "lineStyle": "lineStyle",
                "data": data1,
                "symbol": 'none',
                "itemStyle": {
                    "color": '#F9713C'
                },
                "areaStyle": {
                    "opacity": 0.1
                }
            },
            {
                "name": 'AVG(Male)',
                "type": 'radar',
                "lineStyle": "lineStyle",
                "data": data2,
                "symbol": 'none',
                "itemStyle": {
                    "color": '#B3E4A1'
                },
                "areaStyle": {
                    "opacity": 0.05
                }
            }
        ]
    }

    options2 = {
        "title": {
            "text": 'Health Monitoring - Radar',
            "left": 'center',
            "textStyle": {
                "color": '#eee'
            }
        },
        "legend": {
            "bottom": 5,
            "data": ['AVG(All)', 'AVG(Female)'],
            "itemGap": 20,
            "textStyle": {
                "color": '#fff',
                "fontSize": 14
            },
        },
        "radar": {
            "indicator": [
                {"name": 'Vitamin(mg)', "max": 90},
                {"name": 'Protein(mg)', "max": 80},
                {"name": 'Carbohydrate(g)', "max": 170},
                {"name": 'Fat(kal)', "max": 230},
            ],
            "shape": 'circle',
            "splitNumber": 5,
            "axisName": {
                "color": 'rgb(238, 197, 102)'
            },
            "splitLine": {
                "lineStyle": {
                    "color": [
                        'rgba(238, 197, 102, 0.1)',
                        'rgba(238, 197, 102, 0.2)',
                        'rgba(238, 197, 102, 0.4)',
                        'rgba(238, 197, 102, 0.6)'
                    ].reverse()
                }
            },
            "axisLine": {
                "lineStyle": {
                    "color": 'rgba(238, 197, 102, 0.5)'
                }
            }
        },
        "series": [
            {
                "name": 'AVG(All)',
                "type": 'radar',
                "lineStyle": "lineStyle",
                "data": data1,
                "symbol": 'none',
                "itemStyle": {
                    "color": '#F9713C'
                },
                "areaStyle": {
                    "opacity": 0.1
                }
            },
            {
                "name": 'AVG(Female)',
                "type": 'radar',
                "lineStyle": "lineStyle",
                "data": data3,
                "symbol": 'none',
                "itemStyle": {
                    "color": '#B3E4A1'
                },
                "areaStyle": {
                    "opacity": 0.05
                }
            }
        ]
    }
    # Use the 'columns' attribute to create a side-by-side layout
    col1, col2 = st.columns(2)

    with col1:
        st_echarts(options=options1, height="400px")

    with col2:
        st_echarts(options=options2, height="400px")

    data1 = [[82.2, 69.6, 169.3, 212.3]]
    data4 = [[83.2, 73.6, 186.6, 215.2]]
    data5 = [[81.2, 65.6, 152.0, 194.6]]

    options3 = {
        "title": {
            "text": 'Health Monitoring - Radar',
            "left": 'center',
            "textStyle": {
                "color": '#eee'
            }
        },
        "legend": {
            "bottom": 5,
            "data": ['AVG(All)', 'AVG(Age<35)'],
            "itemGap": 20,
            "textStyle": {
                "color": '#fff',
                "fontSize": 14
            },
        },
        "radar": {
            "indicator": [
                {"name": 'Vitamin(mg)', "max": 90},
                {"name": 'Protein(mg)', "max": 80},
                {"name": 'Carbohydrate(g)', "max": 170},
                {"name": 'Fat(kal)', "max": 230},
            ],
            "shape": 'circle',
            "splitNumber": 5,
            "axisName": {
                "color": 'rgb(238, 197, 102)'
            },
            "splitLine": {
                "lineStyle": {
                    "color": [
                        'rgba(238, 197, 102, 0.1)',
                        'rgba(238, 197, 102, 0.2)',
                        'rgba(238, 197, 102, 0.4)',
                        'rgba(238, 197, 102, 0.6)'
                    ].reverse()
                }
            },
            "axisLine": {
                "lineStyle": {
                    "color": 'rgba(238, 197, 102, 0.5)'
                }
            }
        },
        "series": [
            {
                "name": 'AVG(All)',
                "type": 'radar',
                "lineStyle": "lineStyle",
                "data": data1,
                "symbol": 'none',
                "itemStyle": {
                    "color": '#F9713C'
                },
                "areaStyle": {
                    "opacity": 0.1
                }
            },
            {
                "name": 'AVG(Age<35)',
                "type": 'radar',
                "lineStyle": "lineStyle",
                "data": data4,
                "symbol": 'none',
                "itemStyle": {
                    "color": '#B3E4A1'
                },
                "areaStyle": {
                    "opacity": 0.05
                }
            }
        ]
    }

    options4 = {
        "title": {
            "text": 'Health Monitoring - Radar',
            "left": 'center',
            "textStyle": {
                "color": '#eee'
            }
        },
        "legend": {
            "bottom": 5,
            "data": ['AVG(All)', 'AVG(Age>35)'],
            "itemGap": 20,
            "textStyle": {
                "color": '#fff',
                "fontSize": 14
            },
        },
        "radar": {
            "indicator": [
                {"name": 'Vitamin(mg)', "max": 90},
                {"name": 'Protein(mg)', "max": 80},
                {"name": 'Carbohydrate(g)', "max": 170},
                {"name": 'Fat(kal)', "max": 230},
            ],
            "shape": 'circle',
            "splitNumber": 5,
            "axisName": {
                "color": 'rgb(238, 197, 102)'
            },
            "splitLine": {
                "lineStyle": {
                    "color": [
                        'rgba(238, 197, 102, 0.1)',
                        'rgba(238, 197, 102, 0.2)',
                        'rgba(238, 197, 102, 0.4)',
                        'rgba(238, 197, 102, 0.6)'
                    ].reverse()
                }
            },
            "axisLine": {
                "lineStyle": {
                    "color": 'rgba(238, 197, 102, 0.5)'
                }
            }
        },
        "series": [
            {
                "name": 'AVG(All)',
                "type": 'radar',
                "lineStyle": "lineStyle",
                "data": data1,
                "symbol": 'none',
                "itemStyle": {
                    "color": '#F9713C'
                },
                "areaStyle": {
                    "opacity": 0.1
                }
            },
            {
                "name": 'AVG(Age>35)',
                "type": 'radar',
                "lineStyle": "lineStyle",
                "data": data5,
                "symbol": 'none',
                "itemStyle": {
                    "color": '#B3E4A1'
                },
                "areaStyle": {
                    "opacity": 0.05
                }
            }
        ]
    }
    # Use the 'columns' attribute to create a side-by-side layout
    col3, col4 = st.columns(2)

    with col3:
        st_echarts(options=options3, height="400px")

    with col4:
        st_echarts(options=options4, height="400px")

    image1 = Image.open("shiwu1.jpg")
    image2 = Image.open("shiwu2.jpg")

    st.image([image1, image2], caption=['food1', 'food2'], width=300)


def Sleep1():
    st.write(
        """
        <div style="font-family: Arial; font-size: 22px; color: black; line-height: 1.5;">
            Sleep: 
            The proportion of sleep time per day in the survey is shown by pie chart, 
            compared with men, women and children, and then the bar chart is used to see 
            the trend of sleep quality with age
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    st.markdown("___")
    st.write("")
    options = {
        "tooltip": {
            "trigger": 'item',
            "formatter": '{a} <br/>{b}: {c} ({d}%)'
        },
        "legend": {
            "data": [
                'Male',
                'Female',
                'Old',
                'Young'
            ]
        },
        "series": [
            {
                "name": 'Sleep Time',
                "type": 'pie',
                "selectedMode": 'single',
                "radius": [0, '30%'],
                "label": {
                    "position": 'inner',
                    "fontSize": 14
                },
                "labelLine": {
                    "show": "false"
                },
                "data": [
                    {"value": 7.42, "name": 'Male'},
                    {"value": 7.94, "name": 'Female'},
                ]
            },
            {
                "name": 'Sleep Time',
                "type": 'pie',
                "radius": ['45%', '60%'],
                "labelLine": {
                    "length": 30
                },
                "label": {
                    "formatter": '{a|{a}}{abg|}\n{hr|}\n  {b|{b}:}{c}  {per|{d}%}  ',
                    "backgroundColor": '#F6F8FC',
                    "borderColor": '#8C8D8E',
                    "borderWidth": 1,
                    "borderRadius": 4,
                    "rich": {
                        "a": {
                            "color": '#6E7079',
                            "lineHeight": 22,
                            'align': 'center'
                        },
                        'hr': {
                            'borderColor': '#8C8D8E',
                            'width': '100%',
                            'borderWidth': 1,
                            'height': 0
                        },
                        'b': {
                            'color': '#4C5058',
                            'fontSize': 14,
                            'fontWeight': 'bold',
                            'lineHeight': 33
                        },
                        'c': {
                            'color': '#fff',
                            'backgroundColor': '#4C5058'
                        },
                        'per': {
                            'color': '#fff',
                            'backgroundColor': '#4C5058',
                            'padding': [3, 4],
                            'borderRadius': 4
                        }
                    }
                },
                'data': [
                    {'value': 7.22, "name": 'Young'},
                    {'value': 8.14, 'name': 'Old'},
                ]
            }
        ]
    }
    st_echarts(
        options=options, height="400px",
    )
    options = {
        "tooltip": {
            "trigger": "axis",
            "axisPointer": {"type": "cross", "crossStyle": {"color": "#999"}},
        },
        "toolbox": {
            "feature": {
                "dataView": {"show": True, "readOnly": False},
                "magicType": {"show": True, "type": ["line", "bar"]},
                "restore": {"show": True},
                "saveAsImage": {"show": True},
            }
        },
        "legend": {"data": ["Deep sleep", "Light sleep", "Sleep time"]},
        "xAxis": [
            {
                "name": "Age",
                "type": "category",
                "data": [16, 18, 22, 24, 30, 46, 55, 58, 74, 79],
                "axisPointer": {"type": "shadow"},
            }
        ],
        "yAxis": [
            {
                "type": "value",
                "name": "Account(%)",
                "min": 0,
                "max": 1,
                "interval": 0.1,
                "axisLabel": {"formatter": "{value} "},
            },
            {
                "type": "value",
                "name": "Sleep time(h)",
                "min": 0,
                "max": 10,
                "interval": 1,
                "axisLabel": {"formatter": "{value} "},
            }
        ],
        "series": [
            {
                "name": "Deep sleep(%)",
                "type": "bar",
                "data": [0.8065, 0.8205, 0.729, 0.691, 0.658, 0.5595, 0.5165, 0.473, 0.4085, 0.3545]
            },
            {
                "name": "Light sleep(%)",
                "type": "bar",
                "data": [0.1935, 0.1795, 0.271, 0.309, 0.342, 0.4405, 0.4835, 0.527, 0.5915, 0.6455]
            },
            {
                "name": "Sleep time",
                "type": "line",
                "yAxisIndex": 1,
                "data": [7.5, 6.5, 7.1, 7.5, 8.5, 8.2, 6.8, 7.8, 8.3, 8.6]
            },
        ],
    }
    st_echarts(
        options=options, height="600px",
    )


def Sleep():
    data1 = [
        {
            "name": 'Old',
            "value": 70
        },
        {
            "name": 'Young',
            "value": 70
        },
    ]
    data2 = [
        {
            "name": 'Male',
            "value": 70
        },
        {
            "name": 'Female',
            "value": 70
        },
    ]
    options = {
        "title": [
            {
                "subtext": 'Feature: "Age"',
                "left": '33.33%',
                "top": '15%',
                "textAlign": 'center'
            },
            {
                "subtext": 'Feature: "Gender"',
                "left": '66.67%',
                "top": '15%',
                "textAlign": 'center'
            }
        ],
        "series": [
            {
                "type": 'pie',
                "radius": '25%',
                "center": ['50%', '50%'],
                "data": data1,
                "label": {
                    "position": 'outer',
                    "Feature": 'Age',
                    "bleedMargin": 5
                },
                "left": 0,
                "right": '66.6667%',
                "top": 0,
                "bottom": 0
            },
            {
                "type": 'pie',
                "radius": '25%',
                "center": ['50%', '50%'],
                "data": data2,
                "label": {
                    "position": 'outer',
                    "Feature": 'Gender',
                    "margin": 20
                },
                "left": '66.6667%',
                "right": 0,
                "top": 0,
                "bottom": 0
            }
        ]
    }
    st_echarts(
        options=options, height="400px",
    )


def Sleep():
    # 从CSV文件中读取数据
    df = pd.read_csv("./睡眠数据.csv")

    # 创建男性和女性的子数据集
    male_data = df[df['Gender'] == 'male']
    female_data = df[df['Gender'] == 'female']

    # 创建老年人和青年人的子数据集
    older_data = df[df['Age'] > 40]
    younger_data = df[df['Age'] < 40]

    sex = ['male', "female"]
    age = ['younger', 'older']
    options = {
        "color": '#eee',
        "tooltip": {},
        "visualMap": {
            "max": 7,
            "min": 4,
            "inRange": {
                "color": [
                    '#313695',
                    '#4575b4',
                    '#74add1',
                    '#abd9e9',
                    '#e0f3f8',
                    '#ffffbf',
                    '#fee090',
                    '#fdae61',
                    '#f46d43',
                    '#d73027',
                    '#a50026']
            }
        },
        "xAxis3D": {
            "type": 'category',
            "data": sex
        },
        "yAxis3D": {
            "type": 'category',
            "data": age
        },
        "zAxis3D": {
            "type": 'value'
        },
        "grid3D": {
            "boxWidth": 200,
            "boxDepth": 80,
            "color": '#eee',
            "light": {
                "main": {
                    "intensity": 1.2
                },
                "ambient": {
                    "intensity": 0.3
                }
            }
        },
        "series": [
            {
                "type": 'bar3D',
                "shading": 'color',
                "data": [[0, 0, 4.7], [1, 0, 5], [0, 1, 5.3], [1, 1, 5.5]],
                "label": {
                    "show": "false",
                    "fontSize": 16,
                    "borderWidth": 1
                },
                "itemStyle": {
                    "opacity": 0.4
                },
                "emphasis": {
                    "label": {
                        "fontSize": 20,
                    },
                    "itemStyle": {
                    }
                }
            }
        ]
    }
    st_echarts(
        options=options, height="500px",
    )
    image = Image.open('food.jpg')
    st.image([image], caption=['food'], width=300)
    st.image([image, image], caption=['food', 'food'], width=300)


def Weight():
    st.write(
        """
        <div style="font-family: Arial; font-size: 22px; color: black; line-height: 1.5;">
            Body weight index: Show the bmi data and bfr data of the respondents to see the trend of age and body data change
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    st.markdown("---")
    st.write("")
    options = {
        "tooltip": {
            "trigger": "axis",
            "axisPointer": {"type": "cross", "crossStyle": {"color": "#999"}},
        },
        "toolbox": {
            "feature": {
                "dataView": {"show": True, "readOnly": False},
                "magicType": {"show": True, "type": ["line", "bar"]},
                "restore": {"show": True},
                "saveAsImage": {"show": True},
            }
        },
        "legend": {"data": ["Male", "Female"]},
        "xAxis": [
            {
                "name": "Age",
                "type": "category",
                "data": [16, 18, 22, 24, 30, 46, 55, 58, 74, 79],
                "axisPointer": {"type": "shadow"},
            }
        ],
        "yAxis": [
            {
                "type": "value",
                "name": "BMI",
                "max": 30,
                "interval": 5,
                # "axisLabel": {"formatter": "{value} %"},
            },
        ],
        "series": [
            {
                "name": "Male",
                "type": "bar",
                'color': 'orange',
                "data": [20.3, 21.5, 22.4, 22.6, 26.0, 24.5, 27.6, 25.7, 19.6, 22.0]
            },
            {
                "name": "Female",
                "type": "bar",
                'color': 'green',
                "data": [20.6, 20.8, 20.3, 21.5, 22.9, 25.4, 22.6, 18.3, 20.5, 24.8]
            },
        ],
    }
    st_echarts(
        options=options, height="600px",
    )

    options1 = {
        "tooltip": {
            "trigger": "axis",
            "axisPointer": {"type": "cross", "crossStyle": {"color": "#777"}},
        },
        "toolbox": {
            "feature": {
                "dataView": {"show": True, "readOnly": False},
                "magicType": {"show": True, "type": ["line", "bar"]},
                "restore": {"show": True},
                "saveAsImage": {"show": True},
            }
        },
        "legend": {"data": ["Male", "Female"]},
        "xAxis": [
            {
                "name": "Age",
                "type": "category",
                "data": [16, 18, 22, 24, 30, 46, 55, 58, 74, 79],
                "axisPointer": {"type": "shadow"},
            }
        ],
        "yAxis": [
            {
                "type": "value",
                "name": "BFR",
                "max": 30,

                "interval": 5,
                "axisLabel": {"formatter": "{value} "},
            },
            {
                "type": "value",
                "name": "BFR",
                "max": 30,
                "interval": 5,
                "axisLabel": {"formatter": "{value} %"},
            },
        ],
        "series": [
            {
                "name": "Male",
                "type": "bar",
                "data": [16, 17, 18, 16, 24, 26, 26.6, 26, 19, 22]
            },
            {
                "name": "Female",
                "type": "bar",
                "data": [24, 20, 24, 25, 26, 29, 25, 24, 25, 28]
            },

        ],
    }

    st_echarts(
        options=options1, height="610px",
    )

    image = Image.open("yundong.jpg")
    st.image([image], caption=['food'], width=300)



if __name__ == "__main__":
    st.set_page_config(page_title="Streamlit Echarts Demo", page_icon=":tada:")
    main()
