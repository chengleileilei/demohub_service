webpackJsonp([4],{"9iiv":function(e,a){},jOAV:function(e,a,t){"use strict";Object.defineProperty(a,"__esModule",{value:!0});var s=t("pFYg"),i=t.n(s),n=t("2LA7"),l=t.n(n),o=t("5SbQ"),r=t("Yya3"),u={name:"objectdetection",props:["modelData"],components:{ShowArea:o.a,LoadingAnimationVue:r.a},data:function(){return{baseUrl:l.a.base_url,imageUrl:"",targetImageUrl:"",isLoading:!1,isLoading2:!1}},methods:{getType:function(e){return void 0===e?"undefined":i()(e)},moveClick:function(){var e=this;this.$nextTick(function(){e.$refs.filebutton.dispatchEvent(new MouseEvent("click"))})},stopAxios:function(){void 0!=this.source&&this.source.cancel("Operation canceled by the user.")},submit:function(){var e=this;if(""==this.imageUrl)this.$message({message:"请先上传图片！",type:"warning"});else{this.targetImageUrl="",this.isLoading2=!0;var a={local_image_url:this.imageUrl.split("=")[1],conda_env:this.modelData.condaEnv,args:{},classname:this.modelData.modelType,demoname:this.modelData.modelId};for(var t in this.modelData.args)a.args[t]=this.modelData.args[t].default;this.CancelToken=this.$axios.CancelToken,this.source=this.CancelToken.source(),this.$axios.post(this.baseUrl+"submit",a,{cancelToken:this.source.token}).then(function(a){console.log("kkkkres:",a);var t=a.data[a.data.length-1];t=(t=t.split(" "))[t.length-1],t=e.baseUrl+"absimage?path="+t+"&t="+Math.random(),e.targetImageUrl=t,e.isLoading2=!1}).catch(function(a){e.isLoading2=!1,e.$message({message:a,type:"error"})})}},onDrop:function(e){(window.event||e).preventDefault(),this.$refs.filebutton.files=e.dataTransfer.files,this.fileChange(),console.log(this.$refs.filebutton.files),console.log(e.dataTransfer.files[0])}},mounted:function(){var e=this;setTimeout(function(){var a=e,t=document.getElementById("drop-area");t.ondragenter=t.ondragover=t.ondragleave=function(){return!1},t.addEventListener("drop",a.onDrop)},0);var a=this;this.$eventBus.$on("addClick",function(e){a.moveClick()}),this.$eventBus.$on("addShowImage",function(e){a[e.bindName]=e.showImageUrl})}},c={render:function(){var e=this,a=e.$createElement,s=e._self._c||a;return s("div",[s("el-row",{staticClass:"show-wrap"},[s("el-col",{staticClass:"model-left-wrap",attrs:{xs:24,sm:12,md:12,lg:12,xl:12}},[s("p",{staticClass:"model-inout-tittle"},[e._v(e._s(e.$t("message.input_image")))]),e._v(" "),s("vue-viewer",{directives:[{name:"show",rawName:"v-show",value:""!=e.imageUrl,expression:"imageUrl != ''"}],staticClass:"source-image",attrs:{thumb:e.imageUrl,full:e.imageUrl}}),e._v(" "),s("div",{directives:[{name:"show",rawName:"v-show",value:""==e.imageUrl,expression:"imageUrl == ''"}],staticClass:"input-wrap",attrs:{id:"drop-area"},on:{click:function(a){return e.moveClick()}}},[s("img",{attrs:{src:t("kTpr"),alt:""}}),e._v(" "),s("p",{directives:[{name:"show",rawName:"v-show",value:0==e.isLoading,expression:"isLoading == false"}],staticClass:"input-help"},[e._v("\n          "+e._s(e.$t("message.drop_image"))+"\n        ")]),e._v(" "),s("p",{directives:[{name:"show",rawName:"v-show",value:0==e.isLoading,expression:"isLoading == false"}],staticClass:"input-help"},[e._v("\n          "+e._s(e.$t("message.or"))+"\n        ")]),e._v(" "),s("p",{directives:[{name:"show",rawName:"v-show",value:0==e.isLoading,expression:"isLoading == false"}],staticClass:"input-help"},[e._v("\n          "+e._s(e.$t("message.click_upload"))+"\n        ")]),e._v(" "),s("p",{directives:[{name:"show",rawName:"v-show",value:e.isLoading,expression:"isLoading"}]},[e._v("uploading......")]),e._v(" "),s("input",{directives:[{name:"show",rawName:"v-show",value:0,expression:"0"}],ref:"filebutton",attrs:{type:"file"},on:{change:function(a){return e.fileChange("filebutton","imageUrl","isLoading")}}})]),e._v(" "),s("ShowArea",{staticClass:"centered lr-padding",attrs:{showAreaData:{images:e.modelData.detialData.show_images,bindName:"imageUrl"}}})],1),e._v(" "),s("el-col",{staticClass:"model-right-wrap",attrs:{xs:24,sm:12,md:12,lg:12,xl:12}},[s("p",{staticClass:"model-inout-tittle"},[e._v(e._s(e.$t("message.result")))]),e._v(" "),s("div",[s("LoadingAnimationVue",{directives:[{name:"show",rawName:"v-show",value:e.isLoading2,expression:"isLoading2"}]}),e._v(" "),s("vue-viewer",{directives:[{name:"show",rawName:"v-show",value:""!=e.targetImageUrl,expression:"targetImageUrl != ''"}],staticClass:"source-image",attrs:{thumb:e.targetImageUrl,full:e.targetImageUrl}})],1)])],1),e._v(" "),"{}"!=JSON.stringify(e.modelData.args)&&void 0!==e.modelData.args?s("el-row",{staticClass:"arg-background",attrs:{gutter:10}},e._l(e.modelData.args,function(a,t){return s("el-col",{key:t,attrs:{xs:24,sm:24,md:12,lg:8,xl:8}},[s("div",{staticClass:"arg-wrap"},[s("p",[e._v(e._s(t)+":")]),e._v(" "),"select"==a.type?s("el-select",{attrs:{placeholder:"请选择"},model:{value:a.default,callback:function(t){e.$set(a,"default",t)},expression:"arg_data.default"}},e._l(a.values,function(e){return s("el-option",{key:e,attrs:{label:e,value:e}})}),1):e._e(),e._v(" "),"int"==a.type?s("el-input-number",{attrs:{precision:0,step:1,min:Math.min.apply(null,a.values),max:Math.max.apply(null,a.values)},model:{value:a.default,callback:function(t){e.$set(a,"default",t)},expression:"arg_data.default"}}):e._e(),e._v(" "),"float"==a.type?s("el-input-number",{attrs:{precision:2,step:.1,min:Math.min.apply(null,a.values),max:Math.max.apply(null,a.values)},model:{value:a.default,callback:function(t){e.$set(a,"default",t)},expression:"arg_data.default"}}):e._e()],1)])}),1):e._e(),e._v(" "),s("el-row",{attrs:{gutter:10}},[s("el-col",{attrs:{xs:12,sm:6,md:6,lg:6,xl:6}},[s("a",{staticClass:"clear upload-btn",attrs:{href:"javascript:void(0);"},on:{click:function(a){e.imageClear(e.clearStrs=["imageUrl","targetImageUrl"],e.clearRefNames=["filebutton"],e.clearLoadingTokens=["isLoading","isLoading2"]),e.stopAxios()}}},[e._v(e._s(e.$t("message.clear")))])]),e._v(" "),s("el-col",{attrs:{xs:12,sm:6,md:6,lg:6,xl:6}},[s("a",{staticClass:"submit upload-btn",class:{"submit-forbidden":1==e.isLoading2},attrs:{href:"javascript:void(0);"},on:{click:function(a){return e.submit()}}},[e._v(e._s(e.$t("message.submit")))])])],1)],1)},staticRenderFns:[]};var d=t("VU/8")(u,c,!1,function(e){t("9iiv")},null,null);a.default=d.exports}});
//# sourceMappingURL=4.cb23b668d95416a62d95.js.map