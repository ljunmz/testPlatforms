var vm = new Vue({
    el: '#app',
    mounted: function () {
    },
    data() {
        return {
            url: 'http://apitest.shiguangxu.com:8000',
            activeIndex: '5',
            tableData: [{
                id: '1',
                planName: 'V2.1测试用例执行',
                progress: '80%',
                owner: '柳军',
                startTime: '2016-05-02',
                doneTime: '2016-05-02',
                bugCount: '500',
                caseCount: '2000',
                doneCase: '1000',
                status: '进行中',
                remark: '测试'
            }],
            cols: [
                {prop: 'date', label: '日期'},
                {prop: 'name', label: '姓名'},
            ],
            colTemplate:{
                "colsTest": [
                    {prop: 'id', label: '序号'},
                    {prop: 'type', label: '类别'},
                    {prop: 'module', label: '模块'},
                    {prop: 'totalCase', label: '用例总数'},
                    {prop: 'doneCase', label: '完成用例数'},
                    {prop: 'owner', label: '责任人'},
                    {prop: 'startTime', label: '计划开始时间'},
                    {prop: 'doneTime', label: '计划完成时间'},
                    {prop: 'exStartTime', label: '实际开始时间'},
                    {prop: 'exDoneTime', label: '实际完成时间'},
                    {prop: 'status', label: '状态'},
                    {prop: 'remark', label: '备注'}
                ],
                "colsCase": [
                    {prop: 'id', label: '序号'},
                    {prop: 'type', label: '类别'},
                    {prop: 'module', label: '模块'},
                    {prop: 'totalCase', label: '用例总数'},
                    {prop: 'doneCase', label: '完成用例数'},
                    {prop: 'owner', label: '责任人'},
                    {prop: 'startTime', label: '计划开始时间'},
                    {prop: 'doneTime', label: '计划完成时间'},
                    {prop: 'exStartTime', label: '实际开始时间'},
                    {prop: 'exDoneTime', label: '实际完成时间'},
                    {prop: 'status', label: '状态'},
                    {prop: 'remark', label: '备注'}
                ],
                "colsPlan": [
                    {prop: 'id', label: '序号'},
                    {prop: 'planName', label: '计划名称'},
                    {prop: 'progress', label: '计划进度'},
                    {prop: 'startTime', label: '计划开始时间'},
                    {prop: 'doneTime', label: '计划完成时间'},
                    {prop: 'bugCount', label: 'bug数'},
                    {prop: 'caseCount', label: '用例数'},
                    {prop: 'doneCase', label: '已完成用例'},
                    {prop: 'status', label: '计划状态'},
                    {prop: 'owner', label: '责任人'},
                    {prop: 'remark', label: '备注'}
                ]
            }

        }
    },
    methods: {
        handleSelect(key, keyPath) {
            console.log(key, keyPath);
        },
        addCol(){
            this.tableData.push({
                id: '1',
                planName: '安卓',
                progress: '80%',
                status: '进行中',
                owner: '柳军',
                startTime: '2016-05-02',
                doneTime: '2016-05-02',
                exStartTime: '2016-05-02',
                exDoneTime: '2016-05-02',
                status: '进行中',
                remark: '测试'
            })
        },
    }
});