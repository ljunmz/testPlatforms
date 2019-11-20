var vm = new Vue({
    el: '#app',
    data() {
        return {
            url: 'http://apitest.shiguangxu.com:8000',
            activeIndex: '8',
            registerPhone: "",
            clearPhone: "",
            clearModel: "",
            token: "",
            todo_id: "",
            phone: "",
            clearItemPhone: "",
            email: "",
            phoneCode: "",
            buriedPhone : "",
            userPhone: "",
            buriedInfo:{
                user_id:"",
                device_tag:"",
                event_type:"",
                event_param:"",
                ip:"",
                channel:"",
                os_type:"",
                network_type:"",
                created:"",
                app_version:""
            },
            todoInfo: {
                user_id:'',
                short_title:'',
                status:'',
                deleted:'',
                todo_type:'',
                finish_state:'',
                ahead_type:'',
                todo_time:'',
                next_time:'',
                created:'',
            },
            emailCode: "",
            userInfo: {
                user_id:"",
                user_name:"",
                email:"",
                phoneCode:"",
                emailCode:"",
                isbindQQ:"",
                isbindW:""

            },
            tokenInfo:{
                user_id:"",
                device_tag_app:"",
                moblie:"",
                updated:"",
            },
            UserId: "",
            actionLoading: false,
            actionLoading2: false
        }
    },
    methods: {
        getBuriedInfo(){
            var dataPost = {
                "phone": this.buriedPhone,
            };
            this.$http.post(this.url+'/getBuriedInfo', dataPost).then(
                function (data) {
                    var responData = data.body;
                    if (responData[0].code === 200 || responData[0].code === '200') {
                        this.buriedInfo = responData[0].data;
                        this.$message({
                            showClose: true,
                            message: '恭喜你，获取埋点成功',
                            type: 'success'
                        });
                        this.actionLoading2 = false;
                    } else {
                        this.$message({
                            showClose: true,
                            message: '很遗憾，获取埋点失败',
                            type: 'error'
                        });
                        this.actionLoading2 = false;
                    }
                }
            );
        },
        onSubmit() {
            console.log('submit!');
        },
        handleSelect(key, keyPath) {
            console.log(key, keyPath);
        },
        getTodoInfo(){
            this.actionLoading2 = true;
            var dataPost = {
                "todo_id": this.todo_id,
            };
            this.$http.post(this.url+'/getTodoInfo', dataPost).then(
                function (data) {
                    var responData = data.body;
                    if (responData[0].code === 200 || responData[0].code === '200') {
                        this.todoInfo = responData[0].data;
                        this.$message({
                            showClose: true,
                            message: '恭喜你，日程信息获取成功',
                            type: 'success'
                        });
                        this.actionLoading2 = false;
                    } else {
                        this.$message({
                            showClose: true,
                            message: '很遗憾，日程信息获取失败',
                            type: 'error'
                        });
                        this.actionLoading2 = false;
                    }
                }
            );
        },
        getTokenInfo(){
            this.actionLoading = true;
            var dataPost = {
                "token": this.token,
            };
            this.$http.post(this.url+'/getTokenInfo', dataPost).then(
                function (data) {
                    var responData = data.body;
                    if (responData[0].code === 200 || responData[0].code === '200') {
                        this.tokenInfo = responData[0].data;
                        this.$message({
                            showClose: true,
                            message: '恭喜你，token信息获取成功',
                            type: 'success'
                        });
                        this.actionLoading = false;
                    } else {
                        this.$message({
                            showClose: true,
                            message: '很遗憾，token信息获取失败',
                            type: 'error'
                        });
                        this.actionLoading = false;
                    }
                }
            );
        },
        clearPhoneCodeRecords(){
            var dataPost = {
                "mobile": this.clearPhone,
            };
            this.$http.post(this.url+'/clearPhoneCodeRecords', dataPost).then(
                function (data) {
                    var responData = data.status;
                    if (responData === 200 || responData === '200') {
                        this.$message({
                            showClose: true,
                            message: '恭喜你，手机号获取验证码记录清除成功',
                            type: 'success'
                        });
                        this.actionLoading = false;
                    } else {
                        this.$message({
                            showClose: true,
                            message: '很遗憾，数据清除失败',
                            type: 'error'
                        });
                        this.actionLoading = false;
                    }
                }
            );

        },
        changeCreatedTime(){
            var dataPost = {
                "mobile": this.clearItemPhone,
            };
            this.$http.post(this.url+'/changeCreatedTime', dataPost).then(
                function (data) {
                    var responData = data.status;
                    if (responData === 200 || responData === '200') {
                        this.$message({
                            showClose: true,
                            message: '恭喜你，事项100条限制清除成功',
                            type: 'success'
                        });
                        this.actionLoading = false;
                    } else {
                        this.$message({
                            showClose: true,
                            message: '很遗憾，数据清除失败',
                            type: 'error'
                        });
                        this.actionLoading = false;
                    }
                }
            );
        },
        clearModelCodeRecords(){
            var dataPost = {
                "device_model": this.clearModel,
            };
            this.$http.post(this.url+'/clearModelCodeRecords', dataPost).then(
                function (data) {
                    var responData = data.status;
                    if (responData === 200 || responData === '200') {
                        this.$message({
                            showClose: true,
                            message: '恭喜你，设备获取验证码记录清除成功',
                            type: 'success'
                        });
                        this.actionLoading = false;
                    } else {
                        this.$message({
                            showClose: true,
                            message: '很遗憾，数据清除失败',
                            type: 'error'
                        });
                        this.actionLoading = false;
                    }
                }
            );
        },
        register() {
            this.actionLoading = true;
            var dataPost = {
                "mobile": this.registerPhone,
            };
            this.$http.post(this.url+'/register', dataPost).then(
                function (data) {
                    var responData = data.status;
                    if (responData === 200 || responData === '200') {
                        this.$message({
                            showClose: true,
                            message: '恭喜你，注册成功,账号密码：123456',
                            type: 'success'
                        });
                        this.actionLoading = false;
                    } else {
                        this.$message({
                            showClose: true,
                            message: '很遗憾，注册失败',
                            type: 'error'
                        });
                        this.actionLoading = false;
                    }
                }
            );

        },
        getUserInfo() {
            this.actionLoading = true;
            var dataPost = {
                "mobile": this.userPhone,
            };
            this.$http.post(this.url+'/getUserInfo', dataPost).then(
                function (data) {
                    var responData = data.body;
                    if (responData[0].code === 200 || responData[0].code === '200') {
                        this.userInfo = responData[0].data;
                        console.log(responData[0].data);
                        this.$message({
                            showClose: true,
                            message: '恭喜你，用户信息获取成功',
                            type: 'success'
                        });
                        this.actionLoading = false;
                    } else {
                        this.$message({
                            showClose: true,
                            message: '很遗憾，用户未注册',
                            type: 'error'
                        });
                        this.actionLoading = false;
                    }
                }
            );

        },

    }
})