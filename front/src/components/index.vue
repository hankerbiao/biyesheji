<template>
  <div class="backvideo">
    <el-backtop></el-backtop>
    <el-container>
      <div class="backimage">
        <div class="header-title" style="margin-top: 20px; color: lightseagreen; line-height: 30px">
          <el-row :gutter="20">
            <el-col :span="8">
              <p>
                <i class="el-icon-star-off"></i>&nbsp;&nbsp;我的公众号:&nbsp;&nbsp;城建417
              </p>
            </el-col>
            <el-col :span="16">
              <h4 style="font-weight: 800">
                Y&nbsp;&nbsp;&nbsp;&nbsp;O&nbsp;&nbsp;&nbsp;&nbsp;L&nbsp;&nbsp;&nbsp;&nbsp;O&nbsp;&nbsp;&nbsp;&nbsp;v&nbsp;&nbsp;&nbsp;&nbsp;5&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;&nbsp;&nbsp;&nbsp;W&nbsp;&nbsp;&nbsp;&nbsp;E&nbsp;&nbsp;&nbsp;&nbsp;B&nbsp;&nbsp;&nbsp;&nbsp;端
              </h4>
            </el-col>
          </el-row>
        </div>
        <!-- 搜索框 -->
        <div class="searchbar">
          <el-row type="flex" class="row-bg" justify="space-between">
            <el-col :span="4"> </el-col>
            <el-col :span="16">
              <el-input placeholder="请输入关键字信息" v-model="imagesearch" class="input-with-select" style="font-size: 16px"
                clearable></el-input>
            </el-col>
            <el-col :span="4">
              <el-button type="primary" @click="searchcontent()" style="margin-left: -100px">搜 索</el-button>
            </el-col>
          </el-row>
        </div>
        <div class="main-image">
          <div class="row">
            <div class="col-md-4 col-sm-6">
              <div class="product" v-for="fit2 in srcList" :key="fit2">
                <div class="product-img-wrap" v-for="fit in url" :key="fit">
                  <el-image 
                    style="width: 100px; height: 100px"
                    :src="fit" 
                    :preview-src-list="fit2">
                  </el-image>
                  <!-- <img class="card-img-top" :src="fit" :preview-src-list="fit" alt="img" /> -->
                  <div class="quick-view">文字描述</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </el-container>
  </div>
</template>

<script>
  import axios from "axios";

  export default {
    data() {
      return {
        vedioCanPlay: false,
        fixStyle: "",
        imagesearch: "",
        urls: [],
        url:[],
        srcList: [],
      };
    },

    methods: {
      searchcontent() {
        console.log(this.imagesearch);
        console.log("点击了按钮");

        const path = "http://localhost:5003/test";
        axios
          .get(path)
          .then((res) => {
            this.url = res.data.image_url;
            this.srcList.push(res.data.draw_url);
            console.log(res)
            console.log(this.srcList)
            console.log(this.url)
          })
          .catch((error) => {
            console.log("===== errot =====")
            console.error(error);
            console.log("===============")
          });

      },
    },
  };
</script>

