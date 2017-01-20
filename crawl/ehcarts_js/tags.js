var soure = {
	'美食': 287, '美女': 126, '90': 200, '电影': 267,
	'搞笑': 178, '幽默': 185, '吃货': 67, '听歌': 107,
	'旅游': 334, '旅行': 116, '动漫': 276, '娱乐': 155,
	'音乐': 361, '体育': 191, '摄影': 155, '文艺': 134,
	'爱好者': 115, '80': 129, '数码': 289, '游戏': 199
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
        text:"词云图",
        link:'https://github.com/ecomfe/echarts-wordcloud',
        subtext: 'data-visual.cn',
        sublink:'http://data-visual.cn',
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