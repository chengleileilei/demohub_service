webpackJsonp([2],{QiMY:function(e,s){},"v7+i":function(e,s,t){"use strict";Object.defineProperty(s,"__esModule",{value:!0});var a=t("vB2q"),i={render:function(){var e=this,s=e.$createElement,a=e._self._c||s;return a("div",[a("el-row",{staticClass:"show-wrap"},[a("el-col",{staticClass:"model-left-wrap",attrs:{xs:24,sm:12,md:12,lg:12,xl:12}},[a("p",{staticClass:"model-inout-tittle"},[e._v(e._s(e.$t("message.input_image")))]),e._v(" "),a("vue-viewer",{directives:[{name:"show",rawName:"v-show",value:""!=e.imageUrl,expression:"imageUrl != ''"}],staticClass:"source-image",attrs:{thumb:e.imageUrl,full:e.imageUrl}}),e._v(" "),a("div",{directives:[{name:"show",rawName:"v-show",value:""==e.imageUrl,expression:"imageUrl == ''"}],staticClass:"input-wrap",attrs:{id:"drop-area"},on:{click:function(s){return e.moveClick()}}},[a("img",{attrs:{src:t("kTpr"),alt:""}}),e._v(" "),a("p",{directives:[{name:"show",rawName:"v-show",value:0==e.isLoading,expression:"isLoading == false"}],staticClass:"input-help"},[e._v("\n          "+e._s(e.$t("message.drop_image"))+"\n        ")]),e._v(" "),a("p",{directives:[{name:"show",rawName:"v-show",value:0==e.isLoading,expression:"isLoading == false"}],staticClass:"input-help"},[e._v("\n          "+e._s(e.$t("message.or"))+"\n        ")]),e._v(" "),a("p",{directives:[{name:"show",rawName:"v-show",value:0==e.isLoading,expression:"isLoading == false"}],staticClass:"input-help"},[e._v("\n          "+e._s(e.$t("message.click_upload"))+"\n        ")]),e._v(" "),a("p",{directives:[{name:"show",rawName:"v-show",value:e.isLoading,expression:"isLoading"}]},[e._v("uploading......")]),e._v(" "),a("input",{directives:[{name:"show",rawName:"v-show",value:0,expression:"0"}],ref:"filebutton",attrs:{type:"file"},on:{change:function(s){return e.fileChange()}}})]),e._v(" "),a("ShowArea",{staticClass:"centered lr-padding",attrs:{showImages:e.modelData.showImages}})],1),e._v(" "),a("el-col",{staticClass:"model-right-wrap",attrs:{xs:24,sm:12,md:12,lg:12,xl:12}},[a("p",{staticClass:"model-inout-tittle"},[e._v(e._s(e.$t("message.result")))]),e._v(" "),a("div",[a("LoadingAnimationVue",{directives:[{name:"show",rawName:"v-show",value:e.isLoading2,expression:"isLoading2"}]}),e._v(" "),e.falseShow?a("p",[e._v("False！")]):e._e(),e._v(" "),e._l(e.modelResult,function(s,t){return a("div",{directives:[{name:"show",rawName:"v-show",value:""!=e.modelResult,expression:"modelResult != ''"}],key:t},[a("div",{staticClass:"result-item-percentage"},[a("div",{staticClass:"item-bar",style:"width:"+90*Number(String(s.split(" ").slice(-1)))+"%"}),e._v(" "),a("p",[e._v("\n              "+e._s(String(Number(s.split(" ").slice(-1))).slice(0,4))+"\n            ")])]),e._v(" "),a("p",{staticClass:"result-item-type"},[e._v("\n            "+e._s(String(s.split(" ").slice(0,-1).join(" ")))+"\n          ")])])}),e._v(" "),a("div",{directives:[{name:"show",rawName:"v-show",value:""!=e.modelResult,expression:"modelResult != ''"}],staticClass:"text-res"},[a("p",[e._v("\n            "+e._s(e.modelResult)+"\n          ")])])],2)])],1),e._v(" "),"{}"!=JSON.stringify(e.modelData.args)&&void 0!==e.modelData.args?a("el-row",{staticClass:"arg-background",attrs:{gutter:10}},e._l(e.modelData.args,function(s,t){return a("el-col",{key:t,attrs:{xs:24,sm:24,md:24,lg:12,xl:12}},[a("div",{staticClass:"arg-wrap"},[a("p",[e._v(e._s(t)+":")]),e._v(" "),"select"==s.type?a("el-select",{attrs:{placeholder:"请选择"},model:{value:s.default,callback:function(t){e.$set(s,"default",t)},expression:"arg_data.default"}},e._l(s.values,function(e){return a("el-option",{key:e,attrs:{label:e,value:e}})}),1):e._e(),e._v(" "),"int"==s.type?a("el-input-number",{attrs:{precision:0,step:1,min:Math.min.apply(null,s.values),max:Math.max.apply(null,s.values)},model:{value:s.default,callback:function(t){e.$set(s,"default",t)},expression:"arg_data.default"}}):e._e(),e._v(" "),"float"==s.type?a("el-input-number",{attrs:{precision:2,step:.1,min:Math.min.apply(null,s.values),max:Math.max.apply(null,s.values)},model:{value:s.default,callback:function(t){e.$set(s,"default",t)},expression:"arg_data.default"}}):e._e()],1)])}),1):e._e(),e._v(" "),a("el-row",{attrs:{gutter:10}},[a("el-col",{attrs:{xs:12,sm:6,md:6,lg:6,xl:6}},[a("a",{staticClass:"clear upload-btn",attrs:{href:"javascript:void(0);"},on:{click:function(s){e.imageClear(),e.stopAxios()}}},[e._v(e._s(e.$t("message.clear")))])]),e._v(" "),a("el-col",{attrs:{xs:12,sm:6,md:6,lg:6,xl:6}},[a("a",{staticClass:"submit upload-btn",class:{"submit-forbidden":1==e.isLoading2},attrs:{href:"javascript:void(0);"},on:{click:function(s){return e.submit()}}},[e._v(e._s(e.$t("message.submit")))])])],1)],1)},staticRenderFns:[]};var n=function(e){t("QiMY")},o=t("VU/8")(a.a,i,!1,n,null,null);s.default=o.exports},vB2q:function(module,__webpack_exports__,__webpack_require__){"use strict";var __WEBPACK_IMPORTED_MODULE_0_babel_runtime_helpers_typeof__=__webpack_require__("pFYg"),__WEBPACK_IMPORTED_MODULE_0_babel_runtime_helpers_typeof___default=__webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0_babel_runtime_helpers_typeof__),__WEBPACK_IMPORTED_MODULE_1__assets_config_json__=__webpack_require__("2LA7"),__WEBPACK_IMPORTED_MODULE_1__assets_config_json___default=__webpack_require__.n(__WEBPACK_IMPORTED_MODULE_1__assets_config_json__),__WEBPACK_IMPORTED_MODULE_2__components_modelComponents_ShowArea_vue__=__webpack_require__("Xp0u"),__WEBPACK_IMPORTED_MODULE_3__LoadingAnimation_vue__=__webpack_require__("Jti3");__webpack_exports__.a={name:"classification",props:["modelData"],components:{ShowArea:__WEBPACK_IMPORTED_MODULE_2__components_modelComponents_ShowArea_vue__.a,LoadingAnimationVue:__WEBPACK_IMPORTED_MODULE_3__LoadingAnimation_vue__.a},data:function(){return{baseUrl:__WEBPACK_IMPORTED_MODULE_1__assets_config_json___default.a.base_url,imageUrl:"",isLoading:!1,isLoading2:!1,modelResult:"",falseShow:!1}},methods:{getType:function(e){return void 0===e?"undefined":__WEBPACK_IMPORTED_MODULE_0_babel_runtime_helpers_typeof___default()(e)},moveClick:function(){var e=this;this.$nextTick(function(){e.$refs.filebutton.dispatchEvent(new MouseEvent("click"))})},fileChange:function(){var e=this;this.imageVerification(this.$refs.filebutton)?(this.isLoading=!0,this.$nextTick(function(){console.log(e.$refs.filebutton.files);var s=new FormData;s.append("image",e.$refs.filebutton.files[0]),e.$axios.post(e.baseUrl+"upload",s,{"Content-type":"multipart/form-data"}).then(function(s){console.log(s.data),e.imageUrl=e.baseUrl+"absimage?path="+s.data},function(e){alert("上传图片失败！")}).catch(function(s){e.$message({message:"上传图片失败！"+s,type:"error"})})})):this.$message({message:"图片校验失败！",type:"warning"})},stopAxios:function(){this.source.cancel("Operation canceled by the user.")},imageClear:function(){this.imageUrl="",this.$refs.filebutton.value="",this.isLoading=!1,this.isLoading2=!1,this.modelResult="",this.falseShow=!1},submit:function submit(){var _this3=this;if(""==this.imageUrl)this.$message({message:"请先上传图片！",type:"warning"});else{this.falseShow=!1,this.isLoading2=!0,this.modelResult="";var post_data={local_image_url:this.imageUrl.split("=")[1],conda_env:this.modelData.condaEnv,args:{},classname:this.modelData.modelType,demoname:this.modelData.modelId};for(var arg_name in this.modelData.args)post_data.args[arg_name]=this.modelData.args[arg_name].default;console.log(post_data),this.CancelToken=this.$axios.CancelToken,this.source=this.CancelToken.source(),this.$axios.post(this.baseUrl+"submit",post_data,{cancelToken:this.source.token}).then(function(res){_this3.modelResult=eval(res.data),0==_this3.modelResult&&(_this3.falseShow=!0),console.log("res=>",res),_this3.isLoading2=!1}).catch(function(e){_this3.isLoading2=!1,_this3.$message({message:e,type:"error"})})}},onDrop:function(e){(window.event||e).preventDefault(),this.$refs.filebutton.files=e.dataTransfer.files,this.fileChange(),console.log(this.$refs.filebutton.files),console.log(e.dataTransfer.files[0])}},created:function(){},mounted:function(){var e=this;setTimeout(function(){var s=e,t=document.getElementById("drop-area");t.ondragenter=t.ondragover=t.ondragleave=function(){return!1},t.addEventListener("drop",s.onDrop)},0);var s=this;this.$eventBus.$on("addClick",function(e){s.moveClick()}),this.$eventBus.$on("addShowImage",function(e){s.imageClear(),s.imageUrl=e,console.log(e)})},beforedestroy:function(){eventBus.$off("eventName")}}}});
//# sourceMappingURL=2.f81a0c8a7a7c2e95a31b.js.map