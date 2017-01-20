option = {
    tooltip: {
        trigger: 'item',
        // formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    // legend: {
    //     orient: 'vertical',
    //     x: 'right',
    //     data: ['男', '女'],
    //     formatter: function(name) {
    //         var oa = option.series[0].data;
    //         var num = oa[0].value + oa[1].value;
    //         for (var i = 0; i < option.series[0].data.length; i++) {
    //             if (name == oa[i].name) {
    //                 return name + '     ' + oa[i].value + '     ' + (oa[i].value / num * 100).toFixed(2) + '%';
    //             }
    //         }
    //     }
    // },
    series: [{
        name: '用户属性',
        type: 'pie',
        radius: '55%',
        center: ['40%', '50%'],
        data: [{
            value: 2310,
            name: '男'
        }, {
            value: 689,
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