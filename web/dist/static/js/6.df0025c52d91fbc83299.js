webpackJsonp([6],{"4Dak":function(a,e,t){"use strict";Object.defineProperty(e,"__esModule",{value:!0});var s=t("pFYg"),i=t.n(s),r=t("2LA7"),n=t.n(r),l=t("5SbQ"),o=t("Yya3"),m={name:"segmentation",props:["modelData"],components:{ShowArea:l.a,LoadingAnimationVue:o.a},data:function(){return{baseUrl:n.a.base_url,imageUrl:"",watermarkUrl:"",targetImageUrl:"",extractInputImageUrl:"",extractOutputWatermarkUrl:"",isLoading:!1,isLoadingWatermark:!1,isLoading2:!1,isLoadingExtractInput:!1,isLoadingExtractOutput:!1}},methods:{getType:function(a){return void 0===a?"undefined":i()(a)},moveClick:function(a){var e=this;this.$nextTick(function(){e.$refs[a].dispatchEvent(new MouseEvent("click"))})},stopAxios:function(){void 0!=this.source&&this.source.cancel("Operation canceled by the user.")},stopAxios2:function(){void 0!=this.source2&&this.source2.cancel("Operation canceled by the user.")},submit:function(){var a=this;if(""==this.imageUrl)this.$message({message:"请先上传图片！",type:"warning"});else if(""==this.watermarkUrl)this.$message({message:"请先上传水印！",type:"warning"});else{this.targetImageUrl="",this.isLoading2=!0;var e={local_image_url:this.imageUrl.split("=")[1],local_watermark_url:this.watermarkUrl.split("=")[1],conda_env:this.modelData.condaEnv,args:{},classname:this.modelData.modelType,demoname:this.modelData.modelId};for(var t in this.modelData.args)e.args[t]=this.modelData.args[t].default;console.log(e),this.CancelToken=this.$axios.CancelToken,this.source=this.CancelToken.source(),this.$axios.post(this.baseUrl+"watermark/embed",e,{cancelToken:this.source.token}).then(function(e){console.log("post res:",e);var t=e.data[e.data.length-1];t=(t=t.split(" "))[t.length-1],t=a.baseUrl+"absimage?path="+t+"&t="+Math.random(),a.targetImageUrl=t,a.isLoading2=!1}).catch(function(e){a.isLoading2=!1,a.$message({message:e,type:"error"})})}},submit_extact:function(){var a=this;if(""==this.extractInputImageUrl)this.$message({message:"请先上传图片！",type:"warning"});else{this.extractOutputWatermarkUrl="",this.isLoadingExtractOutput=!0;var e={local_image_url:this.extractInputImageUrl.split("=")[1],conda_env:this.modelData.condaEnv,args:{},classname:this.modelData.modelType,demoname:this.modelData.modelId};for(var t in this.modelData.args)e.args[t]=this.modelData.args[t].default;console.log(e),this.CancelToken2=this.$axios.CancelToken,this.source2=this.CancelToken2.source(),this.$axios.post(this.baseUrl+"watermark/extract",e,{cancelToken:this.source2.token}).then(function(e){console.log("post res:",e);var t=e.data[e.data.length-1];t=(t=t.split(" "))[t.length-1],t=a.baseUrl+"absimage?path="+t+"&t="+Math.random(),a.extractOutputWatermarkUrl=t,a.isLoadingExtractOutput=!1}).catch(function(e){a.isLoadingExtractOutput=!1,a.$message({message:e,type:"error"})})}},onDrop:function(a){(window.event||a).preventDefault(),this.$refs.filebutton.files=a.dataTransfer.files,this.fileChange(),console.log(this.$refs.filebutton.files),console.log(a.dataTransfer.files[0])}},mounted:function(){var a=this;setTimeout(function(){var e=a,t=document.getElementById("drop-area");t.ondragenter=t.ondragover=t.ondragleave=function(){return!1},t.addEventListener("drop",e.onDrop)},0);var e=this;this.$eventBus.$on("addClick",function(a){e.moveClick()}),this.$eventBus.$on("addShowImage",function(a){e[a.bindName]=a.showImageUrl})}},c={render:function(){var a=this,e=a.$createElement,s=a._self._c||e;return s("div",[s("h2",[a._v("Embed:")]),a._v(" "),s("el-row",{staticClass:"show-wrap"},[s("el-col",{staticClass:"model-left-wrap2",attrs:{xs:24,sm:8,md:8,lg:8,xl:8}},[s("p",{staticClass:"model-inout-tittle"},[a._v(a._s(a.$t("message.input_image")))]),a._v(" "),s("vue-viewer",{directives:[{name:"show",rawName:"v-show",value:""!=a.imageUrl,expression:"imageUrl != ''"}],staticClass:"source-image",attrs:{thumb:a.imageUrl,full:a.imageUrl}}),a._v(" "),s("div",{directives:[{name:"show",rawName:"v-show",value:""==a.imageUrl,expression:"imageUrl == ''"}],staticClass:"input-wrap",attrs:{id:"drop-area"},on:{click:function(e){return a.moveClick("filebutton")}}},[s("img",{attrs:{src:t("kTpr"),alt:""}}),a._v(" "),s("p",{directives:[{name:"show",rawName:"v-show",value:0==a.isLoading,expression:"isLoading == false"}],staticClass:"input-help"},[a._v("\n          "+a._s(a.$t("message.drop_image"))+"\n        ")]),a._v(" "),s("p",{directives:[{name:"show",rawName:"v-show",value:0==a.isLoading,expression:"isLoading == false"}],staticClass:"input-help"},[a._v("\n          "+a._s(a.$t("message.or"))+"\n        ")]),a._v(" "),s("p",{directives:[{name:"show",rawName:"v-show",value:0==a.isLoading,expression:"isLoading == false"}],staticClass:"input-help"},[a._v("\n          "+a._s(a.$t("message.click_upload"))+"\n        ")]),a._v(" "),s("p",{directives:[{name:"show",rawName:"v-show",value:a.isLoading,expression:"isLoading"}]},[a._v("uploading......")]),a._v(" "),s("input",{directives:[{name:"show",rawName:"v-show",value:0,expression:"0"}],ref:"filebutton",attrs:{type:"file"},on:{change:function(e){return a.fileChange("filebutton","imageUrl","isLoading")}}})]),a._v(" "),s("ShowArea",{staticClass:"centered lr-padding",attrs:{showAreaData:{images:a.modelData.detialData.show_images,bindName:"imageUrl"}}})],1),a._v(" "),s("el-col",{staticClass:"model-left-wrap2",attrs:{xs:24,sm:4,md:4,lg:4,xl:4}},[s("p",{staticClass:"model-inout-tittle"},[a._v(a._s(a.$t("message.input_watermark")))]),a._v(" "),s("vue-viewer",{directives:[{name:"show",rawName:"v-show",value:""!=a.watermarkUrl,expression:"watermarkUrl != ''"}],staticClass:"source-image",attrs:{thumb:a.watermarkUrl,full:a.watermarkUrl}}),a._v(" "),s("div",{directives:[{name:"show",rawName:"v-show",value:""==a.watermarkUrl,expression:"watermarkUrl == ''"}],staticClass:"input-wrap",attrs:{id:"drop-area"},on:{click:function(e){return a.moveClick("filebutton_watermark")}}},[s("img",{attrs:{src:t("kTpr"),alt:""}}),a._v(" "),s("p",{directives:[{name:"show",rawName:"v-show",value:0==a.isLoadingWatermark,expression:"isLoadingWatermark == false"}],staticClass:"input-help"},[a._v("\n          "+a._s(a.$t("message.drop_image"))+"\n        ")]),a._v(" "),s("p",{directives:[{name:"show",rawName:"v-show",value:0==a.isLoadingWatermark,expression:"isLoadingWatermark == false"}],staticClass:"input-help"},[a._v("\n          "+a._s(a.$t("message.or"))+"\n        ")]),a._v(" "),s("p",{directives:[{name:"show",rawName:"v-show",value:0==a.isLoadingWatermark,expression:"isLoadingWatermark == false"}],staticClass:"input-help"},[a._v("\n          "+a._s(a.$t("message.click_upload"))+"\n        ")]),a._v(" "),s("p",{directives:[{name:"show",rawName:"v-show",value:a.isLoadingWatermark,expression:"isLoadingWatermark"}]},[a._v("uploading......")]),a._v(" "),s("input",{directives:[{name:"show",rawName:"v-show",value:0,expression:"0"}],ref:"filebutton_watermark",attrs:{type:"file"},on:{change:function(e){return a.fileChange("filebutton_watermark","watermarkUrl","isLoadingWatermark")}}})]),a._v(" "),s("ShowArea",{staticClass:"centered lr-padding",attrs:{showAreaData:{images:a.modelData.detialData.watermark_images,bindName:"watermarkUrl"}}})],1),a._v(" "),s("el-col",{staticClass:"model-right-wrap",attrs:{xs:24,sm:12,md:12,lg:12,xl:12}},[s("p",{staticClass:"model-inout-tittle"},[a._v(a._s(a.$t("message.result")))]),a._v(" "),s("div",[s("LoadingAnimationVue",{directives:[{name:"show",rawName:"v-show",value:a.isLoading2,expression:"isLoading2"}]}),a._v(" "),s("vue-viewer",{directives:[{name:"show",rawName:"v-show",value:""!=a.targetImageUrl,expression:"targetImageUrl != ''"}],staticClass:"source-image",attrs:{thumb:a.targetImageUrl,full:a.targetImageUrl}})],1)])],1),a._v(" "),"{}"!=JSON.stringify(a.modelData.args)&&void 0!==a.modelData.args?s("el-row",{staticClass:"arg-background",attrs:{gutter:10}},a._l(a.modelData.args,function(e,t){return s("el-col",{key:t,attrs:{xs:24,sm:24,md:12,lg:8,xl:8}},[s("div",{staticClass:"arg-wrap"},[s("p",[a._v(a._s(t)+":")]),a._v(" "),"select"==e.type?s("el-select",{attrs:{placeholder:"请选择"},model:{value:e.default,callback:function(t){a.$set(e,"default",t)},expression:"arg_data.default"}},a._l(e.values,function(a){return s("el-option",{key:a,attrs:{label:a,value:a}})}),1):a._e(),a._v(" "),"int"==e.type?s("el-input-number",{attrs:{precision:0,step:1,min:Math.min.apply(null,e.values),max:Math.max.apply(null,e.values)},model:{value:e.default,callback:function(t){a.$set(e,"default",t)},expression:"arg_data.default"}}):a._e(),a._v(" "),"float"==e.type?s("el-input-number",{attrs:{precision:2,step:.1,min:Math.min.apply(null,e.values),max:Math.max.apply(null,e.values)},model:{value:e.default,callback:function(t){a.$set(e,"default",t)},expression:"arg_data.default"}}):a._e()],1)])}),1):a._e(),a._v(" "),s("el-row",{attrs:{gutter:10}},[s("el-col",{attrs:{xs:12,sm:6,md:6,lg:6,xl:6}},[s("a",{staticClass:"clear upload-btn",attrs:{href:"javascript:void(0);"},on:{click:function(e){a.imageClear(a.clearStrs=["imageUrl","watermarkUrl","modelResult","targetImageUrl"],a.clearRefNames=["filebutton","filebutton_watermark"],a.clearLoadingTokens=["isLoading","isLoading2","isLoadingWatermark"]),a.stopAxios()}}},[a._v(a._s(a.$t("message.clear")))])]),a._v(" "),s("el-col",{attrs:{xs:12,sm:6,md:6,lg:6,xl:6}},[s("a",{staticClass:"submit upload-btn",class:{"submit-forbidden":1==a.isLoading2},attrs:{href:"javascript:void(0);"},on:{click:function(e){return a.submit()}}},[a._v(a._s(a.$t("message.submit")))])]),a._v(" "),s("el-col",{attrs:{xs:12,sm:6,md:6,lg:6,xl:6}},[s("a",{staticClass:"submit upload-btn",class:{"submit-forbidden":1==a.isLoading2},attrs:{href:"javascript:void(0);"},on:{click:function(e){a.extractInputImageUrl=a.targetImageUrl}}},[a._v(a._s(a.$t("message.trans_embed_image")))])])],1),a._v(" "),s("h2",[a._v("Extract:")]),a._v(" "),s("el-row",{staticClass:"show-wrap"},[s("el-col",{staticClass:"model-left-wrap",attrs:{xs:24,sm:12,md:12,lg:12,xl:12}},[s("p",{staticClass:"model-inout-tittle"},[a._v(a._s(a.$t("message.input_image")))]),a._v(" "),s("vue-viewer",{directives:[{name:"show",rawName:"v-show",value:""!=a.extractInputImageUrl,expression:"extractInputImageUrl != ''"}],staticClass:"source-image",attrs:{thumb:a.extractInputImageUrl,full:a.extractInputImageUrl}}),a._v(" "),s("div",{directives:[{name:"show",rawName:"v-show",value:""==a.extractInputImageUrl,expression:"extractInputImageUrl == ''"}],staticClass:"input-wrap",attrs:{id:"drop-area"},on:{click:function(e){return a.moveClick("filebutton_embeded_img")}}},[s("img",{attrs:{src:t("kTpr"),alt:""}}),a._v(" "),s("p",{directives:[{name:"show",rawName:"v-show",value:0==a.isLoadingExtractInput,expression:"isLoadingExtractInput == false"}],staticClass:"input-help"},[a._v("\n          "+a._s(a.$t("message.drop_image"))+"\n        ")]),a._v(" "),s("p",{directives:[{name:"show",rawName:"v-show",value:0==a.isLoadingExtractInput,expression:"isLoadingExtractInput == false"}],staticClass:"input-help"},[a._v("\n          "+a._s(a.$t("message.or"))+"\n        ")]),a._v(" "),s("p",{directives:[{name:"show",rawName:"v-show",value:0==a.isLoadingExtractInput,expression:"isLoadingExtractInput == false"}],staticClass:"input-help"},[a._v("\n          "+a._s(a.$t("message.click_upload"))+"\n        ")]),a._v(" "),s("p",{directives:[{name:"show",rawName:"v-show",value:a.isLoadingExtractInput,expression:"isLoadingExtractInput"}]},[a._v("uploading......")]),a._v(" "),s("input",{directives:[{name:"show",rawName:"v-show",value:0,expression:"0"}],ref:"filebutton_embeded_img",attrs:{type:"file"},on:{change:function(e){return a.fileChange("filebutton_embeded_img","extractInputImageUrl","isLoadingExtractInput")}}})]),a._v(" "),s("ShowArea",{staticClass:"centered lr-padding",attrs:{showAreaData:{images:a.modelData.detialData.show_images,bindName:"extractInputImageUrl"}}})],1),a._v(" "),s("el-col",{staticClass:"model-right-wrap",attrs:{xs:24,sm:12,md:12,lg:12,xl:12}},[s("p",{staticClass:"model-inout-tittle"},[a._v(a._s(a.$t("message.result")))]),a._v(" "),s("div",[s("LoadingAnimationVue",{directives:[{name:"show",rawName:"v-show",value:a.isLoadingExtractOutput,expression:"isLoadingExtractOutput"}]}),a._v(" "),s("vue-viewer",{directives:[{name:"show",rawName:"v-show",value:""!=a.extractOutputWatermarkUrl,expression:"extractOutputWatermarkUrl != ''"}],staticClass:"source-image",attrs:{thumb:a.extractOutputWatermarkUrl,full:a.extractOutputWatermarkUrl}})],1)])],1),a._v(" "),s("el-row",{attrs:{gutter:10}},[s("el-col",{attrs:{xs:12,sm:6,md:6,lg:6,xl:6}},[s("a",{staticClass:"clear upload-btn",attrs:{href:"javascript:void(0);"},on:{click:function(e){a.imageClear(a.clearStrs=["extractInputImageUrl","extractOutputWatermarkUrl"],a.clearRefNames=["filebutton_embeded_img"],a.clearLoadingTokens=["isLoadingExtractOutput","isLoadingWatermark"]),a.stopAxios()}}},[a._v(a._s(a.$t("message.clear")))])]),a._v(" "),s("el-col",{attrs:{xs:12,sm:6,md:6,lg:6,xl:6}},[s("a",{staticClass:"submit upload-btn",class:{"submit-forbidden":1==a.isLoadingExtractOutput},attrs:{href:"javascript:void(0);"},on:{click:function(e){return a.submit_extact()}}},[a._v(a._s(a.$t("message.submit")))])])],1)],1)},staticRenderFns:[]};var u=t("VU/8")(m,c,!1,function(a){t("9eAp")},null,null);e.default=u.exports},"9eAp":function(a,e){}});
//# sourceMappingURL=6.df0025c52d91fbc83299.js.map