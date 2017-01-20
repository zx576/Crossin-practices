

var data = {'未知': 1726, '中专技校': 13, '小学': 7, '大学': 1195, '高中': 102, '初中': 27};
var cData = function () {
    var name = [];
    var alldata = [];
    for (var i in data){
        var dic = {};
        dic['name'] = i;
        dic['value'] = data[i];
        name.push(i);
        alldata.push(dic)
    }
    return [name,alldata]
};


option = {
    title : {
        text: '学历占比',
        // subtext: '',
        x:'center'
    },
    tooltip : {
        trigger: 'item',
        formatter: "{a} <br/>{b} : {c} ({d}%)"
    },
    legend: {
        orient: 'vertical',
        left: 'left',
        data: cData()[0]
    },
    toolbox: {
        show: true,
        orient: 'vertical',
        left: 'right',
        top: 'center',
        feature: {
            dataView: {readOnly: false},
            restore: {},
            saveAsImage: {}
        }
    },
    series : [
        {
            name: '访问来源',
            type: 'pie',
            radius : '55%',
            center: ['50%', '60%'],
            data:cData()[1],
            itemStyle: {
                emphasis: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
        }
    ]
};
