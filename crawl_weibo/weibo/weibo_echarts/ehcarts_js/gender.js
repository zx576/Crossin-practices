/**
 * Created by ZX on 2017/1/12.
 * 性别-饼图
 */

var myChart = echarts.init(document.getElementById('gender'));
option = {
    title: {
        text: '性别比例',
        // subtext: 'data from PM25.in',
        // sublink: 'http://www.pm25.in',
        left: 'center',
        textStyle: {
            color: 'black'
        },
        top: 20,
        left:20,
    },
    tooltip: {
        trigger: 'item',
        // formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    series: [{
        name: '用户属性',
        type: 'pie',
        radius: '55%',
        center: ['40%', '50%'],
        data: [{
            value: 33133,
            name: '男'
        }, {
            value: 24612,
            name: '女'
        }],
        // itemStyle: {
        //     emphasis: {
        //         shadowBlur: 10,
        //         shadowOffsetX: 0,
        //         shadowColor: 'rgba(0, 0, 0, 0.5)'
        //     }
        // },
        itemStyle: {
            normal: {
                label: {
                    show: true,
                    //	                            position:'inside',
                    formatter: '{b} : {c} ({d}%)'
                }
            },
            labelLine: {
                show: true
            }
        }
    }]
};
myChart.setOption(option);