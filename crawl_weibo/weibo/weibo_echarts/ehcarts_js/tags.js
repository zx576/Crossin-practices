/**
 * Created by ZX on 2017/1/12.
 * 标签云图
 */
var myChart = echarts.init(document.getElementById('tags'));
var soure = {
    '美食': 5350, '90': 2605, '爱好者': 1570, '吃货': 1267,
    '幽默': 3305, '体育': 2410, '美女': 3000, '数码': 2738, '听歌': 1441,
    '摄影': 2215, '文艺': 2330, '电影': 3991, '80': 1628, '游戏': 2687,
    '娱乐': 2588, '搞笑': 3149, '旅游': 5231, '视频': 1873, '动漫': 4254, '音乐': 5220
};

var cData = function () {
    var result = [];
    for (var i in soure){
        var dic = {};
        dic['name'] = i;
        dic['value'] = soure[i];
        result.push(
            dic
        )
    }
    return result
};




option = {
    title:{
        text:"标签云",
        // link:'https://github.com/ecomfe/echarts-wordcloud',
        // subtext: 'data-visual.cn',
        // sublink:'http://data-visual.cn',
    },
    tooltip: {},
    series: [{
        type: 'wordCloud',
        gridSize: 20,
        sizeRange: [12, 50],
        rotationRange: [0, 0],
        shape: 'circle',
        textStyle: {
            normal: {
                color: function () {
                    return 'rgb(' + [
                            Math.round(Math.random() * 160),
                            Math.round(Math.random() * 160),
                            Math.round(Math.random() * 160)
                        ].join(',') + ')';
                }
            },
            emphasis: {
                shadowBlur: 10,
                shadowColor: '#333'
            }
        },
        data: cData()
    }]
};
myChart.setOption(option);