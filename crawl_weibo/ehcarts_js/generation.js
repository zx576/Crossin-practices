/**
 * Created by ZX on 2017/1/12.
 */
var data = {'00s': {'male': 969, 'female': 1389}, '70s': {'male': 728, 'female': 297}, '80s': {'male': 3215, 'female': 1620}, '60s': {'male': 90, 'female': 25}, '60sm': {'male': 238, 'female': 175}, '90s': {'male': 10300, 'female': 7832}};
var xdata = [
    // '60sm',
    '60s',
    '70s',
    '80s',
    '90s',
    '00s'
];
var cData = function () {
    var result = [];
    for (var i = 0;i<xdata.length;i++){
        result.push(data[xdata[i]].male + data[xdata[i]].female);
    }
    return result
};

option = {
    title: {
        text: '不同年代对比',
        textStyle: {
            color: '#000',
            fontWeight: 'bold'
        },
        left: 'center',
        // backgroundColor: 'rgba(0,0,255,0.2)',
        shadowColor: 'rgba(0,0,255,1)',
        shadowBlur: 20
    },
    xAxis: {
        type: 'category',
        name: '',
        nameLocation: 'middle',
        nameGap: 40,
        nameTextStyle: {
            fontWeight: 'bold',
            fontSize: 15
        },
        data: [
            // '60之前',
            '60后',
            '70后',
            '80后',
            '90后',
            '00后'
        ],
        axisLine: {
            onZero: false,
            lineStyle: {
                width: 3
            }
        },
        axisTick: {
            show: false
        },
        axisLabel: {
            margin: 10,
            textStyle: {
                fontWeight: 'bold'
            }
        },
        offset: 1
    },
    yAxis: {
        name: '',
        nameLocation: 'middle',
        nameGap: 45,
        nameTextStyle: {
            fontWeight: 'bold',
            fontSize: 15
        },
        axisTick: {
            show: false
        },
        nameRotate: 0,
        axisLine: {
            onZero: false,
            lineStyle: {
                width: 3
            }
        },
        axisLabel: {
            margin: 10,
            textStyle: {
                fontWeight: 'bold'
            },
            formatter: '{value}'
        },
    },
    series: [{
        type: 'bar',
        data: cData(),
        itemStyle: {
            normal: {
                color: function(params) {
                    var colorList = [
                        '#c23531', '#2f4554', '#61a0a8',
                        '#d48265', '#91c7ae', '#749f83',
                        '#ca8622', '#bda29a', '#6e7074',
                        '#546570', '#c4ccd3'
                    ];
                    return colorList[params.dataIndex]
                }
            }
        },
        barMaxWidth: '40px',
        label: {
            normal: {
                show: true,
                position: 'top',
                formatter: '{c}'
            }
        }
    }],
    tooltip: {
        trigger: 'item',
        formatter: '{c0}'
    }
};