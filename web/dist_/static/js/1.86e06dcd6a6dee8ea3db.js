webpackJsonp([1],{QG2t:function(a,t){},o47g:function(a,t){},qf40:function(a,t,e){"use strict";Object.defineProperty(t,"__esModule",{value:!0});var s=e("pFYg"),i=e.n(s),n=e("2LA7"),o=e.n(n),r=e("Xp0u"),l=e("Jti3"),u={name:"args",props:["argsData"],data:function(){return{funName:"",postData:""}},methods:{transferArgData:function(a){this.$eventBus.$emit("transferArgData",a),console.log("changed")},updataPostData:function(){var a="";for(var t in this.argsData[this.funName].args)a+=t+"="+this.argsData[this.funName].args[t].default+", ";a=a.substring(0,a.length-2),this.postData=a},selectChange:function(){this.updataPostData(),this.transferArgData({funName:this.funName,postData:this.postData})},inputChange:function(){this.transferArgData({funName:this.funName,postData:this.postData})}},created:function(){for(var a in this.argsData){this.funName=a;break}this.updataPostData()}},c={render:function(){var a=this,t=a.$createElement,e=a._self._c||t;return"{}"!=JSON.stringify(a.argsData)?e("el-row",{staticClass:"arg-background",attrs:{gutter:10}},[e("p",{staticClass:"args-tittle"},[a._v("function:")]),a._v(" "),e("el-select",{staticClass:"args-bottom",attrs:{placeholder:"请选择函数"},on:{change:function(t){return a.selectChange()}},model:{value:a.funName,callback:function(t){a.funName=t},expression:"funName"}},a._l(a.argsData,function(a,t){return e("el-option",{key:t,attrs:{label:t,value:t}})}),1),a._v(" "),e("p",{staticClass:"args-tittle"},[a._v("function args:")]),a._v(" "),e("el-input",{staticClass:"args-bottom",attrs:{type:"textarea",autosize:{minRows:1,maxRows:3},placeholder:"请输入函数参数"},on:{change:function(t){return a.inputChange()}},model:{value:a.postData,callback:function(t){a.postData=t},expression:"postData"}}),a._v(" "),""!=a.funName?e("p",{staticClass:"args-tittle"},[a._v("function infomation:")]):a._e(),a._v(" "),""!=a.funName?e("div",[e("p",{staticClass:"fun-info-wrap"},[a._v("\n      "+a._s(a.argsData[a.funName].doc)+"\n    ")])]):a._e()],1):a._e()},staticRenderFns:[]};var g=e("VU/8")(u,c,!1,function(a){e("o47g")},null,null).exports,m={name:"Augumentations",props:["modelData"],components:{ShowArea:r.a,LoadingAnimationVue:l.a,Args:g},data:function(){return{baseUrl:o.a.base_url,imageUrl:"",targetImageUrl:"",isLoading:!1,isLoading2:!1,modelResult:"",argData:""}},methods:{getType:function(a){return void 0===a?"undefined":i()(a)},moveClick:function(){var a=this;this.$nextTick(function(){a.$refs.filebutton.dispatchEvent(new MouseEvent("click"))})},fileChange:function(){var a=this;this.imageVerification(this.$refs.filebutton)?(this.isLoading=!0,this.$nextTick(function(){console.log(a.$refs.filebutton.files);var t=new FormData;t.append("image",a.$refs.filebutton.files[0]),a.$axios.post(a.baseUrl+"upload",t,{"Content-type":"multipart/form-data"}).then(function(t){console.log(t.data),a.imageUrl=a.baseUrl+"absimage?path="+t.data},function(a){alert("上传图片失败！")}).catch(function(t){a.$message({message:"上传图片失败！"+t,type:"error"})})})):this.$message({message:"图片校验失败！",type:"warning"})},stopAxios:function(){this.source.cancel("Operation canceled by the user.")},imageClear:function(){this.imageUrl="",this.$refs.filebutton.value="",this.isLoading=!1,this.isLoading2=!1,this.modelResult="",this.targetImageUrl=""},submit:function(){var a=this;if(""==this.imageUrl)this.$message({message:"请先上传图片！",type:"warning"});else{this.targetImageUrl="",this.isLoading2=!0,this.modelResult="";var t={local_image_url:this.imageUrl.split("=")[1],conda_env:this.modelData.condaEnv,args:{},classname:this.modelData.modelType,demoname:this.modelData.modelId};t.args.funName=this.argData.funName,t.args.funArgs='"'+this.argData.postData+'"',this.CancelToken=this.$axios.CancelToken,this.source=this.CancelToken.source(),this.$axios.post(this.baseUrl+"submit",t,{cancelToken:this.source.token}).then(function(t){console.log("kkkkres:",t);var e=t.data[t.data.length-1];e=(e=e.split(" "))[e.length-1],e=a.baseUrl+"absimage?path="+e,a.targetImageUrl=e,a.isLoading2=!1}).catch(function(t){a.isLoading2=!1,a.$message({message:t,type:"error"})})}},onDrop:function(a){(window.event||a).preventDefault(),this.$refs.filebutton.files=a.dataTransfer.files,this.fileChange(),console.log(this.$refs.filebutton.files),console.log(a.dataTransfer.files[0])}},mounted:function(){var a=this;setTimeout(function(){var t=a,e=document.getElementById("drop-area");e.ondragenter=e.ondragover=e.ondragleave=function(){return!1},e.addEventListener("drop",t.onDrop)},0);var t=this;this.$eventBus.$on("addClick",function(a){t.moveClick()}),this.$eventBus.$on("addShowImage",function(a){t.imageClear(),t.imageUrl=a,console.log(a)}),this.$eventBus.$on("transferArgData",function(a){t.argData=a})}},d={render:function(){var a=this,t=a.$createElement,s=a._self._c||t;return s("div",[s("el-row",{staticClass:"show-wrap"},[s("el-col",{staticClass:"model-left-wrap",attrs:{xs:24,sm:12,md:12,lg:12,xl:12}},[s("p",{staticClass:"model-inout-tittle"},[a._v(a._s(a.$t("message.input_image")))]),a._v(" "),s("vue-viewer",{directives:[{name:"show",rawName:"v-show",value:""!=a.imageUrl,expression:"imageUrl!=''"}],staticClass:"source-image",attrs:{thumb:a.imageUrl,full:a.imageUrl}}),a._v(" "),s("div",{directives:[{name:"show",rawName:"v-show",value:""==a.imageUrl,expression:"imageUrl == ''"}],staticClass:"input-wrap",attrs:{id:"drop-area"},on:{click:function(t){return a.moveClick()}}},[s("img",{attrs:{src:e("kTpr"),alt:""}}),a._v(" "),s("p",{directives:[{name:"show",rawName:"v-show",value:0==a.isLoading,expression:"isLoading == false"}],staticClass:"input-help"},[a._v("\n          "+a._s(a.$t("message.drop_image"))+"\n        ")]),a._v(" "),s("p",{directives:[{name:"show",rawName:"v-show",value:0==a.isLoading,expression:"isLoading == false"}],staticClass:"input-help"},[a._v("\n          "+a._s(a.$t("message.or"))+"\n        ")]),a._v(" "),s("p",{directives:[{name:"show",rawName:"v-show",value:0==a.isLoading,expression:"isLoading == false"}],staticClass:"input-help"},[a._v("\n          "+a._s(a.$t("message.click_upload"))+"\n        ")]),a._v(" "),s("p",{directives:[{name:"show",rawName:"v-show",value:a.isLoading,expression:"isLoading"}]},[a._v("uploading......")]),a._v(" "),s("input",{directives:[{name:"show",rawName:"v-show",value:0,expression:"0"}],ref:"filebutton",attrs:{type:"file"},on:{change:function(t){return a.fileChange()}}})]),a._v(" "),s("ShowArea",{staticClass:"centered lr-padding",attrs:{showImages:a.modelData.showImages}})],1),a._v(" "),s("el-col",{staticClass:"model-right-wrap",attrs:{xs:24,sm:12,md:12,lg:12,xl:12}},[s("p",{staticClass:"model-inout-tittle"},[a._v(a._s(a.$t("message.result")))]),a._v(" "),s("div",[s("LoadingAnimationVue",{directives:[{name:"show",rawName:"v-show",value:a.isLoading2,expression:"isLoading2"}]}),a._v(" "),s("vue-viewer",{directives:[{name:"show",rawName:"v-show",value:""!=a.targetImageUrl,expression:"targetImageUrl!=''"}],staticClass:"source-image",attrs:{thumb:a.targetImageUrl,full:a.targetImageUrl}})],1)])],1),a._v(" "),s("Args",{attrs:{argsData:a.modelData.args}}),a._v(" "),s("el-row",{attrs:{gutter:10}},[s("el-col",{attrs:{xs:12,sm:6,md:6,lg:6,xl:6}},[s("a",{staticClass:"clear upload-btn",attrs:{href:"javascript:void(0);"},on:{click:function(t){a.imageClear(),a.stopAxios()}}},[a._v(a._s(a.$t("message.clear")))])]),a._v(" "),s("el-col",{attrs:{xs:12,sm:6,md:6,lg:6,xl:6}},[s("a",{staticClass:"submit upload-btn",class:{"submit-forbidden":1==a.isLoading2},attrs:{href:"javascript:void(0);"},on:{click:function(t){return a.submit()}}},[a._v(a._s(a.$t("message.submit")))])])],1)],1)},staticRenderFns:[]};var f=e("VU/8")(m,d,!1,function(a){e("QG2t")},null,null);t.default=f.exports}});
//# sourceMappingURL=1.86e06dcd6a6dee8ea3db.js.map