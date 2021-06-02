<template>
  <div class="main">
    <div class="background"></div>
    <div class="front"></div>
    <div class="background">
      <img :src="imgSrc" width="100%" height="100%" alt="" />
  </div>
    <el-input placeholder="请输入关键字信息" v-model="imagesearch" class="input-with-select" style="font-size: 16px;width: 500px;margin-left: -150px;margin-top: 10px;"
    clearable></el-input>
    <el-button type="primary" @click="searchcontent()">搜 索</el-button>
      <div class="product">
        <div class="product-img-wrap" v-for="image_url in image_urls" :key="image_url" style ="float: left;">
            <el-image 
            style="width: 200px; height: 200px;margin-top: 30px;margin-left: 25px;"
            :src="image_url.origin_pics" 
            :preview-src-list="image_url.draw_pics">
          </el-image>                  
        </div>
        </div>
  </div>
</template>

<script>
  import axios from "axios";

  export default {
    data() {
      return {
        imgSrc:require('../assets/images/bg.jpeg'),
        fixStyle: "",
        imagesearch: "",
        image_urls: [],
        draw_urls: [],
      };
    },

    methods: {
      searchcontent() {
        const path = "http://localhost:5003/test";
        axios
          .get(path)
          .then((res) => {
            this.image_urls = res.data.image_url;
          })
          .catch((error) => {
            console.log(error)
          });
      },
    },
  };
</script>

<style>
.background{
    width:100%;  
    height:100%;  /**宽高100%是为了图片铺满屏幕 */
    z-index:-1;
    position: absolute;
}
 
.front{
    z-index:1;
    position: absolute;
}
</style>

