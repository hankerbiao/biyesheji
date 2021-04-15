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
              <div class="product">
                <div class="product-img-wrap">
                  <img class="card-img-top" src="../assets/images/600x400.png" alt="img" />
                  <div class="quick-view">文字描述</div>
                </div>
              </div>
            </div>
            <div class="col-md-4 col-sm-6">
              <div class="product">
                <div class="product-img-wrap">
                  <img class="card-img-top" src="../assets/images/600x280.png" alt="img" />
                  <div class="quick-view">文字描述</div>
                </div>
              </div>
            </div>
            <div class="col-md-4 col-sm-6">
              <div class="product">
                <div class="product-img-wrap">
                  <img class="card-img-top" src="../assets/images/600x320.png" alt="img" />
                  <div class="quick-view">文字描述</div>
                </div>
              </div>
            </div>
            <div class="col-md-4 col-sm-6">
              <div class="product">
                <div class="product-img-wrap">
                  <img class="card-img-top" src="../assets/images/600x600.png" alt="img" />
                  <div class="quick-view">文字描述</div>
                </div>
              </div>
            </div>
            <div class="col-md-4 col-sm-6">
              <div class="product">
                <div class="product-img-wrap">
                  <img class="card-img-top" src="../assets/images/600x400.png" alt="img" />
                  <div class="quick-view">文字描述</div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
      <!-- </div>
    </div> -->
    </el-container>
  </div>
</template>

<script>
  import axios from 'axios';

  export default {
    data() {
      return {
        vedioCanPlay: false,
        fixStyle: "",
        imagesearch: "",
      };
    },

    methods: {
      searchcontent(){
        console.log(this.imagesearch)
        console.log("点击了按钮")

        const path = 'http://localhost:5003/test';
        axios.get(path)
        .then((res) => {
          this.msg = res.data;
          console.log(this.msg)
        })
        .catch((error) => {
          console.error(error);
        });
      },

    },

  };
</script>

<style>
  /* .backvideo {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
  }

  .homepage-hero-module,
  .video-container {
    position: relative;
    overflow: hidden;
  }

  .video-container .poster img,
  .video-container video {
    z-index: 0;
    position: absolute;
  }

  .video-container .filter {
    z-index: 1;
    position: absolute;
    background: rgba(0, 0, 0, 0.4);
  } */
    /* .backimage {
      background-image: url(../assets/video.png);
      background-position: center 0;
      background-repeat: no-repeat;
      background-attachment: fixed;
      background-size: cover;
      -webkit-background-size: cover;
      -o-background-size: cover;
      -moz-background-size: cover;
      -ms-background-size: cover;
    } */

  .main-image {
    /* background-color: #ffffff; */
    float: left;
    margin: 20px;
  }

  .el-input {
    width: 100%;
  }

  .searchbar {
    margin: 24px;
  }

  .product {
    transition: 0.4s;
    background: #ffffff;
    border-radius: 5px;
    margin-bottom: 30px;
  }

  .product:hover {
    box-shadow: 10px 10px 10px rgba(41, 38, 51, 0.09);
  }

  .product .product-img-wrap {
    position: relative;
    transition: 0.5s;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
  }

  .product .product-img-wrap img {
    transition: 0.5s;
  }

  .product:hover .product-img-wrap {
    background: rgba(249, 255, 237, 0.1);
  }

  .product:hover .product-img-wrap img {
    transform: scale(1.1);
  }

  .product .product-img-wrap .quick-view {
    position: absolute;
    display: block;
    background: rgba(255, 255, 255, 0.52);
    width: 100%;
    cursor: pointer;
    opacity: 0;
    transition: 0.5s;
    height: 50px;
    font-weight: 600;
    /* margin-top: 100px; */
    padding: 10px;
  }

  .product:hover .product-img-wrap .quick-view {
    opacity: 1;
  }
</style>
