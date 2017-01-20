/**
 * Created by ZX on 2017/1/13.
 */
var geoCoordMap = {'辽宁': [123.38, 41.8], '福建': [118.1, 24.46], '北京': [116.46, 39.92], '湖南': [113, 28.21], '重庆': [106.54, 29.59], '湖北': [114.31, 30.52], '贵州': [106.71, 26.57], '宁夏': [106.27, 38.47], '浙江': [120.19, 30.26], '山东': [117, 36.65], '新疆': [87.68, 43.77], '河南': [113.65, 34.76], '陕西': [108.95, 34.27], '天津': [117.2, 39.13], '江苏': [118.78, 32.04], '青海': [101.74, 36.56], '四川': [104.06, 30.67], '山西': [112.53, 37.87], '上海': [121.48, 31.22], '江西': [115.89, 28.68], '甘肃': [103.73, 36.03], '黑龙江': [126.63, 45.75], '广东': [113.23, 23.16], '河北': [114.48, 38.03], '安徽': [117.27, 31.86], '吉林': [125.35, 43.88], '西藏': [91.11, 29.97], '内蒙古': [111.65, 40.82], '云南': [102.73, 25.04], '广西': [108.33, 22.84]};
var data = [{'name': 'x', 'value': 1}, {'name': '江苏', 'value': 242}, {'name': '上海', 'value': 262}, {'name': '海外', 'value': 149}, {'name': '山东', 'value': 123}, {'name': '辽宁', 'value': 62}, {'name': '河北', 'value': 70}, {'name': '广东', 'value': 306}, {'name': '湖南', 'value': 59}, {'name': '浙江', 'value': 198}, {'name': '陕西', 'value': 67}, {'name': '广西', 'value': 53}, {'name': '湖北', 'value': 101}, {'name': '福建', 'value': 82}, {'name': '内蒙古', 'value': 15}, {'name': '四川', 'value': 115}, {'name': '重庆', 'value': 58}, {'name': '北京', 'value': 371}, {'name': '河南', 'value': 93}, {'name': '江西', 'value': 45}, {'name': '其他', 'value': 215}, {'name': '吉林', 'value': 36}, {'name': '台湾', 'value': 6}, {'name': '天津', 'value': 40}, {'name': '安徽', 'value': 64}, {'name': '黑龙江', 'value': 28}, {'name': '海南', 'value': 8}, {'name': '贵州', 'value': 20}, {'name': '云南', 'value': 30}, {'name': '山西', 'value': 32}, {'name': '甘肃', 'value': 12}, {'name': '宁夏', 'value': 9}, {'name': '香港', 'value': 12}, {'name': '新疆', 'value': 13}, {'name': '澳门', 'value': 3}, {'name': '青海', 'value': 3}, {'name': '西藏', 'value': 2}]


var convertData = function (data) {
    var res = [];
    for (var i = 0; i < data.length; i++) {
        var geoCoord = geoCoordMap[data[i].name];
        if (geoCoord) {
            res.push(geoCoord.concat(data[i].value));
        }
    }
    return res;
};

option = {
    title: {
        text: '全国各地区关注量热力图',
        // subtext: 'data from PM25.in',
        // sublink: 'http://www.pm25.in',
        left: 'center',
        textStyle: {
            color: '#fff'
        },
        top:40
    },
    backgroundColor: '#404a59',
    visualMap: {
        min: 0,
        max: 400,
        splitNumber:4,
        inRange: {
            color: ['#d94e5d','#eac736','#50a3ba'].reverse()
        },
        textStyle: {
            color: '#fff'
        },
        left:20
    },
    geo: {
        map: 'china',
        label: {
            emphasis: {
                show: false
            }
        },
        roam: true,
        itemStyle: {
            normal: {
                areaColor: '#323c48',
                borderColor: '#111'
            },
            emphasis: {
                areaColor: '#2a333d'
            }
        }
    },
    series: [{
        name: 'AQI',
        type: 'heatmap',
        coordinateSystem: 'geo',
        data: convertData(data)
    }]
}
;

