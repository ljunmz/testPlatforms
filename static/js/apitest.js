
var vm = new Vue({
    el: '#app',
    mounted: function () {
        var dataPost = {"page_id": 1,"page_size":18};
        this.$http.post(this.url + '/getFlowData', dataPost).then(
            function (data) {
                this.FlowlistSize = data.body[0].size;
                this.flowData = data.body[0].flowData;
                console.log(this.flowData);
                console.log(this.FlowlistSize);
            }
        );
        this.$http.get(this.url + '/getEmail').then(
            function (data) {
                this.recipients = data.body[0].email;
            }
        );
    },
    data() {
        return {
            url: 'http://apitest.shiguangxu.com:8000',
            text :"接口运行中...",
            formInline: {
                user: '',
                region: ''
            },
            tableData: [{
                id: '1',
                apiName: '暂无数据',
                url: '暂无数据'
            }],
            colTemplate:[
                {prop: 'serviceName', label: '微服务'},
                {prop: 'apiName', label: '接口描述'},
                {prop: 'url', label: 'url'}
            ],
            filtrate: '',
            path: '',
            unStatisticsData: {},
            unDoList: [{
                id: '1',
                apiName: '暂无数据',
                url: '暂无数据'
            }],
            apiStatisticsData:{},
            recipients: '',
            filters: [
                {text: 'Web端接口', value: 'Web端接口' },
                {text: '内部调用', value: '内部调用' },
                {text: '测试接口', value: '测试接口' },
                {text: '废弃接口', value: '废弃接口' },
                {text: '数据割切', value: '数据割切' },
                {text: '未覆盖', value: '未覆盖' },
                {text: '已覆盖', value: '已覆盖' },
                {text: '运营后台', value: '运营后台' },
                {text: '暂不支持', value: '暂不支持' }
            ],
            pageSize: 18,
            FlowlistSize: 100,
            currentPage: 1,
            activeName:"apitest",
            creater: [
                {
                    "creater": "全部负责人"
                }, {
                    "creater": "柳军"
                }, {
                    "creater": "陈俊波"
                }, {
                    "creater": "崔庆用"
                }, {
                    "creater": "余一鸣"
                }, {
                    "creater": "陆金爱"
                }, {
                    "creater": "刘鎏"
                }],
            deleteFlowId: '',
            deleteNodeId: '',
            nodeFlowId: '',
            isCollapse: true,
            statisticsLoading:false,
            nodeDataDefault: [
                {
                    "pk": "",
                    "order_id": "",
                    "node_name": "",
                    "method": "POST",
                    "path": "",
                    "parameter": "",
                    "expect_response": "",
                    "sleep_time": 0,
                    "state": "1",
                    "isexcute_pre_sql": "0",
                    "pre_keys": "",
                    "pre_sql_str": "",
                    "pre_sql_para": "",
                    "pre_sql_out": "",
                    "ischechdb": "0",
                    "sql_str": "",
                    "sql_para": "",
                    "expect_db": "",
                    "post_keys": "",
                    "post_keys_extractor": "",
                    "post_keys_default": "",
                }
            ],
            flowDataDefault: {
                "pk": "",
                "flow_name": "",
                "account": "",
                "password": "",
                "priority": "1",
                "creater": "",
                "state": "1"
            },
            activeIndex2: '3',
            varListData: [{
                "argumentName":"示例1:变量名称",
                "argumentValue":"示例1:变量值",
            }],
            modal1: false,
            flowName: "",
            search: '',
            modal2: false,
            flowData: [],
            nodeData: [],
            nodeDataALL: [],
            outSqlData: [],
            postKeyData: [],
            preSqlData: [],
            parameterData: [],
            currentRow: '',
            value: true,
            visible: false,
            dialogFormVisible: false,
            dialogParameter: false,
            dialogManualStatistics: false,
            dialogPreSql: false,
            dialogOutSql: false,
            dialogPostKey: false,
            dialogEmailChange: false,
            deleteFlowDialogVisible: false,
            dialogReport: false,
            deleteNodeDialogVisible: false,
            dialogDefaultVar: false,
            dialogCopyNode: false,
            dialogTableVisible: false,
            formLabelWidth: '120px',
            actionLoading: false
        }
    },
    methods: {
        saveUnStatisticsData(row){
            console.log(row);
            var index = this.unStatisticsData.index;
            var dataPost = {
                "unStatisticsData": this.unStatisticsData,
            };
            this.$http.post(this.url + '/saveUnStatisticsData', dataPost).then(
                function (data) {
                    var responData = data.status;
                    if (responData === 200 || responData === '200') {
                        this.dialogManualStatistics = false;
                        this.$message({
                            showClose: true,
                            message: '保存成功',
                            type: 'success'
                        });
                    } else {
                        this.$message({
                            showClose: true,
                            message: '很遗憾，保存失败',
                            type: 'error'
                        });
                    }
                }
            );
        },
        manualStatistics(row){
            this.unStatisticsData = {
                "index":row.id,
                "service":row.serviceName,
                "summary":row.apiName,
                "path":row.url,
                "isAuto":"否",
                "author":"",
                "remark":""
            };
            this.dialogManualStatistics = true;
            console.log("manualStatistics-->",this.unStatisticsData);
        },
        filterPath(){
            var dataPost = {"path": this.path};
            this.$http.post(this.url + '/filterPath()', dataPost).then(
                function (data) {
                    this.flowData = data.body[0].flowData;
                    this.pageSize = 100;
                }
            );
        },
        filterFlowName(){
            var dataPost = {"flow_name": this.flowName};
            this.$http.post(this.url + '/filterFlowName()', dataPost).then(
                function (data) {
                    this.flowData = data.body[0].flowData;
                }
            );
        },
        filterTag(value, row) {
            return row.remark === value;
        },
        copyApi(nodeData,index,row){
            this.nodeDataDefault = [row];
            this.dialogCopyNode = true;
        },
        startTask(){
            this.$http.get(this.url + '/startTask').then(
                function (data) {
                    this.$message({
                        showClose: true,
                        message: 'Beat服务启动成功',
                        type: 'success'
                    });
                }
            );
            this.$http.get(this.url + '/startWork').then(
                function (data) {
                    this.$message({
                        showClose: true,
                        message: 'Work服务启动成功',
                        type: 'success'
                    });
                }
            );
        },
        startWork(){
            this.$http.get(this.url + '/startWork').then(
                function (data) {
                    this.$message({
                        showClose: true,
                        message: '恭喜你，Work服务启动成功',
                        type: 'success'
                    });
                }
            );
        },
        handleClick(targetName){
            if (targetName.name === "apitest"){
                this.activeName = targetName.name;
                console.log(this.activeName);
                var dataPost = {"page_id": 1,"page_size":18};
                this.$http.post(this.url + '/getFlowData', dataPost).then(
                    function (data) {
                        this.FlowlistSize = data.body[0].size;
                        this.flowData = data.body[0].flowData;
                        console.log(this.flowData);
                        console.log(this.FlowlistSize);
                    }
                );
            } else if (targetName.name === "config"){
                this.activeName = targetName.name;
                console.log(this.activeName);
                var dataPost = {"page_id": 1,"page_size":15};
                this.$http.post(this.url + '/getFlowData', dataPost).then(
                    function (data) {
                        this.FlowlistSize = data.body[0].size;
                        this.flowData = data.body[0].flowData;
                        console.log(this.flowData);
                        console.log(this.FlowlistSize);
                    }
                );
            } else if (targetName.name === "task"){
                this.activeName = targetName.name;
                console.log(this.activeName);
            } else if (targetName.name === "statistics") {
                this.statisticsLoading = true;
                this.$http.post(this.url + '/getApiStatistics', dataPost).then(
                    function (data) {
                        code = data.body[0].code;
                        if (code === "200"){
                            this.apiStatisticsData = data.body[0].data;
                            this.tableData = data.body[0].data.unStatisticsList;
                            this.unDoList = data.body[0].data.undoneList;
                            this.statisticsLoading = false;

                        }else {
                            this.statisticsLoading = false;
                        }

                    }
                );
            }

        },
        getDefaultVar(){
            this.$http.get(this.url + '/getDefaultVar').then(
                function (data) {
                    this.varListData = data.body[0].varList;
                }
            );
        },
        handleSizeChange(val) {
            console.log(`每页 ${val} 条`);
            console.log("page_size:",val);
            this.pageSize = val;
            var dataPost = {"page_id": 1,"page_size":this.pageSize};
            this.$http.post(this.url + '/getFlowData', dataPost).then(
                function (data) {
                    var responData = data.status;
                    if (responData === 200 || responData === '200') {
                        this.flowData = data.body[0].flowData;
                    } else {
                        this.$message({
                            showClose: true,
                            message: '很遗憾，切换分页失败',
                            type: 'error'
                        });
                    }

                }
            );

        },
        handleCurrentChange(val) {
            console.log(`当前页: ${val}`);
            var dataPost = {"page_id": val,"page_size":this.pageSize};
            this.$http.post(this.url + '/getFlowData', dataPost).then(
                function (data) {
                    var responData = data.status;
                    if (responData === 200 || responData === '200') {
                        this.flowData = data.body[0].flowData;
                    } else {
                        this.$message({
                            showClose: true,
                            message: '很遗憾，切换分页失败',
                            type: 'error'
                        });
                    }

                }
            );
        },
        handleOpen(key, keyPath) {
            console.log(key, keyPath);
        },
        handleClose(key, keyPath) {
            console.log(key, keyPath);
        },
        savePostKey() {
            console.log("node_id", this.postKeyData.node_id);
            console.log("postKeyData", this.postKeyData);
            var dataPost = {
                "node_id": this.postKeyData.node_id,
                "post_keys": this.postKeyData.post_keys,
                "post_keys_extractor": this.postKeyData.post_keys_extractor,
                "post_keys_default": this.postKeyData.post_keys_default
            };
            this.$http.post(this.url + '/savePostKey', dataPost).then(
                function (data) {
                    var responData = data.status;
                    console.log("responData=", responData);
                    if (responData === 200 || responData === '200') {
                        console.log("this.nodeData=", this.nodeData);
                        var nodeTable = document.getElementById('nodeTable');
                        var currentRow = nodeTable.getElementsByClassName('el-table__body')[0].getElementsByClassName("current-row")[0];
                        console.log('post_keys=', this.postKeyData.post_keys);
                        if (this.postKeyData.post_keys != null || this.postKeyData.post_keys > 0 || this.postKeyData.post_keys !== "") {
                            currentRow.getElementsByClassName("popoverButtonPost")[0].innerHTML = this.postKeyData.post_keys;
                        } else {
                            currentRow.getElementsByClassName("popoverButtonPost")[0].innerHTML = '未提取后置变量';
                        }
                        console.log("postKeyData=", this.postKeyData);
                        this.$message({
                            showClose: true,
                            message: '恭喜你，后置变量提取设置成功',
                            type: 'success'
                        });
                        this.dialogPostKey = false;
                    } else {
                        this.$message({
                            showClose: true,
                            message: '很抱歉，后置变量提取设置失败',
                            type: 'error'
                        });
                    }
                }
            );

        },
        saveParameter() {
            var dataPost = {"node_id": this.parameterData.key, "parameter": this.parameterData.value};
            this.$http.post(this.url + '/editParameter', dataPost).then(
                function (data) {
                    var responData = data.status;
                    if (responData === 200 || responData === '200') {
                        var nodeTable = document.getElementById('nodeTable');
                        var currentRow = nodeTable.getElementsByClassName('el-table__body')[0].getElementsByClassName("current-row")[0];
                        currentRow.getElementsByClassName("parameterButton")[0].innerHTML = this.parameterData.value;
                        this.$message({
                            showClose: true,
                            message: '保存成功',
                            type: 'success'
                        });
                        this.dialogParameter = false;
                    } else {
                        this.$message({
                            showClose: true,
                            message: '很遗憾，保存失败',
                            type: 'error'
                        });
                        this.dialogParameter = false;
                    }

                }
            );
        },
        saveOutSql() {
            var dataPost = {
                "node_id": this.outSqlData.node_id,
                "ischechdb": this.outSqlData.ischechdb,
                "sql_str": this.outSqlData.sql_str,
                "sql_para": this.outSqlData.sql_para,
                "expect_db": this.outSqlData.expect_db
            };
            this.$http.post(this.url + '/editOutSql', dataPost).then(
                function (data) {
                    var responData = data.status;
                    if (responData === 200 || responData === '200') {
                        var nodeTable = document.getElementById('nodeTable');
                        var currentRow = nodeTable.getElementsByClassName('el-table__body')[0].getElementsByClassName("current-row")[0];
                        if (this.outSqlData.ischechdb === '1' || this.outSqlData.ischechdb === 1) {
                            currentRow.getElementsByClassName("popoverButton")[0].innerHTML = '已开启';
                        } else if (this.outSqlData.ischechdb === '0' || this.outSqlData.ischechdb === 0) {
                            currentRow.getElementsByClassName("popoverButton")[0].innerHTML = '已关闭';
                        } else {
                            currentRow.getElementsByClassName("popoverButton")[0].innerHTML = '未配置';
                        }
                        this.dialogOutSql = false;
                        this.$message({
                            showClose: true,
                            message: '保存成功',
                            type: 'success'
                        });
                    } else {
                        this.$message({
                            showClose: true,
                            message: '很遗憾，保存失败',
                            type: 'error'
                        });
                    }
                }
            );
        },
        savePreSql() {
            var dataPost = {
                "node_id": this.preSqlData.node_id,
                "isexcute_pre_sql": this.preSqlData.isexcute_pre_sql,
                "pre_sql_str": this.preSqlData.pre_sql_str,
                "pre_sql_para": this.preSqlData.pre_sql_para,
                "pre_sql_out": this.preSqlData.pre_sql_out,
            };
            this.$http.post(this.url + '/editPreSql', dataPost).then(
                function (data) {
                    var responData = data.status;
                    if (responData === 200 || responData === '200') {
                        var nodeTable = document.getElementById('nodeTable');
                        var currentRow = nodeTable.getElementsByClassName('el-table__body')[0].getElementsByClassName("current-row")[0];
                        if (this.preSqlData.isexcute_pre_sql === '1' || this.preSqlData.isexcute_pre_sql === 1) {
                            currentRow.getElementsByClassName("popoverButtonPre")[0].innerHTML = '已开启';
                        } else if (this.preSqlData.isexcute_pre_sql === '0' || this.preSqlData.isexcute_pre_sql === 0) {
                            currentRow.getElementsByClassName("popoverButtonPre")[0].innerHTML = '已关闭';
                        } else {
                            currentRow.getElementsByClassName("popoverButtonPre")[0].innerHTML = '未配置';
                        }
                        this.dialogPreSql = false;
                        this.$message({
                            showClose: true,
                            message: '保存成功',
                            type: 'success'
                        });
                    } else {
                        this.$message({
                            showClose: true,
                            message: '很遗憾，保存失败',
                            type: 'error'
                        });
                    }
                }
            );
        },
        formatState: function (row, column) {
            console.log(typeof row.state);
            return row.state === 1 || row.state === '1' ? "已开启" : row.state === 0 || row.state === '0' ? "已关闭" : "未设置"
        },
        formatPreSql: function (row, column) {
            return row.isexcute_pre_sql === 1 || row.isexcute_pre_sql === '1' ? '已开启' : row.isexcute_pre_sql === 0 || row.isexcute_pre_sql === '0' ? '已关闭' : '未配置'
        },
        formatOutSql: function (row, column) {
            return row.ischechdb === 1 || row.ischechdb === '1' ? '已开启' : row.ischechdb === 0 || row.ischechdb === '0' ? '已关闭' : '未配置'
        },
        formatStateNode: function (row, column) {
            console.log("row", row);
            return row.state === 1 || row.state === '1' ? '已开启接口' : row.state === 0 || row.state === '0' ? '已关闭接口' : '未设置接口状态'
        },
        formatPostKey: function (row, formatPostKey) {
            return row.post_keys != null && row.post_keys.length > 0 && row.post_keys !== "" ? row.post_keys : '未提取后置变量';
        },
        handleSelect(key, keyPath) {
            console.log(key, keyPath);
        },
        filterHandler(value, row, column) {
            const property = column['prop'];
            return row[property] === value;
        },
        getOutSql(index, row, even) {
            this.currentRow = document.getElementById('nodeTable').getElementsByClassName('el-table__body')[0].getElementsByClassName("current-row ")[0];
            console.log('getOutSql-index', index);
            console.log('getOutSql-this.currentRow', this.currentRow);
            this.outSqlData = '';
            this.dialogOutSql = true;
            var dataPost = {"node_id": row.pk};
            this.$http.post(this.url + '/getOutSql', dataPost).then(
                function (data) {
                    var responData = data.body;
                    console.log("responData=", responData);
                    this.outSqlData = {
                        "node_id": row.pk,
                        "ischechdb": responData[0].ischechdb,
                        "sql_str": responData[0].sql_str,
                        "sql_para": responData[0].sql_para,
                        "expect_db": responData[0].expect_db
                    };
                    console.log("outSqlData=", this.outSqlData);
                }
            )
        },
        getPreSql(index, row) {
            this.currentRow = document.getElementById('nodeTable').getElementsByClassName('el-table__body')[0].getElementsByClassName("current-row ")[0];
            console.log('getPreSql-index', index);
            console.log('getPreSql-row', row);
            console.log('getPreSql-this.currentRow', this.currentRow);
            this.dialogPreSql = true;
            this.preSqlData = '';
            var dataPost = {"node_id": row.pk};
            this.$http.post(this.url + '/getPreSql', dataPost).then(
                function (data) {
                    var responData = data.body;
                    console.log("responData=", responData);
                    this.preSqlData = {
                        "node_id":row.pk,
                        "isexcute_pre_sql": responData[0].isexcute_pre_sql,
                        "pre_sql_str": responData[0].pre_sql_str,
                        "pre_sql_para": responData[0].pre_sql_para,
                        "pre_sql_out": responData[0].pre_sql_out
                    };
                    console.log("preSqlData=", this.preSqlData);
                }
            );
        },
        getPostKey(index, row) {
            this.currentRow = document.getElementById('nodeTable').getElementsByClassName('el-table__body')[0].getElementsByClassName("current-row ")[0];
            console.log('getPostKey-index', index);
            console.log('getPostKey-this.currentRow', this.currentRow);
            this.postKeyData = '';
            this.dialogPostKey = true;
            var dataPost = {"node_id": row.pk};
            this.$http.post(this.url + '/getPostKey', dataPost).then(
                function (data) {
                    var responData = data.body;
                    console.log("responData=", responData);
                    this.postKeyData = {
                        "node_id": row.pk,
                        "post_keys": responData[0].post_keys,
                        "post_keys_extractor": responData[0].post_keys_extractor,
                        "post_keys_default": responData[0].post_keys_default
                    };
                    console.log("postKeyDataGet=", this.postKeyData);
                }
            )
        },
        getParameter(index, row) {
            this.currentRow = document.getElementById('nodeTable').getElementsByClassName('el-table__body')[0].getElementsByClassName("current-row ")[0];
            this.dialogParameter = true;
            this.parameterData = '';
            console.log('getParameter-index', index);
            console.log('getParameter-this.currentRow', this.currentRow);
            var dataPost = {"node_id": row.pk};
            this.$http.post(this.url + '/getParameter', dataPost).then(
                function (data) {
                    var responData = data.body;
                    console.log("responData=", responData);
                    this.parameterData = {
                        "key": row.pk,
                        "value": responData[0].parameter
                    };
                    console.log("parameterData=", this.parameterData);
                }
            )
        },
        addFlowRow(flowData) {
            flowData.push({
                "account": "请输入测试账号",
                "flow_name": "请输入测试流",
                "password": "请输入测试账号密码",
                "priority": "请设置优先级",
                "creater": "请输入负责人",
                "state": "请设置是否开启自动化",
                "pk": flowData.length + 1
            })
        },
        addNodeRow(nodeData) {
            nodeData.push({
                "order_id": nodeData.length + 1,
                "node_name": "",
                "method": "",
                "path": "",
                "parameter": "",
                "pre_keys": "",
                "sleep_time": "",
                "state": "0",
                "expect_response": "",
                "isexcute_pre_sql": "0",
                "pre_sql_str": "",
                "pre_sql_para": "",
                "pre_sql_out": "",
                "ischechdb": "0",
                "sql_str": "",
                "sql_para": "",
                "expect_db": "",
                'post_keys': "",
                'post_keys_extractor': "",
                'post_keys_default': "",
                "pk": nodeData.length + 1
            })
        },
        saveFlowEdit(index, row) {
            var flowTable = document.getElementById('flowTable');
            var currentRow = flowTable.getElementsByClassName('el-table__body')[0].getElementsByClassName("el-table__row")[index];
            for (var i = 1; i < currentRow.children.length - 3; i++) {
                var cell = currentRow.children[i].getElementsByClassName('cell')[0];
                var elInput = cell.children[0];
                var elSpan = cell.children[1];
                elInput.style.display = 'none';
                elSpan.style.display = 'block';
                cell.style.color = 'black';
            }
            this.loading = true;
            var dataPost = {
                "account": row.account,
                "flow_name": row.flow_name,
                "password": row.password,
                "priority": row.priority,
                "creater": row.creater,
                "state": row.state,
                "pk": row.pk
            };
            this.$http.post(this.url + '/editFlow', dataPost).then(
                function (data) {
                    var responData = data.status;
                    if (responData === 200 || responData === '200') {
                        this.$message({
                            showClose: true,
                            message: '恭喜你，保存成功',
                            type: 'success'
                        });
                        currentRow.children[7].getElementsByClassName('save')[0].style.display = 'none';
                        currentRow.children[7].getElementsByClassName('edit')[0].style.display = 'block';
                    } else {
                        this.$message({
                            showClose: true,
                            message: '很遗憾，保存失败，快查查原因吧',
                            type: 'error'
                        });
                    }
                }
            );
        },
        changeFlowState(row) {
            var dataPost = {
                "state": row.state,
                "flow_id": row.pk
            };
            this.$http.post(this.url + '/changeFlowState', dataPost).then(
                function (data) {
                    var responData = data.status;
                    if (responData === 200 || responData === '200') {
                        this.$message({
                            showClose: true,
                            message: '设置测试流状态成功',
                            type: 'success'
                        });
                    } else {
                        this.$message({
                            showClose: true,
                            message: '设置测试流状态失败',
                            type: 'error'
                        });
                    }
                }
            );
        },
        changeNodeState(row) {
            var dataPost = {
                "state": row.state,
                "node_id": row.pk
            };
            this.$http.post(this.url + '/changeNodeState', dataPost).then(
                function (data) {
                    var responData = data.status;
                    if (responData === 200 || responData === '200') {
                        this.$message({
                            showClose: true,
                            message: '配置接口状态成功',
                            type: 'success'
                        });
                    } else {
                        this.$message({
                            showClose: true,
                            message: '配置接口状态失败',
                            type: 'error'
                        });
                    }
                }
            );
        },
        dbEditFlowTable(index, row) {
            var flowTable = document.getElementById('flowTable');
            console.log("flowTable", flowTable);
            var currentRow = flowTable.getElementsByClassName('el-table__body')[0].getElementsByClassName("current-row")[0];
            console.log("currentRow", currentRow);
            for (var i = 1; i < currentRow.children.length - 3; i++) {
                var cell = currentRow.children[i].getElementsByClassName('cell')[0];
                var elInput = cell.children[0];
                var elSpan = cell.children[1];
                elInput.style.display = 'block';
                elSpan.style.display = 'none';
                cell.style.color = 'blue';
            }
            currentRow.children[7].getElementsByClassName('save')[0].style.display = 'block';
            currentRow.children[7].getElementsByClassName('edit')[0].style.display = 'none';
            console.log("row", row);
            console.log("index", index);
        },
        editFlowTable(index, row) {
            var flowTable = document.getElementById('flowTable');
            console.log("flowTable", flowTable);
            var currentRow = flowTable.getElementsByClassName('el-table__body')[0].getElementsByClassName("el-table__row")[index];
            console.log("currentRow", currentRow);
            for (var i = 1; i < currentRow.children.length - 3; i++) {
                var cell = currentRow.children[i].getElementsByClassName('cell')[0];
                var elInput = cell.children[0];
                var elSpan = cell.children[1];
                elInput.style.display = 'block';
                elSpan.style.display = 'none';
                cell.style.color = 'blue';
            }
            currentRow.children[7].getElementsByClassName('save')[0].style.display = 'block';
            currentRow.children[7].getElementsByClassName('edit')[0].style.display = 'none';
                console.log("row", row);
                console.log("index", index);
            },
            editNodeTable(index, row) {
                console.log("this.currentRow", this.currentRow);
                var nodeTable = document.getElementById('nodeTable');
                var currentRow = nodeTable.getElementsByClassName('el-table__body')[0].getElementsByClassName("el-table__row")[index];
                console.log("editNodeTable-index", index);
                console.log("editNodeTable-row", row);
                console.log("editNodeTable-nodeTable", nodeTable);
                console.log("editNodeTable-currentRow", currentRow);
                console.log("editNodeTable-el-table__row", nodeTable.getElementsByClassName('el-table__body')[0].getElementsByClassName("el-table__row"));
                for (var i = 0; i < currentRow.children.length - 5; i++) {
                    var cell = currentRow.children[i].getElementsByClassName('cell')[0];
                    var elInput = cell.children[0];
                var elSpan = cell.children[1];
                elInput.style.display = 'block';
                elSpan.style.display = 'none';
                cell.style.color = 'blue';
            }
            currentRow.children[12].getElementsByClassName('saveNode')[0].style.display = 'block';
            currentRow.children[12].getElementsByClassName('editNode')[0].style.display = 'none';
        },
        dbEditNodeTable(index, row) {
            var nodeTable = document.getElementById('nodeTable');
            var currentRow = nodeTable.getElementsByClassName('el-table__body')[0].getElementsByClassName("current-row")[0];
            for (var i = 0; i < currentRow.children.length - 5; i++) {
                var cell = currentRow.children[i].getElementsByClassName('cell')[0];
                var elInput = cell.children[0];
                var elSpan = cell.children[1];
                elInput.style.display = 'block';
                elSpan.style.display = 'none';
                cell.style.color = 'blue';
            }
            currentRow.children[12].getElementsByClassName('saveNode')[0].style.display = 'block';
            currentRow.children[12].getElementsByClassName('editNode')[0].style.display = 'none';
        },
        saveNodeEdit(index, row, event) {
            var nodeTable = document.getElementById('nodeTable');
            var currentRow = nodeTable.getElementsByClassName('el-table__body')[0].getElementsByClassName("el-table__row")[index];
            console.log("this.currentRow", this.currentRow);
            console.log("saveNodeEdit-row", row);
            console.log("saveNodeEdit-index", index);
            console.log("saveNodeEdit-nodeTable", nodeTable);
            console.log("saveNodeEdit-currentRow", currentRow);

            for (var i = 0; i < currentRow.children.length - 5; i++) {
                var cell = currentRow.children[i].getElementsByClassName('cell')[0];
                var elInput = cell.children[0];
                var elSpan = cell.children[1];
                elInput.style.display = 'none';
                elSpan.style.display = 'block';
                cell.style.color = 'black';
            }
            this.loading = true;
            var dataPost = {
                "order_id": row.order_id,
                "flow_id": this.nodeFlowId,
                "node_name": row.node_name,
                "method": row.method,
                "path": row.path,
                "parameter": row.parameter,
                "pre_keys": row.pre_keys,
                "sleep_time": row.sleep_time,
                "state": row.state,
                "expect_response": row.expect_response,
                "isexcute_pre_sql": row.isexcute_pre_sql,
                "pre_sql_str": row.pre_sql_str,
                "pre_sql_para": row.pre_sql_para,
                "pre_sql_out": row.pre_sql_out,
                "ischechdb": row.ischechdb,
                "sql_str": row.sql_str,
                "sql_para": row.sql_para,
                "expect_db": row.expect_db,
                'post_keys': row.post_keys,
                'post_keys_extractor': row.post_keys_extractor,
                'post_keys_default': row.post_keys_default,
                "pk": row.pk
            };
            this.$http.post(this.url + '/editNode', dataPost).then(
                function (data) {
                    var responData = data.status;
                    if (responData === 200 || responData === '200') {
                        this.$message({
                            showClose: true,
                            message: '恭喜你，保存成功',
                            type: 'success'
                        });
                        currentRow.children[12].getElementsByClassName('saveNode')[0].style.display = 'none';
                        currentRow.children[12].getElementsByClassName('editNode')[0].style.display = 'block';
                    } else {
                        this.$message({
                            showClose: true,
                            message: '很遗憾，保存失败，快查查原因吧',
                            type: 'error'
                        });
                    }
                }
            );
            this.currentRow = currentRow;
            console.log("saveNodeEdit-this.currentRow2", this.currentRow)
        },
        emailChange() {
            var dataPost = {
                "email": this.recipients
            };
            this.$http.post(this.url + '/emailChange', dataPost).then(
                function (data) {
                    var responData = data.status;
                    if (responData === 200 || responData === '200') {
                        this.$message({
                            showClose: true,
                            message: '恭喜你，邮箱修改成功',
                            type: 'success'
                        })
                        this.dialogEmailChange = false;
                    } else {
                        this.$message({
                            showClose: true,
                            message: '很遗憾，邮箱修改失败',
                            type: 'error'
                        });
                        this.dialogEmailChange = false;
                    }
                }
            );
        },
        addFlowOk(flowDataDefault) {
            var account = flowDataDefault.account;
            var flow_name = flowDataDefault.flow_name;
            var password = flowDataDefault.password;
            var priority = flowDataDefault.priority;
            var creater = flowDataDefault.creater;
            var state = flowDataDefault.state;
            if (state === null || state === undefined) {
                alert("请选择是否开启自动化")
            } else {
                this.loading = true;
                var dataPost = {
                    "account": account,
                    "flow_name": flow_name,
                    "password": password,
                    "priority": priority,
                    "creater": creater,
                    "state": state,
                    "pk": this.flowData.length + 1
                };
                this.$http.post(this.url + '/addFlow', dataPost).then(
                    function (data) {
                        var responData = data.status;
                        if (responData === 200 || responData === '200') {
                            this.$message({
                                showClose: true,
                                message: '恭喜你，添加成功',
                                type: 'success'
                            });
                            this.flowData.push(dataPost);
                        } else {
                            this.$message({
                                showClose: true,
                                message: '很遗憾，添加失败了，快查查原因吧',
                                type: 'error'
                            });
                        }
                    }
                );
            }
        },
        addNodeOk(nodeDataDefault) {
            this.loading = true;
            if (nodeDataDefault[0].order_id === '') {
                this.$message({
                    showClose: true,
                    message: '执行顺序不能为空，请填写',
                    type: 'error'
                });
            } else {
                var dataPost = {
                    "order_id": nodeDataDefault[0].order_id,
                    "flow_id": this.nodeFlowId,
                    "node_name": nodeDataDefault[0].node_name,
                    "method": nodeDataDefault[0].method,
                    "path": nodeDataDefault[0].path,
                    "parameter": nodeDataDefault[0].parameter,
                    "pre_keys": nodeDataDefault[0].pre_keys,
                    "sleep_time": nodeDataDefault[0].sleep_time,
                    "state": nodeDataDefault[0].state,
                    "expect_response": nodeDataDefault[0].expect_response,
                    "isexcute_pre_sql": nodeDataDefault[0].isexcute_pre_sql,
                    "pre_sql_out": nodeDataDefault[0].pre_sql_out,
                    "pre_sql_para": nodeDataDefault[0].pre_sql_para,
                    "pre_sql_str": nodeDataDefault[0].pre_sql_str,
                    "expect_db": nodeDataDefault[0].expect_db,
                    "ischechdb": nodeDataDefault[0].ischechdb,
                    "sql_para": nodeDataDefault[0].sql_para,
                    "sql_str": nodeDataDefault[0].sql_str,
                    'post_keys': nodeDataDefault[0].post_keys,
                    'post_keys_extractor': nodeDataDefault[0].post_keys_extractor,
                    'post_keys_default': nodeDataDefault[0].post_keys_default,
                };
                this.$http.post(this.url + '/addNode', dataPost).then(
                    function (data) {
                        console.log(dataPost);
                        var responData = data.status;
                        var node_id = data.body[0].node_id;
                        if (responData === 200 || responData === '200') {
                            this.$message({
                                showClose: true,
                                message: '恭喜你，添加成功',
                                type: 'success'
                            });
                            this.nodeData.push(
                                {
                                    "order_id": nodeDataDefault[0].order_id,
                                    "flow_id": this.nodeFlowId,
                                    "node_name": nodeDataDefault[0].node_name,
                                    "method": nodeDataDefault[0].method,
                                    "path": nodeDataDefault[0].path,
                                    "parameter": nodeDataDefault[0].parameter,
                                    "pre_keys": nodeDataDefault[0].pre_keys,
                                    "sleep_time": nodeDataDefault[0].sleep_time,
                                    "state": nodeDataDefault[0].state,
                                    "expect_response": nodeDataDefault[0].expect_response,
                                    "isexcute_pre_sql": nodeDataDefault[0].isexcute_pre_sql,
                                    "pre_sql_out": nodeDataDefault[0].pre_sql_out,
                                    "pre_sql_para": nodeDataDefault[0].pre_sql_para,
                                    "pre_sql_str": nodeDataDefault[0].pre_sql_str,
                                    "expect_db": nodeDataDefault[0].expect_db,
                                    "ischechdb": nodeDataDefault[0].ischechdb,
                                    "sql_para": nodeDataDefault[0].sql_para,
                                    "sql_str": nodeDataDefault[0].sql_str,
                                    'post_keys': nodeDataDefault[0].post_keys,
                                    'post_keys_extractor': nodeDataDefault[0].post_keys_extractor,
                                    'post_keys_default': nodeDataDefault[0].post_keys_default,
                                    "pk": node_id
                                });
                        } else {
                            this.$message({
                                showClose: true,
                                message: '很遗憾，添加失败了，快查查原因吧',
                                type: 'error'
                            });
                        }
                    }
                );
            }
        },
        copyNodeOk(nodeDataDefault) {
            this.loading = true;
            if (nodeDataDefault[0].order_id === '') {
                this.$message({
                    showClose: true,
                    message: '执行顺序不能为空，请填写',
                    type: 'error'
                });
            } else {
                var dataPost = {
                    "order_id": nodeDataDefault[0].order_id,
                    "flow_id": this.nodeFlowId,
                    "node_name": nodeDataDefault[0].node_name,
                    "method": nodeDataDefault[0].method,
                    "path": nodeDataDefault[0].path,
                    "parameter": nodeDataDefault[0].parameter,
                    "pre_keys": nodeDataDefault[0].pre_keys,
                    "sleep_time": nodeDataDefault[0].sleep_time,
                    "state": nodeDataDefault[0].state,
                    "expect_response": nodeDataDefault[0].expect_response,
                    "isexcute_pre_sql": nodeDataDefault[0].isexcute_pre_sql,
                    "pre_sql_out": nodeDataDefault[0].pre_sql_out,
                    "pre_sql_para": nodeDataDefault[0].pre_sql_para,
                    "pre_sql_str": nodeDataDefault[0].pre_sql_str,
                    "expect_db": nodeDataDefault[0].expect_db,
                    "ischechdb": nodeDataDefault[0].ischechdb,
                    "sql_para": nodeDataDefault[0].sql_para,
                    "sql_str": nodeDataDefault[0].sql_str,
                    'post_keys': nodeDataDefault[0].post_keys,
                    'post_keys_extractor': nodeDataDefault[0].post_keys_extractor,
                    'post_keys_default': nodeDataDefault[0].post_keys_default,
                };
                this.$http.post(this.url + '/addNode', dataPost).then(
                    function (data) {
                        console.log(dataPost);
                        var responData = data.status;
                        var node_id = data.body[0].node_id;
                        if (responData === 200 || responData === '200') {
                            this.$message({
                                showClose: true,
                                message: '恭喜你，添加成功',
                                type: 'success'
                            });
                            this.$http.post(this.url + '/getNodeData', dataPost).then(
                                function (data) {
                                    this.nodeData = data.body;
                                }
                            );
                            this.nodeDataDefault = [
                                {
                                    "pk": "",
                                    "order_id": "",
                                    "node_name": "",
                                    "method": "POST",
                                    "path": "",
                                    "parameter": "",
                                    "expect_response": "",
                                    "sleep_time": 0,
                                    "state": "1",
                                    "isexcute_pre_sql": "0",
                                    "pre_keys": "",
                                    "pre_sql_str": "",
                                    "pre_sql_para": "",
                                    "pre_sql_out": "",
                                    "ischechdb": "0",
                                    "sql_str": "",
                                    "sql_para": "",
                                    "expect_db": "",
                                    "post_keys": "",
                                    "post_keys_extractor": "",
                                    "post_keys_default": "",
                                }
                            ]
                        } else {
                            this.$message({
                                showClose: true,
                                message: '很遗憾，添加失败了，快查查原因吧',
                                type: 'error'
                            });
                        }
                    }
                );
            }
        },
        addFlowCancel() {
            document.body.click();
        },
        addNodeCancel() {
            document.body.click();
        },
        pCancel(row) {
            document.body.click();
            this.dialogParameter =false;
            this.dialogPreSql =false;
            this.dialogPostKey =false;
            this.dialogOutSql =false;
            this.dialogManualStatistics =false;
        },
        expandChange(row, expandedRows, index) {
            this.loading = true;
            if (expandedRows.length > 1) {
                this.expands = [];
                if (row) {
                    this.expands.splice(index, 1);
                }
                this.$refs.flowTableRef.toggleRowExpansion(expandedRows[0]);
                this.nodeFlowId = row.pk;
                console.log("expandChange-nodeFlowId", this.nodeFlowId);
                var dataPost = {"flow_id": row.pk};
                this.$http.post(this.url + '/getNodeData', dataPost).then(
                    function (data) {
                        this.nodeData = data.body;
                        this.currentRow = '';
                    }
                );
            } else {
                this.expands = [];
                this.nodeFlowId = row.pk;
                console.log("expandChange-nodeFlowId", this.nodeFlowId);
                var dataPost = {"flow_id": row.pk};
                this.$http.post(this.url + '/getNodeData', dataPost).then(
                    function (data) {
                        this.nodeData = data.body;
                        this.currentRow = '';
                    }
                );
            }
        },
        formatJson(parameterData) {
            text = parameterData.value;
            if (text.indexOf("$") !== -1) {
                this.parameterData.value = JSON.stringify(JSON.parse(text.replace(/\:\$/g, "\:\"\$").replace(/\$\,/g, "\$\"\,").replace(/\$\}/g, "\$\"\}").replace(/\[\$/g, "\[\"\$").replace(/\$\]/g, "\$\"\]")), null, 2);
            } else {
                this.parameterData.value = JSON.stringify(JSON.parse(text), null, 2);
            }
        },
        deleteFlowRow(index,rows,row) {
            console.log(row);
            this.deleteFlowId = row.pk;
            console.log(this.deleteFlowId);
            console.log(index);
            rows.splice(index, 1);
            this.deleteFlowDialogVisible = true;
        },
        deleteNodeRow(index, rows,row) {
            this.deleteNodeId = row.pk;
            console.log(this.deleteNodeId);
            rows.splice(index, 1);
            this.deleteNodeDialogVisible = true;
        },
        deleteFlowOk() {
            this.loading = true;
            console.log(this.deleteFlowId);
            var dataPost = {
                "flow_id": this.deleteFlowId,
            };
            this.$http.post(this.url + '/deleteFlow', dataPost).then(
                function (data) {
                    var responData = data.status;
                    if (responData === 200 || responData === '200') {
                        this.$message({
                            showClose: true,
                            message: '恭喜你，删除成功',
                            type: 'success'
                        });
                        this.deleteFlowDialogVisible = false
                    } else {
                        this.$message({
                            showClose: true,
                            message: '很遗憾，删除失败，快查查原因吧',
                            type: 'error'
                        });
                    }
                }
            );
        },
        deleteNodeOk() {
            this.loading = true;
            var dataPost = {
                "node_id": this.deleteNodeId,
            };
            this.$http.post(this.url + '/deleteNode', dataPost).then(
                function (data) {
                    var responData = data.status;
                    if (responData === 200 || responData === '200') {
                        this.$message({
                            showClose: true,
                            message: '恭喜你，删除成功',
                            type: 'success'
                        });
                        this.deleteNodeDialogVisible = false
                    } else {
                        this.$message({
                            showClose: true,
                            message: '很遗憾，删除失败，快查查原因吧',
                            type: 'error'
                        });
                    }
                }
            );
        },
        rowClick(row, column, event) {
            console.log("this.currentRow=", this.currentRow);
            console.log("column=", column);
            this.currentRow = document.getElementById('nodeTable').getElementsByClassName("current-row")[0];
            console.log("this.currentRow2=", this.currentRow);
            this.currentRow = document.getElementById('nodeTable').getElementsByClassName("current-row")[0];
            console.log("this.currentRow3=", this.currentRow);
        },
        filtrateCreater() {
            var dataPost = {
                "creater": this.filtrate,
                "page_size":this.pageSize
            };
            this.$http.post(this.url + '/getCreater', dataPost).then(
                function (data) {
                    var responData = data.status;
                    if (responData === 200 || responData === '200') {
                        this.flowData = data.body;
                    } else {
                        this.$message({
                            showClose: true,
                            message: '很遗憾，筛选失败',
                            type: 'error'
                        });
                    }
                }
            );

        },
        getLog(){
            console.log("====getLog===");
            i = 0;
            while(i < 3){
                var dataPost = {};
                this.$http.post(this.url + '/getLog', dataPost).then(
                    function (data) {
                        var responData = data.status;
                        if (responData === 200 || responData === '200') {
                            var t = data.body[0].log;
                            var texts = t.split('==>');
                            for(var i = 0;i<len(texts);i++){
                                this.text = texts[i]
                            }

                        } else {

                        }
                    }
                );
                i++;
            }
        },
        actionFlow(index, row) {
            this.actionLoading = true;
            var dataPost = {
                "flow_id": row.pk,
            };
            this.$http.post(this.url + '/actionFlow', dataPost).then(
                function (data) {
                    var responData = data.status;
                    if (responData === 200 || responData === '200') {
                        this.actionLoading = false;
                        this.$message({
                            showClose: true,
                            message: '测试流接口执行成功，结果请查收邮件',
                            type: 'success'
                        });
                        this.dialogReport = true;
                    } else {
                        this.actionLoading = false;
                        this.$message({
                            showClose: true,
                            message: '很遗憾，接口执行失败',
                            type: 'error'
                        });
                        this.dialogReport = true;
                    }
                }
            );

        },
        actionAllFlow() {
            var dataPost = {};
            this.actionLoading = true;
            this.$http.post(this.url + '/actionAllFlow', dataPost).then(
                function (data) {
                    var responData = data.status;
                    if (responData === 200 || responData === '200') {
                        this.actionLoading = false;
                        this.$message({
                            showClose: true,
                            message: '测试流接口执行成功，结果请查收邮件',
                            type: 'success'
                        });
                        this.dialogReport = true;
                    } else {
                        this.actionLoading = false;
                        this.$message({
                            showClose: true,
                            message: '很遗憾，接口执行失败',
                            type: 'error'
                        });
                        this.dialogReport = true;
                    }
                }
            );


        }
    }
});
