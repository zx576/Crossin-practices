/**
 * Created by ZX on 2017/1/12.
 * 性别-饼图
 */


option = {
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