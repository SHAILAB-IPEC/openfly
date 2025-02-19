<script>
import { Swiper, SwiperSlide} from 'swiper/vue';
import { Navigation, Pagination, Autoplay} from 'swiper/modules';
import 'swiper/css/bundle';

export default {
  components: {
      Swiper,
      SwiperSlide,
      Navigation,
      Pagination,
      Autoplay,
    },
  data() {
    return {
      modules: [
        Navigation,
        Pagination,
        Autoplay,
      ],
      // 选择要轮播的照片
      image_paths: [
        "./carousel/1.jpg",
        "./carousel/2.jpg",
        "./carousel/3.jpg",
        "./carousel/4.jpg",
        "./carousel/5.jpg",
        "./carousel/6.jpg",
      ],
    }
  }
}
</script>

<script setup>
const cover = './cover.png'
</script>
<template>
    <el-row justify="center">
      <el-col :xs="24" :sm="20" :md="16" :lg="12" :xl="10" >
        <el-container class="video-container">
          <!-- <img src="./cover.png" alt="cover" style="width: 100%; height: auto;"> -->
          <el-image :src="cover" class="logo" fit="cover" />
        </el-container>
      </el-col>
    </el-row>
  <!-- <el-row justify="center">
    <el-col :span="24">
      设置轮播图：循环播放、首张图序号、响应式、导航和分页、自动播放
      <swiper
        :loop="true"
        :slidesPerView="1"
        :breakpoints="{
          600: {
            slidesPerView: 2,
          },
          800: {
            slidesPerView: 3,
          },
        }"
        :modules="modules"
        :navigation="{ 
          hideOnClick:true,
        }"
        :pagination="{ 
          hideOnClick:true,
          clickable:true, 
          type:'bullets' 
        }"
        :autoplay="{ 
          delay:5000,
          disableOnInteraction:false,
          pauseOnMouseEnter:true,
        }"
        >
        <swiper-slide v-for="path in image_paths">
          <el-image :src="path"/>
        </swiper-slide>
      </swiper>
    </el-col>
  </el-row> -->
</template>
  
<style>

/* 设置Swiper风格 */
.swiper {
  --swiper-theme-color: white;
}

</style>
  