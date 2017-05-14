/**
 * Created by ZX on 2017/1/12.
 * 星座柱形图
 */

var source = {
    '巨蟹座': {'male': 1574, 'female': 1148}, '双鱼座': {'male': 1645, 'female': 1211},
    '天蝎座': {'male': 2003, 'female': 1506}, '水瓶座': {'male': 1730, 'female': 1439},
    '摩羯座': {'male': 1650, 'female': 1288}, '其他': {'male': 634, 'female': 391},
    '金牛座': {'male': 1488, 'female': 1197}, '天秤座': {'male': 2042, 'female': 1469},
    '处女座': {'male': 1716, 'female': 1288}, '射手座': {'male': 1633, 'female': 1320},
    '双子座': {'male': 1600, 'female': 1284}, '狮子座': {'male': 1666, 'female': 1281},
    '白羊座': {'male': 1604, 'female': 1234}
};
var data = [
    '白羊座',
    '金牛座',
    '双子座',
    '巨蟹座',
    '狮子座',
    '处女座',
    '天秤座',
    '天蝎座',
    '射手座',
    '水瓶座',
    '双鱼座',
    '摩羯座'
    ];
var cData = function () {
    var maledata = [];
    var femaledata = [];
    var totaldata = [];
    for (var i=0;i<data.length;i++) {
        maledata.push(
            source[data[i]].male
        ),
        femaledata.push(
            source[data[i]].female
        ),
        totaldata.push(
            source[data[i]].male + source[data[i]].female
        )
    }
    return [maledata,femaledata,totaldata]
};

option = {
    backgroundColor: "#344b58",
    "title": {
        "text": "星座统计",
        // "subtext": "BY Wang Dingding",
        x: "4%",

        textStyle: {
            color: '#fff',
            fontSize: '22'
        },
    },
    "tooltip": {
        "trigger": "axis",
        "axisPointer": {
            "type": "shadow",
            textStyle: {
                color: "#fff"
            }

        },
    },
    "grid": {
        "borderWidth": 0,
        "top": 110,
        "bottom": 95,
        textStyle: {
            color: "#fff"
        }
    },
    "legend": {
        x: '4%',
        top: '11%',
        textStyle: {
            color: '#90979c',
        },
        "data": ['女', '男', '平均']
    },


    "calculable": true,
    "xAxis": [{
        "type": "category",
        "axisLine": {
            lineStyle: {
                color: '#90979c'
            }
        },
        "splitLine": {
            "show": false
        },
        "axisTick": {
            "show": false
        },
        "splitArea": {
            "show": false
        },
        "axisLabel": {
            "interval": 0,

        },
        "data": data,
    }],
    "yAxis": [{
        "type": "value",
        "splitLine": {
            "show": false
        },
        "axisLine": {
            lineStyle: {
                color: '#90979c'
            }
        },
        "axisTick": {
            "show": false
        },
        "axisLabel": {
            "interval": 0,

        },
        "splitArea": {
            "show": false
        },

    }],
    "dataZoom": [{
        "show": true,
        "height": 30,
        "xAxisIndex": [
            0
        ],
        bottom: 30,
        "start": 10,
        "end": 80,
        handleIcon: 'path://M306.1,413c0,2.2-1.8,4-4,4h-59.8c-2.2,0-4-1.8-4-4V200.8c0-2.2,1.8-4,4-4h59.8c2.2,0,4,1.8,4,4V413z',
        handleSize: '110%',
        handleStyle:{
            color:"#d3dee5",

        },
           textStyle:{
            color:"#fff"},
           borderColor:"#90979c"


    }, {
        "type": "inside",
        "show": true,
        "height": 15,
        "start": 1,
        "end": 35
    }],
    "series": [{
            "name": "女",
            "type": "bar",
            "stack": "总量",
            "barMaxWidth": 35,
            "barGap": "10%",
            "itemStyle": {
                "normal": {
                    "color": "rgba(255,144,128,1)",
                    "label": {
                        "show": true,
                        "textStyle": {
                            "color": "#fff"
                        },
                        "position": "insideTop",
                        formatter: function(p) {
                            return p.value > 0 ? (p.value) : '';
                        }
                    }
                }
            },
            "data": cData()[1],
        },

        {
            "name": "男",
            "type": "bar",
            "stack": "总量",
            "itemStyle": {
                "normal": {
                    "color": "rgba(0,191,183,1)",
                    "barBorderRadius": 0,
                    "label": {
                        "show": true,
                        "position": "top",
                        formatter: function(p) {
                            return p.value > 0 ? (p.value) : '';
                        }
                    }
                }
            },
            "data": cData()[0]
        }, {
            "name": "总数",
            "type": "line",
            "stack": "总量",
            symbolSize:10,
            symbol:'circle',
            "itemStyle": {
                "normal": {
                    "color": "rgba(252,230,48,1)",
                    "barBorderRadius": 0,
                    "label": {
                        "show": true,
                        "position": "top",
                        formatter: function(p) {
                            return p.value > 0 ? (p.value) : '';
                        }
                    }
                }
            },
            "data": cData()[2]
        },
    ]
}